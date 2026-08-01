from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class DocumentDataGroup(DocumentData): 
    """  Contains methods for adding document data for CAE Report.  """
    def AddImageGroup(self) -> ImageGroupDocumentData:
        """
         Creates a new NXOpen.OpenXml.ImageGroupDocumentData object.
                Does not to free this object, it will be free while deleting 
                NXOpen.OpenXml.DocumentDataGroup object
         Returns data ( ImageGroupDocumentData NXOpen):  the image group data .
        """
        pass
    def AddTable(self, columnCount: int, rowCount: int) -> TableDocumentData:
        """
         Creates a new NXOpen.OpenXml.TableDocumentData object.
                Does not to free this object, it will be free while deleting 
                NXOpen.OpenXml.DocumentDataGroup object
         Returns data ( TableDocumentData NXOpen):  the table data .
        """
        pass
    def AddText(self, textContent: str) -> TextDocumentData:
        """
         Creates a new NXOpen.OpenXml.TextDocumentData object.
                Does not to free this object, it will be free while deleting 
                NXOpen.OpenXml.DocumentDataGroup object
         Returns data ( TextDocumentData NXOpen):  the text data .
        """
        pass
    def DeleteAllData(self) -> None:
        """
         Deletes all document data
        """
        pass
    def DeleteNthData(self, index: int) -> None:
        """
         Deletes the nth document data
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetDataCount(self) -> int:
        """
         Gets the number of data to be exported
         Returns dataCount (int):  the number of data .
        """
        pass
    def GetNthData(self, index: int) -> DocumentData:
        """
         Gets the nth document data object.
                Does not to free this object, it will be free while deleting 
                NXOpen.OpenXml.DocumentDataGroup object
         Returns data ( DocumentData NXOpen):  the data.
        """
        pass
import NXOpen
class DocumentData(NXOpen.TransientObject): 
    """ Represents the definition of the base document data"""
    class Type(Enum):
        """
        Members Include: 
         |Base|  the base document data type 
         |Text|  the document data type of text
         |Table|  the document data type of table
         |TableCell|  the document data type of table cell
         |Image|  the document data type of image
         |ImageGroup|  the document data type of image group
         |Group|  the document data type of data group

        """
        Base: int
        Text: int
        Table: int
        TableCell: int
        Image: int
        ImageGroup: int
        Group: int
        @staticmethod
        def ValueOf(value: int) -> DocumentData.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetDataType(self) -> DocumentData.Type:
        """
         Gets a specified document data type 
         Returns dataType ( DocumentData.Type NXOpen):  the data type defined by the NXOpen.OpenXml.DocumentData.Type .
        """
        pass
class ImageDocumentData(DocumentData): 
    """ Represents the image to be exported to the speific Open XML file. """
    class CaptionPosition(Enum):
        """
        Members Include: 
         |Above|  the above position 
         |Bellow|  the bellow position

        """
        Above: int
        Bellow: int
        @staticmethod
        def ValueOf(value: int) -> ImageDocumentData.CaptionPosition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetCaption(self) -> Tuple[str, ImageDocumentData.CaptionPosition]:
        """
         Gets the caption of the image data
         Returns A tuple consisting of (caption, position). 
         - caption is: str.
         - position is:  ImageDocumentData.CaptionPosition NXOpen.

        """
        pass
    def GetFileName(self) -> str:
        """
         Gets the file name of the image data
         Returns fileName (str): .
        """
        pass
    def SetCaption(self, position: ImageDocumentData.CaptionPosition, caption: str) -> None:
        """
         Sets the caption of the image data
        """
        pass
    def SetFileName(self, fileName: str) -> None:
        """
         Sets the file name of the image data
        """
        pass
class ImageGroupDocumentData(DocumentData): 
    """ Represents the group of images to be exported to the speific Open XML file. """
    def AddImage(self, fileName: str, caption: str) -> ImageDocumentData:
        """
         Creates a new NXOpen.OpenXml.ImageDocumentData object.
         Returns data ( ImageDocumentData NXOpen):  the image data .
        """
        pass
    def DeleteAllImages(self) -> None:
        """
         Deletes all images data
        """
        pass
    def DeleteNthImage(self, index: int) -> None:
        """
         Deletes the nth image data
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetImagesCount(self) -> int:
        """
         Gets the number of images 
         Returns imageCount (int):  number of images.
        """
        pass
    def GetNthImage(self, index: int) -> ImageDocumentData:
        """
         Gets the nth image data
         Returns data ( ImageDocumentData NXOpen):  the image data.
        """
        pass
class TableCellData(DocumentData): 
    """ Represents the table cell to be exported to the speific Open XML file. """
    def AddImageGroup(self) -> ImageGroupDocumentData:
        """
         Creates a new NXOpen.OpenXml.ImageGroupDocumentData object.
                Does not to free this object, it will be free while deleting 
                NXOpen.OpenXml.TableCellData object
         Returns data ( ImageGroupDocumentData NXOpen):  the image group data .
        """
        pass
    def AddText(self, textContent: str) -> TextDocumentData:
        """
         Creates a new NXOpen.OpenXml.TextDocumentData object.
                Does not to free this object, it will be free while deleting 
                NXOpen.OpenXml.TableCellData object
         Returns data ( TextDocumentData NXOpen):  the text data .
        """
        pass
    def ClearContents(self) -> None:
        """
         Removes all contents data
        """
        pass
    def DeleteNthContent(self, index: int) -> None:
        """
         Removes the nth content data
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetContentCount(self) -> int:
        """
         Gets the number of content in the table cell
         Returns dataCount (int):  the number of content .
        """
        pass
    def GetGridsId(self) -> List[int]:
        """
         Gets the grid IDs of the table cell
         Returns ids (List[int]):  the grid ID array .
        """
        pass
    def GetNthContent(self, index: int) -> DocumentData:
        """
         Gets the nth content data        
                Does not to free this object, it will be free while deleting 
                NXOpen.OpenXml.TableCellData object
         Returns data ( DocumentData NXOpen):  the content.
        """
        pass
class TableDocumentData(DocumentData): 
    """ Represents the table to be exported to the speific Open XML file. """
    class CaptionPosition(Enum):
        """
        Members Include: 
         |Above|  the above position 
         |Bellow|  the bellow position

        """
        Above: int
        Bellow: int
        @staticmethod
        def ValueOf(value: int) -> TableDocumentData.CaptionPosition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddCellData(self, grids: List[int]) -> TableCellData:
        """
         Creates a new NXOpen.OpenXml.TableCellData object.
                Does not to free this object, it will be free while deleting 
                NXOpen.OpenXml.TableDocumentData object
         Returns cell ( TableCellData NXOpen):  the table cell data .
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetCaption(self) -> Tuple[str, TableDocumentData.CaptionPosition]:
        """
         Gets the caption of the table data
         Returns A tuple consisting of (caption, position). 
         - caption is: str.
         - position is:  TableDocumentData.CaptionPosition NXOpen.

        """
        pass
    def GetCellsCount(self) -> int:
        """
         Gets the number of table cells 
         Returns cellsCount (int):  number of table cells.
        """
        pass
    def GetColumnCount(self) -> int:
        """
         Gets the column count of table data
         Returns columnCount (int): .
        """
        pass
    def GetColumnWidths(self) -> List[float]:
        """
         Gets the width array of the columns 
         Returns widths (List[float]):  the column width array .
        """
        pass
    def GetNthCell(self, index: int) -> TableCellData:
        """
         Gets the nth table cell data
         Returns cell ( TableCellData NXOpen):  the table cell data .
        """
        pass
    def GetRowCount(self) -> int:
        """
         Gets the row count of table data
         Returns columnCount (int): .
        """
        pass
    def GetRowHeigths(self) -> List[float]:
        """
         Gets the height array of the rows 
         Returns heigths (List[float]):  the column width array .
        """
        pass
    def SetCaption(self, position: TableDocumentData.CaptionPosition, caption: str) -> None:
        """
         Sets the caption of the table data
        """
        pass
    def SetColumnWidths(self, widths: List[float]) -> None:
        """
         Sets the width array of the columns 
        """
        pass
    def SetRowHeigths(self, heigths: List[float]) -> None:
        """
         Sets the height array of the rows 
        """
        pass
class TextDocumentData(DocumentData): 
    """ Represents the text to be exported to the speific Open XML file. """
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetContent(self) -> str:
        """
         Gets the content to be exported of text data
         Returns content (str): .
        """
        pass
    def SetContent(self, content: str) -> None:
        """
         Sets the content to be exported of text data
        """
        pass
