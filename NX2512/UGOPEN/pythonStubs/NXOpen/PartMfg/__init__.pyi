from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.PDM
class AddElementToLibraryBuilder(NXOpen.Builder): 
    """ Build class for NXOpen.PartMfg.AddElementToLibraryBuilder.
    """
    @property
    def IsNewSubtype(self) -> bool:
        """
        Getter for property: (bool) IsNewSubtype
         Returns the is new subtype   
            
         
        """
        pass
    @IsNewSubtype.setter
    def IsNewSubtype(self, isNewSubtype: bool):
        """
        Setter for property: (bool) IsNewSubtype
         Returns the is new subtype   
            
         
        """
        pass
    @property
    def IsOverwrite(self) -> bool:
        """
        Getter for property: (bool) IsOverwrite
         Returns the is overwrite   
            
         
        """
        pass
    @IsOverwrite.setter
    def IsOverwrite(self, isOverwrite: bool):
        """
        Setter for property: (bool) IsOverwrite
         Returns the is overwrite   
            
         
        """
        pass
    @property
    def ItemType(self) -> str:
        """
        Getter for property: (str) ItemType
         Returns the is item type   
            
         
        """
        pass
    @ItemType.setter
    def ItemType(self, itemType: str):
        """
        Setter for property: (str) ItemType
         Returns the is item type   
            
         
        """
        pass
    @property
    def LockStructure(self) -> bool:
        """
        Getter for property: (bool) LockStructure
         Returns the lock structure   
            
         
        """
        pass
    @LockStructure.setter
    def LockStructure(self, lockStructure: bool):
        """
        Setter for property: (bool) LockStructure
         Returns the lock structure   
            
         
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
    def Subtype(self) -> str:
        """
        Getter for property: (str) Subtype
         Returns the subtype   
            
         
        """
        pass
    @Subtype.setter
    def Subtype(self, subtype: str):
        """
        Setter for property: (str) Subtype
         Returns the subtype   
            
         
        """
        pass
    def GetDescription(self) -> List[str]:
        """
         Returns the description 
         Returns description (List[str]): .
        """
        pass
    def GetFolder(self) -> str:
        """
         Returns the folder
         Returns folder (str): .
        """
        pass
    def GetPartOperationCreateBuilder(self) -> NXOpen.PDM.PartOperationCreateBuilder:
        """
         Gets NXOpen.PDM.PartOperationCreateBuilder 
         Returns partOperationCreateBuilder ( NXOpen.PDM.PartOperationCreateBuilder): .
        """
        pass
    def SetDescription(self, description: List[str]) -> None:
        """
         Sets the description 
        """
        pass
    def SetFolder(self, folder: str) -> None:
        """
         Sets the folder 
        """
        pass
    def SetPartOperationCreateBuilder(self, partOperationCreateBuilder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
         Sets NXOpen.PDM.PartOperationCreateBuilder 
        """
        pass
class AdHocElementBuilder(BaseBuilder): 
    """ Builder class """
    @property
    def AfterElement(self) -> SelectElement:
        """
        Getter for property: ( SelectElement NXOpen) AfterElement
         Returns the parent selection item   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the properties name item   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the properties name item   
            
         
        """
        pass
import NXOpen
class AssignWorkInstructionTemplateBuilder(NXOpen.Builder): 
    """ Builder class """
    class ApplyTemplateOptionsType(Enum):
        """
        Members Include: 
         |Selected| 
         |AllSameTypes| 
         |AllSameTypeChildren| 

        """
        Selected: int
        AllSameTypes: int
        AllSameTypeChildren: int
        @staticmethod
        def ValueOf(value: int) -> AssignWorkInstructionTemplateBuilder.ApplyTemplateOptionsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ApplyTemplateOption(self) -> AssignWorkInstructionTemplateBuilder.ApplyTemplateOptionsType:
        """
        Getter for property: ( AssignWorkInstructionTemplateBuilder.ApplyTemplateOptionsType NXOpen) ApplyTemplateOption
         Returns the template options   
            
         
        """
        pass
    @ApplyTemplateOption.setter
    def ApplyTemplateOption(self, templateOption: AssignWorkInstructionTemplateBuilder.ApplyTemplateOptionsType):
        """
        Setter for property: ( AssignWorkInstructionTemplateBuilder.ApplyTemplateOptionsType NXOpen) ApplyTemplateOption
         Returns the template options   
            
         
        """
        pass
    @property
    def ReferenceElement(self) -> SelectElement:
        """
        Getter for property: ( SelectElement NXOpen) ReferenceElement
         Returns the reference element selection item   
            
         
        """
        pass
    @property
    def TemplateFile(self) -> str:
        """
        Getter for property: (str) TemplateFile
         Returns the template   
            
         
        """
        pass
    @TemplateFile.setter
    def TemplateFile(self, templateName: str):
        """
        Setter for property: (str) TemplateFile
         Returns the template   
            
         
        """
        pass
import NXOpen
class AttributeBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.PartMfg.AttributeBuilder.  This class is used
    to construct a builder to collect individual attributes that are applied to Bill of Process Elements.
    """
    pass
import NXOpen
class BaseBuilder(NXOpen.Builder): 
    """ Builder class """
    @property
    def AttributeTemplate(self) -> SelectAttributeTemplateBuilder:
        """
        Getter for property: ( SelectAttributeTemplateBuilder NXOpen) AttributeTemplate
         Returns the  PartMfg::SelectAttributeTemplateBuilder  for the Bill of Process element   
            
         
        """
        pass
    @property
    def ElementTemplateFile(self) -> str:
        """
        Getter for property: (str) ElementTemplateFile
         Returns the element template file   
            
         
        """
        pass
    @ElementTemplateFile.setter
    def ElementTemplateFile(self, templateFileName: str):
        """
        Setter for property: (str) ElementTemplateFile
         Returns the element template file   
            
         
        """
        pass
import NXOpen
import NXOpen.PDM
class BaseCreateWorkInstructionBuilder(NXOpen.Builder): 
    """ Builder class """
    @property
    def File(self) -> str:
        """
        Getter for property: (str) File
         Returns the work instruction file   
            
         
        """
        pass
    @File.setter
    def File(self, file: str):
        """
        Setter for property: (str) File
         Returns the work instruction file   
            
         
        """
        pass
    @property
    def ReferenceElement(self) -> SelectElement:
        """
        Getter for property: ( SelectElement NXOpen) ReferenceElement
         Returns the reference element selection item   
            
         
        """
        pass
    @property
    def TemplateFile(self) -> str:
        """
        Getter for property: (str) TemplateFile
         Returns the template   
            
         
        """
        pass
    @TemplateFile.setter
    def TemplateFile(self, templateName: str):
        """
        Setter for property: (str) TemplateFile
         Returns the template   
            
         
        """
        pass
    def GetPartOperationCreateBuilder(self) -> NXOpen.PDM.PartOperationBuilder:
        """
         Gets NXOpen.PDM.PartOperationBuilder 
         Returns partOperationCreateBuilder ( NXOpen.PDM.PartOperationBuilder): .
        """
        pass
    def SetPartOperationCreateBuilder(self, partOperationBuilder: NXOpen.PDM.PartOperationBuilder) -> None:
        """
         Sets NXOpen.PDM.PartOperationBuilder 
        """
        pass
    def SetUseBlankTemplate(self, blankTemplateUnit: NXOpen.Part.Units) -> None:
        """
         Sets the use blank template of input unit type, it supports only Inches and Millimeters 
        """
        pass
class BopPart(PartMfgPart): 
    """ Represents the BopPart. It will provide the collections to access the BoP element.
     """
    def CreateSaveStructureBuilder(self) -> SaveStructureBuilder:
        """
         Create save structure builder. 
         Returns builder ( SaveStructureBuilder NXOpen): .
        """
        pass
    def SetAutoSequencedFromCD(self) -> None:
        """
         Set auto sequencing for active bill of process part in session 
        """
        pass
    def SetIsAutoSequenced(self, autoSequenced: bool) -> None:
        """
         Set auto sequencing for active bill of process part in session 
        """
        pass
import NXOpen
class ClientManager(NXOpen.Object): 
    """ Represents a manager for external clients for the PartMfg applications.
     """
    def CreateClient(self, clientName: str) -> Client:
        """
                Creates an instance of NXOpen.PartMfg.Client and registers that new client with MBPM.
                
         Returns newClient ( Client NXOpen): .
        """
        pass
import NXOpen
class Client(NXOpen.NXObject): 
    """ Represents an external client that contributes custom elements to a Bill of Process.
     """
    @property
    def ClientName(self) -> str:
        """
        Getter for property: (str) ClientName
         Returns the client name   
            
         
        """
        pass
    RefreshElementsHandler = Callable[[RefreshElementContent], None]
    def Register(self, handler: Client.RefreshElementsHandler) -> None:
        """
         Registers the client 
        """
        pass
import NXOpen
class CopyObjectsManager(NXOpen.Object): 
    """ Represents the collection object for Text in document.
     """
    def CopyObjects(self, objects: List[Element], parentElementTag: Element, insertAtPosition: int) -> None:
        """
         Copies the input objects to part. 
        """
        pass
class CreateWorkInstructionBuilder(BaseCreateWorkInstructionBuilder): 
    """ Builder class """
    pass
class CreateWorkInstructionTemplateBuilder(BaseCreateWorkInstructionBuilder): 
    """ Builder class """
    pass
import NXOpen
class DocumentElementBuilder(BaseBuilder): 
    """ Buider class """
    @property
    def AfterElement(self) -> SelectElement:
        """
        Getter for property: ( SelectElement NXOpen) AfterElement
         Returns the parent selection item   
            
         
        """
        pass
    @property
    def InstanceMethod(self) -> Element.InstanceMethodType:
        """
        Getter for property: ( Element.InstanceMethodType NXOpen) InstanceMethod
         Returns the property Instance method   
            
         
        """
        pass
    @InstanceMethod.setter
    def InstanceMethod(self, instanceMethod: Element.InstanceMethodType):
        """
        Setter for property: ( Element.InstanceMethodType NXOpen) InstanceMethod
         Returns the property Instance method   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the document name item   
            
         
        """
        pass
    @Name.setter
    def Name(self, documentNameItem: str):
        """
        Setter for property: (str) Name
         Returns the document name item   
            
         
        """
        pass
    @property
    def RequiredState(self) -> bool:
        """
        Getter for property: (bool) RequiredState
         Returns the property state ( required or not )   
            
         
        """
        pass
    @RequiredState.setter
    def RequiredState(self, requiredState: bool):
        """
        Setter for property: (bool) RequiredState
         Returns the property state ( required or not )   
            
         
        """
        pass
import NXOpen
class ElementCollection(NXOpen.TaggedObjectCollection): 
    """ Represents the collection object for Elements in a Bill of Process.
     """
    def AddElements(self, elementsToBeAdded: List[Element], parentLineElement: Element, targetIndex: int) -> None:
        """
                Insert instances of PartMfg.Element
                
        """
        pass
    def AdoptAllocatedElements(self, objects: List[Element], clientName: str) -> List[Element]:
        """
         Adopt the allocated elements for a client 
         Returns copiedObjects ( Element List[NXOp):  copied elements .
        """
        pass
    def ConsumeDesignReferenceElements(self, objects: List[Element]) -> List[Element]:
        """
         Promote the unallocated elements to allocated 
         Returns copiedObjects ( Element List[NXOp):  copied elements .
        """
        pass
    def CreateAdHocElementBuilder(self, element: Element) -> AdHocElementBuilder:
        """
                Creates an instance of NXOpen.PartMfg.AdHocElementBuilder
                
         Returns builder ( AdHocElementBuilder NXOpen): .
        """
        pass
    def CreateAttributeBuilder(self) -> AttributeBuilder:
        """
                Creates an instance of NXOpen.PartMfg.AttributeBuilder
                
         Returns builder ( AttributeBuilder NXOpen): .
        """
        pass
    def CreateDocumentElementBuilder(self, element: Element) -> DocumentElementBuilder:
        """
                Creates an instance of NXOpen.PartMfg.DocumentElementBuilder
                
         Returns builder ( DocumentElementBuilder NXOpen): .
        """
        pass
    def CreateFolderElementBuilder(self, element: Element) -> FolderElementBuilder:
        """
                Creates an instance of NXOpen.PartMfg.FolderElementBuilder
                
         Returns builder ( FolderElementBuilder NXOpen): .
        """
        pass
    def CreateMaterialElementBuilder(self, element: Element) -> MaterialElementBuilder:
        """
                Creates an instance of NXOpen.PartMfg.MaterialElementBuilder
                
         Returns builder ( MaterialElementBuilder NXOpen): .
        """
        pass
    def CreateModelElementBuilder(self, element: Element) -> ModelElementBuilder:
        """
                Creates an instance of NXOpen.PartMfg.ModelElementBuilder
                
         Returns builder ( ModelElementBuilder NXOpen): .
        """
        pass
    def CreateOperationElementBuilder(self, element: Element) -> OperationElementBuilder:
        """
                Creates an instance of NXOpen.PartMfg.OperationElementBuilder
                
         Returns builder ( OperationElementBuilder NXOpen): .
        """
        pass
    def CreateResourceElementBuilder(self, element: Element) -> ResourceElementBuilder:
        """
                Creates an instance of NXOpen.PartMfg.ResourceElementBuilder
                
         Returns builder ( ResourceElementBuilder NXOpen): .
        """
        pass
    def CreateRoleElementBuilder(self, element: Element) -> RoleElementBuilder:
        """
                Creates an instance of NXOpen.PartMfg.RoleElementBuilder
                
         Returns builder ( RoleElementBuilder NXOpen): .
        """
        pass
    def CreateStepElementBuilder(self, element: Element) -> StepElementBuilder:
        """
                Creates an instance of NXOpen.PartMfg.StepElementBuilder
                
         Returns builder ( StepElementBuilder NXOpen): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Element:
        """
         Finds the NXOpen.PartMfg.Element with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns element ( Element NXOpen):  NXOpen.PartMfg.Element with this name. .
        """
        pass
    def MoveElements(self, elementsToBeMoved: List[Element], parentLineElement: Element, targetElement: Element) -> None:
        """
                Insert instances of PartMfg.Element
                
        """
        pass
    def RemoveNthElements(self, nthIndexes: List[int], parentLineElement: Element) -> None:
        """
                Removes instances of PartMfg.Element
                
        """
        pass
    def ReorderNthElements(self, nthIndexes: List[int], parentLineElement: Element, tagretIndex: int) -> None:
        """
                Removes instances of PartMfg.Element
                
        """
        pass
import NXOpen
class Element(NXOpen.NXObject): 
    """ Represents an element in a Bill of Process.
     """
    class ElementTypes(Enum):
        """
        Members Include: 
         |AdHoc|  AdHoc Bill of Process element 
         |Folder|  Folder Bill of Process element 
         |Material|  Material Bill of Process element 
         |Model|  Model Bill of Process element 
         |Operation|  Operation Bill of Process element 
         |Step|  Step Bill of Process element 
         |Role|  Role Bill of Process element 
         |Resource|  Resource Bill of Process element 
         |Document|  Document Bill of Process element 

        """
        AdHoc: int
        Folder: int
        Material: int
        Model: int
        Operation: int
        Step: int
        Role: int
        Resource: int
        Document: int
        @staticmethod
        def ValueOf(value: int) -> Element.ElementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InstanceMethodType(Enum):
        """
        Members Include: 
         |Restricted| 
         |Seeded| 
         |Empty| 
         |Na| 

        """
        Restricted: int
        Seeded: int
        Empty: int
        Na: int
        @staticmethod
        def ValueOf(value: int) -> Element.InstanceMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RequiredStateType(Enum):
        """
        Members Include: 
         |NotRequired| 
         |Required| 
         |Na| 

        """
        NotRequired: int
        Required: int
        Na: int
        @staticmethod
        def ValueOf(value: int) -> Element.RequiredStateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AttachProcessDocument(self, processDocument: str) -> None:
        """
         Attach a process document to a Bill of Process element 
        """
        pass
    def GetChildren(self) -> List[Element]:
        """
         Get the children of element 
         Returns children ( Element List[NXOp): .
        """
        pass
    def GetElementDescription(self) -> str:
        """
         Get the description of element in the navigator 
         Returns description (str):  sequence number .
        """
        pass
    def GetElementExpandState(self) -> bool:
        """
         Get the expand state of element in the navigator 
         Returns expandState (bool):  expand state of node .
        """
        pass
    def GetElementInstancemethod(self) -> Element.InstanceMethodType:
        """
         Get the instance method of element in the  
         Returns instanceMethod ( Element.InstanceMethodType NXOpen):  instanceMethod   .
        """
        pass
    def GetElementRequiredstate(self) -> Element.RequiredStateType:
        """
         Get the isRequired of element in the  
         Returns required ( Element.RequiredStateType NXOpen):  required state  .
        """
        pass
    def GetElementSequence(self) -> str:
        """
         Get the sequence of element in the navigator 
         Returns sequence (str):  sequence number .
        """
        pass
    def GetElementType(self) -> Element.ElementTypes:
        """
         Sets the type of the element 
         Returns type ( Element.ElementTypes NXOpen):  Element type .
        """
        pass
    def GetSubtype(self) -> str:
        """
         Get the element subtype name 
         Returns subtype (str):  element subtype name .
        """
        pass
    def GetSubtypeLibrarySourceSpecifiction(self) -> str:
        """
         Get the subtype library source specification 
         Returns specification (str):  subtype library source specification .
        """
        pass
    def GetWorkInstructionSpecification(self) -> str:
        """
         Get the work instruction specification 
         Returns specification (str):  work instruction specification .
        """
        pass
    def GetWorkInstructionTemplateSpecification(self) -> str:
        """
         Get the work instruction template specification 
         Returns specification (str):  work instruction template specification .
        """
        pass
    def OpenStyleSheetForReview(self) -> NXOpen.Part:
        """
         API open a style sheet for review. 
         Returns styleSheetPart ( NXOpen.Part): .
        """
        pass
    def RemoveProcessDocument(self, processDocument: str) -> None:
        """
         Removes a process document to a Bill of Process element 
        """
        pass
    def SetElementDescription(self, description: str) -> None:
        """
         Sets the description of element in the navigator 
        """
        pass
    def SetElementExpandState(self, expandState: bool) -> None:
        """
         Sets the expand state of element in the navigator 
        """
        pass
    def SetElementInstancemethod(self, instanceMethod: Element.InstanceMethodType) -> None:
        """
         Sets the instance method of element  
        """
        pass
    def SetElementRequiredstate(self, required: Element.RequiredStateType) -> None:
        """
         Sets the isRequired state of element  
        """
        pass
    def SetElementSequence(self, sequence: str) -> None:
        """
         Sets the sequence of element in the navigator 
        """
        pass
    def SetName(self, name: str) -> None:
        """
         Sets the name of the element 
        """
        pass
    def SetNextInSequence(self, nextElementInSequence: Element) -> None:
        """
         Sets the next element in sequence 
        """
        pass
class FolderElementBuilder(BaseBuilder): 
    """ Buider class """
    @property
    def AfterElement(self) -> SelectElement:
        """
        Getter for property: ( SelectElement NXOpen) AfterElement
         Returns the location selection item   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the property name item   
            
         
        """
        pass
    @Name.setter
    def Name(self, propertyNameItem: str):
        """
        Setter for property: (str) Name
         Returns the property name item   
            
         
        """
        pass
import NXOpen
class MaterialElementBuilder(BaseBuilder): 
    """ Builder class """
    @property
    def AfterElement(self) -> SelectElement:
        """
        Getter for property: ( SelectElement NXOpen) AfterElement
         Returns the location selection item   
            
         
        """
        pass
    @property
    def InstanceMethod(self) -> Element.InstanceMethodType:
        """
        Getter for property: ( Element.InstanceMethodType NXOpen) InstanceMethod
         Returns the property Instance method   
            
         
        """
        pass
    @InstanceMethod.setter
    def InstanceMethod(self, instanceMethod: Element.InstanceMethodType):
        """
        Setter for property: ( Element.InstanceMethodType NXOpen) InstanceMethod
         Returns the property Instance method   
            
         
        """
        pass
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
         Returns the material name   
            
         
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
    def Name(self, propertyNameItem: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @property
    def OccType(self) -> str:
        """
        Getter for property: (str) OccType
         Returns the material teamcenter occurrence type   
            
         
        """
        pass
    @OccType.setter
    def OccType(self, occType: str):
        """
        Setter for property: (str) OccType
         Returns the material teamcenter occurrence type   
            
         
        """
        pass
    @property
    def RequiredState(self) -> bool:
        """
        Getter for property: (bool) RequiredState
         Returns the property state ( required or not )   
            
         
        """
        pass
    @RequiredState.setter
    def RequiredState(self, requiredState: bool):
        """
        Setter for property: (bool) RequiredState
         Returns the property state ( required or not )   
            
         
        """
        pass
import NXOpen
class ModelElementBuilder(BaseBuilder): 
    """ Buider class """
    class JaPartmfgModelElementType(Enum):
        """
        Members Include: 
         |Model| 
         |Assembly| 
         |StageModel| 
         |StageModelSet| 
         |StageModelStockPart| 
         |NotDefined| 

        """
        Model: int
        Assembly: int
        StageModel: int
        StageModelSet: int
        StageModelStockPart: int
        NotDefined: int
        @staticmethod
        def ValueOf(value: int) -> ModelElementBuilder.JaPartmfgModelElementType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AfterElement(self) -> SelectElement:
        """
        Getter for property: ( SelectElement NXOpen) AfterElement
         Returns the location selection item   
            
         
        """
        pass
    @property
    def InstanceMethod(self) -> Element.InstanceMethodType:
        """
        Getter for property: ( Element.InstanceMethodType NXOpen) InstanceMethod
         Returns the property Instance method   
            
         
        """
        pass
    @InstanceMethod.setter
    def InstanceMethod(self, instanceMethod: Element.InstanceMethodType):
        """
        Setter for property: ( Element.InstanceMethodType NXOpen) InstanceMethod
         Returns the property Instance method   
            
         
        """
        pass
    @property
    def ModelFileBrowserItem(self) -> str:
        """
        Getter for property: (str) ModelFileBrowserItem
         Returns the model file browser item   
            
         
        """
        pass
    @ModelFileBrowserItem.setter
    def ModelFileBrowserItem(self, filename: str):
        """
        Setter for property: (str) ModelFileBrowserItem
         Returns the model file browser item   
            
         
        """
        pass
    @property
    def ModelType(self) -> ModelElementBuilder.JaPartmfgModelElementType:
        """
        Getter for property: ( ModelElementBuilder.JaPartmfgModelElementType NXOpen) ModelType
         Returns the model type   
            
         
        """
        pass
    @ModelType.setter
    def ModelType(self, partType: ModelElementBuilder.JaPartmfgModelElementType):
        """
        Setter for property: ( ModelElementBuilder.JaPartmfgModelElementType NXOpen) ModelType
         Returns the model type   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the model name item   
            
         
        """
        pass
    @Name.setter
    def Name(self, modelNameItem: str):
        """
        Setter for property: (str) Name
         Returns the model name item   
            
         
        """
        pass
    @property
    def RequiredState(self) -> bool:
        """
        Getter for property: (bool) RequiredState
         Returns the property state ( required or not )   
            
         
        """
        pass
    @RequiredState.setter
    def RequiredState(self, requiredState: bool):
        """
        Setter for property: (bool) RequiredState
         Returns the property state ( required or not )   
            
         
        """
        pass
import NXOpen
class ObjectStateManager(NXOpen.BaseObjectStateManager): 
    """ Represents Process Model object state manager which manages state of reused, wave-linked, copied objects.
    """
    pass
import NXOpen
class OperationBuilder(OperationElementBuilder): 
    """ Builder class """
    @property
    def ConsolidateGeometry(self) -> bool:
        """
        Getter for property: (bool) ConsolidateGeometry
         Returns the flag that determines whether to consolidate multiple geometry into a single feature   
            
         
        """
        pass
    @ConsolidateGeometry.setter
    def ConsolidateGeometry(self, consolidateGeometry: bool):
        """
        Setter for property: (bool) ConsolidateGeometry
         Returns the flag that determines whether to consolidate multiple geometry into a single feature   
            
         
        """
        pass
    @property
    def CreateAutomaticPmi(self) -> bool:
        """
        Getter for property: (bool) CreateAutomaticPmi
         Returns the flag that determines whether to automatically create PMI based to fill in those not specified by the manual PMI   
            
         
        """
        pass
    @CreateAutomaticPmi.setter
    def CreateAutomaticPmi(self, createAutomaticPmi: bool):
        """
        Setter for property: (bool) CreateAutomaticPmi
         Returns the flag that determines whether to automatically create PMI based to fill in those not specified by the manual PMI   
            
         
        """
        pass
    @property
    def Datums(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Datums
         Returns the datums   
            
         
        """
        pass
    @property
    def IdNumber(self) -> str:
        """
        Getter for property: (str) IdNumber
         Returns the id number   
            
         
        """
        pass
    @IdNumber.setter
    def IdNumber(self, idNumber: str):
        """
        Setter for property: (str) IdNumber
         Returns the id number   
            
         
        """
        pass
    @property
    def ManualPmi(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ManualPmi
         Returns the manual pmi   
            
         
        """
        pass
    @property
    def OperationSettings(self) -> OperationSettingsBuilder:
        """
        Getter for property: ( OperationSettingsBuilder NXOpen) OperationSettings
         Returns the create process toggle when set creates the process view   
            
         
        """
        pass
import NXOpen
class OperationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents the collection object for Operations in Process Modeler.
     """
    def CreateOperationBuilder(self, operation: Operation) -> OperationBuilder:
        """
                Creates an instance of NXOpen.PartMfg.OperationBuilder
                
         Returns builder ( OperationBuilder NXOpen): .
        """
        pass
import NXOpen
class OperationElementBuilder(BaseBuilder): 
    """ the builder """
    @property
    def AfterElement(self) -> SelectElement:
        """
        Getter for property: ( SelectElement NXOpen) AfterElement
         Returns the location selection item   
            
         
        """
        pass
    @property
    def Geometry(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Geometry
         Returns the select geometry   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the property name item   
            
         
        """
        pass
    @Name.setter
    def Name(self, propertyNameItem: str):
        """
        Setter for property: (str) Name
         Returns the property name item   
            
         
        """
        pass
    @property
    def SelectModel(self) -> SelectElement:
        """
        Getter for property: ( SelectElement NXOpen) SelectModel
         Returns the select model   
            
         
        """
        pass
    @property
    def SequenceNumber(self) -> str:
        """
        Getter for property: (str) SequenceNumber
         Returns the property sequence number   
            
         
        """
        pass
    @SequenceNumber.setter
    def SequenceNumber(self, sequenceNumber: str):
        """
        Setter for property: (str) SequenceNumber
         Returns the property sequence number   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class OperationSettingsBuilder(NXOpen.TaggedObject): 
    """
    Represents a OperationSettingsBuilder
    """
    @property
    def Tolerances(self) -> ToleranceSettingsBuilder:
        """
        Getter for property: ( ToleranceSettingsBuilder NXOpen) Tolerances
         Returns    the preferences general builder   
            
         
        """
        pass
class Operation(Element): 
    """ Represents an operation in a Process Model.
     """
    pass
import NXOpen
class PartMfgPart(NXOpen.Part): 
    """ Represents the PartMfg Part. It will provide the collections to access the BoP element.
     """
    @property
    def Elements() -> ElementCollection:
        """
         Returns the  NXOpen::PartMfg::ElementCollection   belonging to this part 
        """
        pass
    @property
    def Operations() -> OperationCollection:
        """
         Returns the  NXOpen::PartMfg::OperationCollection   belonging to this part 
        """
        pass
    @property
    def WorkInstructionManager() -> WorkInstructionManager:
        """
         Returns the  NXOpen::PartMfg::WorkInstructionManager   belonging to this part 
        """
        pass
    @property
    def CopyObjectsManager() -> CopyObjectsManager:
        """
         Returns the  NXOpen::PartMfg::CopyObjectsManager   belonging to this part 
        """
        pass
    def CreateAddElementToLibraryBuilder(self, element: Element) -> AddElementToLibraryBuilder:
        """
         Creates an instance of NXOpen.PartMfg.AddElementToLibraryBuilder 
         Returns builder ( AddElementToLibraryBuilder NXOpen): .
        """
        pass
    def CreateSaveAsTemplateBuilder(self) -> SaveAsTemplateBuilder:
        """
         Creates an instance of NXOpen.PartMfg.SaveAsTemplateBuilder 
         Returns builder ( SaveAsTemplateBuilder NXOpen): .
        """
        pass
    def GetDesignPart(self) -> NXOpen.Part:
        """
         Get the design part tag 
         Returns designPart ( NXOpen.Part):  design part .
        """
        pass
    def GetWorkInstructionSpecification(self) -> str:
        """
         Get the work instruction specification 
         Returns specification (str):  work instruction specification .
        """
        pass
    def GetWorkInstructionTemplateSpecification(self) -> str:
        """
         Get the work instruction template specification 
         Returns specification (str):  work instruction template specification .
        """
        pass
    def RefreshClientElements(self) -> None:
        """
         Refresh design model references
        """
        pass
class PMPart(PartMfgPart): 
    """ Represents the PMPart. It will provide the collections to access the PM element.
     """
    @property
    def ToleranceValidations() -> ToleranceCollection:
        """
         Returns the  NXOpen::PartMfg::ToleranceCollection   belonging to this part 
        """
        pass
    def CreatePmSaveAsTemplateBuilder(self) -> PMSaveAsTemplateBuilder:
        """
         Creates an instance of NXOpen.PartMfg.PMSaveAsTemplateBuilder 
         Returns builder ( PMSaveAsTemplateBuilder NXOpen): .
        """
        pass
import NXOpen
import NXOpen.PDM
class PMSaveAsTemplateBuilder(NXOpen.Builder): 
    """ Build class for NXOpen.PartMfg.PMSaveAsTemplateBuilder, used to create
        a Process Model template.
    """
    @property
    def IncludeGeometry(self) -> bool:
        """
        Getter for property: (bool) IncludeGeometry
         Returns the include geometry setting   
            
         
        """
        pass
    @IncludeGeometry.setter
    def IncludeGeometry(self, includeGeometry: bool):
        """
        Setter for property: (bool) IncludeGeometry
         Returns the include geometry setting   
            
         
        """
        pass
    @property
    def IncludeModelViews(self) -> bool:
        """
        Getter for property: (bool) IncludeModelViews
         Returns the include model views setting   
            
         
        """
        pass
    @IncludeModelViews.setter
    def IncludeModelViews(self, includeModelViews: bool):
        """
        Setter for property: (bool) IncludeModelViews
         Returns the include model views setting   
            
         
        """
        pass
    @property
    def IncludePmi(self) -> bool:
        """
        Getter for property: (bool) IncludePmi
         Returns the include pmi setting   
            
         
        """
        pass
    @IncludePmi.setter
    def IncludePmi(self, includePmi: bool):
        """
        Setter for property: (bool) IncludePmi
         Returns the include pmi setting   
            
         
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
    def TemplateFile(self) -> str:
        """
        Getter for property: (str) TemplateFile
         Returns the template file   
            
         
        """
        pass
    @TemplateFile.setter
    def TemplateFile(self, filename: str):
        """
        Setter for property: (str) TemplateFile
         Returns the template file   
            
         
        """
        pass
    def GetDescription(self) -> List[str]:
        """
         Returns the description 
         Returns description (List[str]): .
        """
        pass
    def GetPartOperationCreateBuilder(self) -> NXOpen.PDM.PartOperationBuilder:
        """
         Gets NXOpen.PDM.PartOperationBuilder 
         Returns partOperationCreateBuilder ( NXOpen.PDM.PartOperationBuilder): .
        """
        pass
    def SetDescription(self, description: List[str]) -> None:
        """
         Sets the description 
        """
        pass
    def SetPartOperationCreateBuilder(self, partOperationBuilder: NXOpen.PDM.PartOperationBuilder) -> None:
        """
         Sets NXOpen.PDM.PartOperationBuilder 
        """
        pass
import NXOpen
class ProcessTolerance(NXOpen.NXObject): 
    """ Represents a process tolerance in a Process Model.
     """
    pass
import NXOpen
class RefreshElementContent(NXOpen.TransientObject): 
    """ Represents an operation in a Process Model.
     """
    def Dispose(self) -> None:
        """
         Disposes the object 
        """
        pass
    def GetContextPart(self) -> BopPart:
        """
         Gets the Bill of Process part in which the refresh operation applies 
         Returns contextPart ( BopPart NXOpen): .
        """
        pass
    def GetElementsToSync(self) -> Tuple[List[Element], List[str]]:
        """
         Elements to synchronize 
         Returns A tuple consisting of (elements, identifiers). 
         - elements is:  Element List[NXOp. the elements .
         - identifiers is: List[str]. the identifiers .

        """
        pass
    def GetRefreshModel(self) -> NXOpen.Part:
        """
         Gets the model in which the refresh operation applies 
         Returns model ( NXOpen.Part): .
        """
        pass
    def SetSyncedElements(self, elements: List[Element], identifiers: List[str]) -> None:
        """
         Synchronized elements 
        """
        pass
import NXOpen
class ResourceElementBuilder(BaseBuilder): 
    """ Builder class """
    @property
    def AfterElement(self) -> SelectElement:
        """
        Getter for property: ( SelectElement NXOpen) AfterElement
         Returns the location selection item   
            
         
        """
        pass
    @property
    def InstanceMethod(self) -> Element.InstanceMethodType:
        """
        Getter for property: ( Element.InstanceMethodType NXOpen) InstanceMethod
         Returns the property Instance method   
            
         
        """
        pass
    @InstanceMethod.setter
    def InstanceMethod(self, instanceMethod: Element.InstanceMethodType):
        """
        Setter for property: ( Element.InstanceMethodType NXOpen) InstanceMethod
         Returns the property Instance method   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the property name item   
            
         
        """
        pass
    @Name.setter
    def Name(self, propertyNameItem: str):
        """
        Setter for property: (str) Name
         Returns the property name item   
            
         
        """
        pass
    @property
    def OccType(self) -> str:
        """
        Getter for property: (str) OccType
         Returns the resource teamcenter occurrence type   
            
         
        """
        pass
    @OccType.setter
    def OccType(self, occType: str):
        """
        Setter for property: (str) OccType
         Returns the resource teamcenter occurrence type   
            
         
        """
        pass
    @property
    def RequiredState(self) -> bool:
        """
        Getter for property: (bool) RequiredState
         Returns the property state ( required or not )   
            
         
        """
        pass
    @RequiredState.setter
    def RequiredState(self, requiredState: bool):
        """
        Setter for property: (bool) RequiredState
         Returns the property state ( required or not )   
            
         
        """
        pass
    @property
    def ResourceName(self) -> str:
        """
        Getter for property: (str) ResourceName
         Returns the resource property name   
            
         
        """
        pass
    @ResourceName.setter
    def ResourceName(self, resourceName: str):
        """
        Setter for property: (str) ResourceName
         Returns the resource property name   
            
         
        """
        pass
import NXOpen
class ReuseManager(NXOpen.Object): 
    """ Represents the Process Model Reuse Manager class."""
    def CreateObjectStateManager() -> ObjectStateManager:
        """
         Creates Process Model object state manager 
         Returns manager ( ObjectStateManager NXOpen): .
        """
        pass
    def CreateReusePmiBuilder(procModelPartTag: NXOpen.Part) -> ReusePmiBuilder:
        """
         Creates a NXOpen.PartMfg.ReusePmiBuilder 
         Returns builder ( ReusePmiBuilder NXOpen): .
        """
        pass
    def CreateReuseViewBuilder(procModelPartTag: NXOpen.Part) -> ReuseViewBuilder:
        """
         Creates a NXOpen.PartMfg.ReuseViewBuilder 
         Returns builder ( ReuseViewBuilder NXOpen): .
        """
        pass
import NXOpen
import NXOpen.Annotations
class ReusePmiBuilder(NXOpen.Builder): 
    """ Represents a  NXOpen.PartMfg.ReusePmiBuilder."""
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative PMI reuse value   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative PMI reuse value   
            
         
        """
        pass
    @property
    def ReusePMI(self) -> NXOpen.Annotations.PmiInterpartSelectionBuilder:
        """
        Getter for property: ( NXOpen.Annotations.PmiInterpartSelectionBuilder) ReusePMI
         Returns the list of selected PMI to be re-used   
            
         
        """
        pass
import NXOpen
class ReuseViewBuilder(NXOpen.Builder): 
    """ Represents a  NXOpen.PartMfg.ReuseViewBuilder."""
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative PMI reuse value   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative PMI reuse value   
            
         
        """
        pass
    @property
    def IncludePmi(self) -> bool:
        """
        Getter for property: (bool) IncludePmi
         Returns the include pmi setting   
            
         
        """
        pass
    @IncludePmi.setter
    def IncludePmi(self, includePmi: bool):
        """
        Setter for property: (bool) IncludePmi
         Returns the include pmi setting   
            
         
        """
        pass
    def GetSelectedViews(self) -> List[NXOpen.View]:
        """
         The selected views 
         Returns selectedViews ( NXOpen.View Li): .
        """
        pass
    def SetSelectedViews(self, selectedViews: List[NXOpen.View]) -> None:
        """
         The selected views 
        """
        pass
import NXOpen
class RoleElementBuilder(BaseBuilder): 
    """ Builder class """
    @property
    def AfterElement(self) -> SelectElement:
        """
        Getter for property: ( SelectElement NXOpen) AfterElement
         Returns the location selection item   
            
         
        """
        pass
    @property
    def InstanceMethod(self) -> Element.InstanceMethodType:
        """
        Getter for property: ( Element.InstanceMethodType NXOpen) InstanceMethod
         Returns the property Instance method   
            
         
        """
        pass
    @InstanceMethod.setter
    def InstanceMethod(self, instanceMethod: Element.InstanceMethodType):
        """
        Setter for property: ( Element.InstanceMethodType NXOpen) InstanceMethod
         Returns the property Instance method   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the property name item   
            
         
        """
        pass
    @Name.setter
    def Name(self, propertyNameItem: str):
        """
        Setter for property: (str) Name
         Returns the property name item   
            
         
        """
        pass
    @property
    def OccType(self) -> str:
        """
        Getter for property: (str) OccType
         Returns the role teamcenter occurrence type   
            
         
        """
        pass
    @OccType.setter
    def OccType(self, occType: str):
        """
        Setter for property: (str) OccType
         Returns the role teamcenter occurrence type   
            
         
        """
        pass
    @property
    def RequiredState(self) -> bool:
        """
        Getter for property: (bool) RequiredState
         Returns the property state ( required or not )   
            
         
        """
        pass
    @RequiredState.setter
    def RequiredState(self, requiredState: bool):
        """
        Setter for property: (bool) RequiredState
         Returns the property state ( required or not )   
            
         
        """
        pass
import NXOpen
import NXOpen.PDM
class SaveAsTemplateBuilder(NXOpen.Builder): 
    """ Build class for NXOpen.PartMfg.SaveAsTemplateBuilder, used to create
        a Bill of Process template.
    """
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
    def TemplateFile(self) -> str:
        """
        Getter for property: (str) TemplateFile
         Returns the template file   
            
         
        """
        pass
    @TemplateFile.setter
    def TemplateFile(self, filename: str):
        """
        Setter for property: (str) TemplateFile
         Returns the template file   
            
         
        """
        pass
    def GetDescription(self) -> List[str]:
        """
         Returns the description 
         Returns description (List[str]): .
        """
        pass
    def GetPartOperationCreateBuilder(self) -> NXOpen.PDM.PartOperationBuilder:
        """
         Gets NXOpen.PDM.PartOperationBuilder 
         Returns partOperationCreateBuilder ( NXOpen.PDM.PartOperationBuilder): .
        """
        pass
    def SetDescription(self, description: List[str]) -> None:
        """
         Sets the description 
        """
        pass
    def SetPartOperationCreateBuilder(self, partOperationBuilder: NXOpen.PDM.PartOperationBuilder) -> None:
        """
         Sets NXOpen.PDM.PartOperationBuilder 
        """
        pass
import NXOpen
class SaveStructureBuilder(NXOpen.Builder): 
    """ Builder class """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectAttributeTemplateBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.PartMfg.SelectAttributeTemplateBuilder.  This class is used
    to construct an attribute template seletion builder used to apply a collection of attributes to Bill of
    Process Elements.
    """
    def SetAttributeTemplateFile(self, attributeTemplate: str) -> None:
        """
         Set attribute template file 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectElement(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> Element:
        """
        Getter for property: ( Element NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: Element):
        """
        Setter for property: ( Element NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[Element, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  Element NXOpen. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Element, NXOpen.View, NXOpen.Point3d, Element, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  Element NXOpen. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  Element NXOpen. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def SetValue(self, selection: Element, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Element, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Element, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
import NXOpen
import NXOpen.Document
class SessionManager(NXOpen.Object): 
    """ Represents an NXOpen.PartMfg.SessionManager object.
     """
    @property
    def Clients() -> ClientManager:
        """
         Returns the  NXOpen::PartMfg::ClientManager  belonging to this part 
        """
        pass
    def CreateAttributeTemplateBuilder(part: NXOpen.Document.DocumentPart) -> StylesheetAttributeTemplatesBuilder:
        """
         Creates an instance of NXOpen.PartMfg.StylesheetAttributeTemplatesBuilder 
         Returns builder ( StylesheetAttributeTemplatesBuilder NXOpen): .
        """
        pass
    def CreateBlankBopPart(designPart: NXOpen.Part) -> BopPart:
        """
         Create blank bill of process part in session 
         Returns activeBillOfProcess ( BopPart NXOpen): .
        """
        pass
    def GetActiveBillOfProcess() -> BopPart:
        """
         Get a active bill of process part in session 
         Returns activeBillOfProcess ( BopPart NXOpen): .
        """
        pass
    def SetActiveBillOfProcess(activeBillOfProcess: BopPart) -> None:
        """
         Set a active bill of process part in session 
        """
        pass
class StepElementBuilder(BaseBuilder): 
    """ Builder class """
    class StepType(Enum):
        """
        Members Include: 
         |Generic| 
         |Manufacturing| 
         |Setup| 

        """
        Generic: int
        Manufacturing: int
        Setup: int
        @staticmethod
        def ValueOf(value: int) -> StepElementBuilder.StepType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the property name item   
            
         
        """
        pass
    @Name.setter
    def Name(self, propertyNameItem: str):
        """
        Setter for property: (str) Name
         Returns the property name item   
            
         
        """
        pass
    @property
    def ParentElement(self) -> SelectElement:
        """
        Getter for property: ( SelectElement NXOpen) ParentElement
         Returns the parent selection item   
            
         
        """
        pass
    @property
    def PropertyStepType(self) -> StepElementBuilder.StepType:
        """
        Getter for property: ( StepElementBuilder.StepType NXOpen) PropertyStepType
         Returns the property type item   
            
         
        """
        pass
    @PropertyStepType.setter
    def PropertyStepType(self, propertyTypeItem: StepElementBuilder.StepType):
        """
        Setter for property: ( StepElementBuilder.StepType NXOpen) PropertyStepType
         Returns the property type item   
            
         
        """
        pass
    @property
    def SequenceNumber(self) -> str:
        """
        Getter for property: (str) SequenceNumber
         Returns the property sequence number   
            
         
        """
        pass
    @SequenceNumber.setter
    def SequenceNumber(self, sequenceNumber: str):
        """
        Setter for property: (str) SequenceNumber
         Returns the property sequence number   
            
         
        """
        pass
import NXOpen.Document
class StylesheetAttributeTemplatesBuilder(NXOpen.Document.DocumentAttributeTemplatesBuilder): 
    """ Represents a AttributeTemplatesBuilder """
    @property
    def LockInUserMode(self) -> bool:
        """
        Getter for property: (bool) LockInUserMode
         Returns the user level lock status of attribute title   
            
         
        """
        pass
    @LockInUserMode.setter
    def LockInUserMode(self, status: bool):
        """
        Setter for property: (bool) LockInUserMode
         Returns the user level lock status of attribute title   
            
         
        """
        pass
import NXOpen
import NXOpen.Annotations
class ToleranceCollection(NXOpen.TaggedObjectCollection): 
    """ Represents the collection object for tolerance validation """
    def CreateToleranceValidationBuilder(self) -> ToleranceValidationBuilder:
        """
                Creates an instance of NXOpen.PartMfg.ToleranceValidationBuilder
                
         Returns builder ( ToleranceValidationBuilder NXOpen): .
        """
        pass
    def SetToleranceManufacturingMethod(self, pmi: NXOpen.Annotations.Pmi, method: str) -> None:
        """
                Set tolerance manufacturing method
                
        """
        pass
    def SetToleranceProcessCapability(self, pmi: NXOpen.Annotations.Pmi, proessCapability: float) -> None:
        """
                Set tolerance process capability
                
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ToleranceSettingsBuilder(NXOpen.TaggedObject): 
    """
        Process Modeler Operation Settings for Tolerances (Operation - Settings - Tolerances or Operation - MB3 - Settings - Tolerances)
    """
    class ToleranceType(Enum):
        """
        Members Include: 
         |Size| 
         |Form| 
         |Position| 

        """
        Size: int
        Form: int
        Position: int
        @staticmethod
        def ValueOf(value: int) -> ToleranceSettingsBuilder.ToleranceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssociativeReuse(self) -> bool:
        """
        Getter for property: (bool) AssociativeReuse
         Returns the associative reuse   
            
         
        """
        pass
    @AssociativeReuse.setter
    def AssociativeReuse(self, associativeReuse: bool):
        """
        Setter for property: (bool) AssociativeReuse
         Returns the associative reuse   
            
         
        """
        pass
    @property
    def Method(self) -> str:
        """
        Getter for property: (str) Method
         Returns the method which is generated from the tolerance table file  
            
         
        """
        pass
    @Method.setter
    def Method(self, method: str):
        """
        Setter for property: (str) Method
         Returns the method which is generated from the tolerance table file  
            
         
        """
        pass
    @property
    def ProcessCapability(self) -> float:
        """
        Getter for property: (float) ProcessCapability
         Returns the process capability   
            
         
        """
        pass
    @ProcessCapability.setter
    def ProcessCapability(self, processCapability: float):
        """
        Setter for property: (float) ProcessCapability
         Returns the process capability   
            
         
        """
        pass
    @property
    def ToleranceTableFile(self) -> str:
        """
        Getter for property: (str) ToleranceTableFile
         Returns the tolerance table file path   
            
         
        """
        pass
    @ToleranceTableFile.setter
    def ToleranceTableFile(self, filename: str):
        """
        Setter for property: (str) ToleranceTableFile
         Returns the tolerance table file path   
            
         
        """
        pass
    def GetToleranceTypes(self) -> List[ToleranceSettingsBuilder.ToleranceType]:
        """
         Returns the tolerance types 
         Returns toleranceTypes ( ToleranceSettingsBuilder.ToleranceType List[NXOp): The tolerance types .
        """
        pass
    def SetToleranceTypes(self, toleranceTypes: List[ToleranceSettingsBuilder.ToleranceType]) -> None:
        """
         Sets the tolerance types 
        """
        pass
import NXOpen
class ToleranceValidationBuilder(NXOpen.Builder): 
    """ Builder class """
    @property
    def ControlLimit(self) -> int:
        """
        Getter for property: (int) ControlLimit
         Returns the control limit   
            
         
        """
        pass
    @ControlLimit.setter
    def ControlLimit(self, controlLimit: int):
        """
        Setter for property: (int) ControlLimit
         Returns the control limit   
            
         
        """
        pass
    @property
    def Method(self) -> int:
        """
        Getter for property: (int) Method
         Returns the method   
            
         
        """
        pass
    @Method.setter
    def Method(self, method: int):
        """
        Setter for property: (int) Method
         Returns the method   
            
         
        """
        pass
    @property
    def TargetDesignCapability(self) -> float:
        """
        Getter for property: (float) TargetDesignCapability
         Returns the target design capability   
            
         
        """
        pass
    @TargetDesignCapability.setter
    def TargetDesignCapability(self, targetDesignCapability: float):
        """
        Setter for property: (float) TargetDesignCapability
         Returns the target design capability   
            
         
        """
        pass
import NXOpen
class ToleranceValidation(NXOpen.NXObject): 
    """ Represents tolerance validation in a process model """
    pass
import NXOpen
class WorkInstructionManager(NXOpen.Object): 
    """ Represents the manager object for Work instructions.
     """
    def CreateAssignWorkInstructionTemplateBuilder(self) -> AssignWorkInstructionTemplateBuilder:
        """
                Creates an instance of NXOpen.PartMfg.AssignWorkInstructionTemplateBuilder
                
         Returns builder ( AssignWorkInstructionTemplateBuilder NXOpen): .
        """
        pass
    def CreateTemplateBuilder(self) -> CreateWorkInstructionTemplateBuilder:
        """
                Creates an instance of NXOpen.PartMfg.CreateWorkInstructionTemplateBuilder
                
         Returns builder ( CreateWorkInstructionTemplateBuilder NXOpen): .
        """
        pass
    def CreateWorkInstructionBuilder(self) -> CreateWorkInstructionBuilder:
        """
                Creates an instance of NXOpen.PartMfg.CreateWorkInstructionBuilder
                
         Returns builder ( CreateWorkInstructionBuilder NXOpen): .
        """
        pass
