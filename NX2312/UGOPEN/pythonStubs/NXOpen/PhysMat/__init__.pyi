from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen.Fields
##   @brief Implementation of the @link NXOpen::Fields::IApplication NXOpen::Fields::IApplication@endlink . 
##     This application extends fields with solver specific attributes. 
## 
##   <br> Not support KF.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DynaFieldApplication(NXOpen.Fields.IApplication): 
    """ <summary>Implementation of the <ja_class>NXOpen.Fields.IApplication</ja_class>. 
    This application extends fields with solver specific attributes.</summary>"""


    ##  Creates a new set of attributes that can be attached to a field. 
    ##         See @link NXOpen::PhysMat::DynaFieldAttributes NXOpen::PhysMat::DynaFieldAttributes@endlink  for more information about
    ##         these attributes.
    ##  @return attributes (@link DynaFieldAttributes NXOpen.PhysMat.DynaFieldAttributes@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="loadCurveUsage"> (@link DynaFieldAttributes.LoadCurveUsage NXOpen.PhysMat.DynaFieldAttributes.LoadCurveUsage@endlink) </param>
    ## <param name="dataType"> (@link DynaFieldAttributes.DataType NXOpen.PhysMat.DynaFieldAttributes.DataType@endlink) </param>
    ## <param name="numDiscPts"> (int) </param>
    def CreateAttributes(app: DynaFieldApplication, loadCurveUsage: DynaFieldAttributes.LoadCurveUsage, dataType: DynaFieldAttributes.DataType, numDiscPts: int) -> DynaFieldAttributes:
        """
         Creates a new set of attributes that can be attached to a field. 
                See @link NXOpen::PhysMat::DynaFieldAttributes NXOpen::PhysMat::DynaFieldAttributes@endlink  for more information about
                these attributes.
         @return attributes (@link DynaFieldAttributes NXOpen.PhysMat.DynaFieldAttributes@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.Fields
##   @brief Implementation of the @link NXOpen::Fields::IApplicationData NXOpen::Fields::IApplicationData@endlink . 
##     This specific implementation extends fields with solver specific attributes.
##     Instances of this class are created through the @link NXOpen::PhysMat::DynaFieldApplication NXOpen::PhysMat::DynaFieldApplication@endlink  object. 
## 
##   <br> Not support KF.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DynaFieldAttributes(NXOpen.NXObject): 
    """ <summary>Implementation of the <ja_class>NXOpen.Fields.IApplicationData</ja_class>. 
    This specific implementation extends fields with solver specific attributes.
    Instances of this class are created through the <ja_class>NXOpen.PhysMat.DynaFieldApplication</ja_class> object.</summary>"""


    ##  This enum defines the data type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ChemicalShrinkage</term><description> 
    ## </description> </item><item><term> 
    ## FabricStress</term><description> 
    ## </description> </item><item><term> 
    ## General</term><description> 
    ## </description> </item><item><term> 
    ## GeneralXY</term><description> 
    ## </description> </item><item><term> 
    ## GeneralRS</term><description> 
    ## </description> </item></list>
    class DataType(Enum):
        """
        Members Include: <ChemicalShrinkage> <FabricStress> <General> <GeneralXY> <GeneralRS>
        """
        ChemicalShrinkage: int
        FabricStress: int
        General: int
        GeneralXY: int
        GeneralRS: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DynaFieldAttributes.DataType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum defines the load curve usage type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NormalAnalysisPhase</term><description> 
    ## </description> </item><item><term> 
    ## DynamicRelaxationPhase</term><description> 
    ## </description> </item><item><term> 
    ## BothPhases</term><description> 
    ## </description> </item></list>
    class LoadCurveUsage(Enum):
        """
        Members Include: <NormalAnalysisPhase> <DynamicRelaxationPhase> <BothPhases>
        """
        NormalAnalysisPhase: int
        DynamicRelaxationPhase: int
        BothPhases: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DynaFieldAttributes.LoadCurveUsage:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link DynaFieldAttributes.DataType NXOpen.PhysMat.DynaFieldAttributes.DataType@endlink) DataTypeAttribute
    ##   a data type attribute.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return DynaFieldAttributes.DataType
    @property
    def DataTypeAttribute(self) -> DynaFieldAttributes.DataType:
        """
        Getter for property: (@link DynaFieldAttributes.DataType NXOpen.PhysMat.DynaFieldAttributes.DataType@endlink) DataTypeAttribute
          a data type attribute.  
            
         
        """
        pass
    
    ## Setter for property: (@link DynaFieldAttributes.DataType NXOpen.PhysMat.DynaFieldAttributes.DataType@endlink) DataTypeAttribute

    ##   a data type attribute.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @DataTypeAttribute.setter
    def DataTypeAttribute(self, dataType: DynaFieldAttributes.DataType):
        """
        Setter for property: (@link DynaFieldAttributes.DataType NXOpen.PhysMat.DynaFieldAttributes.DataType@endlink) DataTypeAttribute
          a data type attribute.  
            
         
        """
        pass
    
    ## Getter for property: (@link DynaFieldAttributes.LoadCurveUsage NXOpen.PhysMat.DynaFieldAttributes.LoadCurveUsage@endlink) LoadCurveUsageAttribute
    ##   a load curve usage attribute.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return DynaFieldAttributes.LoadCurveUsage
    @property
    def LoadCurveUsageAttribute(self) -> DynaFieldAttributes.LoadCurveUsage:
        """
        Getter for property: (@link DynaFieldAttributes.LoadCurveUsage NXOpen.PhysMat.DynaFieldAttributes.LoadCurveUsage@endlink) LoadCurveUsageAttribute
          a load curve usage attribute.  
            
         
        """
        pass
    
    ## Setter for property: (@link DynaFieldAttributes.LoadCurveUsage NXOpen.PhysMat.DynaFieldAttributes.LoadCurveUsage@endlink) LoadCurveUsageAttribute

    ##   a load curve usage attribute.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @LoadCurveUsageAttribute.setter
    def LoadCurveUsageAttribute(self, loadCurveUsage: DynaFieldAttributes.LoadCurveUsage):
        """
        Setter for property: (@link DynaFieldAttributes.LoadCurveUsage NXOpen.PhysMat.DynaFieldAttributes.LoadCurveUsage@endlink) LoadCurveUsageAttribute
          a load curve usage attribute.  
            
         
        """
        pass
    
    ## Getter for property: (int) NumDiscretizationPointsAttribute
    ##   the number of discretization points.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def NumDiscretizationPointsAttribute(self) -> int:
        """
        Getter for property: (int) NumDiscretizationPointsAttribute
          the number of discretization points.  
            
         
        """
        pass
    
    ## Setter for property: (int) NumDiscretizationPointsAttribute

    ##   the number of discretization points.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @NumDiscretizationPointsAttribute.setter
    def NumDiscretizationPointsAttribute(self, numDiscPts: int):
        """
        Setter for property: (int) NumDiscretizationPointsAttribute
          the number of discretization points.  
            
         
        """
        pass
    
import NXOpen
##  Represents a Physical Material Assign Builder  <br> To create a new instance of this class, use @link NXOpen::PhysicalMaterialCollection::CreateMaterialAssignBuilder  NXOpen::PhysicalMaterialCollection::CreateMaterialAssignBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class PhysicalMaterialAssignBuilder(NXOpen.Builder): 
    """ Represents a Physical Material Assign Builder """
    pass


import NXOpen
##  Represents a @link NXOpen::PhysMat::PhysicalMaterialLibMgrBuilder NXOpen::PhysMat::PhysicalMaterialLibMgrBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::PhysicalMaterialCollection::CreateMaterialLibmgrBuilder  NXOpen::PhysicalMaterialCollection::CreateMaterialLibmgrBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class PhysicalMaterialLibMgrBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.PhysMat.PhysicalMaterialLibMgrBuilder</ja_class> builder """
    pass


import NXOpen
##  This builder is used by the Materials list component that allows copying, editing, deleting. etc.
##      materials.
##      <br> To create a new instance of this class, use @link NXOpen::PhysicalMaterialCollection::CreateListBlockBuilder  NXOpen::PhysicalMaterialCollection::CreateListBlockBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class PhysicalMaterialListBuilder(NXOpen.Builder): 
    """ This builder is used by the Materials list component that allows copying, editing, deleting. etc.
     materials.
    """
    pass


## @package NXOpen.PhysMat
## Classes, Enums and Structs under NXOpen.PhysMat namespace

##  @link DynaFieldAttributesDataType NXOpen.PhysMat.DynaFieldAttributesDataType @endlink is an alias for @link DynaFieldAttributes.DataType NXOpen.PhysMat.DynaFieldAttributes.DataType@endlink
DynaFieldAttributesDataType = DynaFieldAttributes.DataType


##  @link DynaFieldAttributesLoadCurveUsage NXOpen.PhysMat.DynaFieldAttributesLoadCurveUsage @endlink is an alias for @link DynaFieldAttributes.LoadCurveUsage NXOpen.PhysMat.DynaFieldAttributes.LoadCurveUsage@endlink
DynaFieldAttributesLoadCurveUsage = DynaFieldAttributes.LoadCurveUsage


