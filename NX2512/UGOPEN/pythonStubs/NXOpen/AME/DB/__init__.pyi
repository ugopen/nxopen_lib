from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class DocumentStructure(NXOpen.TaggedObject): 
    """ Class to define Document Structure object"""
    class Attribute(Enum):
        """
        Members Include: 
         |NotSet| 
         |Function| 
         |Location| 
         |Product| 
         |Dcc| 

        """
        NotSet: int
        Function: int
        Location: int
        Product: int
        Dcc: int
        @staticmethod
        def ValueOf(value: int) -> DocumentStructure.Attribute:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetClassificationCode(self) -> str:
        """
         Get the Classification Code. 
         Returns dccString (str): .
        """
        pass
    def GetDocumentStructureString(self) -> str:
        """
         Get the Document Structure string from Document Structur object. 
         Returns docStructString (str): .
        """
        pass
    def SetClassificationCode(self, dccString: str) -> None:
        """
         Set the Classification Code. 
        """
        pass
    @overload
    def SetDocumentStructure(self, firstAttr: DocumentStructure.Attribute, secondAttr: DocumentStructure.Attribute, thirdAttr: DocumentStructure.Attribute, fourthAttr: DocumentStructure.Attribute) -> None:
        """
         Set all four attributes of Document Structure order in sequence. 
        """
        pass
    @overload
    def SetDocumentStructure(self, firstAttr: DocumentStructure.Attribute, secondAttr: DocumentStructure.Attribute, thirdAttr: DocumentStructure.Attribute) -> None:
        """
         Set any three attributes of Document Structure order in sequence 
        """
        pass
    @overload
    def SetDocumentStructure(self, firstAttr: DocumentStructure.Attribute, secondAttr: DocumentStructure.Attribute) -> None:
        """
         Set any two attributes of Document Structure order in sequence. 
        """
        pass
    @overload
    def SetDocumentStructure(self, firstAttr: DocumentStructure.Attribute) -> None:
        """
         Set any one attribute of Document Structure order. 
        """
        pass
