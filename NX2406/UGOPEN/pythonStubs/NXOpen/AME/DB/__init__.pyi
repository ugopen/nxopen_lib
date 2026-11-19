from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Class to define Document Structure object <br> This object does not need a creator.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class DocumentStructure(NXOpen.TaggedObject): 
    """ Class to define Document Structure object"""


    ##  Represents the attribute for Document Structure 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Function</term><description> 
    ## </description> </item><item><term> 
    ## Location</term><description> 
    ## </description> </item><item><term> 
    ## Product</term><description> 
    ## </description> </item><item><term> 
    ## Dcc</term><description> 
    ## </description> </item></list>
    class Attribute(Enum):
        """
        Members Include: <NotSet> <Function> <Location> <Product> <Dcc>
        """
        NotSet: int
        Function: int
        Location: int
        Product: int
        Dcc: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DocumentStructure.Attribute:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Get the Classification Code. 
    ##  @return dccString (str): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ad_automation_design ("FULL AUTOMATION DESIGNER")
    def GetClassificationCode(self) -> str:
        """
         Get the Classification Code. 
         @return dccString (str): .
        """
        pass
    
    ##  Get the Document Structure string from Document Structur object. 
    ##  @return docStructString (str): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ad_automation_design ("FULL AUTOMATION DESIGNER")
    def GetDocumentStructureString(self) -> str:
        """
         Get the Document Structure string from Document Structur object. 
         @return docStructString (str): .
        """
        pass
    
    ##  Set the Classification Code. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ad_automation_design ("FULL AUTOMATION DESIGNER")
    ## 
    ## <param name="dccString"> (str) </param>
    def SetClassificationCode(self, dccString: str) -> None:
        """
         Set the Classification Code. 
        """
        pass
    
    ##  Set all four attributes of Document Structure order in sequence. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ad_automation_design ("FULL AUTOMATION DESIGNER")
    ## <param name="docStruct"> (@link DocumentStructure NXOpen.AME.DB.DocumentStructure@endlink) </param>
    ## <param name="firstAttr"> (@link DocumentStructure.Attribute NXOpen.AME.DB.DocumentStructure.Attribute@endlink) </param>
    ## <param name="secondAttr"> (@link DocumentStructure.Attribute NXOpen.AME.DB.DocumentStructure.Attribute@endlink) </param>
    ## <param name="thirdAttr"> (@link DocumentStructure.Attribute NXOpen.AME.DB.DocumentStructure.Attribute@endlink) </param>
    ## <param name="fourthAttr"> (@link DocumentStructure.Attribute NXOpen.AME.DB.DocumentStructure.Attribute@endlink) </param>
    @overload
    def SetDocumentStructure(self, firstAttr: DocumentStructure.Attribute, secondAttr: DocumentStructure.Attribute, thirdAttr: DocumentStructure.Attribute, fourthAttr: DocumentStructure.Attribute) -> None:
        """
         Set all four attributes of Document Structure order in sequence. 
        """
        pass
    
    ##  Set any three attributes of Document Structure order in sequence 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ad_automation_design ("FULL AUTOMATION DESIGNER")
    ## <param name="docStruct"> (@link DocumentStructure NXOpen.AME.DB.DocumentStructure@endlink) </param>
    ## <param name="firstAttr"> (@link DocumentStructure.Attribute NXOpen.AME.DB.DocumentStructure.Attribute@endlink) </param>
    ## <param name="secondAttr"> (@link DocumentStructure.Attribute NXOpen.AME.DB.DocumentStructure.Attribute@endlink) </param>
    ## <param name="thirdAttr"> (@link DocumentStructure.Attribute NXOpen.AME.DB.DocumentStructure.Attribute@endlink) </param>
    @overload
    def SetDocumentStructure(self, firstAttr: DocumentStructure.Attribute, secondAttr: DocumentStructure.Attribute, thirdAttr: DocumentStructure.Attribute) -> None:
        """
         Set any three attributes of Document Structure order in sequence 
        """
        pass
    
    ##  Set any two attributes of Document Structure order in sequence. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ad_automation_design ("FULL AUTOMATION DESIGNER")
    ## <param name="docStruct"> (@link DocumentStructure NXOpen.AME.DB.DocumentStructure@endlink) </param>
    ## <param name="firstAttr"> (@link DocumentStructure.Attribute NXOpen.AME.DB.DocumentStructure.Attribute@endlink) </param>
    ## <param name="secondAttr"> (@link DocumentStructure.Attribute NXOpen.AME.DB.DocumentStructure.Attribute@endlink) </param>
    @overload
    def SetDocumentStructure(self, firstAttr: DocumentStructure.Attribute, secondAttr: DocumentStructure.Attribute) -> None:
        """
         Set any two attributes of Document Structure order in sequence. 
        """
        pass
    
    ##  Set any one attribute of Document Structure order. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ad_automation_design ("FULL AUTOMATION DESIGNER")
    ## <param name="docStruct"> (@link DocumentStructure NXOpen.AME.DB.DocumentStructure@endlink) </param>
    ## <param name="firstAttr"> (@link DocumentStructure.Attribute NXOpen.AME.DB.DocumentStructure.Attribute@endlink) </param>
    @overload
    def SetDocumentStructure(self, firstAttr: DocumentStructure.Attribute) -> None:
        """
         Set any one attribute of Document Structure order. 
        """
        pass
    
## @package NXOpen.AME.DB
## Classes, Enums and Structs under NXOpen.AME.DB namespace

##  @link DocumentStructureAttribute NXOpen.AME.DB.DocumentStructureAttribute @endlink is an alias for @link DocumentStructure.Attribute NXOpen.AME.DB.DocumentStructure.Attribute@endlink
DocumentStructureAttribute = DocumentStructure.Attribute


