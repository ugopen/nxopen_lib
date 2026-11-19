from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class DocumentElement(NXOpen.TransientObject): 
    """ Tools for formating contents to be displayed in the Information window. """
    class Format(Enum):
        """
        Members Include: 
         |FontBold| 
         |FontColorError|  use this to highlight something that requires correction 
         |FontColorWarning|  use this to highlight something that may require intervention 
         |FontColorInfo|  use this to highlight specific information 
         |FontColorSuccess|  use this to highlight something that was successful  

        """
        FontBold: int
        FontColorError: int
        FontColorWarning: int
        FontColorInfo: int
        FontColorSuccess: int
        @staticmethod
        def ValueOf(value: int) -> DocumentElement.Format:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddFormatting(self, format_type: DocumentElement.Format) -> None:
        """
         Adds a text formating type to the document element. This can be bold and one of 4 color types. 
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory. After this method is called, the object cannot be used.
                    In .NET and Java, this method is automatically called when the object is deleted by the garbage collector. 
        """
        pass
import NXOpen
class Document(NXOpen.TransientObject): 
    """ Tools for creating contents to be displayed in the Information window. """
    class HeadingType(Enum):
        """
        Members Include: 
         |H1|  as h1 HTML tag (largest) 
         |H2|  as h2 HTML tag (subheadings) 
         |H3|  as h3 HTML tag 
         |H4|  as h4 HTML tag (smallest) 

        """
        H1: int
        H2: int
        H3: int
        H4: int
        @staticmethod
        def ValueOf(value: int) -> Document.HeadingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddCoordinateCells(self, tableid: str, label: str, point: NXOpen.Point3d, isAbsolute: bool) -> None:
        """
         Creates cells containing the elements of a 3D point coordinate. These cells will make up the next row in the table. 
        """
        pass
    def AddDateCell(self, tableid: str, rowid: str) -> DocumentElement:
        """
         Creates a cell containing the current date and time in a table row. 
         Returns cell ( DocumentElement NXOpen.I):  access object for formatting .
        """
        pass
    def AddDoubleCell(self, tableid: str, rowid: str, number: float) -> DocumentElement:
        """
         Creates a cell containing a double in a table row. 
         Returns cell ( DocumentElement NXOpen.I):  access object for formatting .
        """
        pass
    def AddHeading(self, text: str, size: Document.HeadingType) -> None:
        """
         Creates a heading with the supplied text in document.
                    Sizing is controlled by the heading type, reflecting HTML heading types h1 to h4, with h1 being the largest. 
        """
        pass
    def AddParagraph(self, text: str) -> None:
        """
         Creates an paragraph with the supplied text in document. 
        """
        pass
    def AddTable(self, identifier: str, title: str) -> None:
        """
         Creates a table. Identifier is used to reference the table going forward.
                    Tables include rows and cells within rows. The first column of a table always displays bold. 
        """
        pass
    def AddTableRow(self, tableid: str, rowid: str) -> None:
        """
         Creates a row in a table. Identifier is used to reference the row going forward. 
        """
        pass
    def AddTextCell(self, tableid: str, rowid: str, label: str) -> DocumentElement:
        """
         Creates a cell containing text in a table row. 
         Returns cell ( DocumentElement NXOpen.I):  access object for formatting .
        """
        pass
    def BeginGroup(self, identifier: str, label: str, collapse: bool) -> None:
        """
         Creates a collapsible group in document. All new contents will be added here until the group is ended. 
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory. After this method is called, the object cannot be used.
                    In .NET and Java, this method is automatically called when the object is deleted by the garbage collector. 
        """
        pass
    def EndGroup(self, identifier: str) -> None:
        """
         End group by identifier (any child groups are also ended at this point). No more contents may be added. 
        """
        pass
import NXOpen
class Manager(NXOpen.Object): 
    """ Manages the Information window, including creating and displaying NXOpen.InfoWindow.Document instances. """
    class SaveType(Enum):
        """
        Members Include: 
         |Html|  content is saved as HTML format with tags 
         |Text|  only simple text content is saved 

        """
        Html: int
        Text: int
        @staticmethod
        def ValueOf(value: int) -> Manager.SaveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Close(clear_contents: bool) -> None:
        """
         Closes the Information window in an interactive session. 
                    If requested, clears the Information window so that the current contents are no longer present the next time the Information window is displayed. 
        """
        pass
    def DisplayDocument(document: Document) -> None:
        """
         Displays the document in the Information window if the user interface is present. 
        """
        pass
    def NewDocument() -> Document:
        """
         Constructs a new NXOpen.InfoWindow.Document instance to which contents can be added and displayed. 
         Returns document ( Document NXOpen.I):  .
        """
        pass
    def Open() -> None:
        """
         Displays the Information window to the screen in an interactive session. 
        """
        pass
    def SaveContents(saveType: Manager.SaveType, filename: str) -> None:
        """
         Saves the contents of the Information window to a file. Contents can be in HTML format or plain text.
                    If plain text is used, some of the HTML-styled contents may not be reproduced fully. If the specified file 
                    already exists its contents will be overwritten. 
        """
        pass
