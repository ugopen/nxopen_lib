from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class BaseExplicitOrderBuilder(NXOpen.Builder): 
    """ This is the NXOpen.Gateway.BaseExplicitOrderBuilder for the explicit order"""
    @property
    def SaveName(self) -> str:
        """
        Getter for property: (str) SaveName
         Returns the save name   
            
         
        """
        pass
    @SaveName.setter
    def SaveName(self, saveName: str):
        """
        Setter for property: (str) SaveName
         Returns the save name   
            
         
        """
        pass
    def Clear(self) -> None:
        """
         Clears the current order and restores it to the default order 
        """
        pass
    def Delete(self, selectedEntries: List[str], currentOrder: List[str], numOfRemainingEntries: int) -> List[str]:
        """
         Deletes the saved orderorders that hashave been selected by the user from the list of saved orders 
         Returns newOrder (List[str]): .
        """
        pass
    def DownArrow(self, selectedEntries: List[str], currentOrder: List[str]) -> List[str]:
        """
         Moves down the rowrows selected by the user in the lists 
         Returns newOrder (List[str]): .
        """
        pass
    def Paste(self, pastePoint: int, selectedEntries: List[str], currentOrder: List[str]) -> List[str]:
        """
         Pastes the rows that have been previously selected using the cut operation 
         Returns newOrder (List[str]): .
        """
        pass
    def Save(self, orderList: List[str], saveName: str) -> None:
        """
         Saves an explicit order defined by the user 
        """
        pass
    def SaveAsTextFile(self, savedOrderName: str, saveFileName: str, overwriteFile: bool) -> None:
        """
         Saves the selected saved order in the form of a text file 
        """
        pass
    def UpArrow(self, selectedEntries: List[str], currentOrder: List[str]) -> List[str]:
        """
         Moves up the rowrows selected by the user in the lists 
         Returns newOrder (List[str]): .
        """
        pass
import NXOpen
class BookmarkFile(NXOpen.Object): 
    """ Represents operations which can be done on bookmark files.
    """
    def Delete(pathName: str) -> None:
        """
         Deletes an existing bookmark file. 
        """
        pass
    def Rename(oldPathName: str, newFileName: str, okToOverwriteExistingFile: bool) -> str:
        """
         Renames an existing bookmark file. 
         Returns newPathName (str):  Full path name to the renamed bookmark file.
                                                                 This text string must be freed by the
                                                                 caller. .
        """
        pass
    def SaveWithDescription(pathName: str, bookmarkOption: NXOpen.BasePart.BookmarkOption, description: str) -> None:
        """
         Creates a bookmark file including a description.
                    See NXOpen.BasePart.BookmarkOption for an explanation of the options
                    which are not supported in batch mode.  Also in batch mode, the description is not
                    written to the bookmark file. 
        """
        pass
    def SetDescription(pathName: str, description: str) -> None:
        """
         Changes the description of an existing bookmark file. Otherwise the bookmark file is unchanged. 
        """
        pass
import NXOpen
class CopyCutBuilder(NXOpen.Builder): 
    """
Represents a NXOpen.Gateway.CopyCutBuilder
"""
    class Status(Enum):
        """
        Members Include: 
         |NoObjectsCopied|  No objects were successfully copied 
         |NonExportableObjects|  Certain non-exportable objects were not copied 
         |PartExportFailed|  Error while exporting part with copiedcut objects 
         |ErrorDuringCut|  Error during the cut operation 
         |AllObjectsCopied|  All objects were successfully copied 

        """
        NoObjectsCopied: int
        NonExportableObjects: int
        PartExportFailed: int
        ErrorDuringCut: int
        AllObjectsCopied: int
        @staticmethod
        def ValueOf(value: int) -> CopyCutBuilder.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanCopyAsSketch(self) -> bool:
        """
        Getter for property: (bool) CanCopyAsSketch
         Returns a flag indicating whether to copy as sketch curves or not   
            
         
        """
        pass
    @CanCopyAsSketch.setter
    def CanCopyAsSketch(self, canCopyAsSketch: bool):
        """
        Setter for property: (bool) CanCopyAsSketch
         Returns a flag indicating whether to copy as sketch curves or not   
            
         
        """
        pass
    @property
    def CopyNonAssociative(self) -> bool:
        """
        Getter for property: (bool) CopyNonAssociative
         Returns the flag indicating if non-associative copy is being made.  
           Non-associative copy is limited
                to curve and body features where only geometry is copied without the feature.   
         
        """
        pass
    @CopyNonAssociative.setter
    def CopyNonAssociative(self, isCopyNonAssociative: bool):
        """
        Setter for property: (bool) CopyNonAssociative
         Returns the flag indicating if non-associative copy is being made.  
           Non-associative copy is limited
                to curve and body features where only geometry is copied without the feature.   
         
        """
        pass
    @property
    def DestinationFilename(self) -> str:
        """
        Getter for property: (str) DestinationFilename
         Returns the string of the filename to which to copy or cut the objects to   
            
         
        """
        pass
    @DestinationFilename.setter
    def DestinationFilename(self, filename: str):
        """
        Setter for property: (str) DestinationFilename
         Returns the string of the filename to which to copy or cut the objects to   
            
         
        """
        pass
    @property
    def InitialCopyLocation(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) InitialCopyLocation
         Returns the initial copy location mainly used to define default copy location of sketch objects   
            
         
        """
        pass
    @InitialCopyLocation.setter
    def InitialCopyLocation(self, copyLocation: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) InitialCopyLocation
         Returns the initial copy location mainly used to define default copy location of sketch objects   
            
         
        """
        pass
    @property
    def IsCut(self) -> bool:
        """
        Getter for property: (bool) IsCut
         Returns a flag indicating whether it is a copy or cut operation   
            
         
        """
        pass
    @IsCut.setter
    def IsCut(self, isCut: bool):
        """
        Setter for property: (bool) IsCut
         Returns a flag indicating whether it is a copy or cut operation   
            
         
        """
        pass
    @property
    def ToClipboard(self) -> bool:
        """
        Getter for property: (bool) ToClipboard
         Returns a flag indicating whether copy cut to clipboard or copy cut to a file  
            
         
        """
        pass
    @ToClipboard.setter
    def ToClipboard(self, isToClipboard: bool):
        """
        Setter for property: (bool) ToClipboard
         Returns a flag indicating whether copy cut to clipboard or copy cut to a file  
            
         
        """
        pass
    def GetCopyCutStatus(self) -> CopyCutBuilder.Status:
        """
         Gets the status of copy-cut operation 
         Returns copyCutStatus ( CopyCutBuilder.Status NXOpen): .
        """
        pass
    def GetNonExportableObjects(self) -> List[NXOpen.NXObject]:
        """
         Gets all non-exportable objects 
         Returns nonExportableObjects ( NXOpen.NXObject Li):  All the non-exportable objects .
        """
        pass
    def GetObjects(self) -> List[NXOpen.NXObject]:
        """
         Gets all objects to be copied or to be cut 
         Returns objects ( NXOpen.NXObject Li):  All the objects to be copied or to be cut.
        """
        pass
    def ResetInitialCopyLocation(self) -> None:
        """
         Reset the initial copy location. After this previously set initial copy location will not be used 
        """
        pass
    def SetObjects(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Sets objects to be copied or cut. Note that PMI, feature, drafting view and other drafting objects are not supported by this class. 
        """
        pass
import NXOpen
class FileNewTemplateManager(NXOpen.Object): 
    """  Represents a manager class to manage file new templates """
    def CreateFileNewTemplateNode(seedPart: NXOpen.Part, tabName: str, relationType: str, templateApplication: str, itemType: str) -> FileNewTemplateNode:
        """
         This function creates the template creation object 
         Returns templateNode ( FileNewTemplateNode NXOpen): .
        """
        pass
    def Free(templateNode: FileNewTemplateNode) -> None:
        """
         Destroys the object 
        """
        pass
    def SaveAsTemplate(templateNode: FileNewTemplateNode) -> NXOpen.ErrorList:
        """
         Saves the part as template with given information 
         Returns errorList ( NXOpen.ErrorList):  Errors encountered .
        """
        pass
import NXOpen
class FileNewTemplateNode(NXOpen.NXObject): 
    """
    Represents the class that contains effectivity parameters.
    """
    def SetDescription(self, attrValue: str) -> None:
        """
         SetDescrption 
        """
        pass
    def SetItemType(self, attrValue: str) -> None:
        """
         SetItemType
        """
        pass
    def SetRelationType(self, attrValue: str) -> None:
        """
         SetRelationType 
        """
        pass
    def SetTemplateApplication(self, attrValue: str) -> None:
        """
         SetTemplateApplication 
        """
        pass
    def SetTemplatePresentationName(self, attrValue: str) -> None:
        """
         SetTemplatePresentationName 
        """
        pass
import NXOpen
import NXOpen.PDM
class GenericFileNewBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Generic File New operations. 
        """
    def CreateLogicalObjects(self) -> List[NXOpen.PDM.LogicalObject]:
        """
         Creates the pre-creation objects for the parts 
         Returns logicalObjects ( NXOpen.PDM.LogicalObject Li): .
        """
        pass
    def SetApplicationBuilder(self, applicationBuilder: IGenericFileNewApplicationBuilder) -> None:
        """
         Sets NXOpen.Gateway.IGenericFileNewApplicationBuilder 
        """
        pass
import NXOpen
class IGenericFileNewApplicationBuilder(NXOpen.Builder): 
    """
        Represents the class Application Builder.
    """
    pass
import NXOpen
class ImageCaptureBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Gateway.ImageCaptureBuilder builder """
    class CaptureMethodType(Enum):
        """
        Members Include: 
         |GraphicsArea|  the graphics area
         |Region|  the region area
         |File|  the input from file
         |Automatic|  the automatic preview mode

        """
        GraphicsArea: int
        Region: int
        File: int
        Automatic: int
        @staticmethod
        def ValueOf(value: int) -> ImageCaptureBuilder.CaptureMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImageFormat(Enum):
        """
        Members Include: 
         |Bmp|  the bmp image format
         |Jpg|  the jpg image format
         |Gif|  the gif image format
         |Png|  the png image format
         |Tiff|  the tiff image format

        """
        Bmp: int
        Jpg: int
        Gif: int
        Png: int
        Tiff: int
        @staticmethod
        def ValueOf(value: int) -> ImageCaptureBuilder.ImageFormat:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImageSize(Enum):
        """
        Members Include: 
         |Pixels16|  the 16 pixel size
         |Pixels24|  the 24 pixel size
         |Pixels32|  the 32 pixel size
         |Pixels48|  the 48 pixel size
         |Pixels64|  the 64 pixel size
         |Pixels96|  the 96 pixel size
         |Pixels128|  the 128 pixel size

        """
        Pixels16: int
        Pixels24: int
        Pixels32: int
        Pixels48: int
        Pixels64: int
        Pixels96: int
        Pixels128: int
        @staticmethod
        def ValueOf(value: int) -> ImageCaptureBuilder.ImageSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CaptureMethod(self) -> ImageCaptureBuilder.CaptureMethodType:
        """
        Getter for property: ( ImageCaptureBuilder.CaptureMethodType NXOpen) CaptureMethod
         Returns the capture method   
            
         
        """
        pass
    @CaptureMethod.setter
    def CaptureMethod(self, captureMethod: ImageCaptureBuilder.CaptureMethodType):
        """
        Setter for property: ( ImageCaptureBuilder.CaptureMethodType NXOpen) CaptureMethod
         Returns the capture method   
            
         
        """
        pass
    @property
    def File(self) -> str:
        """
        Getter for property: (str) File
         Returns the file   
            
         
        """
        pass
    @File.setter
    def File(self, filename: str):
        """
        Setter for property: (str) File
         Returns the file   
            
         
        """
        pass
    @property
    def Format(self) -> ImageCaptureBuilder.ImageFormat:
        """
        Getter for property: ( ImageCaptureBuilder.ImageFormat NXOpen) Format
         Returns the format   
            
         
        """
        pass
    @Format.setter
    def Format(self, format: ImageCaptureBuilder.ImageFormat):
        """
        Setter for property: ( ImageCaptureBuilder.ImageFormat NXOpen) Format
         Returns the format   
            
         
        """
        pass
    @property
    def ImageFile(self) -> str:
        """
        Getter for property: (str) ImageFile
         Returns the image file   
            
         
        """
        pass
    @ImageFile.setter
    def ImageFile(self, imageFilename: str):
        """
        Setter for property: (str) ImageFile
         Returns the image file   
            
         
        """
        pass
    @property
    def Size(self) -> ImageCaptureBuilder.ImageSize:
        """
        Getter for property: ( ImageCaptureBuilder.ImageSize NXOpen) Size
         Returns the size   
            
         
        """
        pass
    @Size.setter
    def Size(self, size: ImageCaptureBuilder.ImageSize):
        """
        Setter for property: ( ImageCaptureBuilder.ImageSize NXOpen) Size
         Returns the size   
            
         
        """
        pass
    def GetRegion(self) -> Tuple[List[int], List[int]]:
        """
         Returns the region 
         Returns A tuple consisting of (topLeftCorner, bottomRightCorner). 
         - topLeftCorner is: List[int]. Array of 2 integers for Top Left Corner of Region .
         - bottomRightCorner is: List[int]. Array of 2 integers for Bottom Right Corner of Region .

        """
        pass
    def SetRegion(self, topLeftCorner: List[int], bottomRightCorner: List[int]) -> None:
        """
         Sets the region 
        """
        pass
import NXOpen
class ImageCaptureManager(NXOpen.Object): 
    """ The ImageCaptureManager class provides methods to create 
    NXOpen.Gateway.ImageCaptureBuilder object"""
    def CreateImageCaptureBuilder(self) -> ImageCaptureBuilder:
        """
         Creates a NXOpen.Gateway.ImageCaptureBuilder 
         Returns builder ( ImageCaptureBuilder NXOpen): .
        """
        pass
import NXOpen
class ImageExportBuilder(NXOpen.Builder): 
    """
    
        Captures the image in the active graphics window (or in a rectangular region of the active
        graphics window), and then exportssaves the image in a file of a specified format.
    
    
        This class can be used to export an image file that contains the contents of the
        active graphics window.  The image may be limited to a rectangular region of the display
        via Gateway.ImageExportBuilder.RegionMode.
        Gateway.ImageExportBuilder.FileFormats enumerates
        the file formats exported images may be saved in.
        The background of the exported image may be changed to any
        of the options available in
        Gateway.ImageExportBuilder.BackgroundOptions.
        After configuring the image export, an image file is saved by calling the Commit
        method.
    
    """
    class BackgroundOptions(Enum):
        """
        Members Include: 
         |Original|  Use the currently displayed background 
         |CustomColor|  Use the solid color set by Gateway.ImageExportBuilder.SetCustomBackgroundColor 
         |Transparent|  Use a transparent background (only available in PNG and TIFF file formats) 

        """
        Original: int
        CustomColor: int
        Transparent: int
        @staticmethod
        def ValueOf(value: int) -> ImageExportBuilder.BackgroundOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FileFormats(Enum):
        """
        Members Include: 
         |Png|  PNG File Format 
         |Jpg|  JPG File Format 
         |Gif|  GIF File Format 
         |Tiff|  Compressed TIFF File Format
         |Bmp|  BMP File Format (Windows Only) 
         |Xwd|  XWD File Format (Unix Only) 

        """
        Png: int
        Jpg: int
        Gif: int
        Tiff: int
        Bmp: int
        Xwd: int
        @staticmethod
        def ValueOf(value: int) -> ImageExportBuilder.FileFormats:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BackgroundOption(self) -> ImageExportBuilder.BackgroundOptions:
        """
        Getter for property: ( ImageExportBuilder.BackgroundOptions NXOpen) BackgroundOption
         Returns
                  
                    the background style used when capturing the image.  
          
                 
         
                
                    The image may be captured with any of the background styles enumerated in
                     Gateway::ImageExportBuilder::BackgroundOptions .  If the Custom Color background
                    option is used, the background color may be specified with
                     Gateway::ImageExportBuilder::SetCustomBackgroundColor .
                
                  
         
        """
        pass
    @BackgroundOption.setter
    def BackgroundOption(self, backgroundOption: ImageExportBuilder.BackgroundOptions):
        """
        Setter for property: ( ImageExportBuilder.BackgroundOptions NXOpen) BackgroundOption
         Returns
                  
                    the background style used when capturing the image.  
          
                 
         
                
                    The image may be captured with any of the background styles enumerated in
                     Gateway::ImageExportBuilder::BackgroundOptions .  If the Custom Color background
                    option is used, the background color may be specified with
                     Gateway::ImageExportBuilder::SetCustomBackgroundColor .
                
                  
         
        """
        pass
    @property
    def DeviceHeight(self) -> int:
        """
        Getter for property: (int) DeviceHeight
         Returns
                  
                    the height of the graphics device.  
          
                 
         
                
                    When capturing entire device content, this is image height in pixels.
                    Specifying zero uses default device height.
                
                  
         
        """
        pass
    @DeviceHeight.setter
    def DeviceHeight(self, deviceHeight: int):
        """
        Setter for property: (int) DeviceHeight
         Returns
                  
                    the height of the graphics device.  
          
                 
         
                
                    When capturing entire device content, this is image height in pixels.
                    Specifying zero uses default device height.
                
                  
         
        """
        pass
    @property
    def DeviceWidth(self) -> int:
        """
        Getter for property: (int) DeviceWidth
         Returns
                  
                    the width of the graphics device.  
          
                 
         
                
                    When capturing entire device content, this is image width in pixels.
                    Specifying zero uses default device width.
                
                  
         
        """
        pass
    @DeviceWidth.setter
    def DeviceWidth(self, deviceWidth: int):
        """
        Setter for property: (int) DeviceWidth
         Returns
                  
                    the width of the graphics device.  
          
                 
         
                
                    When capturing entire device content, this is image width in pixels.
                    Specifying zero uses default device width.
                
                  
         
        """
        pass
    @property
    def EnhanceEdges(self) -> bool:
        """
        Getter for property: (bool) EnhanceEdges
         Returns
                  
                    a boolean value that, if true, indicates the image will be captured with antialiasing disabled and edge emphasis enabled.  
          
                 
         
                
                    When capturing an image with many edges, such as a wireframe view of a part, antialiasing may cause thin edges to blur with the
                    background of the image.  This effect may be particularly noticeable when using a transparent background.  Disabling antialiasing
                    and enabling edge emphasis helps to eliminate this blurring at the cost of a more pixelated image.
                    
                  
         
        """
        pass
    @EnhanceEdges.setter
    def EnhanceEdges(self, enhanceEdges: bool):
        """
        Setter for property: (bool) EnhanceEdges
         Returns
                  
                    a boolean value that, if true, indicates the image will be captured with antialiasing disabled and edge emphasis enabled.  
          
                 
         
                
                    When capturing an image with many edges, such as a wireframe view of a part, antialiasing may cause thin edges to blur with the
                    background of the image.  This effect may be particularly noticeable when using a transparent background.  Disabling antialiasing
                    and enabling edge emphasis helps to eliminate this blurring at the cost of a more pixelated image.
                    
                  
         
        """
        pass
    @property
    def FileFormat(self) -> ImageExportBuilder.FileFormats:
        """
        Getter for property: ( ImageExportBuilder.FileFormats NXOpen) FileFormat
         Returns
                  
                    the file format of the exported image file.  
          
                 
         
                
                    The exported image may be stored in any of the file formats enumerated in
                     Gateway::ImageExportBuilder::FileFormats .  Please note that transparency is only
                    available in TIFF and PNG formats.
                
                  
         
        """
        pass
    @FileFormat.setter
    def FileFormat(self, fileFormat: ImageExportBuilder.FileFormats):
        """
        Setter for property: ( ImageExportBuilder.FileFormats NXOpen) FileFormat
         Returns
                  
                    the file format of the exported image file.  
          
                 
         
                
                    The exported image may be stored in any of the file formats enumerated in
                     Gateway::ImageExportBuilder::FileFormats .  Please note that transparency is only
                    available in TIFF and PNG formats.
                
                  
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns
                  
                    the full path of the exported image file.  
          
                 
         
                
                    This value should be set to the desired destination of the exported image file.
                
                  
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns
                  
                    the full path of the exported image file.  
          
                 
         
                
                    This value should be set to the desired destination of the exported image file.
                
                  
         
        """
        pass
    @property
    def RegionHeight(self) -> int:
        """
        Getter for property: (int) RegionHeight
         Returns
                  
                    the height of the region of the graphics window that will be captured if
                     Gateway::ImageExportBuilder::RegionMode  is true.  
          
                 
         
                
                    See  Gateway::ImageExportBuilder::RegionMode  for
                    more information on capturing a region of the graphics window.
                
                  
         
        """
        pass
    @RegionHeight.setter
    def RegionHeight(self, regionHeight: int):
        """
        Setter for property: (int) RegionHeight
         Returns
                  
                    the height of the region of the graphics window that will be captured if
                     Gateway::ImageExportBuilder::RegionMode  is true.  
          
                 
         
                
                    See  Gateway::ImageExportBuilder::RegionMode  for
                    more information on capturing a region of the graphics window.
                
                  
         
        """
        pass
    @property
    def RegionMode(self) -> bool:
        """
        Getter for property: (bool) RegionMode
         Returns
                  
                    a boolean value that, if true, indicates that a rectangular region of the graphics window will be captured, rather than the entire graphics window.  
          
                 
         
                
                    The region used to generate the image file is defined using  Gateway::ImageExportBuilder::SetRegionTopLeftPoint ,
                     Gateway::ImageExportBuilder::SetRegionWidth  and  Gateway::ImageExportBuilder::SetRegionHeight .
                
                  
         
        """
        pass
    @RegionMode.setter
    def RegionMode(self, regionMode: bool):
        """
        Setter for property: (bool) RegionMode
         Returns
                  
                    a boolean value that, if true, indicates that a rectangular region of the graphics window will be captured, rather than the entire graphics window.  
          
                 
         
                
                    The region used to generate the image file is defined using  Gateway::ImageExportBuilder::SetRegionTopLeftPoint ,
                     Gateway::ImageExportBuilder::SetRegionWidth  and  Gateway::ImageExportBuilder::SetRegionHeight .
                
                  
         
        """
        pass
    @property
    def RegionWidth(self) -> int:
        """
        Getter for property: (int) RegionWidth
         Returns
                  
                    the width of the region of the graphics window that will be captured if
                     Gateway::ImageExportBuilder::RegionMode  is true.  
          
                 
         
                
                    See  Gateway::ImageExportBuilder::RegionMode  for
                    more information on capturing a region of the graphics window.
                
                  
         
        """
        pass
    @RegionWidth.setter
    def RegionWidth(self, regionWidth: int):
        """
        Setter for property: (int) RegionWidth
         Returns
                  
                    the width of the region of the graphics window that will be captured if
                     Gateway::ImageExportBuilder::RegionMode  is true.  
          
                 
         
                
                    See  Gateway::ImageExportBuilder::RegionMode  for
                    more information on capturing a region of the graphics window.
                
                  
         
        """
        pass
    def GetCustomBackgroundColor(self) -> List[float]:
        """
                
                    Returns the background color the image will be captured with if
                    Gateway.ImageExportBuilder.BackgroundOption is set to Custom Color.
                
                
                    
                
                
         Returns customBackgroundColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetRegionTopLeftPoint(self) -> List[int]:
        """
                
                    Returns the top left point of the region of the graphics window that will be captured if
                    Gateway.ImageExportBuilder.RegionMode is true.
                
                
                    This value is a window coordinate.  See
                    Gateway.ImageExportBuilder.RegionMode for more information on capturing
                    a region of the graphics window.
                
                
         Returns regionTopLeftPoint (List[int]):  Array of 2 int values representing the x and y window coordinate of the top left point of the captured region .
        """
        pass
    def SetCustomBackgroundColor(self, customBackgroundColor: List[float]) -> None:
        """
                
                    Sets the background color the image will be captured with if
                    Gateway.ImageExportBuilder.BackgroundOption is set to Custom Color.
                
                
                    
                
                
        """
        pass
    def SetRegionTopLeftPoint(self, regionTopLeftPoint: List[int]) -> None:
        """
                
                    Sets the top left point of the region of the graphics window that will be captured if
                    Gateway.ImageExportBuilder.RegionMode is true.
                
                
                    This value is a window coordinate.  See
                    Gateway.ImageExportBuilder.RegionMode for more information on capturing
                    a region of the graphics window.
                
                
        """
        pass
import NXOpen
class MassAssignmentBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Gateway.MassAssignmentBuilder builder. """
    class MassTypes(Enum):
        """
        Members Include: 
         |MassOnly| 
         |DensityMass| 
         |DensityVolume| 
         |MassVolume| 

        """
        MassOnly: int
        DensityMass: int
        DensityVolume: int
        MassVolume: int
        @staticmethod
        def ValueOf(value: int) -> MassAssignmentBuilder.MassTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ValueTypes(Enum):
        """
        Members Include: 
         |Asserted| 
         |UserDefined1| 
         |UserDefined2| 
         |UserDefined3| 
         |UserDefined4| 
         |Budget| 

        """
        Asserted: int
        UserDefined1: int
        UserDefined2: int
        UserDefined3: int
        UserDefined4: int
        Budget: int
        @staticmethod
        def ValueOf(value: int) -> MassAssignmentBuilder.ValueTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Area(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Area
         Returns the area   
            
         
        """
        pass
    @property
    def AreaStatus(self) -> bool:
        """
        Getter for property: (bool) AreaStatus
         Returns the area status   
            
         
        """
        pass
    @AreaStatus.setter
    def AreaStatus(self, areaStatus: bool):
        """
        Setter for property: (bool) AreaStatus
         Returns the area status   
            
         
        """
        pass
    @property
    def AssignmentStatus(self) -> bool:
        """
        Getter for property: (bool) AssignmentStatus
         Returns the assignment status   
            
         
        """
        pass
    @AssignmentStatus.setter
    def AssignmentStatus(self, assignmentStatus: bool):
        """
        Setter for property: (bool) AssignmentStatus
         Returns the assignment status   
            
         
        """
        pass
    @property
    def Density(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Density
         Returns the density   
            
         
        """
        pass
    @property
    def DensityStatus(self) -> bool:
        """
        Getter for property: (bool) DensityStatus
         Returns the density status   
            
         
        """
        pass
    @DensityStatus.setter
    def DensityStatus(self, densityStatus: bool):
        """
        Setter for property: (bool) DensityStatus
         Returns the density status   
            
         
        """
        pass
    @property
    def DeriveOption(self) -> int:
        """
        Getter for property: (int) DeriveOption
         Returns the deriveOption   
            
         
        """
        pass
    @DeriveOption.setter
    def DeriveOption(self, deriveOption: int):
        """
        Setter for property: (int) DeriveOption
         Returns the deriveOption   
            
         
        """
        pass
    @property
    def GravityCenterStatus(self) -> bool:
        """
        Getter for property: (bool) GravityCenterStatus
         Returns the mass center status   
            
         
        """
        pass
    @GravityCenterStatus.setter
    def GravityCenterStatus(self, gravityCenterStatus: bool):
        """
        Setter for property: (bool) GravityCenterStatus
         Returns the mass center status   
            
         
        """
        pass
    @property
    def GravityCenterX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) GravityCenterX
         Returns the mass center x   
            
         
        """
        pass
    @property
    def GravityCenterY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) GravityCenterY
         Returns the mass center y   
            
         
        """
        pass
    @property
    def GravityCenterZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) GravityCenterZ
         Returns the mass center z   
            
         
        """
        pass
    @property
    def InertiaStatus(self) -> bool:
        """
        Getter for property: (bool) InertiaStatus
         Returns the inertia status   
            
         
        """
        pass
    @InertiaStatus.setter
    def InertiaStatus(self, inertiaStatus: bool):
        """
        Setter for property: (bool) InertiaStatus
         Returns the inertia status   
            
         
        """
        pass
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Mass
         Returns the mass   
            
         
        """
        pass
    @property
    def MassStatus(self) -> bool:
        """
        Getter for property: (bool) MassStatus
         Returns the mass status   
            
         
        """
        pass
    @MassStatus.setter
    def MassStatus(self, massStatus: bool):
        """
        Setter for property: (bool) MassStatus
         Returns the mass status   
            
         
        """
        pass
    @property
    def MassType(self) -> MassAssignmentBuilder.MassTypes:
        """
        Getter for property: ( MassAssignmentBuilder.MassTypes NXOpen) MassType
         Returns the mass type   
            
         
        """
        pass
    @MassType.setter
    def MassType(self, massType: MassAssignmentBuilder.MassTypes):
        """
        Setter for property: ( MassAssignmentBuilder.MassTypes NXOpen) MassType
         Returns the mass type   
            
         
        """
        pass
    @property
    def MomentsInertiaXX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MomentsInertiaXX
         Returns the moments of inertia xx   
            
         
        """
        pass
    @property
    def MomentsInertiaYY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MomentsInertiaYY
         Returns the moments of inertia yy   
            
         
        """
        pass
    @property
    def MomentsInertiaZZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MomentsInertiaZZ
         Returns the moments of inertia zz   
            
         
        """
        pass
    @property
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Objects
         Returns the objects   
            
         
        """
        pass
    @property
    def ProductsInertiaXY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProductsInertiaXY
         Returns the products of inertia XY   
            
         
        """
        pass
    @property
    def ProductsInertiaXZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProductsInertiaXZ
         Returns the products of inertia XZ   
            
         
        """
        pass
    @property
    def ProductsInertiaYZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProductsInertiaYZ
         Returns the products of inertia YZ   
            
         
        """
        pass
    @property
    def ValueType(self) -> MassAssignmentBuilder.ValueTypes:
        """
        Getter for property: ( MassAssignmentBuilder.ValueTypes NXOpen) ValueType
         Returns the value type   
            
         
        """
        pass
    @ValueType.setter
    def ValueType(self, valueType: MassAssignmentBuilder.ValueTypes):
        """
        Setter for property: ( MassAssignmentBuilder.ValueTypes NXOpen) ValueType
         Returns the value type   
            
         
        """
        pass
    @property
    def Volume(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Volume
         Returns the volume   
            
         
        """
        pass
    @property
    def VolumeStatus(self) -> bool:
        """
        Getter for property: (bool) VolumeStatus
         Returns the volume status   
            
         
        """
        pass
    @VolumeStatus.setter
    def VolumeStatus(self, volumeStatus: bool):
        """
        Setter for property: (bool) VolumeStatus
         Returns the volume status   
            
         
        """
        pass
    def GetAssignmentValues(self) -> None:
        """
         Get the assignment values of the root part or user selected object, and save to the builder . 
        """
        pass
import NXOpen
class MassCalculationBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Gateway.MassCalculationBuilder builder. """
    @property
    def ComponentGroupName(self) -> str:
        """
        Getter for property: (str) ComponentGroupName
         Returns the name of component group   
            
         
        """
        pass
    @ComponentGroupName.setter
    def ComponentGroupName(self, componentGroupName: str):
        """
        Setter for property: (str) ComponentGroupName
         Returns the name of component group   
            
         
        """
        pass
    @property
    def IncludeChildren(self) -> bool:
        """
        Getter for property: (bool) IncludeChildren
         Returns the include children.  
            
         
        """
        pass
    @IncludeChildren.setter
    def IncludeChildren(self, includeChildren: bool):
        """
        Setter for property: (bool) IncludeChildren
         Returns the include children.  
            
         
        """
        pass
    @property
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Objects
         Returns the objects   
            
         
        """
        pass
import NXOpen
class MassCollection(NXOpen.TaggedObjectCollection): 
    """ This class contains the factory method for creating mass builder. """
    def CreateAssignmentBuilder(self, componentTag: NXOpen.NXObject) -> MassAssignmentBuilder:
        """
         Creates a NXOpen.Gateway.MassAssignmentBuilder 
         Returns builder ( MassAssignmentBuilder NXOpen):  .
        """
        pass
    def CreateCalculationBuilder(self, componentTags: List[NXOpen.NXObject]) -> MassCalculationBuilder:
        """
         Creates a NXOpen.Gateway.MassCalculationBuilder 
         Returns builder ( MassCalculationBuilder NXOpen):  .
        """
        pass
    def CreateExportBuilder(self, componentTags: List[NXOpen.NXObject]) -> MassExportBuilder:
        """
         Creates a NXOpen.Gateway.MassExportBuilder 
         Returns builder ( MassExportBuilder NXOpen):  .
        """
        pass
    def CreateLimitationBuilder(self, componentTag: NXOpen.NXObject) -> MassLimitationBuilder:
        """
         Creates a NXOpen.Gateway.MassLimitationBuilder 
         Returns builder ( MassLimitationBuilder NXOpen):  .
        """
        pass
    def CreatePartSpecificOptionsBuilder(self) -> MassPartSpecificOptionsBuilder:
        """
         Creates a NXOpen.Gateway.MassPartSpecificOptionsBuilder 
         Returns builder ( MassPartSpecificOptionsBuilder NXOpen):  .
        """
        pass
    def CreatePropertyOptionsBuilder(self) -> MassPropertyOptionsBuilder:
        """
         Creates a NXOpen.Gateway.MassPropertyOptionsBuilder 
         Returns builder ( MassPropertyOptionsBuilder NXOpen):  .
        """
        pass
    def CreateValueBuilder(self, componentTag: NXOpen.NXObject) -> MassValueBuilder:
        """
         Creates a NXOpen.Gateway.MassValueBuilder 
         Returns builder ( MassValueBuilder NXOpen):  .
        """
        pass
import NXOpen
class MassExportBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Gateway.MassExportBuilder builder. """
    class BodyHeader(Enum):
        """
        Members Include: 
         |SourcePrecedence| 
         |ReferenceSetUsed| 
         |Accuracy| 
         |Count| 

        """
        SourcePrecedence: int
        ReferenceSetUsed: int
        Accuracy: int
        Count: int
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.BodyHeader:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentHeader(Enum):
        """
        Members Include: 
         |SourcePrecedence| 
         |ReferenceSetPrecedence| 
         |ReferenceSetUsed| 
         |ComponentGroup| 
         |Arrangement| 
         |Accuracy| 
         |Coating| 
         |Count| 

        """
        SourcePrecedence: int
        ReferenceSetPrecedence: int
        ReferenceSetUsed: int
        ComponentGroup: int
        Arrangement: int
        Accuracy: int
        Coating: int
        Count: int
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.ComponentHeader:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DataModes(Enum):
        """
        Members Include: 
         |AssemblyOnly| 
         |IncludeChildren| 
         |Solid| 

        """
        AssemblyOnly: int
        IncludeChildren: int
        Solid: int
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.DataModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NodeType(Enum):
        """
        Members Include: 
         |ComponentHeader| 
         |BodyHeader| 
         |PerComponentResult| 
         |PerBodyResult| 
         |OverallResult| 

        """
        ComponentHeader: int
        BodyHeader: int
        PerComponentResult: int
        PerBodyResult: int
        OverallResult: int
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.NodeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputTypes(Enum):
        """
        Members Include: 
         |Information| 
         |Xlsx| 
         |Csv| 
         |Xml| 
         |Json| 

        """
        Information: int
        Xlsx: int
        Csv: int
        Xml: int
        Json: int
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.OutputTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OverallResult(Enum):
        """
        Members Include: 
         |Material| 
         |Density| 
         |DensitySource| 
         |Area| 
         |AreaSource| 
         |Volume| 
         |VolumeSource| 
         |Mass| 
         |MassSource| 
         |Weight| 
         |WeightSource| 
         |CenterOfMassWCS| 
         |CenterOfMassAbsolute| 
         |CenterOfMassSource| 
         |FirstMomentsWCS| 
         |MomentsOfInertiaWCS| 
         |MomentsOfInertiaCentroidal| 
         |MomentsOfInertiaCentroidalSource| 
         |MomentsOfInertiaSpherical| 
         |ProductsOfInertiaWCS| 
         |ProductsOfInertiaCentroidal| 
         |ProductsOfInertiaCentroidalSource| 
         |PrincipalMomentsOfInertia| 
         |RadiiOfGyrationWCS| 
         |RadiiOfGyrationCentroidal| 
         |RadiiOfGyrationSpherical| 
         |PrincipalAxisWCS| 
         |EstimatedErrorRanges|  Unused from NX2206 
         |Warnings| 
         |Count| 

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
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.OverallResult:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PerBodyResult(Enum):
        """
        Members Include: 
         |BodyName| 
         |Count| 

        """
        BodyName: int
        Count: int
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.PerBodyResult:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PerComponentResult(Enum):
        """
        Members Include: 
         |ComponentName| 
         |ObjectDisplayName| 
         |ItemID| 
         |ItemName| 
         |ItemRevision| 
         |FileName| 
         |DescriptivePartName| 
         |ParentName| 
         |Count| 

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
        @staticmethod
        def ValueOf(value: int) -> MassExportBuilder.PerComponentResult:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DataMode(self) -> MassExportBuilder.DataModes:
        """
        Getter for property: ( MassExportBuilder.DataModes NXOpen) DataMode
         Returns the include children   
            
         
        """
        pass
    @DataMode.setter
    def DataMode(self, dataMode: MassExportBuilder.DataModes):
        """
        Setter for property: ( MassExportBuilder.DataModes NXOpen) DataMode
         Returns the include children   
            
         
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
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Objects
         Returns the objects   
            
         
        """
        pass
    @property
    def Output(self) -> MassExportBuilder.OutputTypes:
        """
        Getter for property: ( MassExportBuilder.OutputTypes NXOpen) Output
         Returns the output   
            
         
        """
        pass
    @Output.setter
    def Output(self, output: MassExportBuilder.OutputTypes):
        """
        Setter for property: ( MassExportBuilder.OutputTypes NXOpen) Output
         Returns the output   
            
         
        """
        pass
    @property
    def TemplateFileName(self) -> str:
        """
        Getter for property: (str) TemplateFileName
         Returns the template file name   
            
         
        """
        pass
    @TemplateFileName.setter
    def TemplateFileName(self, templateFileName: str):
        """
        Setter for property: (str) TemplateFileName
         Returns the template file name   
            
         
        """
        pass
    @property
    def UseLegacyLayoutForXLSX(self) -> bool:
        """
        Getter for property: (bool) UseLegacyLayoutForXLSX
         Returns the use legacy layout for XLSX   
            
         
        """
        pass
    @UseLegacyLayoutForXLSX.setter
    def UseLegacyLayoutForXLSX(self, useLegacyLayout: bool):
        """
        Setter for property: (bool) UseLegacyLayoutForXLSX
         Returns the use legacy layout for XLSX   
            
         
        """
        pass
    def AddAttributeToOverallResults(self, nodeNameBeforeAttr: str, attrName: str, state: bool) -> None:
        """
         Add attribute to overall results 
        """
        pass
    def LoadSystemDefault(self) -> None:
        """
         Load system default template values 
        """
        pass
    def MoveDown(self, nodeType: MassExportBuilder.NodeType, nodeId: int) -> None:
        """
         Move down node 
        """
        pass
    def MoveDownByName(self, nodeType: MassExportBuilder.NodeType, nodeName: str) -> None:
        """
         Move down node 
        """
        pass
    def MoveUp(self, nodeType: MassExportBuilder.NodeType, nodeId: int) -> None:
        """
         Move up node 
        """
        pass
    def MoveUpByName(self, nodeType: MassExportBuilder.NodeType, nodeName: str) -> None:
        """
         Move up node 
        """
        pass
    def OpenFromFile(self, fileName: str) -> None:
        """
         Open from a template file 
        """
        pass
    def RemoveAttributeFromOverallResults(self, attrName: str) -> None:
        """
         Remove attribute from overall results 
        """
        pass
    def RestoreDefault(self) -> None:
        """
         Restore to default template 
        """
        pass
    def SaveAsDefault(self) -> None:
        """
         Save current selection as default template 
        """
        pass
    def SaveToFile(self, fileName: str) -> None:
        """
         Save a template file 
        """
        pass
    def SetToggleState(self, nodeType: MassExportBuilder.NodeType, nodeId: int, state: bool) -> None:
        """
         Set node toggle state 
        """
        pass
    def SetToggleStateByName(self, nodeType: MassExportBuilder.NodeType, nodeName: str, state: bool) -> None:
        """
         Set node toggle state 
        """
        pass
import NXOpen
class MassLimitationBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Gateway.MassLimitationBuilder builder. """
    @property
    def MaximumArea(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumArea
         Returns the maximum area   
            
         
        """
        pass
    @property
    def MaximumAreaStatus(self) -> bool:
        """
        Getter for property: (bool) MaximumAreaStatus
         Returns the maximum area status   
            
         
        """
        pass
    @MaximumAreaStatus.setter
    def MaximumAreaStatus(self, areaLimitStatus: bool):
        """
        Setter for property: (bool) MaximumAreaStatus
         Returns the maximum area status   
            
         
        """
        pass
    @property
    def MaximumDensity(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumDensity
         Returns the maximum density   
            
         
        """
        pass
    @property
    def MaximumDensityStatus(self) -> bool:
        """
        Getter for property: (bool) MaximumDensityStatus
         Returns the maximum density status   
            
         
        """
        pass
    @MaximumDensityStatus.setter
    def MaximumDensityStatus(self, densityLimitStatus: bool):
        """
        Setter for property: (bool) MaximumDensityStatus
         Returns the maximum density status   
            
         
        """
        pass
    @property
    def MaximumGravityCenterStatusX(self) -> bool:
        """
        Getter for property: (bool) MaximumGravityCenterStatusX
         Returns the maximum gravity center status X   
            
         
        """
        pass
    @MaximumGravityCenterStatusX.setter
    def MaximumGravityCenterStatusX(self, gravityCenterLimitStatus: bool):
        """
        Setter for property: (bool) MaximumGravityCenterStatusX
         Returns the maximum gravity center status X   
            
         
        """
        pass
    @property
    def MaximumGravityCenterStatusY(self) -> bool:
        """
        Getter for property: (bool) MaximumGravityCenterStatusY
         Returns the maximum gravity center status Y   
            
         
        """
        pass
    @MaximumGravityCenterStatusY.setter
    def MaximumGravityCenterStatusY(self, gravityCenterLimitStatus: bool):
        """
        Setter for property: (bool) MaximumGravityCenterStatusY
         Returns the maximum gravity center status Y   
            
         
        """
        pass
    @property
    def MaximumGravityCenterStatusZ(self) -> bool:
        """
        Getter for property: (bool) MaximumGravityCenterStatusZ
         Returns the maximum gravity center status Z  
            
         
        """
        pass
    @MaximumGravityCenterStatusZ.setter
    def MaximumGravityCenterStatusZ(self, gravityCenterLimitStatus: bool):
        """
        Setter for property: (bool) MaximumGravityCenterStatusZ
         Returns the maximum gravity center status Z  
            
         
        """
        pass
    @property
    def MaximumGravityCenterX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumGravityCenterX
         Returns the maximum gravity center X  
            
         
        """
        pass
    @property
    def MaximumGravityCenterY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumGravityCenterY
         Returns the maximum gravity center Y  
            
         
        """
        pass
    @property
    def MaximumGravityCenterZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumGravityCenterZ
         Returns the maximum gravity center Z  
            
         
        """
        pass
    @property
    def MaximumMass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumMass
         Returns the maximum mass   
            
         
        """
        pass
    @property
    def MaximumMassStatus(self) -> bool:
        """
        Getter for property: (bool) MaximumMassStatus
         Returns the maximum mass status   
            
         
        """
        pass
    @MaximumMassStatus.setter
    def MaximumMassStatus(self, massLimitStatus: bool):
        """
        Setter for property: (bool) MaximumMassStatus
         Returns the maximum mass status   
            
         
        """
        pass
    @property
    def MaximumMomentsInertiaStatusXX(self) -> bool:
        """
        Getter for property: (bool) MaximumMomentsInertiaStatusXX
         Returns the maximum moments inertia status XX  
            
         
        """
        pass
    @MaximumMomentsInertiaStatusXX.setter
    def MaximumMomentsInertiaStatusXX(self, inertiaLimitStatus: bool):
        """
        Setter for property: (bool) MaximumMomentsInertiaStatusXX
         Returns the maximum moments inertia status XX  
            
         
        """
        pass
    @property
    def MaximumMomentsInertiaStatusYY(self) -> bool:
        """
        Getter for property: (bool) MaximumMomentsInertiaStatusYY
         Returns the maximum moments inertia status YY  
            
         
        """
        pass
    @MaximumMomentsInertiaStatusYY.setter
    def MaximumMomentsInertiaStatusYY(self, inertiaLimitStatus: bool):
        """
        Setter for property: (bool) MaximumMomentsInertiaStatusYY
         Returns the maximum moments inertia status YY  
            
         
        """
        pass
    @property
    def MaximumMomentsInertiaStatusZZ(self) -> bool:
        """
        Getter for property: (bool) MaximumMomentsInertiaStatusZZ
         Returns the maximum moments inertia status ZZ  
            
         
        """
        pass
    @MaximumMomentsInertiaStatusZZ.setter
    def MaximumMomentsInertiaStatusZZ(self, inertiaLimitStatus: bool):
        """
        Setter for property: (bool) MaximumMomentsInertiaStatusZZ
         Returns the maximum moments inertia status ZZ  
            
         
        """
        pass
    @property
    def MaximumMomentsInertiaXX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumMomentsInertiaXX
         Returns the maximum moments inertia XX  
            
         
        """
        pass
    @property
    def MaximumMomentsInertiaYY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumMomentsInertiaYY
         Returns the maximum moments inertia YY  
            
         
        """
        pass
    @property
    def MaximumMomentsInertiaZZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumMomentsInertiaZZ
         Returns the maximum moments inertia ZZ  
            
         
        """
        pass
    @property
    def MaximumProductsInertiaStatusXY(self) -> bool:
        """
        Getter for property: (bool) MaximumProductsInertiaStatusXY
         Returns the maximum products inertia status XY  
            
         
        """
        pass
    @MaximumProductsInertiaStatusXY.setter
    def MaximumProductsInertiaStatusXY(self, inertiaLimitStatus: bool):
        """
        Setter for property: (bool) MaximumProductsInertiaStatusXY
         Returns the maximum products inertia status XY  
            
         
        """
        pass
    @property
    def MaximumProductsInertiaStatusXZ(self) -> bool:
        """
        Getter for property: (bool) MaximumProductsInertiaStatusXZ
         Returns the maximum products inertia status XZ  
            
         
        """
        pass
    @MaximumProductsInertiaStatusXZ.setter
    def MaximumProductsInertiaStatusXZ(self, inertiaLimitStatus: bool):
        """
        Setter for property: (bool) MaximumProductsInertiaStatusXZ
         Returns the maximum products inertia status XZ  
            
         
        """
        pass
    @property
    def MaximumProductsInertiaStatusYZ(self) -> bool:
        """
        Getter for property: (bool) MaximumProductsInertiaStatusYZ
         Returns the maximum products inertia status YZ  
            
         
        """
        pass
    @MaximumProductsInertiaStatusYZ.setter
    def MaximumProductsInertiaStatusYZ(self, inertiaLimitStatus: bool):
        """
        Setter for property: (bool) MaximumProductsInertiaStatusYZ
         Returns the maximum products inertia status YZ  
            
         
        """
        pass
    @property
    def MaximumProductsInertiaXY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumProductsInertiaXY
         Returns the maximum products inertia XY  
            
         
        """
        pass
    @property
    def MaximumProductsInertiaXZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumProductsInertiaXZ
         Returns the maximum products inertia XZ  
            
         
        """
        pass
    @property
    def MaximumProductsInertiaYZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumProductsInertiaYZ
         Returns the maximum products inertia YZ  
            
         
        """
        pass
    @property
    def MaximumVolume(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumVolume
         Returns the maximum volume   
            
         
        """
        pass
    @property
    def MaximumVolumeStatus(self) -> bool:
        """
        Getter for property: (bool) MaximumVolumeStatus
         Returns the maximum volume status   
            
         
        """
        pass
    @MaximumVolumeStatus.setter
    def MaximumVolumeStatus(self, volumeLimitStatus: bool):
        """
        Setter for property: (bool) MaximumVolumeStatus
         Returns the maximum volume status   
            
         
        """
        pass
    @property
    def MinimumArea(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumArea
         Returns the minimum area   
            
         
        """
        pass
    @property
    def MinimumAreaStatus(self) -> bool:
        """
        Getter for property: (bool) MinimumAreaStatus
         Returns the minimum area status   
            
         
        """
        pass
    @MinimumAreaStatus.setter
    def MinimumAreaStatus(self, areaLimitStatus: bool):
        """
        Setter for property: (bool) MinimumAreaStatus
         Returns the minimum area status   
            
         
        """
        pass
    @property
    def MinimumDensity(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumDensity
         Returns the minimum density   
            
         
        """
        pass
    @property
    def MinimumDensityStatus(self) -> bool:
        """
        Getter for property: (bool) MinimumDensityStatus
         Returns the minimum density status   
            
         
        """
        pass
    @MinimumDensityStatus.setter
    def MinimumDensityStatus(self, densityLimitStatus: bool):
        """
        Setter for property: (bool) MinimumDensityStatus
         Returns the minimum density status   
            
         
        """
        pass
    @property
    def MinimumGravityCenterStatusX(self) -> bool:
        """
        Getter for property: (bool) MinimumGravityCenterStatusX
         Returns the minimum gravity center status X   
            
         
        """
        pass
    @MinimumGravityCenterStatusX.setter
    def MinimumGravityCenterStatusX(self, gravityCenterLimitStatus: bool):
        """
        Setter for property: (bool) MinimumGravityCenterStatusX
         Returns the minimum gravity center status X   
            
         
        """
        pass
    @property
    def MinimumGravityCenterStatusY(self) -> bool:
        """
        Getter for property: (bool) MinimumGravityCenterStatusY
         Returns the minimum gravity center status Y   
            
         
        """
        pass
    @MinimumGravityCenterStatusY.setter
    def MinimumGravityCenterStatusY(self, gravityCenterLimitStatus: bool):
        """
        Setter for property: (bool) MinimumGravityCenterStatusY
         Returns the minimum gravity center status Y   
            
         
        """
        pass
    @property
    def MinimumGravityCenterStatusZ(self) -> bool:
        """
        Getter for property: (bool) MinimumGravityCenterStatusZ
         Returns the minimum gravity center status Z  
            
         
        """
        pass
    @MinimumGravityCenterStatusZ.setter
    def MinimumGravityCenterStatusZ(self, gravityCenterLimitStatus: bool):
        """
        Setter for property: (bool) MinimumGravityCenterStatusZ
         Returns the minimum gravity center status Z  
            
         
        """
        pass
    @property
    def MinimumGravityCenterX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumGravityCenterX
         Returns the minimum gravity center X  
            
         
        """
        pass
    @property
    def MinimumGravityCenterY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumGravityCenterY
         Returns the minimum gravity center Y  
            
         
        """
        pass
    @property
    def MinimumGravityCenterZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumGravityCenterZ
         Returns the minimum gravity center Z  
            
         
        """
        pass
    @property
    def MinimumMass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumMass
         Returns the minimum mass   
            
         
        """
        pass
    @property
    def MinimumMassStatus(self) -> bool:
        """
        Getter for property: (bool) MinimumMassStatus
         Returns the minimum mass status   
            
         
        """
        pass
    @MinimumMassStatus.setter
    def MinimumMassStatus(self, massLimitStatus: bool):
        """
        Setter for property: (bool) MinimumMassStatus
         Returns the minimum mass status   
            
         
        """
        pass
    @property
    def MinimumMomentsInertiaStatusXX(self) -> bool:
        """
        Getter for property: (bool) MinimumMomentsInertiaStatusXX
         Returns the minimum moments inertia status XX  
            
         
        """
        pass
    @MinimumMomentsInertiaStatusXX.setter
    def MinimumMomentsInertiaStatusXX(self, inertiaLimitStatus: bool):
        """
        Setter for property: (bool) MinimumMomentsInertiaStatusXX
         Returns the minimum moments inertia status XX  
            
         
        """
        pass
    @property
    def MinimumMomentsInertiaStatusYY(self) -> bool:
        """
        Getter for property: (bool) MinimumMomentsInertiaStatusYY
         Returns the minimum moments inertia status YY  
            
         
        """
        pass
    @MinimumMomentsInertiaStatusYY.setter
    def MinimumMomentsInertiaStatusYY(self, inertiaLimitStatus: bool):
        """
        Setter for property: (bool) MinimumMomentsInertiaStatusYY
         Returns the minimum moments inertia status YY  
            
         
        """
        pass
    @property
    def MinimumMomentsInertiaStatusZZ(self) -> bool:
        """
        Getter for property: (bool) MinimumMomentsInertiaStatusZZ
         Returns the minimum moments inertia status ZZ  
            
         
        """
        pass
    @MinimumMomentsInertiaStatusZZ.setter
    def MinimumMomentsInertiaStatusZZ(self, inertiaLimitStatus: bool):
        """
        Setter for property: (bool) MinimumMomentsInertiaStatusZZ
         Returns the minimum moments inertia status ZZ  
            
         
        """
        pass
    @property
    def MinimumMomentsInertiaXX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumMomentsInertiaXX
         Returns the minimum moments inertia XX  
            
         
        """
        pass
    @property
    def MinimumMomentsInertiaYY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumMomentsInertiaYY
         Returns the minimum moments inertia YY  
            
         
        """
        pass
    @property
    def MinimumMomentsInertiaZZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumMomentsInertiaZZ
         Returns the minimum moments inertia ZZ  
            
         
        """
        pass
    @property
    def MinimumProductsInertiaStatusXY(self) -> bool:
        """
        Getter for property: (bool) MinimumProductsInertiaStatusXY
         Returns the minimum products inertia status XY  
            
         
        """
        pass
    @MinimumProductsInertiaStatusXY.setter
    def MinimumProductsInertiaStatusXY(self, inertiaLimitStatus: bool):
        """
        Setter for property: (bool) MinimumProductsInertiaStatusXY
         Returns the minimum products inertia status XY  
            
         
        """
        pass
    @property
    def MinimumProductsInertiaStatusXZ(self) -> bool:
        """
        Getter for property: (bool) MinimumProductsInertiaStatusXZ
         Returns the minimum products inertia status XZ  
            
         
        """
        pass
    @MinimumProductsInertiaStatusXZ.setter
    def MinimumProductsInertiaStatusXZ(self, inertiaLimitStatus: bool):
        """
        Setter for property: (bool) MinimumProductsInertiaStatusXZ
         Returns the minimum products inertia status XZ  
            
         
        """
        pass
    @property
    def MinimumProductsInertiaStatusYZ(self) -> bool:
        """
        Getter for property: (bool) MinimumProductsInertiaStatusYZ
         Returns the minimum products inertia status YZ  
            
         
        """
        pass
    @MinimumProductsInertiaStatusYZ.setter
    def MinimumProductsInertiaStatusYZ(self, inertiaLimitStatus: bool):
        """
        Setter for property: (bool) MinimumProductsInertiaStatusYZ
         Returns the minimum products inertia status YZ  
            
         
        """
        pass
    @property
    def MinimumProductsInertiaXY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumProductsInertiaXY
         Returns the minimum product inertia XY  
            
         
        """
        pass
    @property
    def MinimumProductsInertiaXZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumProductsInertiaXZ
         Returns the minimum product inertia XZ  
            
         
        """
        pass
    @property
    def MinimumProductsInertiaYZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumProductsInertiaYZ
         Returns the minimum product inertia YZ  
            
         
        """
        pass
    @property
    def MinimumVolume(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumVolume
         Returns the minimum volume   
            
         
        """
        pass
    @property
    def MinimumVolumeStatus(self) -> bool:
        """
        Getter for property: (bool) MinimumVolumeStatus
         Returns the minimum volume status   
            
         
        """
        pass
    @MinimumVolumeStatus.setter
    def MinimumVolumeStatus(self, volumeLimitStatus: bool):
        """
        Setter for property: (bool) MinimumVolumeStatus
         Returns the minimum volume status   
            
         
        """
        pass
    @property
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Objects
         Returns the objects   
            
         
        """
        pass
    def GetLimitationValues(self) -> None:
        """
         Get the limitation of the root part or user selected object, and save to the builder . 
        """
        pass
import NXOpen
class MassPartSpecificOptionsBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Gateway.MassPartSpecificOptionsBuilder builder. """
    @property
    def OverrideReferenceSet(self) -> bool:
        """
        Getter for property: (bool) OverrideReferenceSet
         Returns the name of reference set   
            
         
        """
        pass
    @OverrideReferenceSet.setter
    def OverrideReferenceSet(self, overrideReferenceSet: bool):
        """
        Setter for property: (bool) OverrideReferenceSet
         Returns the name of reference set   
            
         
        """
        pass
    @property
    def ReferenceSetName(self) -> str:
        """
        Getter for property: (str) ReferenceSetName
         Returns the name of reference set   
            
         
        """
        pass
    @ReferenceSetName.setter
    def ReferenceSetName(self, referenceSetName: str):
        """
        Setter for property: (str) ReferenceSetName
         Returns the name of reference set   
            
         
        """
        pass
    def RemovePartSpecificSetting(self) -> None:
        """
         Remove the reference set setting from this builder. 
        """
        pass
import NXOpen
class MassPropertyOptionsBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Gateway.MassPropertyOptionsBuilder builder. """
    class AccuracyTypes(Enum):
        """
        Members Include: 
         |Value1| 
         |Value2| 
         |Value3| 
         |Value4| 
         |Value5| 
         |Value6| 

        """
        Value1: int
        Value2: int
        Value3: int
        Value4: int
        Value5: int
        Value6: int
        @staticmethod
        def ValueOf(value: int) -> MassPropertyOptionsBuilder.AccuracyTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AccuracyType(self) -> MassPropertyOptionsBuilder.AccuracyTypes:
        """
        Getter for property: ( MassPropertyOptionsBuilder.AccuracyTypes NXOpen) AccuracyType
         Returns the accuracy   
            
         
        """
        pass
    @AccuracyType.setter
    def AccuracyType(self, accuracy: MassPropertyOptionsBuilder.AccuracyTypes):
        """
        Setter for property: ( MassPropertyOptionsBuilder.AccuracyTypes NXOpen) AccuracyType
         Returns the accuracy   
            
         
        """
        pass
    @property
    def ComponentGroupName(self) -> str:
        """
        Getter for property: (str) ComponentGroupName
         Returns the name of component group   
            
         
        """
        pass
    @ComponentGroupName.setter
    def ComponentGroupName(self, componentGroupName: str):
        """
        Setter for property: (str) ComponentGroupName
         Returns the name of component group   
            
         
        """
        pass
    @property
    def MarkerColorOfAllComponents(self) -> int:
        """
        Getter for property: (int) MarkerColorOfAllComponents
         Returns the mark color of all components   
            
         
        """
        pass
    @MarkerColorOfAllComponents.setter
    def MarkerColorOfAllComponents(self, color: int):
        """
        Setter for property: (int) MarkerColorOfAllComponents
         Returns the mark color of all components   
            
         
        """
        pass
    @property
    def MarkerColorOfDisplayedPart(self) -> int:
        """
        Getter for property: (int) MarkerColorOfDisplayedPart
         Returns the mark color of display part   
            
         
        """
        pass
    @MarkerColorOfDisplayedPart.setter
    def MarkerColorOfDisplayedPart(self, color: int):
        """
        Setter for property: (int) MarkerColorOfDisplayedPart
         Returns the mark color of display part   
            
         
        """
        pass
    @property
    def MarkerColorOfSelectedComponentSet(self) -> int:
        """
        Getter for property: (int) MarkerColorOfSelectedComponentSet
         Returns the mark color of selected component set   
            
         
        """
        pass
    @MarkerColorOfSelectedComponentSet.setter
    def MarkerColorOfSelectedComponentSet(self, color: int):
        """
        Setter for property: (int) MarkerColorOfSelectedComponentSet
         Returns the mark color of selected component set   
            
         
        """
        pass
    @property
    def MarkerColorOfSelectedComponents(self) -> int:
        """
        Getter for property: (int) MarkerColorOfSelectedComponents
         Returns the mark color of selected components   
            
         
        """
        pass
    @MarkerColorOfSelectedComponents.setter
    def MarkerColorOfSelectedComponents(self, color: int):
        """
        Setter for property: (int) MarkerColorOfSelectedComponents
         Returns the mark color of selected components   
            
         
        """
        pass
    @property
    def UseAllComponents(self) -> bool:
        """
        Getter for property: (bool) UseAllComponents
         Returns the value of using all components   
            
         
        """
        pass
    @UseAllComponents.setter
    def UseAllComponents(self, enabled: bool):
        """
        Setter for property: (bool) UseAllComponents
         Returns the value of using all components   
            
         
        """
        pass
    @property
    def UseDisplayedPart(self) -> bool:
        """
        Getter for property: (bool) UseDisplayedPart
         Returns the value of using displayed part   
            
         
        """
        pass
    @UseDisplayedPart.setter
    def UseDisplayedPart(self, enabled: bool):
        """
        Setter for property: (bool) UseDisplayedPart
         Returns the value of using displayed part   
            
         
        """
        pass
    @property
    def UseSelectedComponentSet(self) -> bool:
        """
        Getter for property: (bool) UseSelectedComponentSet
         Returns the value of using selected component set   
            
         
        """
        pass
    @UseSelectedComponentSet.setter
    def UseSelectedComponentSet(self, enabled: bool):
        """
        Setter for property: (bool) UseSelectedComponentSet
         Returns the value of using selected component set   
            
         
        """
        pass
    @property
    def UseSelectedComponents(self) -> bool:
        """
        Getter for property: (bool) UseSelectedComponents
         Returns the value of using selected components   
            
         
        """
        pass
    @UseSelectedComponents.setter
    def UseSelectedComponents(self, enabled: bool):
        """
        Setter for property: (bool) UseSelectedComponents
         Returns the value of using selected components   
            
         
        """
        pass
    @property
    def UseSourceHierarchy(self) -> bool:
        """
        Getter for property: (bool) UseSourceHierarchy
         Returns the value of using source hierarchy   
            
         
        """
        pass
    @UseSourceHierarchy.setter
    def UseSourceHierarchy(self, enabled: bool):
        """
        Setter for property: (bool) UseSourceHierarchy
         Returns the value of using source hierarchy   
            
         
        """
        pass
    def GetSourceHierarchy(self) -> List[int]:
        """
         Get Source Hierarchy  
         Returns variableSources (List[int]):  .
        """
        pass
    def SetSourceHierarchy(self, variableSources: List[int]) -> None:
        """
         Set Source Hierarchy  
        """
        pass
import NXOpen
class MassValueBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Gateway.MassValueBuilder builder. """
    class MassTypes(Enum):
        """
        Members Include: 
         |Unset| 
         |MassOnly| 
         |DensityOnly| 
         |VolumeOnly| 
         |DensityMass| 
         |DensityVolume| 
         |MassVolume| 
         |AssertAll| 

        """
        Unset: int
        MassOnly: int
        DensityOnly: int
        VolumeOnly: int
        DensityMass: int
        DensityVolume: int
        MassVolume: int
        AssertAll: int
        @staticmethod
        def ValueOf(value: int) -> MassValueBuilder.MassTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ValueSourceType(Enum):
        """
        Members Include: 
         |Unset| 
         |Computed| 
         |Asserted| 
         |UserDefined1| 
         |UserDefined2| 
         |UserDefined3| 
         |UserDefined4| 
         |ComputedCoated| 

        """
        Unset: int
        Computed: int
        Asserted: int
        UserDefined1: int
        UserDefined2: int
        UserDefined3: int
        UserDefined4: int
        ComputedCoated: int
        @staticmethod
        def ValueOf(value: int) -> MassValueBuilder.ValueSourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Area(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) Area
         Returns the area   
            
         
        """
        pass
    @Area.setter
    def Area(self, area: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) Area
         Returns the area   
            
         
        """
        pass
    @property
    def AssignRolledUpAttribute(self) -> bool:
        """
        Getter for property: (bool) AssignRolledUpAttribute
         Returns the assignRolledUpAttribute   
            
         
        """
        pass
    @AssignRolledUpAttribute.setter
    def AssignRolledUpAttribute(self, assignRolledUpAttribute: bool):
        """
        Setter for property: (bool) AssignRolledUpAttribute
         Returns the assignRolledUpAttribute   
            
         
        """
        pass
    @property
    def Density(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) Density
         Returns the density   
            
         
        """
        pass
    @Density.setter
    def Density(self, density: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) Density
         Returns the density   
            
         
        """
        pass
    @property
    def DeriveOption(self) -> int:
        """
        Getter for property: (int) DeriveOption
         Returns the deriveOption   
            
         
        """
        pass
    @DeriveOption.setter
    def DeriveOption(self, deriveOption: int):
        """
        Setter for property: (int) DeriveOption
         Returns the deriveOption   
            
         
        """
        pass
    @property
    def GravityCenterX(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) GravityCenterX
         Returns the gravity center x   
            
         
        """
        pass
    @GravityCenterX.setter
    def GravityCenterX(self, gravityCenterX: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) GravityCenterX
         Returns the gravity center x   
            
         
        """
        pass
    @property
    def GravityCenterY(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) GravityCenterY
         Returns the gravity center y   
            
         
        """
        pass
    @GravityCenterY.setter
    def GravityCenterY(self, gravityCenterY: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) GravityCenterY
         Returns the gravity center y   
            
         
        """
        pass
    @property
    def GravityCenterZ(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) GravityCenterZ
         Returns the gravity center z   
            
         
        """
        pass
    @GravityCenterZ.setter
    def GravityCenterZ(self, gravityCenterZ: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) GravityCenterZ
         Returns the gravity center z   
            
         
        """
        pass
    @property
    def InertiaXX(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) InertiaXX
         Returns the inertia xx   
            
         
        """
        pass
    @InertiaXX.setter
    def InertiaXX(self, inertiaXX: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) InertiaXX
         Returns the inertia xx   
            
         
        """
        pass
    @property
    def InertiaXY(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) InertiaXY
         Returns the inertia xy   
            
         
        """
        pass
    @InertiaXY.setter
    def InertiaXY(self, inertiaXY: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) InertiaXY
         Returns the inertia xy   
            
         
        """
        pass
    @property
    def InertiaXZ(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) InertiaXZ
         Returns the inertia xz   
            
         
        """
        pass
    @InertiaXZ.setter
    def InertiaXZ(self, inertiaXZ: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) InertiaXZ
         Returns the inertia xz   
            
         
        """
        pass
    @property
    def InertiaYY(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) InertiaYY
         Returns the inertia yy   
            
         
        """
        pass
    @InertiaYY.setter
    def InertiaYY(self, inertiaYY: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) InertiaYY
         Returns the inertia yy   
            
         
        """
        pass
    @property
    def InertiaYZ(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) InertiaYZ
         Returns the inertia yz   
            
         
        """
        pass
    @InertiaYZ.setter
    def InertiaYZ(self, inertiaYZ: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) InertiaYZ
         Returns the inertia yz   
            
         
        """
        pass
    @property
    def InertiaZZ(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) InertiaZZ
         Returns the inertia zz   
            
         
        """
        pass
    @InertiaZZ.setter
    def InertiaZZ(self, inertiaZZ: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) InertiaZZ
         Returns the inertia zz   
            
         
        """
        pass
    @property
    def Mass(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) Mass
         Returns the mass   
            
         
        """
        pass
    @Mass.setter
    def Mass(self, mass: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) Mass
         Returns the mass   
            
         
        """
        pass
    @property
    def MassType(self) -> MassValueBuilder.MassTypes:
        """
        Getter for property: ( MassValueBuilder.MassTypes NXOpen) MassType
         Returns the mass type   
            
         
        """
        pass
    @MassType.setter
    def MassType(self, massType: MassValueBuilder.MassTypes):
        """
        Setter for property: ( MassValueBuilder.MassTypes NXOpen) MassType
         Returns the mass type   
            
         
        """
        pass
    @property
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Objects
         Returns the objects   
            
         
        """
        pass
    @property
    def Volume(self) -> MassValueBuilder.ValueSourceType:
        """
        Getter for property: ( MassValueBuilder.ValueSourceType NXOpen) Volume
         Returns the volume   
            
         
        """
        pass
    @Volume.setter
    def Volume(self, volume: MassValueBuilder.ValueSourceType):
        """
        Setter for property: ( MassValueBuilder.ValueSourceType NXOpen) Volume
         Returns the volume   
            
         
        """
        pass
    def GetMassValues(self) -> None:
        """
         Get the value settings of the root part or user selected object, and save to the builder . 
        """
        pass
    def UpdateDensityValueSource(self, valueType: MassValueBuilder.ValueSourceType) -> None:
        """
         Update the value source of density. 
        """
        pass
    def UpdateMassValueSource(self, valueType: MassValueBuilder.ValueSourceType) -> None:
        """
         Update the value source of mass. 
        """
        pass
    def UpdateVolumeValueSource(self, valueType: MassValueBuilder.ValueSourceType) -> None:
        """
         Update the value source of volume. 
        """
        pass
import NXOpen
class Mass(NXOpen.TaggedObject): 
    """ Represents a mass abstract class """
    pass
import NXOpen
class PasteBuilder(NXOpen.Builder): 
    """
Represents a NXOpen.Gateway.PasteBuilder
"""
    pass
