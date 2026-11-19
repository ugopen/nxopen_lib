from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
##   @brief  Contains methods for adding document data for CAE Report.  
## 
##   
## 
##   <br>  Created in NX11.0.0  <br> 

class DocumentDataGroup(DocumentData): 
    """ <summary> Contains methods for adding document data for CAE Report. </summary> """


    ##  Creates a new @link NXOpen::OpenXml::ImageGroupDocumentData NXOpen::OpenXml::ImageGroupDocumentData@endlink  object.
    ##         Does not to free this object, it will be free while deleting 
    ##         @link NXOpen::OpenXml::DocumentDataGroup NXOpen::OpenXml::DocumentDataGroup@endlink  object
    ##  @return data (@link ImageGroupDocumentData NXOpen.OpenXml.ImageGroupDocumentData@endlink):  the image group data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def AddImageGroup(self) -> ImageGroupDocumentData:
        """
         Creates a new @link NXOpen::OpenXml::ImageGroupDocumentData NXOpen::OpenXml::ImageGroupDocumentData@endlink  object.
                Does not to free this object, it will be free while deleting 
                @link NXOpen::OpenXml::DocumentDataGroup NXOpen::OpenXml::DocumentDataGroup@endlink  object
         @return data (@link ImageGroupDocumentData NXOpen.OpenXml.ImageGroupDocumentData@endlink):  the image group data .
        """
        pass
    
    ##  Creates a new @link NXOpen::OpenXml::TableDocumentData NXOpen::OpenXml::TableDocumentData@endlink  object.
    ##         Does not to free this object, it will be free while deleting 
    ##         @link NXOpen::OpenXml::DocumentDataGroup NXOpen::OpenXml::DocumentDataGroup@endlink  object
    ##  @return data (@link TableDocumentData NXOpen.OpenXml.TableDocumentData@endlink):  the table data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="columnCount"> (int)  the column size of the table</param>
    ## <param name="rowCount"> (int)  the row size of the table</param>
    def AddTable(self, columnCount: int, rowCount: int) -> TableDocumentData:
        """
         Creates a new @link NXOpen::OpenXml::TableDocumentData NXOpen::OpenXml::TableDocumentData@endlink  object.
                Does not to free this object, it will be free while deleting 
                @link NXOpen::OpenXml::DocumentDataGroup NXOpen::OpenXml::DocumentDataGroup@endlink  object
         @return data (@link TableDocumentData NXOpen.OpenXml.TableDocumentData@endlink):  the table data .
        """
        pass
    
    ##  Creates a new @link NXOpen::OpenXml::TextDocumentData NXOpen::OpenXml::TextDocumentData@endlink  object.
    ##         Does not to free this object, it will be free while deleting 
    ##         @link NXOpen::OpenXml::DocumentDataGroup NXOpen::OpenXml::DocumentDataGroup@endlink  object
    ##  @return data (@link TextDocumentData NXOpen.OpenXml.TextDocumentData@endlink):  the text data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="textContent"> (str)  the content of the text data</param>
    def AddText(self, textContent: str) -> TextDocumentData:
        """
         Creates a new @link NXOpen::OpenXml::TextDocumentData NXOpen::OpenXml::TextDocumentData@endlink  object.
                Does not to free this object, it will be free while deleting 
                @link NXOpen::OpenXml::DocumentDataGroup NXOpen::OpenXml::DocumentDataGroup@endlink  object
         @return data (@link TextDocumentData NXOpen.OpenXml.TextDocumentData@endlink):  the text data .
        """
        pass
    
    ##  Deletes all document data
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def DeleteAllData(self) -> None:
        """
         Deletes all document data
        """
        pass
    
    ##  Deletes the nth document data
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  the index of data</param>
    def DeleteNthData(self, index: int) -> None:
        """
         Deletes the nth document data
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Gets the number of data to be exported
    ##  @return dataCount (int):  the number of data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetDataCount(self) -> int:
        """
         Gets the number of data to be exported
         @return dataCount (int):  the number of data .
        """
        pass
    
    ##  Gets the nth document data object.
    ##         Does not to free this object, it will be free while deleting 
    ##         @link NXOpen::OpenXml::DocumentDataGroup NXOpen::OpenXml::DocumentDataGroup@endlink  object
    ##  @return data (@link DocumentData NXOpen.OpenXml.DocumentData@endlink):  the data.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  the index of data</param>
    def GetNthData(self, index: int) -> DocumentData:
        """
         Gets the nth document data object.
                Does not to free this object, it will be free while deleting 
                @link NXOpen::OpenXml::DocumentDataGroup NXOpen::OpenXml::DocumentDataGroup@endlink  object
         @return data (@link DocumentData NXOpen.OpenXml.DocumentData@endlink):  the data.
        """
        pass
    
import NXOpen
##  Represents the definition of the base document data
## 
##   <br>  Created in NX11.0.0  <br> 

class DocumentData(NXOpen.TransientObject): 
    """ Represents the definition of the base document data"""


    ##  the document data type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Base</term><description> 
    ##  the base document data type </description> </item><item><term> 
    ## Text</term><description> 
    ##  the document data type of text</description> </item><item><term> 
    ## Table</term><description> 
    ##  the document data type of table</description> </item><item><term> 
    ## TableCell</term><description> 
    ##  the document data type of table cell</description> </item><item><term> 
    ## Image</term><description> 
    ##  the document data type of image</description> </item><item><term> 
    ## ImageGroup</term><description> 
    ##  the document data type of image group</description> </item><item><term> 
    ## Group</term><description> 
    ##  the document data type of data group</description> </item></list>
    class Type(Enum):
        """
        Members Include: <Base> <Text> <Table> <TableCell> <Image> <ImageGroup> <Group>
        """
        Base: int
        Text: int
        Table: int
        TableCell: int
        Image: int
        ImageGroup: int
        Group: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DocumentData.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Gets a specified document data type 
    ##  @return dataType (@link DocumentData.Type NXOpen.OpenXml.DocumentData.Type@endlink):  the data type defined by the @link NXOpen::OpenXml::DocumentData::Type NXOpen::OpenXml::DocumentData::Type@endlink  .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetDataType(self) -> DocumentData.Type:
        """
         Gets a specified document data type 
         @return dataType (@link DocumentData.Type NXOpen.OpenXml.DocumentData.Type@endlink):  the data type defined by the @link NXOpen::OpenXml::DocumentData::Type NXOpen::OpenXml::DocumentData::Type@endlink  .
        """
        pass
    
##  Represents the image to be exported to the speific Open XML file. 
## 
##   <br>  Created in NX11.0.0  <br> 

class ImageDocumentData(DocumentData): 
    """ Represents the image to be exported to the speific Open XML file. """


    ##  the location of the caption for image data
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Above</term><description> 
    ##  the above position </description> </item><item><term> 
    ## Bellow</term><description> 
    ##  the bellow position</description> </item></list>
    class CaptionPosition(Enum):
        """
        Members Include: <Above> <Bellow>
        """
        Above: int
        Bellow: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ImageDocumentData.CaptionPosition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Gets the caption of the image data
    ##  @return A tuple consisting of (caption, position). 
    ##  - caption is: str.
    ##  - position is: @link ImageDocumentData.CaptionPosition NXOpen.OpenXml.ImageDocumentData.CaptionPosition@endlink.

    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetCaption(self) -> Tuple[str, ImageDocumentData.CaptionPosition]:
        """
         Gets the caption of the image data
         @return A tuple consisting of (caption, position). 
         - caption is: str.
         - position is: @link ImageDocumentData.CaptionPosition NXOpen.OpenXml.ImageDocumentData.CaptionPosition@endlink.

        """
        pass
    
    ##  Gets the file name of the image data
    ##  @return fileName (str): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetFileName(self) -> str:
        """
         Gets the file name of the image data
         @return fileName (str): .
        """
        pass
    
    ##  Sets the caption of the image data
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="position"> (@link ImageDocumentData.CaptionPosition NXOpen.OpenXml.ImageDocumentData.CaptionPosition@endlink) </param>
    ## <param name="caption"> (str) </param>
    def SetCaption(self, position: ImageDocumentData.CaptionPosition, caption: str) -> None:
        """
         Sets the caption of the image data
        """
        pass
    
    ##  Sets the file name of the image data
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fileName"> (str) </param>
    def SetFileName(self, fileName: str) -> None:
        """
         Sets the file name of the image data
        """
        pass
    
##  Represents the group of images to be exported to the speific Open XML file. 
## 
##   <br>  Created in NX11.0.0  <br> 

class ImageGroupDocumentData(DocumentData): 
    """ Represents the group of images to be exported to the speific Open XML file. """


    ##  Creates a new @link NXOpen::OpenXml::ImageDocumentData NXOpen::OpenXml::ImageDocumentData@endlink  object.
    ##  @return data (@link ImageDocumentData NXOpen.OpenXml.ImageDocumentData@endlink):  the image data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fileName"> (str)  the file name of the image data</param>
    ## <param name="caption"> (str)  the caption of the image data</param>
    def AddImage(self, fileName: str, caption: str) -> ImageDocumentData:
        """
         Creates a new @link NXOpen::OpenXml::ImageDocumentData NXOpen::OpenXml::ImageDocumentData@endlink  object.
         @return data (@link ImageDocumentData NXOpen.OpenXml.ImageDocumentData@endlink):  the image data .
        """
        pass
    
    ##  Deletes all images data
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def DeleteAllImages(self) -> None:
        """
         Deletes all images data
        """
        pass
    
    ##  Deletes the nth image data
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  the index of image</param>
    def DeleteNthImage(self, index: int) -> None:
        """
         Deletes the nth image data
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Gets the number of images 
    ##  @return imageCount (int):  number of images.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetImagesCount(self) -> int:
        """
         Gets the number of images 
         @return imageCount (int):  number of images.
        """
        pass
    
    ##  Gets the nth image data
    ##  @return data (@link ImageDocumentData NXOpen.OpenXml.ImageDocumentData@endlink):  the image data.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  the index of image data</param>
    def GetNthImage(self, index: int) -> ImageDocumentData:
        """
         Gets the nth image data
         @return data (@link ImageDocumentData NXOpen.OpenXml.ImageDocumentData@endlink):  the image data.
        """
        pass
    
##  Represents the table cell to be exported to the speific Open XML file. 
## 
##   <br>  Created in NX11.0.0  <br> 

class TableCellData(DocumentData): 
    """ Represents the table cell to be exported to the speific Open XML file. """


    ##  Creates a new @link NXOpen::OpenXml::ImageGroupDocumentData NXOpen::OpenXml::ImageGroupDocumentData@endlink  object.
    ##         Does not to free this object, it will be free while deleting 
    ##         @link NXOpen::OpenXml::TableCellData NXOpen::OpenXml::TableCellData@endlink  object
    ##  @return data (@link ImageGroupDocumentData NXOpen.OpenXml.ImageGroupDocumentData@endlink):  the image group data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def AddImageGroup(self) -> ImageGroupDocumentData:
        """
         Creates a new @link NXOpen::OpenXml::ImageGroupDocumentData NXOpen::OpenXml::ImageGroupDocumentData@endlink  object.
                Does not to free this object, it will be free while deleting 
                @link NXOpen::OpenXml::TableCellData NXOpen::OpenXml::TableCellData@endlink  object
         @return data (@link ImageGroupDocumentData NXOpen.OpenXml.ImageGroupDocumentData@endlink):  the image group data .
        """
        pass
    
    ##  Creates a new @link NXOpen::OpenXml::TextDocumentData NXOpen::OpenXml::TextDocumentData@endlink  object.
    ##         Does not to free this object, it will be free while deleting 
    ##         @link NXOpen::OpenXml::TableCellData NXOpen::OpenXml::TableCellData@endlink  object
    ##  @return data (@link TextDocumentData NXOpen.OpenXml.TextDocumentData@endlink):  the text data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="textContent"> (str)  the content of the text data</param>
    def AddText(self, textContent: str) -> TextDocumentData:
        """
         Creates a new @link NXOpen::OpenXml::TextDocumentData NXOpen::OpenXml::TextDocumentData@endlink  object.
                Does not to free this object, it will be free while deleting 
                @link NXOpen::OpenXml::TableCellData NXOpen::OpenXml::TableCellData@endlink  object
         @return data (@link TextDocumentData NXOpen.OpenXml.TextDocumentData@endlink):  the text data .
        """
        pass
    
    ##  Removes all contents data
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def ClearContents(self) -> None:
        """
         Removes all contents data
        """
        pass
    
    ##  Removes the nth content data
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  the index of content</param>
    def DeleteNthContent(self, index: int) -> None:
        """
         Removes the nth content data
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Gets the number of content in the table cell
    ##  @return dataCount (int):  the number of content .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetContentCount(self) -> int:
        """
         Gets the number of content in the table cell
         @return dataCount (int):  the number of content .
        """
        pass
    
    ##  Gets the grid IDs of the table cell
    ##  @return ids (List[int]):  the grid ID array .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetGridsId(self) -> List[int]:
        """
         Gets the grid IDs of the table cell
         @return ids (List[int]):  the grid ID array .
        """
        pass
    
    ##  Gets the nth content data        
    ##         Does not to free this object, it will be free while deleting 
    ##         @link NXOpen::OpenXml::TableCellData NXOpen::OpenXml::TableCellData@endlink  object
    ##  @return data (@link DocumentData NXOpen.OpenXml.DocumentData@endlink):  the content.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  the index of content</param>
    def GetNthContent(self, index: int) -> DocumentData:
        """
         Gets the nth content data        
                Does not to free this object, it will be free while deleting 
                @link NXOpen::OpenXml::TableCellData NXOpen::OpenXml::TableCellData@endlink  object
         @return data (@link DocumentData NXOpen.OpenXml.DocumentData@endlink):  the content.
        """
        pass
    
##  Represents the table to be exported to the speific Open XML file. 
## 
##   <br>  Created in NX11.0.0  <br> 

class TableDocumentData(DocumentData): 
    """ Represents the table to be exported to the speific Open XML file. """


    ##  the location of the caption for table data
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Above</term><description> 
    ##  the above position </description> </item><item><term> 
    ## Bellow</term><description> 
    ##  the bellow position</description> </item></list>
    class CaptionPosition(Enum):
        """
        Members Include: <Above> <Bellow>
        """
        Above: int
        Bellow: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TableDocumentData.CaptionPosition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Creates a new @link NXOpen::OpenXml::TableCellData NXOpen::OpenXml::TableCellData@endlink  object.
    ##         Does not to free this object, it will be free while deleting 
    ##         @link NXOpen::OpenXml::TableDocumentData NXOpen::OpenXml::TableDocumentData@endlink  object
    ##  @return cell (@link TableCellData NXOpen.OpenXml.TableCellData@endlink):  the table cell data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="grids"> (List[int])  the grid IDs to be mergered into the cell data</param>
    def AddCellData(self, grids: List[int]) -> TableCellData:
        """
         Creates a new @link NXOpen::OpenXml::TableCellData NXOpen::OpenXml::TableCellData@endlink  object.
                Does not to free this object, it will be free while deleting 
                @link NXOpen::OpenXml::TableDocumentData NXOpen::OpenXml::TableDocumentData@endlink  object
         @return cell (@link TableCellData NXOpen.OpenXml.TableCellData@endlink):  the table cell data .
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Gets the caption of the table data
    ##  @return A tuple consisting of (caption, position). 
    ##  - caption is: str.
    ##  - position is: @link TableDocumentData.CaptionPosition NXOpen.OpenXml.TableDocumentData.CaptionPosition@endlink.

    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetCaption(self) -> Tuple[str, TableDocumentData.CaptionPosition]:
        """
         Gets the caption of the table data
         @return A tuple consisting of (caption, position). 
         - caption is: str.
         - position is: @link TableDocumentData.CaptionPosition NXOpen.OpenXml.TableDocumentData.CaptionPosition@endlink.

        """
        pass
    
    ##  Gets the number of table cells 
    ##  @return cellsCount (int):  number of table cells.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetCellsCount(self) -> int:
        """
         Gets the number of table cells 
         @return cellsCount (int):  number of table cells.
        """
        pass
    
    ##  Gets the column count of table data
    ##  @return columnCount (int): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetColumnCount(self) -> int:
        """
         Gets the column count of table data
         @return columnCount (int): .
        """
        pass
    
    ##  Gets the width array of the columns 
    ##  @return widths (List[float]):  the column width array .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetColumnWidths(self) -> List[float]:
        """
         Gets the width array of the columns 
         @return widths (List[float]):  the column width array .
        """
        pass
    
    ##  Gets the nth table cell data
    ##  @return cell (@link TableCellData NXOpen.OpenXml.TableCellData@endlink):  the table cell data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  the index of table cell data</param>
    def GetNthCell(self, index: int) -> TableCellData:
        """
         Gets the nth table cell data
         @return cell (@link TableCellData NXOpen.OpenXml.TableCellData@endlink):  the table cell data .
        """
        pass
    
    ##  Gets the row count of table data
    ##  @return columnCount (int): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetRowCount(self) -> int:
        """
         Gets the row count of table data
         @return columnCount (int): .
        """
        pass
    
    ##  Gets the height array of the rows 
    ##  @return heigths (List[float]):  the column width array .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetRowHeigths(self) -> List[float]:
        """
         Gets the height array of the rows 
         @return heigths (List[float]):  the column width array .
        """
        pass
    
    ##  Sets the caption of the table data
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="position"> (@link TableDocumentData.CaptionPosition NXOpen.OpenXml.TableDocumentData.CaptionPosition@endlink) </param>
    ## <param name="caption"> (str) </param>
    def SetCaption(self, position: TableDocumentData.CaptionPosition, caption: str) -> None:
        """
         Sets the caption of the table data
        """
        pass
    
    ##  Sets the width array of the columns 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="widths"> (List[float])  the column width array </param>
    def SetColumnWidths(self, widths: List[float]) -> None:
        """
         Sets the width array of the columns 
        """
        pass
    
    ##  Sets the height array of the rows 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="heigths"> (List[float])  the column width array </param>
    def SetRowHeigths(self, heigths: List[float]) -> None:
        """
         Sets the height array of the rows 
        """
        pass
    
##  Represents the text to be exported to the speific Open XML file. 
## 
##   <br>  Created in NX11.0.0  <br> 

class TextDocumentData(DocumentData): 
    """ Represents the text to be exported to the speific Open XML file. """


    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Gets the content to be exported of text data
    ##  @return content (str): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetContent(self) -> str:
        """
         Gets the content to be exported of text data
         @return content (str): .
        """
        pass
    
    ##  Sets the content to be exported of text data
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="content"> (str) </param>
    def SetContent(self, content: str) -> None:
        """
         Sets the content to be exported of text data
        """
        pass
    
## @package NXOpen.OpenXml
## Classes, Enums and Structs under NXOpen.OpenXml namespace

##  @link DocumentDataType NXOpen.OpenXml.DocumentDataType @endlink is an alias for @link DocumentData.Type NXOpen.OpenXml.DocumentData.Type@endlink
DocumentDataType = DocumentData.Type


##  @link ImageDocumentDataCaptionPosition NXOpen.OpenXml.ImageDocumentDataCaptionPosition @endlink is an alias for @link ImageDocumentData.CaptionPosition NXOpen.OpenXml.ImageDocumentData.CaptionPosition@endlink
ImageDocumentDataCaptionPosition = ImageDocumentData.CaptionPosition


##  @link TableDocumentDataCaptionPosition NXOpen.OpenXml.TableDocumentDataCaptionPosition @endlink is an alias for @link TableDocumentData.CaptionPosition NXOpen.OpenXml.TableDocumentData.CaptionPosition@endlink
TableDocumentDataCaptionPosition = TableDocumentData.CaptionPosition


