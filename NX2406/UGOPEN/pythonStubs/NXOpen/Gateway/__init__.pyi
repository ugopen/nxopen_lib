from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  This is the @link NXOpen::Gateway::BaseExplicitOrderBuilder NXOpen::Gateway::BaseExplicitOrderBuilder@endlink  for the explicit order <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class BaseExplicitOrderBuilder(NXOpen.Builder): 
    """ This is the <ja_class>NXOpen.Gateway.BaseExplicitOrderBuilder</ja_class> for the explicit order"""


    ## Getter for property: (str) SaveName
    ##  Returns the save name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def SaveName(self) -> str:
        """
        Getter for property: (str) SaveName
         Returns the save name   
            
         
        """
        pass
    
    ## Setter for property: (str) SaveName

    ##  Returns the save name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SaveName.setter
    def SaveName(self, saveName: str):
        """
        Setter for property: (str) SaveName
         Returns the save name   
            
         
        """
        pass
    
    ##  Clears the current order and restores it to the default order 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def Clear(self) -> None:
        """
         Clears the current order and restores it to the default order 
        """
        pass
    
    ##  Deletes the saved order/orders that has/have been selected by the user from the list of saved orders 
    ##  @return newOrder (List[str]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedEntries"> (List[str]) </param>
    ## <param name="currentOrder"> (List[str]) </param>
    ## <param name="numOfRemainingEntries"> (int) </param>
    def Delete(self, selectedEntries: List[str], currentOrder: List[str], numOfRemainingEntries: int) -> List[str]:
        """
         Deletes the saved order/orders that has/have been selected by the user from the list of saved orders 
         @return newOrder (List[str]): .
        """
        pass
    
    ##  Moves down the row/rows selected by the user in the lists 
    ##  @return newOrder (List[str]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedEntries"> (List[str]) </param>
    ## <param name="currentOrder"> (List[str]) </param>
    def DownArrow(self, selectedEntries: List[str], currentOrder: List[str]) -> List[str]:
        """
         Moves down the row/rows selected by the user in the lists 
         @return newOrder (List[str]): .
        """
        pass
    
    ##  Pastes the rows that have been previously selected using the cut operation 
    ##  @return newOrder (List[str]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pastePoint"> (int) </param>
    ## <param name="selectedEntries"> (List[str]) </param>
    ## <param name="currentOrder"> (List[str]) </param>
    def Paste(self, pastePoint: int, selectedEntries: List[str], currentOrder: List[str]) -> List[str]:
        """
         Pastes the rows that have been previously selected using the cut operation 
         @return newOrder (List[str]): .
        """
        pass
    
    ##  Saves an explicit order defined by the user 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="orderList"> (List[str]) </param>
    ## <param name="saveName"> (str) </param>
    def Save(self, orderList: List[str], saveName: str) -> None:
        """
         Saves an explicit order defined by the user 
        """
        pass
    
    ##  Saves the selected saved order in the form of a text file 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="savedOrderName"> (str) </param>
    ## <param name="saveFileName"> (str) </param>
    ## <param name="overwriteFile"> (bool) </param>
    def SaveAsTextFile(self, savedOrderName: str, saveFileName: str, overwriteFile: bool) -> None:
        """
         Saves the selected saved order in the form of a text file 
        """
        pass
    
    ##  Moves up the row/rows selected by the user in the lists 
    ##  @return newOrder (List[str]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedEntries"> (List[str]) </param>
    ## <param name="currentOrder"> (List[str]) </param>
    def UpArrow(self, selectedEntries: List[str], currentOrder: List[str]) -> List[str]:
        """
         Moves up the row/rows selected by the user in the lists 
         @return newOrder (List[str]): .
        """
        pass
    
import NXOpen
##  Represents operations which can be done on bookmark files.
##      <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class BookmarkFile(NXOpen.Object): 
    """ Represents operations which can be done on bookmark files.
    """


    ##  Deletes an existing bookmark file. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="pathName"> (str)  Full path name of existing bookmark file to delete </param>
    def Delete(pathName: str) -> None:
        """
         Deletes an existing bookmark file. 
        """
        pass
    
    ##  Renames an existing bookmark file. 
    ##  @return newPathName (str):  Full path name to the renamed bookmark file.
    ##                                                          This text string must be freed by the
    ##                                                          caller. .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="oldPathName"> (str)  Full path name of existing bookmark file. </param>
    ## <param name="newFileName"> (str)  New name to assign to the bookmark file.
    ##                                                          This will replace the basic name in
    ##                                                          the old path name. </param>
    ## <param name="okToOverwriteExistingFile"> (bool)  Is it okay to overwrite an existing file
    ##                                                          with the same name as the old path name plus
    ##                                                          the new file name? </param>
    def Rename(oldPathName: str, newFileName: str, okToOverwriteExistingFile: bool) -> str:
        """
         Renames an existing bookmark file. 
         @return newPathName (str):  Full path name to the renamed bookmark file.
                                                                 This text string must be freed by the
                                                                 caller. .
        """
        pass
    
    ##  Creates a bookmark file including a description.
    ##             See @link NXOpen::BasePart::BookmarkOption NXOpen::BasePart::BookmarkOption@endlink  for an explanation of the options
    ##             which are not supported in batch mode.  Also in batch mode, the description is not
    ##             written to the bookmark file. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="pathName"> (str)  Full path name of bookmark file. </param>
    ## <param name="bookmarkOption"> (@link NXOpen.BasePart.BookmarkOption NXOpen.BasePart.BookmarkOption@endlink)  See definitions of @link NXOpen::BasePart::BookmarkOption NXOpen::BasePart::BookmarkOption@endlink  </param>
    ## <param name="description"> (str)  A text string to be stored in the bookmark file </param>
    def SaveWithDescription(pathName: str, bookmarkOption: NXOpen.BasePart.BookmarkOption, description: str) -> None:
        """
         Creates a bookmark file including a description.
                    See @link NXOpen::BasePart::BookmarkOption NXOpen::BasePart::BookmarkOption@endlink  for an explanation of the options
                    which are not supported in batch mode.  Also in batch mode, the description is not
                    written to the bookmark file. 
        """
        pass
    
    ##  Changes the description of an existing bookmark file. Otherwise the bookmark file is unchanged. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="pathName"> (str)  Full path name of an existing bookmark file. </param>
    ## <param name="description"> (str)  A text string to replace the current description in the bookmark file </param>
    def SetDescription(pathName: str, description: str) -> None:
        """
         Changes the description of an existing bookmark file. Otherwise the bookmark file is unchanged. 
        """
        pass
    
import NXOpen
## 
## Represents a @link NXOpen::Gateway::CopyCutBuilder NXOpen::Gateway::CopyCutBuilder@endlink 
##  <br> To create a new instance of this class, use @link NXOpen::ClipboardOperationsManager::CreateCopyCutBuilder  NXOpen::ClipboardOperationsManager::CreateCopyCutBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class CopyCutBuilder(NXOpen.Builder): 
    """
Represents a <ja_class>NXOpen.Gateway.CopyCutBuilder</ja_class>
"""


    ##  Status of Copy or Cut Operation 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoObjectsCopied</term><description> 
    ##  No objects were successfully copied </description> </item><item><term> 
    ## NonExportableObjects</term><description> 
    ##  Certain non-exportable objects were not copied </description> </item><item><term> 
    ## PartExportFailed</term><description> 
    ##  Error while exporting part with copied/cut objects </description> </item><item><term> 
    ## ErrorDuringCut</term><description> 
    ##  Error during the cut operation </description> </item><item><term> 
    ## AllObjectsCopied</term><description> 
    ##  All objects were successfully copied </description> </item></list>
    class Status(Enum):
        """
        Members Include: <NoObjectsCopied> <NonExportableObjects> <PartExportFailed> <ErrorDuringCut> <AllObjectsCopied>
        """
        NoObjectsCopied: int
        NonExportableObjects: int
        PartExportFailed: int
        ErrorDuringCut: int
        AllObjectsCopied: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CopyCutBuilder.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CanCopyAsSketch
    ##  Returns a flag indicating whether to copy as sketch curves or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def CanCopyAsSketch(self) -> bool:
        """
        Getter for property: (bool) CanCopyAsSketch
         Returns a flag indicating whether to copy as sketch curves or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) CanCopyAsSketch

    ##  Returns a flag indicating whether to copy as sketch curves or not   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @CanCopyAsSketch.setter
    def CanCopyAsSketch(self, canCopyAsSketch: bool):
        """
        Setter for property: (bool) CanCopyAsSketch
         Returns a flag indicating whether to copy as sketch curves or not   
            
         
        """
        pass
    
    ## Getter for property: (bool) CopyNonAssociative
    ##  Returns the flag indicating if non-associative copy is being made.  
    ##    Non-associative copy is limited
    ##         to curve and body features where only geometry is copied without the feature.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def CopyNonAssociative(self) -> bool:
        """
        Getter for property: (bool) CopyNonAssociative
         Returns the flag indicating if non-associative copy is being made.  
           Non-associative copy is limited
                to curve and body features where only geometry is copied without the feature.   
         
        """
        pass
    
    ## Setter for property: (bool) CopyNonAssociative

    ##  Returns the flag indicating if non-associative copy is being made.  
    ##    Non-associative copy is limited
    ##         to curve and body features where only geometry is copied without the feature.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @CopyNonAssociative.setter
    def CopyNonAssociative(self, isCopyNonAssociative: bool):
        """
        Setter for property: (bool) CopyNonAssociative
         Returns the flag indicating if non-associative copy is being made.  
           Non-associative copy is limited
                to curve and body features where only geometry is copied without the feature.   
         
        """
        pass
    
    ## Getter for property: (str) DestinationFilename
    ##  Returns the string of the filename to which to copy or cut the objects to   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def DestinationFilename(self) -> str:
        """
        Getter for property: (str) DestinationFilename
         Returns the string of the filename to which to copy or cut the objects to   
            
         
        """
        pass
    
    ## Setter for property: (str) DestinationFilename

    ##  Returns the string of the filename to which to copy or cut the objects to   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @DestinationFilename.setter
    def DestinationFilename(self, filename: str):
        """
        Setter for property: (str) DestinationFilename
         Returns the string of the filename to which to copy or cut the objects to   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) InitialCopyLocation
    ##  Returns the initial copy location mainly used to define default copy location of sketch objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def InitialCopyLocation(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) InitialCopyLocation
         Returns the initial copy location mainly used to define default copy location of sketch objects   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) InitialCopyLocation

    ##  Returns the initial copy location mainly used to define default copy location of sketch objects   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @InitialCopyLocation.setter
    def InitialCopyLocation(self, copyLocation: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) InitialCopyLocation
         Returns the initial copy location mainly used to define default copy location of sketch objects   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsCut
    ##  Returns a flag indicating whether it is a copy or cut operation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def IsCut(self) -> bool:
        """
        Getter for property: (bool) IsCut
         Returns a flag indicating whether it is a copy or cut operation   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsCut

    ##  Returns a flag indicating whether it is a copy or cut operation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @IsCut.setter
    def IsCut(self, isCut: bool):
        """
        Setter for property: (bool) IsCut
         Returns a flag indicating whether it is a copy or cut operation   
            
         
        """
        pass
    
    ## Getter for property: (bool) ToClipboard
    ##  Returns a flag indicating whether copy cut to clipboard or copy cut to a file  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def ToClipboard(self) -> bool:
        """
        Getter for property: (bool) ToClipboard
         Returns a flag indicating whether copy cut to clipboard or copy cut to a file  
            
         
        """
        pass
    
    ## Setter for property: (bool) ToClipboard

    ##  Returns a flag indicating whether copy cut to clipboard or copy cut to a file  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ToClipboard.setter
    def ToClipboard(self, isToClipboard: bool):
        """
        Setter for property: (bool) ToClipboard
         Returns a flag indicating whether copy cut to clipboard or copy cut to a file  
            
         
        """
        pass
    
    ##  Gets the status of copy-cut operation 
    ##  @return copyCutStatus (@link CopyCutBuilder.Status NXOpen.Gateway.CopyCutBuilder.Status@endlink): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def GetCopyCutStatus(self) -> CopyCutBuilder.Status:
        """
         Gets the status of copy-cut operation 
         @return copyCutStatus (@link CopyCutBuilder.Status NXOpen.Gateway.CopyCutBuilder.Status@endlink): .
        """
        pass
    
    ##  Gets all non-exportable objects 
    ##  @return nonExportableObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  All the non-exportable objects .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def GetNonExportableObjects(self) -> List[NXOpen.NXObject]:
        """
         Gets all non-exportable objects 
         @return nonExportableObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  All the non-exportable objects .
        """
        pass
    
    ##  Gets all objects to be copied or to be cut 
    ##  @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  All the objects to be copied or to be cut.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def GetObjects(self) -> List[NXOpen.NXObject]:
        """
         Gets all objects to be copied or to be cut 
         @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  All the objects to be copied or to be cut.
        """
        pass
    
    ##  Reset the initial copy location. After this previously set initial copy location will not be used 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def ResetInitialCopyLocation(self) -> None:
        """
         Reset the initial copy location. After this previously set initial copy location will not be used 
        """
        pass
    
    ##  Sets objects to be copied or cut. Note that PMI, feature, drafting view and other drafting objects are not supported by this class. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  All the objects to be copied or to be cut</param>
    def SetObjects(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Sets objects to be copied or cut. Note that PMI, feature, drafting view and other drafting objects are not supported by this class. 
        """
        pass
    
import NXOpen
##   @brief  Represents a manager class to manage file new templates  
## 
##   <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class FileNewTemplateManager(NXOpen.Object): 
    """ <summary> Represents a manager class to manage file new templates </summary>"""


    ##  This function creates the template creation object 
    ##  @return templateNode (@link FileNewTemplateNode NXOpen.Gateway.FileNewTemplateNode@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="seedPart"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="tabName"> (str) </param>
    ## <param name="relationType"> (str) </param>
    ## <param name="templateApplication"> (str) </param>
    ## <param name="itemType"> (str) </param>
    def CreateFileNewTemplateNode(seedPart: NXOpen.Part, tabName: str, relationType: str, templateApplication: str, itemType: str) -> FileNewTemplateNode:
        """
         This function creates the template creation object 
         @return templateNode (@link FileNewTemplateNode NXOpen.Gateway.FileNewTemplateNode@endlink): .
        """
        pass
    
    ##  Destroys the object 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="templateNode"> (@link FileNewTemplateNode NXOpen.Gateway.FileNewTemplateNode@endlink) </param>
    def Free(templateNode: FileNewTemplateNode) -> None:
        """
         Destroys the object 
        """
        pass
    
    ##  Saves the part as template with given information 
    ##  @return errorList (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Errors encountered .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="templateNode"> (@link FileNewTemplateNode NXOpen.Gateway.FileNewTemplateNode@endlink) </param>
    def SaveAsTemplate(templateNode: FileNewTemplateNode) -> NXOpen.ErrorList:
        """
         Saves the part as template with given information 
         @return errorList (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Errors encountered .
        """
        pass
    
import NXOpen
## 
##     Represents the class that contains effectivity parameters.
##      <br> Use @link NXOpen::Gateway::FileNewTemplateManager::CreateFileNewTemplateNode NXOpen::Gateway::FileNewTemplateManager::CreateFileNewTemplateNode@endlink  to create instance of this class.  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class FileNewTemplateNode(NXOpen.NXObject): 
    """
    Represents the class that contains effectivity parameters.
    """


    ##  SetDescrption 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attrValue"> (str) </param>
    def SetDescription(self, attrValue: str) -> None:
        """
         SetDescrption 
        """
        pass
    
    ##  SetItemType
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attrValue"> (str) </param>
    def SetItemType(self, attrValue: str) -> None:
        """
         SetItemType
        """
        pass
    
    ##  SetRelationType 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attrValue"> (str) </param>
    def SetRelationType(self, attrValue: str) -> None:
        """
         SetRelationType 
        """
        pass
    
    ##  SetTemplateApplication 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attrValue"> (str) </param>
    def SetTemplateApplication(self, attrValue: str) -> None:
        """
         SetTemplateApplication 
        """
        pass
    
    ##  SetTemplatePresentationName 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attrValue"> (str) </param>
    def SetTemplatePresentationName(self, attrValue: str) -> None:
        """
         SetTemplatePresentationName 
        """
        pass
    
import NXOpen
import NXOpen.PDM
##  Represents a builder class that performs Generic File New operations. 
##          <br> To create a new instance of this class, use @link NXOpen::PartCollection::CreateGenericFileNewBuilder  NXOpen::PartCollection::CreateGenericFileNewBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class GenericFileNewBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Generic File New operations. 
        """


    ##  Creates the pre-creation objects for the parts 
    ##  @return logicalObjects (@link NXOpen.PDM.LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def CreateLogicalObjects(self) -> List[NXOpen.PDM.LogicalObject]:
        """
         Creates the pre-creation objects for the parts 
         @return logicalObjects (@link NXOpen.PDM.LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
        """
        pass
    
    ##  Sets @link NXOpen::Gateway::IGenericFileNewApplicationBuilder NXOpen::Gateway::IGenericFileNewApplicationBuilder@endlink  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="applicationBuilder"> (@link IGenericFileNewApplicationBuilder NXOpen.Gateway.IGenericFileNewApplicationBuilder@endlink) </param>
    def SetApplicationBuilder(self, applicationBuilder: IGenericFileNewApplicationBuilder) -> None:
        """
         Sets @link NXOpen::Gateway::IGenericFileNewApplicationBuilder NXOpen::Gateway::IGenericFileNewApplicationBuilder@endlink  
        """
        pass
    
import NXOpen
## 
##         Represents the class Application Builder.
##      <br> Instances of this class can be accessed through various application specific builders  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class IGenericFileNewApplicationBuilder(NXOpen.Builder): 
    """
        Represents the class Application Builder.
    """
    pass


import NXOpen
##  Represents a @link NXOpen::Gateway::ImageCaptureBuilder NXOpen::Gateway::ImageCaptureBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Gateway::ImageCaptureManager::CreateImageCaptureBuilder  NXOpen::Gateway::ImageCaptureManager::CreateImageCaptureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CaptureMethod </term> <description> 
##  
## GraphicsArea </description> </item> 
## 
## <item><term> 
##  
## Format </term> <description> 
##  
## Bmp </description> </item> 
## 
## <item><term> 
##  
## Size </term> <description> 
##  
## Pixels64 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class ImageCaptureBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Gateway.ImageCaptureBuilder</ja_class> builder """


    ##  the selection method
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## GraphicsArea</term><description> 
    ##  the graphics area</description> </item><item><term> 
    ## Region</term><description> 
    ##  the region area</description> </item><item><term> 
    ## File</term><description> 
    ##  the input from file</description> </item><item><term> 
    ## Automatic</term><description> 
    ##  the automatic preview mode</description> </item></list>
    class CaptureMethodType(Enum):
        """
        Members Include: <GraphicsArea> <Region> <File> <Automatic>
        """
        GraphicsArea: int
        Region: int
        File: int
        Automatic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ImageCaptureBuilder.CaptureMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the image format
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Bmp</term><description> 
    ##  the bmp image format</description> </item><item><term> 
    ## Jpg</term><description> 
    ##  the jpg image format</description> </item><item><term> 
    ## Gif</term><description> 
    ##  the gif image format</description> </item><item><term> 
    ## Png</term><description> 
    ##  the png image format</description> </item><item><term> 
    ## Tiff</term><description> 
    ##  the tiff image format</description> </item></list>
    class ImageFormat(Enum):
        """
        Members Include: <Bmp> <Jpg> <Gif> <Png> <Tiff>
        """
        Bmp: int
        Jpg: int
        Gif: int
        Png: int
        Tiff: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ImageCaptureBuilder.ImageFormat:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the image size
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Pixels16</term><description> 
    ##  the 16 pixel size</description> </item><item><term> 
    ## Pixels24</term><description> 
    ##  the 24 pixel size</description> </item><item><term> 
    ## Pixels32</term><description> 
    ##  the 32 pixel size</description> </item><item><term> 
    ## Pixels48</term><description> 
    ##  the 48 pixel size</description> </item><item><term> 
    ## Pixels64</term><description> 
    ##  the 64 pixel size</description> </item><item><term> 
    ## Pixels96</term><description> 
    ##  the 96 pixel size</description> </item><item><term> 
    ## Pixels128</term><description> 
    ##  the 128 pixel size</description> </item></list>
    class ImageSize(Enum):
        """
        Members Include: <Pixels16> <Pixels24> <Pixels32> <Pixels48> <Pixels64> <Pixels96> <Pixels128>
        """
        Pixels16: int
        Pixels24: int
        Pixels32: int
        Pixels48: int
        Pixels64: int
        Pixels96: int
        Pixels128: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ImageCaptureBuilder.ImageSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ImageCaptureBuilder.CaptureMethodType NXOpen.Gateway.ImageCaptureBuilder.CaptureMethodType@endlink) CaptureMethod
    ##  Returns the capture method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return ImageCaptureBuilder.CaptureMethodType
    @property
    def CaptureMethod(self) -> ImageCaptureBuilder.CaptureMethodType:
        """
        Getter for property: (@link ImageCaptureBuilder.CaptureMethodType NXOpen.Gateway.ImageCaptureBuilder.CaptureMethodType@endlink) CaptureMethod
         Returns the capture method   
            
         
        """
        pass
    
    ## Setter for property: (@link ImageCaptureBuilder.CaptureMethodType NXOpen.Gateway.ImageCaptureBuilder.CaptureMethodType@endlink) CaptureMethod

    ##  Returns the capture method   
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @CaptureMethod.setter
    def CaptureMethod(self, captureMethod: ImageCaptureBuilder.CaptureMethodType):
        """
        Setter for property: (@link ImageCaptureBuilder.CaptureMethodType NXOpen.Gateway.ImageCaptureBuilder.CaptureMethodType@endlink) CaptureMethod
         Returns the capture method   
            
         
        """
        pass
    
    ## Getter for property: (str) File
    ##  Returns the file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def File(self) -> str:
        """
        Getter for property: (str) File
         Returns the file   
            
         
        """
        pass
    
    ## Setter for property: (str) File

    ##  Returns the file   
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @File.setter
    def File(self, filename: str):
        """
        Setter for property: (str) File
         Returns the file   
            
         
        """
        pass
    
    ## Getter for property: (@link ImageCaptureBuilder.ImageFormat NXOpen.Gateway.ImageCaptureBuilder.ImageFormat@endlink) Format
    ##  Returns the format   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return ImageCaptureBuilder.ImageFormat
    @property
    def Format(self) -> ImageCaptureBuilder.ImageFormat:
        """
        Getter for property: (@link ImageCaptureBuilder.ImageFormat NXOpen.Gateway.ImageCaptureBuilder.ImageFormat@endlink) Format
         Returns the format   
            
         
        """
        pass
    
    ## Setter for property: (@link ImageCaptureBuilder.ImageFormat NXOpen.Gateway.ImageCaptureBuilder.ImageFormat@endlink) Format

    ##  Returns the format   
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Format.setter
    def Format(self, format: ImageCaptureBuilder.ImageFormat):
        """
        Setter for property: (@link ImageCaptureBuilder.ImageFormat NXOpen.Gateway.ImageCaptureBuilder.ImageFormat@endlink) Format
         Returns the format   
            
         
        """
        pass
    
    ## Getter for property: (str) ImageFile
    ##  Returns the image file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def ImageFile(self) -> str:
        """
        Getter for property: (str) ImageFile
         Returns the image file   
            
         
        """
        pass
    
    ## Setter for property: (str) ImageFile

    ##  Returns the image file   
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ImageFile.setter
    def ImageFile(self, imageFilename: str):
        """
        Setter for property: (str) ImageFile
         Returns the image file   
            
         
        """
        pass
    
    ## Getter for property: (@link ImageCaptureBuilder.ImageSize NXOpen.Gateway.ImageCaptureBuilder.ImageSize@endlink) Size
    ##  Returns the size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return ImageCaptureBuilder.ImageSize
    @property
    def Size(self) -> ImageCaptureBuilder.ImageSize:
        """
        Getter for property: (@link ImageCaptureBuilder.ImageSize NXOpen.Gateway.ImageCaptureBuilder.ImageSize@endlink) Size
         Returns the size   
            
         
        """
        pass
    
    ## Setter for property: (@link ImageCaptureBuilder.ImageSize NXOpen.Gateway.ImageCaptureBuilder.ImageSize@endlink) Size

    ##  Returns the size   
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Size.setter
    def Size(self, size: ImageCaptureBuilder.ImageSize):
        """
        Setter for property: (@link ImageCaptureBuilder.ImageSize NXOpen.Gateway.ImageCaptureBuilder.ImageSize@endlink) Size
         Returns the size   
            
         
        """
        pass
    
    ##  Returns the region 
    ##  @return A tuple consisting of (topLeftCorner, bottomRightCorner). 
    ##  - topLeftCorner is: List[int]. Array of 2 integers for Top Left Corner of Region .
    ##  - bottomRightCorner is: List[int]. Array of 2 integers for Bottom Right Corner of Region .

    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def GetRegion(self) -> Tuple[List[int], List[int]]:
        """
         Returns the region 
         @return A tuple consisting of (topLeftCorner, bottomRightCorner). 
         - topLeftCorner is: List[int]. Array of 2 integers for Top Left Corner of Region .
         - bottomRightCorner is: List[int]. Array of 2 integers for Bottom Right Corner of Region .

        """
        pass
    
    ##  Sets the region 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ## 
    ## <param name="topLeftCorner"> (List[int])  Array of 2 integers for Top Left Corner of Region </param>
    ## <param name="bottomRightCorner"> (List[int])  Array of 2 integers for Bottom Right Corner of Region </param>
    def SetRegion(self, topLeftCorner: List[int], bottomRightCorner: List[int]) -> None:
        """
         Sets the region 
        """
        pass
    
import NXOpen
##  The ImageCaptureManager class provides methods to create 
##     @link NXOpen::Gateway::ImageCaptureBuilder NXOpen::Gateway::ImageCaptureBuilder@endlink  object <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class ImageCaptureManager(NXOpen.Object): 
    """ The ImageCaptureManager class provides methods to create 
    <ja_class>NXOpen.Gateway.ImageCaptureBuilder</ja_class> object"""


    ##  Creates a @link NXOpen::Gateway::ImageCaptureBuilder NXOpen::Gateway::ImageCaptureBuilder@endlink  
    ##  @return builder (@link ImageCaptureBuilder NXOpen.Gateway.ImageCaptureBuilder@endlink): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def CreateImageCaptureBuilder(self) -> ImageCaptureBuilder:
        """
         Creates a @link NXOpen::Gateway::ImageCaptureBuilder NXOpen::Gateway::ImageCaptureBuilder@endlink  
         @return builder (@link ImageCaptureBuilder NXOpen.Gateway.ImageCaptureBuilder@endlink): .
        """
        pass
    
import NXOpen
## 
##      @brief 
##         Captures the image in the active graphics window (or in a rectangular region of the active
##         graphics window), and then exports/saves the image in a file of a specified format.
##      
## 
##  
##     
##         This class can be used to export an image file that contains the contents of the
##         active graphics window.  The image may be limited to a rectangular region of the display
##         via @link Gateway::ImageExportBuilder::SetRegionMode Gateway::ImageExportBuilder::SetRegionMode@endlink .
##         @link Gateway::ImageExportBuilder::FileFormats Gateway::ImageExportBuilder::FileFormats@endlink  enumerates
##         the file formats exported images may be saved in.
##         The background of the exported image may be changed to any
##         of the options available in
##         @link Gateway::ImageExportBuilder::BackgroundOptions Gateway::ImageExportBuilder::BackgroundOptions@endlink .
##         After configuring the image export, an image file is saved by calling the Commit
##         method.
##     
##      <br> To create a new instance of this class, use @link NXOpen::ViewCollection::CreateImageExportBuilder  NXOpen::ViewCollection::CreateImageExportBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BackgroundOption </term> <description> 
##  
## Original </description> </item> 
## 
## <item><term> 
##  
## FileFormat </term> <description> 
##  
## Png </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX12.0.1  <br> 

class ImageExportBuilder(NXOpen.Builder): 
    """
    <summary>
        Captures the image in the active graphics window (or in a rectangular region of the active
        graphics window), and then exports/saves the image in a file of a specified format.
    </summary>
    <remarks>
        This class can be used to export an image file that contains the contents of the
        active graphics window.  The image may be limited to a rectangular region of the display
        via <ja_property_set>Gateway.ImageExportBuilder.RegionMode</ja_property_set>.
        <ja_enum>Gateway.ImageExportBuilder.FileFormats</ja_enum> enumerates
        the file formats exported images may be saved in.
        The background of the exported image may be changed to any
        of the options available in
        <ja_enum>Gateway.ImageExportBuilder.BackgroundOptions</ja_enum>.
        After configuring the image export, an image file is saved by calling the Commit
        method.
    </remarks>
    """


    ## 
    ##          @brief 
    ##             The background style of the captured image.
    ##          
    ## 
    ##  
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Original</term><description> 
    ##  Use the currently displayed background </description> </item><item><term> 
    ## CustomColor</term><description> 
    ##  Use the solid color set by @link Gateway::ImageExportBuilder::SetCustomBackgroundColor Gateway::ImageExportBuilder::SetCustomBackgroundColor@endlink  </description> </item><item><term> 
    ## Transparent</term><description> 
    ##  Use a transparent background (only available in PNG and TIFF file formats) </description> </item></list>
    class BackgroundOptions(Enum):
        """
        Members Include: <Original> <CustomColor> <Transparent>
        """
        Original: int
        CustomColor: int
        Transparent: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ImageExportBuilder.BackgroundOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##          @brief 
    ##             The format of the exported image file.
    ##          
    ## 
    ##  
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Png</term><description> 
    ##  PNG File Format </description> </item><item><term> 
    ## Jpg</term><description> 
    ##  JPG File Format </description> </item><item><term> 
    ## Gif</term><description> 
    ##  GIF File Format </description> </item><item><term> 
    ## Tiff</term><description> 
    ##  Compressed TIFF File Format</description> </item><item><term> 
    ## Bmp</term><description> 
    ##  BMP File Format (Windows Only) </description> </item><item><term> 
    ## Xwd</term><description> 
    ##  XWD File Format (Unix Only) </description> </item></list>
    class FileFormats(Enum):
        """
        Members Include: <Png> <Jpg> <Gif> <Tiff> <Bmp> <Xwd>
        """
        Png: int
        Jpg: int
        Gif: int
        Tiff: int
        Bmp: int
        Xwd: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ImageExportBuilder.FileFormats:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ImageExportBuilder.BackgroundOptions NXOpen.Gateway.ImageExportBuilder.BackgroundOptions@endlink) BackgroundOption
    ##  Returns
    ##          @brief 
    ##             the background style used when capturing the image.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             The image may be captured with any of the background styles enumerated in
    ##             @link Gateway::ImageExportBuilder::BackgroundOptions Gateway::ImageExportBuilder::BackgroundOptions@endlink .  If the Custom Color background
    ##             option is used, the background color may be specified with
    ##             @link Gateway::ImageExportBuilder::SetCustomBackgroundColor Gateway::ImageExportBuilder::SetCustomBackgroundColor@endlink .
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return ImageExportBuilder.BackgroundOptions
    @property
    def BackgroundOption(self) -> ImageExportBuilder.BackgroundOptions:
        """
        Getter for property: (@link ImageExportBuilder.BackgroundOptions NXOpen.Gateway.ImageExportBuilder.BackgroundOptions@endlink) BackgroundOption
         Returns
                 @brief 
                    the background style used when capturing the image.  
          
                 
        
         
                
                    The image may be captured with any of the background styles enumerated in
                    @link Gateway::ImageExportBuilder::BackgroundOptions Gateway::ImageExportBuilder::BackgroundOptions@endlink .  If the Custom Color background
                    option is used, the background color may be specified with
                    @link Gateway::ImageExportBuilder::SetCustomBackgroundColor Gateway::ImageExportBuilder::SetCustomBackgroundColor@endlink .
                
                  
         
        """
        pass
    
    ## Setter for property: (@link ImageExportBuilder.BackgroundOptions NXOpen.Gateway.ImageExportBuilder.BackgroundOptions@endlink) BackgroundOption

    ##  Returns
    ##          @brief 
    ##             the background style used when capturing the image.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             The image may be captured with any of the background styles enumerated in
    ##             @link Gateway::ImageExportBuilder::BackgroundOptions Gateway::ImageExportBuilder::BackgroundOptions@endlink .  If the Custom Color background
    ##             option is used, the background color may be specified with
    ##             @link Gateway::ImageExportBuilder::SetCustomBackgroundColor Gateway::ImageExportBuilder::SetCustomBackgroundColor@endlink .
    ##         
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @BackgroundOption.setter
    def BackgroundOption(self, backgroundOption: ImageExportBuilder.BackgroundOptions):
        """
        Setter for property: (@link ImageExportBuilder.BackgroundOptions NXOpen.Gateway.ImageExportBuilder.BackgroundOptions@endlink) BackgroundOption
         Returns
                 @brief 
                    the background style used when capturing the image.  
          
                 
        
         
                
                    The image may be captured with any of the background styles enumerated in
                    @link Gateway::ImageExportBuilder::BackgroundOptions Gateway::ImageExportBuilder::BackgroundOptions@endlink .  If the Custom Color background
                    option is used, the background color may be specified with
                    @link Gateway::ImageExportBuilder::SetCustomBackgroundColor Gateway::ImageExportBuilder::SetCustomBackgroundColor@endlink .
                
                  
         
        """
        pass
    
    ## Getter for property: (int) DeviceHeight
    ##  Returns
    ##          @brief 
    ##             the height of the graphics device.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             When capturing entire device content, this is image height in pixels.
    ##             Specifying zero uses default device height.
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def DeviceHeight(self) -> int:
        """
        Getter for property: (int) DeviceHeight
         Returns
                 @brief 
                    the height of the graphics device.  
          
                 
        
         
                
                    When capturing entire device content, this is image height in pixels.
                    Specifying zero uses default device height.
                
                  
         
        """
        pass
    
    ## Setter for property: (int) DeviceHeight

    ##  Returns
    ##          @brief 
    ##             the height of the graphics device.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             When capturing entire device content, this is image height in pixels.
    ##             Specifying zero uses default device height.
    ##         
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DeviceHeight.setter
    def DeviceHeight(self, deviceHeight: int):
        """
        Setter for property: (int) DeviceHeight
         Returns
                 @brief 
                    the height of the graphics device.  
          
                 
        
         
                
                    When capturing entire device content, this is image height in pixels.
                    Specifying zero uses default device height.
                
                  
         
        """
        pass
    
    ## Getter for property: (int) DeviceWidth
    ##  Returns
    ##          @brief 
    ##             the width of the graphics device.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             When capturing entire device content, this is image width in pixels.
    ##             Specifying zero uses default device width.
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def DeviceWidth(self) -> int:
        """
        Getter for property: (int) DeviceWidth
         Returns
                 @brief 
                    the width of the graphics device.  
          
                 
        
         
                
                    When capturing entire device content, this is image width in pixels.
                    Specifying zero uses default device width.
                
                  
         
        """
        pass
    
    ## Setter for property: (int) DeviceWidth

    ##  Returns
    ##          @brief 
    ##             the width of the graphics device.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             When capturing entire device content, this is image width in pixels.
    ##             Specifying zero uses default device width.
    ##         
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DeviceWidth.setter
    def DeviceWidth(self, deviceWidth: int):
        """
        Setter for property: (int) DeviceWidth
         Returns
                 @brief 
                    the width of the graphics device.  
          
                 
        
         
                
                    When capturing entire device content, this is image width in pixels.
                    Specifying zero uses default device width.
                
                  
         
        """
        pass
    
    ## Getter for property: (bool) EnhanceEdges
    ##  Returns
    ##          @brief 
    ##             a boolean value that, if true, indicates the image will be captured with antialiasing disabled and edge emphasis enabled.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             When capturing an image with many edges, such as a wireframe view of a part, antialiasing may cause thin edges to blur with the
    ##             background of the image.  This effect may be particularly noticeable when using a transparent background.  Disabling antialiasing
    ##             and enabling edge emphasis helps to eliminate this blurring at the cost of a more pixelated image.
    ##             
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def EnhanceEdges(self) -> bool:
        """
        Getter for property: (bool) EnhanceEdges
         Returns
                 @brief 
                    a boolean value that, if true, indicates the image will be captured with antialiasing disabled and edge emphasis enabled.  
          
                 
        
         
                
                    When capturing an image with many edges, such as a wireframe view of a part, antialiasing may cause thin edges to blur with the
                    background of the image.  This effect may be particularly noticeable when using a transparent background.  Disabling antialiasing
                    and enabling edge emphasis helps to eliminate this blurring at the cost of a more pixelated image.
                    
                  
         
        """
        pass
    
    ## Setter for property: (bool) EnhanceEdges

    ##  Returns
    ##          @brief 
    ##             a boolean value that, if true, indicates the image will be captured with antialiasing disabled and edge emphasis enabled.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             When capturing an image with many edges, such as a wireframe view of a part, antialiasing may cause thin edges to blur with the
    ##             background of the image.  This effect may be particularly noticeable when using a transparent background.  Disabling antialiasing
    ##             and enabling edge emphasis helps to eliminate this blurring at the cost of a more pixelated image.
    ##             
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @EnhanceEdges.setter
    def EnhanceEdges(self, enhanceEdges: bool):
        """
        Setter for property: (bool) EnhanceEdges
         Returns
                 @brief 
                    a boolean value that, if true, indicates the image will be captured with antialiasing disabled and edge emphasis enabled.  
          
                 
        
         
                
                    When capturing an image with many edges, such as a wireframe view of a part, antialiasing may cause thin edges to blur with the
                    background of the image.  This effect may be particularly noticeable when using a transparent background.  Disabling antialiasing
                    and enabling edge emphasis helps to eliminate this blurring at the cost of a more pixelated image.
                    
                  
         
        """
        pass
    
    ## Getter for property: (@link ImageExportBuilder.FileFormats NXOpen.Gateway.ImageExportBuilder.FileFormats@endlink) FileFormat
    ##  Returns
    ##          @brief 
    ##             the file format of the exported image file.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             The exported image may be stored in any of the file formats enumerated in
    ##             @link Gateway::ImageExportBuilder::FileFormats Gateway::ImageExportBuilder::FileFormats@endlink .  Please note that transparency is only
    ##             available in TIFF and PNG formats.
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return ImageExportBuilder.FileFormats
    @property
    def FileFormat(self) -> ImageExportBuilder.FileFormats:
        """
        Getter for property: (@link ImageExportBuilder.FileFormats NXOpen.Gateway.ImageExportBuilder.FileFormats@endlink) FileFormat
         Returns
                 @brief 
                    the file format of the exported image file.  
          
                 
        
         
                
                    The exported image may be stored in any of the file formats enumerated in
                    @link Gateway::ImageExportBuilder::FileFormats Gateway::ImageExportBuilder::FileFormats@endlink .  Please note that transparency is only
                    available in TIFF and PNG formats.
                
                  
         
        """
        pass
    
    ## Setter for property: (@link ImageExportBuilder.FileFormats NXOpen.Gateway.ImageExportBuilder.FileFormats@endlink) FileFormat

    ##  Returns
    ##          @brief 
    ##             the file format of the exported image file.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             The exported image may be stored in any of the file formats enumerated in
    ##             @link Gateway::ImageExportBuilder::FileFormats Gateway::ImageExportBuilder::FileFormats@endlink .  Please note that transparency is only
    ##             available in TIFF and PNG formats.
    ##         
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @FileFormat.setter
    def FileFormat(self, fileFormat: ImageExportBuilder.FileFormats):
        """
        Setter for property: (@link ImageExportBuilder.FileFormats NXOpen.Gateway.ImageExportBuilder.FileFormats@endlink) FileFormat
         Returns
                 @brief 
                    the file format of the exported image file.  
          
                 
        
         
                
                    The exported image may be stored in any of the file formats enumerated in
                    @link Gateway::ImageExportBuilder::FileFormats Gateway::ImageExportBuilder::FileFormats@endlink .  Please note that transparency is only
                    available in TIFF and PNG formats.
                
                  
         
        """
        pass
    
    ## Getter for property: (str) FileName
    ##  Returns
    ##          @brief 
    ##             the full path of the exported image file.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             This value should be set to the desired destination of the exported image file.
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns
                 @brief 
                    the full path of the exported image file.  
          
                 
        
         
                
                    This value should be set to the desired destination of the exported image file.
                
                  
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##  Returns
    ##          @brief 
    ##             the full path of the exported image file.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             This value should be set to the desired destination of the exported image file.
    ##         
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns
                 @brief 
                    the full path of the exported image file.  
          
                 
        
         
                
                    This value should be set to the desired destination of the exported image file.
                
                  
         
        """
        pass
    
    ## Getter for property: (int) RegionHeight
    ##  Returns
    ##          @brief 
    ##             the height of the region of the graphics window that will be captured if
    ##             @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  is true.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             See @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  for
    ##             more information on capturing a region of the graphics window.
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return int
    @property
    def RegionHeight(self) -> int:
        """
        Getter for property: (int) RegionHeight
         Returns
                 @brief 
                    the height of the region of the graphics window that will be captured if
                    @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  is true.  
          
                 
        
         
                
                    See @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  for
                    more information on capturing a region of the graphics window.
                
                  
         
        """
        pass
    
    ## Setter for property: (int) RegionHeight

    ##  Returns
    ##          @brief 
    ##             the height of the region of the graphics window that will be captured if
    ##             @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  is true.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             See @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  for
    ##             more information on capturing a region of the graphics window.
    ##         
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @RegionHeight.setter
    def RegionHeight(self, regionHeight: int):
        """
        Setter for property: (int) RegionHeight
         Returns
                 @brief 
                    the height of the region of the graphics window that will be captured if
                    @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  is true.  
          
                 
        
         
                
                    See @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  for
                    more information on capturing a region of the graphics window.
                
                  
         
        """
        pass
    
    ## Getter for property: (bool) RegionMode
    ##  Returns
    ##          @brief 
    ##             a boolean value that, if true, indicates that a rectangular region of the graphics window will be captured, rather than the entire graphics window.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             The region used to generate the image file is defined using @link Gateway::ImageExportBuilder::SetRegionTopLeftPoint Gateway::ImageExportBuilder::SetRegionTopLeftPoint@endlink ,
    ##             @link Gateway::ImageExportBuilder::SetRegionWidth Gateway::ImageExportBuilder::SetRegionWidth@endlink  and @link Gateway::ImageExportBuilder::SetRegionHeight Gateway::ImageExportBuilder::SetRegionHeight@endlink .
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def RegionMode(self) -> bool:
        """
        Getter for property: (bool) RegionMode
         Returns
                 @brief 
                    a boolean value that, if true, indicates that a rectangular region of the graphics window will be captured, rather than the entire graphics window.  
          
                 
        
         
                
                    The region used to generate the image file is defined using @link Gateway::ImageExportBuilder::SetRegionTopLeftPoint Gateway::ImageExportBuilder::SetRegionTopLeftPoint@endlink ,
                    @link Gateway::ImageExportBuilder::SetRegionWidth Gateway::ImageExportBuilder::SetRegionWidth@endlink  and @link Gateway::ImageExportBuilder::SetRegionHeight Gateway::ImageExportBuilder::SetRegionHeight@endlink .
                
                  
         
        """
        pass
    
    ## Setter for property: (bool) RegionMode

    ##  Returns
    ##          @brief 
    ##             a boolean value that, if true, indicates that a rectangular region of the graphics window will be captured, rather than the entire graphics window.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             The region used to generate the image file is defined using @link Gateway::ImageExportBuilder::SetRegionTopLeftPoint Gateway::ImageExportBuilder::SetRegionTopLeftPoint@endlink ,
    ##             @link Gateway::ImageExportBuilder::SetRegionWidth Gateway::ImageExportBuilder::SetRegionWidth@endlink  and @link Gateway::ImageExportBuilder::SetRegionHeight Gateway::ImageExportBuilder::SetRegionHeight@endlink .
    ##         
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @RegionMode.setter
    def RegionMode(self, regionMode: bool):
        """
        Setter for property: (bool) RegionMode
         Returns
                 @brief 
                    a boolean value that, if true, indicates that a rectangular region of the graphics window will be captured, rather than the entire graphics window.  
          
                 
        
         
                
                    The region used to generate the image file is defined using @link Gateway::ImageExportBuilder::SetRegionTopLeftPoint Gateway::ImageExportBuilder::SetRegionTopLeftPoint@endlink ,
                    @link Gateway::ImageExportBuilder::SetRegionWidth Gateway::ImageExportBuilder::SetRegionWidth@endlink  and @link Gateway::ImageExportBuilder::SetRegionHeight Gateway::ImageExportBuilder::SetRegionHeight@endlink .
                
                  
         
        """
        pass
    
    ## Getter for property: (int) RegionWidth
    ##  Returns
    ##          @brief 
    ##             the width of the region of the graphics window that will be captured if
    ##             @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  is true.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             See @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  for
    ##             more information on capturing a region of the graphics window.
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return int
    @property
    def RegionWidth(self) -> int:
        """
        Getter for property: (int) RegionWidth
         Returns
                 @brief 
                    the width of the region of the graphics window that will be captured if
                    @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  is true.  
          
                 
        
         
                
                    See @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  for
                    more information on capturing a region of the graphics window.
                
                  
         
        """
        pass
    
    ## Setter for property: (int) RegionWidth

    ##  Returns
    ##          @brief 
    ##             the width of the region of the graphics window that will be captured if
    ##             @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  is true.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             See @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  for
    ##             more information on capturing a region of the graphics window.
    ##         
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @RegionWidth.setter
    def RegionWidth(self, regionWidth: int):
        """
        Setter for property: (int) RegionWidth
         Returns
                 @brief 
                    the width of the region of the graphics window that will be captured if
                    @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  is true.  
          
                 
        
         
                
                    See @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  for
                    more information on capturing a region of the graphics window.
                
                  
         
        """
        pass
    
    ## 
    ##          @brief 
    ##             Returns the background color the image will be captured with if
    ##             @link Gateway::ImageExportBuilder::BackgroundOption Gateway::ImageExportBuilder::BackgroundOption@endlink  is set to Custom Color.
    ##          
    ## 
    ##  
    ##         
    ##             
    ##         
    ##         
    ##  @return customBackgroundColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetCustomBackgroundColor(self) -> List[float]:
        """
        
                 @brief 
                    Returns the background color the image will be captured with if
                    @link Gateway::ImageExportBuilder::BackgroundOption Gateway::ImageExportBuilder::BackgroundOption@endlink  is set to Custom Color.
                 
        
         
                
                    
                
                
         @return customBackgroundColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ## 
    ##          @brief 
    ##             Returns the top left point of the region of the graphics window that will be captured if
    ##             @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  is true.
    ##          
    ## 
    ##  
    ##         
    ##             This value is a window coordinate.  See
    ##             @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  for more information on capturing
    ##             a region of the graphics window.
    ##         
    ##         
    ##  @return regionTopLeftPoint (List[int]):  Array of 2 int values representing the x and y window coordinate of the top left point of the captured region .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetRegionTopLeftPoint(self) -> List[int]:
        """
        
                 @brief 
                    Returns the top left point of the region of the graphics window that will be captured if
                    @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  is true.
                 
        
         
                
                    This value is a window coordinate.  See
                    @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  for more information on capturing
                    a region of the graphics window.
                
                
         @return regionTopLeftPoint (List[int]):  Array of 2 int values representing the x and y window coordinate of the top left point of the captured region .
        """
        pass
    
    ## 
    ##          @brief 
    ##             Sets the background color the image will be captured with if
    ##             @link Gateway::ImageExportBuilder::BackgroundOption Gateway::ImageExportBuilder::BackgroundOption@endlink  is set to Custom Color.
    ##          
    ## 
    ##  
    ##         
    ##             
    ##         
    ##         
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="customBackgroundColor"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetCustomBackgroundColor(self, customBackgroundColor: List[float]) -> None:
        """
        
                 @brief 
                    Sets the background color the image will be captured with if
                    @link Gateway::ImageExportBuilder::BackgroundOption Gateway::ImageExportBuilder::BackgroundOption@endlink  is set to Custom Color.
                 
        
         
                
                    
                
                
        """
        pass
    
    ## 
    ##          @brief 
    ##             Sets the top left point of the region of the graphics window that will be captured if
    ##             @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  is true.
    ##          
    ## 
    ##  
    ##         
    ##             This value is a window coordinate.  See
    ##             @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  for more information on capturing
    ##             a region of the graphics window.
    ##         
    ##         
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="regionTopLeftPoint"> (List[int])  Array of 2 int values representing the x and y window coordinate of the top left point of the captured region </param>
    def SetRegionTopLeftPoint(self, regionTopLeftPoint: List[int]) -> None:
        """
        
                 @brief 
                    Sets the top left point of the region of the graphics window that will be captured if
                    @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  is true.
                 
        
         
                
                    This value is a window coordinate.  See
                    @link Gateway::ImageExportBuilder::RegionMode Gateway::ImageExportBuilder::RegionMode@endlink  for more information on capturing
                    a region of the graphics window.
                
                
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Gateway::MassAssignmentBuilder NXOpen::Gateway::MassAssignmentBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Gateway::MassCollection::CreateAssignmentBuilder  NXOpen::Gateway::MassCollection::CreateAssignmentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Area.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## AreaStatus </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## AssignmentStatus </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Density.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GravityCenterStatus </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## GravityCenterX.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GravityCenterY.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GravityCenterZ.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## InertiaStatus </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Mass.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MassType </term> <description> 
##  
## MassOnly </description> </item> 
## 
## <item><term> 
##  
## MomentsInertiaXX.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MomentsInertiaYY.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MomentsInertiaZZ.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ProductsInertiaXY.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ProductsInertiaXZ.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ProductsInertiaYZ.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ValueType </term> <description> 
##  
## Asserted </description> </item> 
## 
## <item><term> 
##  
## Volume.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1872.0.0  <br> 

class MassAssignmentBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Gateway.MassAssignmentBuilder</ja_class> builder. """


    ##  the mass definition type
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## MassOnly</term><description> 
    ## </description> </item><item><term> 
    ## DensityMass</term><description> 
    ## </description> </item><item><term> 
    ## DensityVolume</term><description> 
    ## </description> </item><item><term> 
    ## MassVolume</term><description> 
    ## </description> </item></list>
    class MassTypes(Enum):
        """
        Members Include: <MassOnly> <DensityMass> <DensityVolume> <MassVolume>
        """
        MassOnly: int
        DensityMass: int
        DensityVolume: int
        MassVolume: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassAssignmentBuilder.MassTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the value type
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Asserted</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined1</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined2</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined3</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined4</term><description> 
    ## </description> </item></list>
    class ValueTypes(Enum):
        """
        Members Include: <Asserted> <UserDefined1> <UserDefined2> <UserDefined3> <UserDefined4>
        """
        Asserted: int
        UserDefined1: int
        UserDefined2: int
        UserDefined3: int
        UserDefined4: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassAssignmentBuilder.ValueTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
import NXOpen
##  Represents a @link NXOpen::Gateway::MassCalculationBuilder NXOpen::Gateway::MassCalculationBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Gateway::MassCollection::CreateCalculationBuilder  NXOpen::Gateway::MassCollection::CreateCalculationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class MassCalculationBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Gateway.MassCalculationBuilder</ja_class> builder. """
    pass


import NXOpen
##  This class contains the factory method for creating mass builder.  <br> To obtain an instance of this class, refer to @link NXOpen::PropertiesManager  NXOpen::PropertiesManager @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class MassCollection(NXOpen.TaggedObjectCollection): 
    """ This class contains the factory method for creating mass builder. """
    pass


import NXOpen
##  Represents a @link NXOpen::Gateway::MassExportBuilder NXOpen::Gateway::MassExportBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Gateway::MassCollection::CreateExportBuilder  NXOpen::Gateway::MassCollection::CreateExportBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Output </term> <description> 
##  
## Information </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class MassExportBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Gateway.MassExportBuilder</ja_class> builder. """


    ##  the body header node ID 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SourcePrecedence</term><description> 
    ## </description> </item><item><term> 
    ## ReferenceSetUsed</term><description> 
    ## </description> </item><item><term> 
    ## Accuracy</term><description> 
    ## </description> </item><item><term> 
    ## Count</term><description> 
    ## </description> </item></list>
    class BodyHeader(Enum):
        """
        Members Include: <SourcePrecedence> <ReferenceSetUsed> <Accuracy> <Count>
        """
        SourcePrecedence: int
        ReferenceSetUsed: int
        Accuracy: int
        Count: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.BodyHeader:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the component header node ID 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SourcePrecedence</term><description> 
    ## </description> </item><item><term> 
    ## ReferenceSetPrecedence</term><description> 
    ## </description> </item><item><term> 
    ## ReferenceSetUsed</term><description> 
    ## </description> </item><item><term> 
    ## ComponentGroup</term><description> 
    ## </description> </item><item><term> 
    ## Arrangement</term><description> 
    ## </description> </item><item><term> 
    ## Accuracy</term><description> 
    ## </description> </item><item><term> 
    ## Coating</term><description> 
    ## </description> </item><item><term> 
    ## Count</term><description> 
    ## </description> </item></list>
    class ComponentHeader(Enum):
        """
        Members Include: <SourcePrecedence> <ReferenceSetPrecedence> <ReferenceSetUsed> <ComponentGroup> <Arrangement> <Accuracy> <Coating> <Count>
        """
        SourcePrecedence: int
        ReferenceSetPrecedence: int
        ReferenceSetUsed: int
        ComponentGroup: int
        Arrangement: int
        Accuracy: int
        Coating: int
        Count: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.ComponentHeader:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the data modes 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AssemblyOnly</term><description> 
    ## </description> </item><item><term> 
    ## IncludeChildren</term><description> 
    ## </description> </item><item><term> 
    ## Solid</term><description> 
    ## </description> </item></list>
    class DataModes(Enum):
        """
        Members Include: <AssemblyOnly> <IncludeChildren> <Solid>
        """
        AssemblyOnly: int
        IncludeChildren: int
        Solid: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.DataModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the node type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ComponentHeader</term><description> 
    ## </description> </item><item><term> 
    ## BodyHeader</term><description> 
    ## </description> </item><item><term> 
    ## PerComponentResult</term><description> 
    ## </description> </item><item><term> 
    ## PerBodyResult</term><description> 
    ## </description> </item><item><term> 
    ## OverallResult</term><description> 
    ## </description> </item></list>
    class NodeType(Enum):
        """
        Members Include: <ComponentHeader> <BodyHeader> <PerComponentResult> <PerBodyResult> <OverallResult>
        """
        ComponentHeader: int
        BodyHeader: int
        PerComponentResult: int
        PerBodyResult: int
        OverallResult: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.NodeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the output types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Information</term><description> 
    ## </description> </item><item><term> 
    ## Xlsx</term><description> 
    ## </description> </item><item><term> 
    ## Csv</term><description> 
    ## </description> </item><item><term> 
    ## Xml</term><description> 
    ## </description> </item><item><term> 
    ## Json</term><description> 
    ## </description> </item></list>
    class OutputTypes(Enum):
        """
        Members Include: <Information> <Xlsx> <Csv> <Xml> <Json>
        """
        Information: int
        Xlsx: int
        Csv: int
        Xml: int
        Json: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.OutputTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the overall result node ID 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Material</term><description> 
    ## </description> </item><item><term> 
    ## Density</term><description> 
    ## </description> </item><item><term> 
    ## DensitySource</term><description> 
    ## </description> </item><item><term> 
    ## Area</term><description> 
    ## </description> </item><item><term> 
    ## AreaSource</term><description> 
    ## </description> </item><item><term> 
    ## Volume</term><description> 
    ## </description> </item><item><term> 
    ## VolumeSource</term><description> 
    ## </description> </item><item><term> 
    ## Mass</term><description> 
    ## </description> </item><item><term> 
    ## MassSource</term><description> 
    ## </description> </item><item><term> 
    ## Weight</term><description> 
    ## </description> </item><item><term> 
    ## WeightSource</term><description> 
    ## </description> </item><item><term> 
    ## CenterOfMassWCS</term><description> 
    ## </description> </item><item><term> 
    ## CenterOfMassAbsolute</term><description> 
    ## </description> </item><item><term> 
    ## CenterOfMassSource</term><description> 
    ## </description> </item><item><term> 
    ## FirstMomentsWCS</term><description> 
    ## </description> </item><item><term> 
    ## MomentsOfInertiaWCS</term><description> 
    ## </description> </item><item><term> 
    ## MomentsOfInertiaCentroidal</term><description> 
    ## </description> </item><item><term> 
    ## MomentsOfInertiaCentroidalSource</term><description> 
    ## </description> </item><item><term> 
    ## MomentsOfInertiaSpherical</term><description> 
    ## </description> </item><item><term> 
    ## ProductsOfInertiaWCS</term><description> 
    ## </description> </item><item><term> 
    ## ProductsOfInertiaCentroidal</term><description> 
    ## </description> </item><item><term> 
    ## ProductsOfInertiaCentroidalSource</term><description> 
    ## </description> </item><item><term> 
    ## PrincipalMomentsOfInertia</term><description> 
    ## </description> </item><item><term> 
    ## RadiiOfGyrationWCS</term><description> 
    ## </description> </item><item><term> 
    ## RadiiOfGyrationCentroidal</term><description> 
    ## </description> </item><item><term> 
    ## RadiiOfGyrationSpherical</term><description> 
    ## </description> </item><item><term> 
    ## PrincipalAxisWCS</term><description> 
    ## </description> </item><item><term> 
    ## EstimatedErrorRanges</term><description> 
    ##  Unused from NX2206 </description> </item><item><term> 
    ## Warnings</term><description> 
    ## </description> </item><item><term> 
    ## Count</term><description> 
    ## </description> </item></list>
    class OverallResult(Enum):
        """
        Members Include: <Material> <Density> <DensitySource> <Area> <AreaSource> <Volume> <VolumeSource> <Mass> <MassSource> <Weight> <WeightSource> <CenterOfMassWCS> <CenterOfMassAbsolute> <CenterOfMassSource> <FirstMomentsWCS> <MomentsOfInertiaWCS> <MomentsOfInertiaCentroidal> <MomentsOfInertiaCentroidalSource> <MomentsOfInertiaSpherical> <ProductsOfInertiaWCS> <ProductsOfInertiaCentroidal> <ProductsOfInertiaCentroidalSource> <PrincipalMomentsOfInertia> <RadiiOfGyrationWCS> <RadiiOfGyrationCentroidal> <RadiiOfGyrationSpherical> <PrincipalAxisWCS> <EstimatedErrorRanges> <Warnings> <Count>
        """
        Material: int
        Density: int
        DensitySource: int
        Area: int
        AreaSource: int
        Volume: int
        VolumeSource: int
        Mass: int
        MassSource: int
        Weight: int
        WeightSource: int
        CenterOfMassWCS: int
        CenterOfMassAbsolute: int
        CenterOfMassSource: int
        FirstMomentsWCS: int
        MomentsOfInertiaWCS: int
        MomentsOfInertiaCentroidal: int
        MomentsOfInertiaCentroidalSource: int
        MomentsOfInertiaSpherical: int
        ProductsOfInertiaWCS: int
        ProductsOfInertiaCentroidal: int
        ProductsOfInertiaCentroidalSource: int
        PrincipalMomentsOfInertia: int
        RadiiOfGyrationWCS: int
        RadiiOfGyrationCentroidal: int
        RadiiOfGyrationSpherical: int
        PrincipalAxisWCS: int
        EstimatedErrorRanges: int
        Warnings: int
        Count: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.OverallResult:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the per body result node ID 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## BodyName</term><description> 
    ## </description> </item><item><term> 
    ## Count</term><description> 
    ## </description> </item></list>
    class PerBodyResult(Enum):
        """
        Members Include: <BodyName> <Count>
        """
        BodyName: int
        Count: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.PerBodyResult:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the per component result node ID 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ComponentName</term><description> 
    ## </description> </item><item><term> 
    ## ObjectDisplayName</term><description> 
    ## </description> </item><item><term> 
    ## ItemID</term><description> 
    ## </description> </item><item><term> 
    ## ItemName</term><description> 
    ## </description> </item><item><term> 
    ## ItemRevision</term><description> 
    ## </description> </item><item><term> 
    ## FileName</term><description> 
    ## </description> </item><item><term> 
    ## DescriptivePartName</term><description> 
    ## </description> </item><item><term> 
    ## ParentName</term><description> 
    ## </description> </item><item><term> 
    ## Count</term><description> 
    ## </description> </item></list>
    class PerComponentResult(Enum):
        """
        Members Include: <ComponentName> <ObjectDisplayName> <ItemID> <ItemName> <ItemRevision> <FileName> <DescriptivePartName> <ParentName> <Count>
        """
        ComponentName: int
        ObjectDisplayName: int
        ItemID: int
        ItemName: int
        ItemRevision: int
        FileName: int
        DescriptivePartName: int
        ParentName: int
        Count: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.PerComponentResult:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
import NXOpen
##  Represents a @link NXOpen::Gateway::MassLimitationBuilder NXOpen::Gateway::MassLimitationBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Gateway::MassCollection::CreateLimitationBuilder  NXOpen::Gateway::MassCollection::CreateLimitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class MassLimitationBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Gateway.MassLimitationBuilder</ja_class> builder. """
    pass


import NXOpen
##  Represents a @link NXOpen::Gateway::MassPartSpecificOptionsBuilder NXOpen::Gateway::MassPartSpecificOptionsBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Gateway::MassCollection::CreatePartSpecificOptionsBuilder  NXOpen::Gateway::MassCollection::CreatePartSpecificOptionsBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class MassPartSpecificOptionsBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Gateway.MassPartSpecificOptionsBuilder</ja_class> builder. """
    pass


import NXOpen
##  Represents a @link NXOpen::Gateway::MassPropertyOptionsBuilder NXOpen::Gateway::MassPropertyOptionsBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Gateway::MassCollection::CreatePropertyOptionsBuilder  NXOpen::Gateway::MassCollection::CreatePropertyOptionsBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MarkerColorOfAllComponents </term> <description> 
##  
## 125 </description> </item> 
## 
## <item><term> 
##  
## MarkerColorOfDisplayedPart </term> <description> 
##  
## 186 </description> </item> 
## 
## <item><term> 
##  
## MarkerColorOfSelectedComponentSet </term> <description> 
##  
## 108 </description> </item> 
## 
## <item><term> 
##  
## MarkerColorOfSelectedComponents </term> <description> 
##  
## 211 </description> </item> 
## 
## <item><term> 
##  
## UseAllComponents </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## UseDisplayedPart </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## UseSelectedComponentSet </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## UseSelectedComponents </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1872.0.0  <br> 

class MassPropertyOptionsBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Gateway.MassPropertyOptionsBuilder</ja_class> builder. """


    ## the accuracy type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Value1</term><description> 
    ## </description> </item><item><term> 
    ## Value2</term><description> 
    ## </description> </item><item><term> 
    ## Value3</term><description> 
    ## </description> </item><item><term> 
    ## Value4</term><description> 
    ## </description> </item><item><term> 
    ## Value5</term><description> 
    ## </description> </item><item><term> 
    ## Value6</term><description> 
    ## </description> </item></list>
    class AccuracyTypes(Enum):
        """
        Members Include: <Value1> <Value2> <Value3> <Value4> <Value5> <Value6>
        """
        Value1: int
        Value2: int
        Value3: int
        Value4: int
        Value5: int
        Value6: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassPropertyOptionsBuilder.AccuracyTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
import NXOpen
##  Represents a @link NXOpen::Gateway::MassValueBuilder NXOpen::Gateway::MassValueBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Gateway::MassCollection::CreateValueBuilder  NXOpen::Gateway::MassCollection::CreateValueBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Area </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## Density </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## GravityCenterX </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## GravityCenterY </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## GravityCenterZ </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## InertiaXX </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## InertiaXY </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## InertiaXZ </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## InertiaYY </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## InertiaYZ </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## InertiaZZ </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## Mass </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## MassType </term> <description> 
##  
## Unset </description> </item> 
## 
## <item><term> 
##  
## Volume </term> <description> 
##  
## Unset </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1872.0.0  <br> 

class MassValueBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Gateway.MassValueBuilder</ja_class> builder. """


    ## the mass value type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unset</term><description> 
    ## </description> </item><item><term> 
    ## MassOnly</term><description> 
    ## </description> </item><item><term> 
    ## DensityOnly</term><description> 
    ## </description> </item><item><term> 
    ## VolumeOnly</term><description> 
    ## </description> </item><item><term> 
    ## DensityMass</term><description> 
    ## </description> </item><item><term> 
    ## DensityVolume</term><description> 
    ## </description> </item><item><term> 
    ## MassVolume</term><description> 
    ## </description> </item><item><term> 
    ## AssertAll</term><description> 
    ## </description> </item></list>
    class MassTypes(Enum):
        """
        Members Include: <Unset> <MassOnly> <DensityOnly> <VolumeOnly> <DensityMass> <DensityVolume> <MassVolume> <AssertAll>
        """
        Unset: int
        MassOnly: int
        DensityOnly: int
        VolumeOnly: int
        DensityMass: int
        DensityVolume: int
        MassVolume: int
        AssertAll: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassValueBuilder.MassTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the value source type
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unset</term><description> 
    ## </description> </item><item><term> 
    ## Computed</term><description> 
    ## </description> </item><item><term> 
    ## Asserted</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined1</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined2</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined3</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined4</term><description> 
    ## </description> </item><item><term> 
    ## ComputedCoated</term><description> 
    ## </description> </item></list>
    class ValueSourceType(Enum):
        """
        Members Include: <Unset> <Computed> <Asserted> <UserDefined1> <UserDefined2> <UserDefined3> <UserDefined4> <ComputedCoated>
        """
        Unset: int
        Computed: int
        Asserted: int
        UserDefined1: int
        UserDefined2: int
        UserDefined3: int
        UserDefined4: int
        ComputedCoated: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MassValueBuilder.ValueSourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
import NXOpen
##  Represents a mass abstract class  <br> This is an abstract class.  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class Mass(NXOpen.TaggedObject): 
    """ Represents a mass abstract class """
    pass


import NXOpen
## 
## Represents a @link NXOpen::Gateway::PasteBuilder NXOpen::Gateway::PasteBuilder@endlink 
##  <br> To create a new instance of this class, use @link NXOpen::ClipboardOperationsManager::CreatePasteBuilder  NXOpen::ClipboardOperationsManager::CreatePasteBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class PasteBuilder(NXOpen.Builder): 
    """
Represents a <ja_class>NXOpen.Gateway.PasteBuilder</ja_class>
"""
    pass


## @package NXOpen.Gateway
## Classes, Enums and Structs under NXOpen.Gateway namespace

##  @link CopyCutBuilderStatus NXOpen.Gateway.CopyCutBuilderStatus @endlink is an alias for @link CopyCutBuilder.Status NXOpen.Gateway.CopyCutBuilder.Status@endlink
CopyCutBuilderStatus = CopyCutBuilder.Status


##  @link ImageCaptureBuilderCaptureMethodType NXOpen.Gateway.ImageCaptureBuilderCaptureMethodType @endlink is an alias for @link ImageCaptureBuilder.CaptureMethodType NXOpen.Gateway.ImageCaptureBuilder.CaptureMethodType@endlink
ImageCaptureBuilderCaptureMethodType = ImageCaptureBuilder.CaptureMethodType


##  @link ImageCaptureBuilderImageFormat NXOpen.Gateway.ImageCaptureBuilderImageFormat @endlink is an alias for @link ImageCaptureBuilder.ImageFormat NXOpen.Gateway.ImageCaptureBuilder.ImageFormat@endlink
ImageCaptureBuilderImageFormat = ImageCaptureBuilder.ImageFormat


##  @link ImageCaptureBuilderImageSize NXOpen.Gateway.ImageCaptureBuilderImageSize @endlink is an alias for @link ImageCaptureBuilder.ImageSize NXOpen.Gateway.ImageCaptureBuilder.ImageSize@endlink
ImageCaptureBuilderImageSize = ImageCaptureBuilder.ImageSize


##  @link ImageExportBuilderBackgroundOptions NXOpen.Gateway.ImageExportBuilderBackgroundOptions @endlink is an alias for @link ImageExportBuilder.BackgroundOptions NXOpen.Gateway.ImageExportBuilder.BackgroundOptions@endlink
ImageExportBuilderBackgroundOptions = ImageExportBuilder.BackgroundOptions


##  @link ImageExportBuilderFileFormats NXOpen.Gateway.ImageExportBuilderFileFormats @endlink is an alias for @link ImageExportBuilder.FileFormats NXOpen.Gateway.ImageExportBuilder.FileFormats@endlink
ImageExportBuilderFileFormats = ImageExportBuilder.FileFormats


##  @link MassAssignmentBuilderMassTypes NXOpen.Gateway.MassAssignmentBuilderMassTypes @endlink is an alias for @link MassAssignmentBuilder.MassTypes NXOpen.Gateway.MassAssignmentBuilder.MassTypes@endlink
MassAssignmentBuilderMassTypes = MassAssignmentBuilder.MassTypes


##  @link MassAssignmentBuilderValueTypes NXOpen.Gateway.MassAssignmentBuilderValueTypes @endlink is an alias for @link MassAssignmentBuilder.ValueTypes NXOpen.Gateway.MassAssignmentBuilder.ValueTypes@endlink
MassAssignmentBuilderValueTypes = MassAssignmentBuilder.ValueTypes


##  @link MassExportBuilderBodyHeader NXOpen.Gateway.MassExportBuilderBodyHeader @endlink is an alias for @link MassExportBuilder.BodyHeader NXOpen.Gateway.MassExportBuilder.BodyHeader@endlink
MassExportBuilderBodyHeader = MassExportBuilder.BodyHeader


##  @link MassExportBuilderComponentHeader NXOpen.Gateway.MassExportBuilderComponentHeader @endlink is an alias for @link MassExportBuilder.ComponentHeader NXOpen.Gateway.MassExportBuilder.ComponentHeader@endlink
MassExportBuilderComponentHeader = MassExportBuilder.ComponentHeader


##  @link MassExportBuilderDataModes NXOpen.Gateway.MassExportBuilderDataModes @endlink is an alias for @link MassExportBuilder.DataModes NXOpen.Gateway.MassExportBuilder.DataModes@endlink
MassExportBuilderDataModes = MassExportBuilder.DataModes


##  @link MassExportBuilderNodeType NXOpen.Gateway.MassExportBuilderNodeType @endlink is an alias for @link MassExportBuilder.NodeType NXOpen.Gateway.MassExportBuilder.NodeType@endlink
MassExportBuilderNodeType = MassExportBuilder.NodeType


##  @link MassExportBuilderOutputTypes NXOpen.Gateway.MassExportBuilderOutputTypes @endlink is an alias for @link MassExportBuilder.OutputTypes NXOpen.Gateway.MassExportBuilder.OutputTypes@endlink
MassExportBuilderOutputTypes = MassExportBuilder.OutputTypes


##  @link MassExportBuilderOverallResult NXOpen.Gateway.MassExportBuilderOverallResult @endlink is an alias for @link MassExportBuilder.OverallResult NXOpen.Gateway.MassExportBuilder.OverallResult@endlink
MassExportBuilderOverallResult = MassExportBuilder.OverallResult


##  @link MassExportBuilderPerBodyResult NXOpen.Gateway.MassExportBuilderPerBodyResult @endlink is an alias for @link MassExportBuilder.PerBodyResult NXOpen.Gateway.MassExportBuilder.PerBodyResult@endlink
MassExportBuilderPerBodyResult = MassExportBuilder.PerBodyResult


##  @link MassExportBuilderPerComponentResult NXOpen.Gateway.MassExportBuilderPerComponentResult @endlink is an alias for @link MassExportBuilder.PerComponentResult NXOpen.Gateway.MassExportBuilder.PerComponentResult@endlink
MassExportBuilderPerComponentResult = MassExportBuilder.PerComponentResult


##  @link MassPropertyOptionsBuilderAccuracyTypes NXOpen.Gateway.MassPropertyOptionsBuilderAccuracyTypes @endlink is an alias for @link MassPropertyOptionsBuilder.AccuracyTypes NXOpen.Gateway.MassPropertyOptionsBuilder.AccuracyTypes@endlink
MassPropertyOptionsBuilderAccuracyTypes = MassPropertyOptionsBuilder.AccuracyTypes


##  @link MassValueBuilderMassTypes NXOpen.Gateway.MassValueBuilderMassTypes @endlink is an alias for @link MassValueBuilder.MassTypes NXOpen.Gateway.MassValueBuilder.MassTypes@endlink
MassValueBuilderMassTypes = MassValueBuilder.MassTypes


##  @link MassValueBuilderValueSourceType NXOpen.Gateway.MassValueBuilderValueSourceType @endlink is an alias for @link MassValueBuilder.ValueSourceType NXOpen.Gateway.MassValueBuilder.ValueSourceType@endlink
MassValueBuilderValueSourceType = MassValueBuilder.ValueSourceType


