from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##   @brief  Provides methods to query the loaded AFU files  
## 
##    <br> To obtain an instance of this class use @link NXOpen::CAE::FTK::DataManager::AfuFileManager NXOpen::CAE::FTK::DataManager::AfuFileManager@endlink .  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class AfuFileManager(NXOpen.Object): 
    """ <summary> Provides methods to query the loaded AFU files </summary> """


    ##  Deletes an AFU file 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="afuFileName"> (str) </param>
    @staticmethod
    def DeleteFile(afuFileName: str) -> None:
        """
         Deletes an AFU file 
        """
        pass
    
    ##  Gets all record names in an AFU file which must be loaded 
    ##  @return recordNames (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="afuFileName"> (str) </param>
    @staticmethod
    def GetAllRecordNamesInFile(afuFileName: str) -> List[str]:
        """
         Gets all record names in an AFU file which must be loaded 
         @return recordNames (List[str]): .
        """
        pass
    
    ##  Gets all loaded AFU files 
    ##  @return afuFileNames (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLoadedFiles() -> List[str]:
        """
         Gets all loaded AFU files 
         @return afuFileNames (List[str]): .
        """
        pass
    
    ##  Gets an AFU record in an AFU file which must be loaded 
    ##  @return afuRecord (@link BaseRecord NXOpen.CAE.FTK.BaseRecord@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="afuFileName"> (str) </param>
    ## <param name="recordName"> (str) </param>
    def GetRecord(afuFileName: str, recordName: str) -> BaseRecord:
        """
         Gets an AFU record in an AFU file which must be loaded 
         @return afuRecord (@link BaseRecord NXOpen.CAE.FTK.BaseRecord@endlink): .
        """
        pass
    
    ##  Loads an AFU file to the specified container.
    ##                 
    ##                 An AFU file can be loaded under associated container, solution result container or user container.
    ##                 The container type indicates under which container the file is loaded.
    ##                 
    ##              
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="afuFileName"> (str) </param>
    ## <param name="containerType"> (@link DataManager.FileContainerType NXOpen.CAE.FTK.DataManager.FileContainerType@endlink) </param>
    def LoadFile(afuFileName: str, containerType: DataManager.FileContainerType) -> None:
        """
         Loads an AFU file to the specified container.
                        
                        An AFU file can be loaded under associated container, solution result container or user container.
                        The container type indicates under which container the file is loaded.
                        
                     
        """
        pass
    
    ##  Unloads an AFU file from the specified container.
    ##                 
    ##                 An AFU file can be loaded under associated container, solution result container or user container.
    ##                 The container type indicates under which container the file is unloaded.
    ##                 
    ##              
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="afuFileName"> (str) </param>
    ## <param name="containerType"> (@link DataManager.FileContainerType NXOpen.CAE.FTK.DataManager.FileContainerType@endlink) </param>
    def UnloadFile(afuFileName: str, containerType: DataManager.FileContainerType) -> None:
        """
         Unloads an AFU file from the specified container.
                        
                        An AFU file can be loaded under associated container, solution result container or user container.
                        The container type indicates under which container the file is unloaded.
                        
                     
        """
        pass
    
##  Manages the @link CAE::FTK::ArrayRecord2DEven CAE::FTK::ArrayRecord2DEven@endlink  with Z value  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ArrayRecord2DEvenWithZValue(ArrayRecord2DEven): 
    """ Manages the <ja_class>CAE.FTK.ArrayRecord2DEven</ja_class> with Z value """


    ## Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit
    ##   the Z unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return BaseUnit
    @property
    def Unit(self) -> BaseUnit:
        """
        Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit
          the Z unit   
            
         
        """
        pass
    
    ## Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit

    ##   the Z unit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Unit.setter
    def Unit(self, zValueUnit: BaseUnit):
        """
        Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit
          the Z unit   
            
         
        """
        pass
    
    ## Getter for property: (float) Value
    ##   the Z value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
          the Z value   
            
         
        """
        pass
    
    ## Setter for property: (float) Value

    ##   the Z value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Value.setter
    def Value(self, zValue: float):
        """
        Setter for property: (float) Value
          the Z value   
            
         
        """
        pass
    
##  Manages the 2d array record with even abscissa data  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class ArrayRecord2DEven(ArrayRecord2D): 
    """ Manages the 2d array record with even abscissa data """


    ##  Gets even complex data 
    ##  @return A tuple consisting of (y_coordinate_real, x_minimum, x_increment, y_coordinate_imag). 
    ##  - y_coordinate_real is: List[float]. Real part of Y-Coordinate data .
    ##  - x_minimum is: float. Minimum abscissa data value .
    ##  - x_increment is: float. Abscissa increment .
    ##  - y_coordinate_imag is: List[float]. Imaginary part of Y-Coordinate data .

    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEvenComplexData(array_record: ArrayRecord2DEven) -> Tuple[List[float], float, float, List[float]]:
        """
         Gets even complex data 
         @return A tuple consisting of (y_coordinate_real, x_minimum, x_increment, y_coordinate_imag). 
         - y_coordinate_real is: List[float]. Real part of Y-Coordinate data .
         - x_minimum is: float. Minimum abscissa data value .
         - x_increment is: float. Abscissa increment .
         - y_coordinate_imag is: List[float]. Imaginary part of Y-Coordinate data .

        """
        pass
    
    ##  Gets even real data 
    ##  @return A tuple consisting of (y_coordinate_points, x_minimum, x_increment). 
    ##  - y_coordinate_points is: List[float]. Y-Coordinate data .
    ##  - x_minimum is: float. Minimum abscissa data value .
    ##  - x_increment is: float. Abscissa increment .

    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEvenRealData(array_record: ArrayRecord2DEven) -> Tuple[List[float], float, float]:
        """
         Gets even real data 
         @return A tuple consisting of (y_coordinate_points, x_minimum, x_increment). 
         - y_coordinate_points is: List[float]. Y-Coordinate data .
         - x_minimum is: float. Minimum abscissa data value .
         - x_increment is: float. Abscissa increment .

        """
        pass
    
    ##  Sets even complex data 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  Minimum abscissa data value 
    def SetEvenComplexData(array_record: ArrayRecord2DEven, x_minimum: float, x_increment: float, y_coordinate_real: List[float], y_coordinate_imag: List[float]) -> None:
        """
         Sets even complex data 
        """
        pass
    
    ##  Sets even real data 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  Minimum abscissa data value 
    def SetEvenRealData(array_record: ArrayRecord2DEven, x_minimum: float, x_increment: float, y_coordinate_points: List[float]) -> None:
        """
         Sets even real data 
        """
        pass
    
##  Manages the @link CAE::FTK::ArrayRecord2D CAE::FTK::ArrayRecord2D@endlink  with Z value  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ArrayRecord2DWithZValue(ArrayRecord2D): 
    """ Manages the <ja_class>CAE.FTK.ArrayRecord2D</ja_class> with Z value """


    ## Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit
    ##   the Z unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return BaseUnit
    @property
    def Unit(self) -> BaseUnit:
        """
        Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit
          the Z unit   
            
         
        """
        pass
    
    ## Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit

    ##   the Z unit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Unit.setter
    def Unit(self, zValueUnit: BaseUnit):
        """
        Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit
          the Z unit   
            
         
        """
        pass
    
    ## Getter for property: (float) Value
    ##   the Z value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
          the Z value   
            
         
        """
        pass
    
    ## Setter for property: (float) Value

    ##   the Z value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Value.setter
    def Value(self, zValue: float):
        """
        Setter for property: (float) Value
          the Z value   
            
         
        """
        pass
    
##  Manages the 2d array record  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class ArrayRecord2D(BaseRecord): 
    """ Manages the 2d array record """


    ##  Gets complex points data 
    ##  @return A tuple consisting of (x_coordinate_points, y_coordinate_real, y_coordinate_imag). 
    ##  - x_coordinate_points is: List[float]. X-Coordinate data .
    ##  - y_coordinate_real is: List[float]. Real part of Y-Coordinate data .
    ##  - y_coordinate_imag is: List[float]. Imaginary part of Y-Coordinate data .

    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetComplexData(array_record: ArrayRecord2D) -> Tuple[List[float], List[float], List[float]]:
        """
         Gets complex points data 
         @return A tuple consisting of (x_coordinate_points, y_coordinate_real, y_coordinate_imag). 
         - x_coordinate_points is: List[float]. X-Coordinate data .
         - y_coordinate_real is: List[float]. Real part of Y-Coordinate data .
         - y_coordinate_imag is: List[float]. Imaginary part of Y-Coordinate data .

        """
        pass
    
    ##  Gets real points data 
    ##  @return A tuple consisting of (x_coordinate_points, y_coordinate_points). 
    ##  - x_coordinate_points is: List[float]. X-Coordinate data .
    ##  - y_coordinate_points is: List[float]. Y-Coordinate data .

    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRealData(array_record: ArrayRecord2D) -> Tuple[List[float], List[float]]:
        """
         Gets real points data 
         @return A tuple consisting of (x_coordinate_points, y_coordinate_points). 
         - x_coordinate_points is: List[float]. X-Coordinate data .
         - y_coordinate_points is: List[float]. Y-Coordinate data .

        """
        pass
    
    ##  Gets the title 
    ##  @return title (str): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTitle(array_record: ArrayRecord2D) -> str:
        """
         Gets the title 
         @return title (str): .
        """
        pass
    
    ##  Gets X-Coordinate unit 
    ##  @return x_coordinate_unit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink):  X-Coordinate unit .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetXCoordinateUnit(array_record: ArrayRecord2D) -> BaseUnit:
        """
         Gets X-Coordinate unit 
         @return x_coordinate_unit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink):  X-Coordinate unit .
        """
        pass
    
    ##  Gets Y-Coordinate unit 
    ##  @return y_coordinate_unit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink):  Y-Coordinate unit .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetYCoordinateUnit(array_record: ArrayRecord2D) -> BaseUnit:
        """
         Gets Y-Coordinate unit 
         @return y_coordinate_unit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink):  Y-Coordinate unit .
        """
        pass
    
    ##  Sets complex points data 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  X-Coordinate data 
    def SetComplexData(array_record: ArrayRecord2D, x_coordinate_points: List[float], y_coordinate_real: List[float], y_coordinate_imag: List[float]) -> None:
        """
         Sets complex points data 
        """
        pass
    
    ##  Sets the point labels 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pointLabels"> (List[str]) </param>
    def SetPointLabels(arrayRecord: ArrayRecord2D, pointLabels: List[str]) -> None:
        """
         Sets the point labels 
        """
        pass
    
    ##  Sets real points data 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  X-Coordinate data 
    def SetRealData(array_record: ArrayRecord2D, x_coordinate_points: List[float], y_coordinate_points: List[float]) -> None:
        """
         Sets real points data 
        """
        pass
    
    ##  Sets X-Coordinate unit 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  X-Coordinate unit 
    def SetXCoordinateUnit(array_record: ArrayRecord2D, x_coordinate_unit: BaseUnit) -> None:
        """
         Sets X-Coordinate unit 
        """
        pass
    
    ##  Sets Y-Coordinate unit 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Y-Coordinate unit 
    def SetYCoordinateUnit(array_record: ArrayRecord2D, y_coordinate_unit: BaseUnit) -> None:
        """
         Sets Y-Coordinate unit 
        """
        pass
    
##  Manages the 3d array record  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class ArrayRecord3D(ArrayRecord2D): 
    """ Manages the 3d array record """


    ##  Edits Z-Coordinate units.
    ##                 If the input units are different with the old units, the units are updated with new ones, and the data are also converted to new units.
    ##                 
    ##                 At least one of names must be provided.
    ##                 <ol>
    ##                 <li>
    ##                 If the units is a Unitless related measure or quantity, measure name or quantity name must be provided, unit type name is not needed.
    ##                 </li>
    ##                 <li>
    ##                 If the units is a measure but not a Unitless related measure, measure name is optional, unit type name must be provided.
    ##                 </li>
    ##                 <li>
    ##                 If the units is a quantity but not a Unitless related quantity, both quantity name and unit type name must be provided.
    ##                 </li>
    ##                 </ol>
    ##                 
    ##             
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="measureOrQuantityName"> (str) </param>
    ## <param name="unitName"> (str) </param>
    def EditZCoordinateUnit(arrayRecord: ArrayRecord3D, measureOrQuantityName: str, unitName: str) -> None:
        """
         Edits Z-Coordinate units.
                        If the input units are different with the old units, the units are updated with new ones, and the data are also converted to new units.
                        
                        At least one of names must be provided.
                        <ol>
                        <li>
                        If the units is a Unitless related measure or quantity, measure name or quantity name must be provided, unit type name is not needed.
                        </li>
                        <li>
                        If the units is a measure but not a Unitless related measure, measure name is optional, unit type name must be provided.
                        </li>
                        <li>
                        If the units is a quantity but not a Unitless related quantity, both quantity name and unit type name must be provided.
                        </li>
                        </ol>
                        
                    
        """
        pass
    
    ##  Gets Z-Coordinate unit 
    ##  @return z_coordinate_unit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink):  Z-Coordinate unit .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetZCoordinateUnit(array_record: ArrayRecord3D) -> BaseUnit:
        """
         Gets Z-Coordinate unit 
         @return z_coordinate_unit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink):  Z-Coordinate unit .
        """
        pass
    
    ##  Sets Z-Coordinate points 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Z-Coordinate data 
    def SetZCoordinatePoints(array_record: ArrayRecord3D, z_coordinate_points: List[float]) -> None:
        """
         Sets Z-Coordinate points 
        """
        pass
    
    ##  Sets Z-Coordinate unit 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Z-Coordinate unit 
    def SetZCoordinateUnit(array_record: ArrayRecord3D, z_coordinate_unit: BaseUnit) -> None:
        """
         Sets Z-Coordinate unit 
        """
        pass
    
import NXOpen
##  Manages the base record.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class BaseRecord(NXOpen.NXObject): 
    """ Manages the base record. """


    ## Getter for property: (str) LegendName
    ##   the legend name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def LegendName(self) -> str:
        """
        Getter for property: (str) LegendName
          the legend name   
            
         
        """
        pass
    
    ## Getter for property: (str) ResultInformation
    ##   the result information of a record  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def ResultInformation(self) -> str:
        """
        Getter for property: (str) ResultInformation
          the result information of a record  
            
         
        """
        pass
    
    ## Setter for property: (str) ResultInformation

    ##   the result information of a record  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ResultInformation.setter
    def ResultInformation(self, resultInformation: str):
        """
        Setter for property: (str) ResultInformation
          the result information of a record  
            
         
        """
        pass
    
    ##  Gets the abscissa unit 
    ##  @return abscissaUnit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAbscissaUnit(baseRecord: BaseRecord) -> BaseUnit:
        """
         Gets the abscissa unit 
         @return abscissaUnit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink): .
        """
        pass
    
    ##  Gets the description 
    ##  @return description (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDescription(baseRecord: BaseRecord) -> List[str]:
        """
         Gets the description 
         @return description (List[str]): .
        """
        pass
    
    ##  Gets the ordinate unit 
    ##  @return ordinateUnit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetOrdinateUnit(baseRecord: BaseRecord) -> BaseUnit:
        """
         Gets the ordinate unit 
         @return ordinateUnit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink): .
        """
        pass
    
    ##  Gets the point labels 
    ##  @return pointLabels (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPointLabels(baseRecord: BaseRecord) -> List[str]:
        """
         Gets the point labels 
         @return pointLabels (List[str]): .
        """
        pass
    
    ##  Sets the description 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="description"> (List[str]) </param>
    def SetDescription(baseRecord: BaseRecord, description: List[str]) -> None:
        """
         Sets the description 
        """
        pass
    
import NXOpen
##  Manages the base unit  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class BaseUnit(NXOpen.NXObject): 
    """ Manages the base unit """


    ##  Gets constituent unit by index
    ##  @return constituentUnit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink):  constituent unit .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  The index must be greater or equal to 0  and less than @link CAE::FTK::BaseUnit::GetConstituentUnitsCount CAE::FTK::BaseUnit::GetConstituentUnitsCount@endlink  
    def GetConstituentUnit(base_unit: BaseUnit, nthConstituentUnitIndex: int) -> BaseUnit:
        """
         Gets constituent unit by index
         @return constituentUnit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink):  constituent unit .
        """
        pass
    
    ##  Gets the count of constituent units 
    ##  @return constituentUnitsCount (int):  constituent units count .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetConstituentUnitsCount(base_unit: BaseUnit) -> int:
        """
         Gets the count of constituent units 
         @return constituentUnitsCount (int):  constituent units count .
        """
        pass
    
    ##  Sets measure name 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Measure name 
    def SetMeasureName(base_unit: BaseUnit, measure_name: str) -> None:
        """
         Sets measure name 
        """
        pass
    
    ##   @brief Sets nx unit. 
    ## 
    ##  
    ##             
    ##                 To make sure the base unit could be changed successfully,two conditions must be satisfied:
    ##             <ol>
    ##                 <li>The measure of input nx unit must be same as the nx unit saved in BaseUnit.</li>
    ##                 <li>The BaseUnit must be created by method @link CAE::FTK::DataManager::CreateArrayUnit CAE::FTK::DataManager::CreateArrayUnit@endlink ,but except for the method which creates
    ##                     unit by numerator and denominator unit.</li>
    ##             </ol>
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##   
    def SetNxUnit(base_unit: BaseUnit, nxUnit: NXOpen.Unit) -> None:
        """
          @brief Sets nx unit. 
        
         
                    
                        To make sure the base unit could be changed successfully,two conditions must be satisfied:
                    <ol>
                        <li>The measure of input nx unit must be same as the nx unit saved in BaseUnit.</li>
                        <li>The BaseUnit must be created by method @link CAE::FTK::DataManager::CreateArrayUnit CAE::FTK::DataManager::CreateArrayUnit@endlink ,but except for the method which creates
                            unit by numerator and denominator unit.</li>
                    </ol>
                    
        """
        pass
    
    ##  Sets unit name 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Unit name 
    def SetUnitName(base_unit: BaseUnit, unit_name: str) -> None:
        """
         Sets unit name 
        """
        pass
    
##  Represents a section based matrix record which has complex data values.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ComplexSectionBasedMatrixRecord(SectionBasedMatrixRecord): 
    """ Represents a section based matrix record which has complex data values. """


    ##  Adds the complex data values for each section. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  X-Coordinate data 
    def AddSectionData(matrixRecord: ComplexSectionBasedMatrixRecord, xCoordinatePoints: List[float], yCoordinateReal: List[float], yCoordinateImag: List[float], zCoordinatePoint: float) -> None:
        """
         Adds the complex data values for each section. 
        """
        pass
    
    ##  Gets the complex data values from specific section. 
    ##  @return A tuple consisting of (xCoordinatePoints, yCoordinateReal, yCoordinateImag, zCoordinatePoints). 
    ##  - xCoordinatePoints is: List[float]. X-Coordinate data .
    ##  - yCoordinateReal is: List[float]. Real part of Y-Coordinate data .
    ##  - yCoordinateImag is: List[float]. Imaginary part of Y-Coordinate data .
    ##  - zCoordinatePoints is: float. Z-Coordinate data .

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Section index 
    @staticmethod
    def GetSectionData(matrixRecord: ComplexSectionBasedMatrixRecord, sectionIndex: int) -> Tuple[List[float], List[float], List[float], float]:
        """
         Gets the complex data values from specific section. 
         @return A tuple consisting of (xCoordinatePoints, yCoordinateReal, yCoordinateImag, zCoordinatePoints). 
         - xCoordinatePoints is: List[float]. X-Coordinate data .
         - yCoordinateReal is: List[float]. Real part of Y-Coordinate data .
         - yCoordinateImag is: List[float]. Imaginary part of Y-Coordinate data .
         - zCoordinatePoints is: float. Z-Coordinate data .

        """
        pass
    
import NXOpen
##  Ftk data manager  <br> To obtain an instance of this class use @link NXOpen::Session::DataManager NXOpen::Session::DataManager@endlink .  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class DataManager(NXOpen.Object): 
    """ Ftk data manager """


    ##  Represents the method to get Z value for afu record in 3D plot 
    ##  The Z value is selection order 
    class AfuRecordZValue(Enum):
        """
        Members Include: <SelectionOrder> <General> <Rpm> <Time> <Order>
        """
        SelectionOrder: int
        General: int
        Rpm: int
        Time: int
        Order: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DataManager.AfuRecordZValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the file container type 
    ##  Not any container 
    class FileContainerType(Enum):
        """
        Members Include: <NotSet> <AssociatedContainer> <ResultContainer> <UserContainer> <All>
        """
        NotSet: int
        AssociatedContainer: int
        ResultContainer: int
        UserContainer: int
        All: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DataManager.FileContainerType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Returns the @link NXOpen::CAE::FTK::AfuFileManager NXOpen::CAE::FTK::AfuFileManager@endlink  belonging to FTK data manager 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @link AfuFileManager NXOpen.CAE.FTK.AfuFileManager@endlink
    @property
    def AfuFileManager() -> AfuFileManager:
        """
         Returns the @link NXOpen::CAE::FTK::AfuFileManager NXOpen::CAE::FTK::AfuFileManager@endlink  belonging to FTK data manager 
        """
        pass
    
    ##  Returns the @link NXOpen::CAE::FTK::Op2FileManager NXOpen::CAE::FTK::Op2FileManager@endlink  belonging to FTK data manager 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @link Op2FileManager NXOpen.CAE.FTK.Op2FileManager@endlink
    @property
    def Op2FileManager() -> Op2FileManager:
        """
         Returns the @link NXOpen::CAE::FTK::Op2FileManager NXOpen::CAE::FTK::Op2FileManager@endlink  belonging to FTK data manager 
        """
        pass
    
    ##  Creates 2d array record 
    ##  @return array_record (@link ArrayRecord2D NXOpen.CAE.FTK.ArrayRecord2D@endlink):  2D array record .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Title name 
    def CreateArrayRecord2d(title_name: str, legend_name: str, num_points: int) -> ArrayRecord2D:
        """
         Creates 2d array record 
         @return array_record (@link ArrayRecord2D NXOpen.CAE.FTK.ArrayRecord2D@endlink):  2D array record .
        """
        pass
    
    ##  Creates 2d array record with even spacing 
    ##  @return array_record (@link ArrayRecord2DEven NXOpen.CAE.FTK.ArrayRecord2DEven@endlink):  2D even array record .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  Title name 
    def CreateArrayRecord2dEvenSpacing(title_name: str, legend_name: str) -> ArrayRecord2DEven:
        """
         Creates 2d array record with even spacing 
         @return array_record (@link ArrayRecord2DEven NXOpen.CAE.FTK.ArrayRecord2DEven@endlink):  2D even array record .
        """
        pass
    
    ##  Creates 2d array record with even spacing and data attributes 
    ##  @return arrayRecord (@link ArrayRecord2DEvenWithZValue NXOpen.CAE.FTK.ArrayRecord2DEvenWithZValue@endlink):  2D array record with even spacing and data attributes .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  Title name 
    def CreateArrayRecord2dEvenSpacingWithZValue(titleName: str, legendName: str) -> ArrayRecord2DEvenWithZValue:
        """
         Creates 2d array record with even spacing and data attributes 
         @return arrayRecord (@link ArrayRecord2DEvenWithZValue NXOpen.CAE.FTK.ArrayRecord2DEvenWithZValue@endlink):  2D array record with even spacing and data attributes .
        """
        pass
    
    ##  Creates 2d array record with data attributes 
    ##  @return arrayRecord (@link ArrayRecord2DWithZValue NXOpen.CAE.FTK.ArrayRecord2DWithZValue@endlink):  2D array record with data attributes .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  Title name 
    def CreateArrayRecord2dWithZValue(titleName: str, legendName: str, numPoints: int) -> ArrayRecord2DWithZValue:
        """
         Creates 2d array record with data attributes 
         @return arrayRecord (@link ArrayRecord2DWithZValue NXOpen.CAE.FTK.ArrayRecord2DWithZValue@endlink):  2D array record with data attributes .
        """
        pass
    
    ##  Creates 3d array record 
    ##  @return array_record (@link ArrayRecord3D NXOpen.CAE.FTK.ArrayRecord3D@endlink):  3D array record .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Title name 
    def CreateArrayRecord3d(title_name: str, legend_name: str, num_points: int) -> ArrayRecord3D:
        """
         Creates 3d array record 
         @return array_record (@link ArrayRecord3D NXOpen.CAE.FTK.ArrayRecord3D@endlink):  3D array record .
        """
        pass
    
    ##  Creates array unit by nx system unit 
    ##  @return array_unit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink):  Array unit .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  NX system unit 
    @overload
    def CreateArrayUnit(self, nx_unit: NXOpen.Unit) -> BaseUnit:
        """
         Creates array unit by nx system unit 
         @return array_unit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink):  Array unit .
        """
        pass
    
    ##   @brief  Creates the object @link NXOpen::CAE::FTK::BaseUnit NXOpen::CAE::FTK::BaseUnit@endlink  by @link NXOpen::Unit NXOpen::Unit@endlink 
    ##             with alias measure name and localized alias measure name.  
    ## 
    ##  
    ##             
    ##             Please use the method @link NXOpen::CAE::FTK::DataManager::CreateArrayUnit NXOpen::CAE::FTK::DataManager::CreateArrayUnit@endlink  which has two arguments
    ##             if alias measure name is not needed.
    ##             
    ##             
    ##  @return arrayUnit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="nxUnit"> (@link NXOpen.Unit NXOpen.Unit@endlink) </param>
    ## <param name="aliasMeasureName"> (str) </param>
    ## <param name="localizedAliasMeasureName"> (str) </param>
    @overload
    def CreateArrayUnit(self, nxUnit: NXOpen.Unit, aliasMeasureName: str, localizedAliasMeasureName: str) -> BaseUnit:
        """
          @brief  Creates the object @link NXOpen::CAE::FTK::BaseUnit NXOpen::CAE::FTK::BaseUnit@endlink  by @link NXOpen::Unit NXOpen::Unit@endlink 
                    with alias measure name and localized alias measure name.  
        
         
                    
                    Please use the method @link NXOpen::CAE::FTK::DataManager::CreateArrayUnit NXOpen::CAE::FTK::DataManager::CreateArrayUnit@endlink  which has two arguments
                    if alias measure name is not needed.
                    
                    
         @return arrayUnit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink): .
        """
        pass
    
    ##  Creates array unit by numerator and denominator unit 
    ##  @return array_unit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink):  Array unit .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Numerator unit 
    @overload
    def CreateArrayUnit(self, numerator_unit: BaseUnit, denominator_unit: BaseUnit) -> BaseUnit:
        """
         Creates array unit by numerator and denominator unit 
         @return array_unit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink):  Array unit .
        """
        pass
    
    ##  Creates an empty complex matrix record which section data is complex data. 
    ##  @return matrix_record (@link ComplexSectionBasedMatrixRecord NXOpen.CAE.FTK.ComplexSectionBasedMatrixRecord@endlink):  Complex matrix record .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Title name 
    def CreateComplexMatrixRecord(title_name: str, legend_name: str) -> ComplexSectionBasedMatrixRecord:
        """
         Creates an empty complex matrix record which section data is complex data. 
         @return matrix_record (@link ComplexSectionBasedMatrixRecord NXOpen.CAE.FTK.ComplexSectionBasedMatrixRecord@endlink):  Complex matrix record .
        """
        pass
    
    ##  Creates an empty record for matrix plot. 
    ##  @return pMatrixPlotRecord (@link MatrixPlotRecord NXOpen.CAE.FTK.MatrixPlotRecord@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="titleName"> (str) </param>
    ## <param name="legendName"> (str) </param>
    def CreateMatrixPlotRecord(titleName: str, legendName: str) -> MatrixPlotRecord:
        """
         Creates an empty record for matrix plot. 
         @return pMatrixPlotRecord (@link MatrixPlotRecord NXOpen.CAE.FTK.MatrixPlotRecord@endlink): .
        """
        pass
    
    ##  Creates an empty real matrix record which section data is real data. 
    ##  @return matrix_record (@link RealSectionBasedMatrixRecord NXOpen.CAE.FTK.RealSectionBasedMatrixRecord@endlink):  Real matrix record .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Title name 
    def CreateRealMatrixRecord(title_name: str, legend_name: str) -> RealSectionBasedMatrixRecord:
        """
         Creates an empty real matrix record which section data is real data. 
         @return matrix_record (@link RealSectionBasedMatrixRecord NXOpen.CAE.FTK.RealSectionBasedMatrixRecord@endlink):  Real matrix record .
        """
        pass
    
    ##  Creates unitless unit 
    ##  @return arrayUnit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="measureName"> (str) </param>
    ## <param name="localizedMeasureName"> (str) </param>
    def CreateUnitlessUnit(measureName: str, localizedMeasureName: str) -> BaseUnit:
        """
         Creates unitless unit 
         @return arrayUnit (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink): .
        """
        pass
    
    ##  Deletes array unit 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  Deleted unit 
    @staticmethod
    def DeleteArrayUnit(deleted_unit: BaseUnit) -> None:
        """
         Deletes array unit 
        """
        pass
    
    ##  Deletes record 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Deleted record 
    @staticmethod
    def DeleteRecord(deleted_record: BaseRecord) -> None:
        """
         Deletes record 
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Represents the parameter settings for exporting data to external files.  <br> This is an abstract class  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ExportFilesParameter(NXOpen.TransientObject): 
    """ Represents the parameter settings for exporting data to external files. """


    ##  Defines the header options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FileDescription</term><description> 
    ## </description> </item><item><term> 
    ## General</term><description> 
    ## </description> </item><item><term> 
    ## Abscissa</term><description> 
    ## </description> </item><item><term> 
    ## Ordinate</term><description> 
    ## </description> </item><item><term> 
    ## AbscissaZ</term><description> 
    ## </description> </item><item><term> 
    ## ApplicationSpecific</term><description> 
    ## </description> </item></list>
    class HeaderOptions(Enum):
        """
        Members Include: <FileDescription> <General> <Abscissa> <Ordinate> <AbscissaZ> <ApplicationSpecific>
        """
        FileDescription: int
        General: int
        Abscissa: int
        Ordinate: int
        AbscissaZ: int
        ApplicationSpecific: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExportFilesParameter.HeaderOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the expor behavior when file is exist 
    ##  Rename the file name with number postfix, like A -> A1 
    class OverrideOption(Enum):
        """
        Members Include: <Rename> <Append> <Replace> <Skip>
        """
        Rename: int
        Append: int
        Replace: int
        Skip: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExportFilesParameter.OverrideOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) IsHeaderExportRequired
    ##   the full header print required.  
    ##    If the setting is true, all header options are required for export.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def IsHeaderExportRequired(self) -> bool:
        """
        Getter for property: (bool) IsHeaderExportRequired
          the full header print required.  
           If the setting is true, all header options are required for export.   
         
        """
        pass
    
    ## Setter for property: (bool) IsHeaderExportRequired

    ##   the full header print required.  
    ##    If the setting is true, all header options are required for export.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @IsHeaderExportRequired.setter
    def IsHeaderExportRequired(self, hasHeader: bool):
        """
        Setter for property: (bool) IsHeaderExportRequired
          the full header print required.  
           If the setting is true, all header options are required for export.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.NumberFormat NXOpen.CAE.NumberFormat@endlink) NumberFormat
    ##   the number format options.  
    ##   
    ##             
    ##             The NumberFormat object will be deleted along with the file parameter object.
    ##             
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.NumberFormat
    @property
    def NumberFormat(self) -> NXOpen.CAE.NumberFormat:
        """
        Getter for property: (@link NXOpen.CAE.NumberFormat NXOpen.CAE.NumberFormat@endlink) NumberFormat
          the number format options.  
          
                    
                    The NumberFormat object will be deleted along with the file parameter object.
                    
                      
         
        """
        pass
    
    ## Getter for property: (@link ExportFilesParameter.OverrideOption NXOpen.CAE.FTK.ExportFilesParameter.OverrideOption@endlink) OverrideSetting
    ##   the file override option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return ExportFilesParameter.OverrideOption
    @property
    def OverrideSetting(self) -> ExportFilesParameter.OverrideOption:
        """
        Getter for property: (@link ExportFilesParameter.OverrideOption NXOpen.CAE.FTK.ExportFilesParameter.OverrideOption@endlink) OverrideSetting
          the file override option   
            
         
        """
        pass
    
    ## Setter for property: (@link ExportFilesParameter.OverrideOption NXOpen.CAE.FTK.ExportFilesParameter.OverrideOption@endlink) OverrideSetting

    ##   the file override option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @OverrideSetting.setter
    def OverrideSetting(self, overrideOption: ExportFilesParameter.OverrideOption):
        """
        Setter for property: (@link ExportFilesParameter.OverrideOption NXOpen.CAE.FTK.ExportFilesParameter.OverrideOption@endlink) OverrideSetting
          the file override option   
            
         
        """
        pass
    
    ##  Destroys the object 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(param: ExportFilesParameter) -> None:
        """
         Destroys the object 
        """
        pass
    
    ##  Gets the custom record names for export 
    ##  @return customRecordNames (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCustomRecordNames(param: ExportFilesParameter) -> List[str]:
        """
         Gets the custom record names for export 
         @return customRecordNames (List[str]): .
        """
        pass
    
    ##  Gets the external files for export 
    ##  @return fileNames (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFileNames(param: ExportFilesParameter) -> List[str]:
        """
         Gets the external files for export 
         @return fileNames (List[str]): .
        """
        pass
    
    ##  Asks whether to export the specified header option 
    ##  @return required (bool): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="whichHeader"> (@link ExportFilesParameter.HeaderOptions NXOpen.CAE.FTK.ExportFilesParameter.HeaderOptions@endlink) </param>
    def GetIsCertainHeaderExportRequired(param: ExportFilesParameter, whichHeader: ExportFilesParameter.HeaderOptions) -> bool:
        """
         Asks whether to export the specified header option 
         @return required (bool): .
        """
        pass
    
    ##  Sets the custom record names for export 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="customRecordNames"> (List[str]) </param>
    def SetCustomRecordNames(param: ExportFilesParameter, customRecordNames: List[str]) -> None:
        """
         Sets the custom record names for export 
        """
        pass
    
    ##  Sets the external files for export 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fileNames"> (List[str]) </param>
    def SetFileNames(param: ExportFilesParameter, fileNames: List[str]) -> None:
        """
         Sets the external files for export 
        """
        pass
    
    ##  Sets whether or not a specific header is required 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="whichHeader"> (@link ExportFilesParameter.HeaderOptions NXOpen.CAE.FTK.ExportFilesParameter.HeaderOptions@endlink) </param>
    ## <param name="required"> (bool) </param>
    def SetIsCertainHeaderExportRequired(param: ExportFilesParameter, whichHeader: ExportFilesParameter.HeaderOptions, required: bool) -> None:
        """
         Sets whether or not a specific header is required 
        """
        pass
    
import NXOpen
##  FTK function data manager  <br> To obtain an instance of this class use @link NXOpen::Session::FTKManager NXOpen::Session::FTKManager@endlink .  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class FTKManager(NXOpen.Object): 
    """ FTK function data manager """


    ##  Returns the @link NXOpen::CAE::FTK::OptionSetting NXOpen::CAE::FTK::OptionSetting@endlink  belonging to this session 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @link OptionSetting NXOpen.CAE.FTK.OptionSetting@endlink
    @property
    def OptionSetting() -> OptionSetting:
        """
         Returns the @link NXOpen::CAE::FTK::OptionSetting NXOpen::CAE::FTK::OptionSetting@endlink  belonging to this session 
        """
        pass
    
import NXOpen
##  Represents the interface for  application specific data owner
## 
##   <br>  Created in NX12.0.0  <br> 

class IApplicationDataOwner(NXOpen.Object): 
    """ Represents the interface for  application specific data owner"""


    ##  Gets the application specific data associated with the record 
    ##  @return applicationData (@link IApplicationData NXOpen.CAE.FTK.IApplicationData@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetApplicationData(applicationDataOwner: IApplicationDataOwner) -> IApplicationData:
        """
         Gets the application specific data associated with the record 
         @return applicationData (@link IApplicationData NXOpen.CAE.FTK.IApplicationData@endlink): .
        """
        pass
    
    ##  Sets the application specific data to the record 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="applicationData"> (@link IApplicationData NXOpen.CAE.FTK.IApplicationData@endlink) </param>
    @abstractmethod
    def SetApplicationData(applicationDataOwner: IApplicationDataOwner, applicationData: IApplicationData) -> None:
        """
         Sets the application specific data to the record 
        """
        pass
    
import NXOpen
##  Represents the interface for  application specific data class
## 
##   <br>  Created in NX12.0.0  <br> 

class IApplicationData(NXOpen.Object): 
    """ Represents the interface for  application specific data class"""


    ##  Asks the name of a displayable attribute 
    ##  @return attributeName (str): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nth"> (int) </param>
    @abstractmethod
    def AskNthDisplayableAttributeName(applicationData: IApplicationData, nth: int) -> str:
        """
         Asks the name of a displayable attribute 
         @return attributeName (str): .
        """
        pass
    
    ##  Asks the value of a displayable attribute 
    ##  @return attributeValue (str): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nth"> (int) </param>
    @abstractmethod
    def AskNthDisplayableAttributeValue(applicationData: IApplicationData, nth: int) -> str:
        """
         Asks the value of a displayable attribute 
         @return attributeValue (str): .
        """
        pass
    
    ##  Asks the count of attributes which could be showed on legend table 
    ##  @return count (int): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def AskNumberOfDisplayableAttributes(applicationData: IApplicationData) -> int:
        """
         Asks the count of attributes which could be showed on legend table 
         @return count (int): .
        """
        pass
    
import NXOpen
##  Represents the interface for a record with Z value
## 
##   <br>  Created in NX1926.0.0  <br> 

class IRecordWithZValue(NXOpen.Object): 
    """ Represents the interface for a record with Z value"""


    ## Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit
    ##   the Z unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return BaseUnit
    @property
    @abstractmethod
    def Unit(self) -> BaseUnit:
        """
        Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit
          the Z unit   
            
         
        """
        pass
    
    ## Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit

    ##   the Z unit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Unit.setter
    def Unit(self, zValueUnit: BaseUnit):
        """
        Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit
          the Z unit   
            
         
        """
        pass
    
    ## Getter for property: (float) Value
    ##   the Z value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    @abstractmethod
    def Value(self) -> float:
        """
        Getter for property: (float) Value
          the Z value   
            
         
        """
        pass
    
    ## Setter for property: (float) Value

    ##   the Z value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Value.setter
    def Value(self, zValue: float):
        """
        Setter for property: (float) Value
          the Z value   
            
         
        """
        pass
    
##  Represents record data for matrix plot.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MatrixPlotRecord(BaseRecord): 
    """ Represents record data for matrix plot. """


    ## Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) DataUnit
    ##   the data unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return BaseUnit
    @property
    def DataUnit(self) -> BaseUnit:
        """
        Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) DataUnit
          the data unit   
            
         
        """
        pass
    
    ## Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) DataUnit

    ##   the data unit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DataUnit.setter
    def DataUnit(self, pDataUnit: BaseUnit):
        """
        Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) DataUnit
          the data unit   
            
         
        """
        pass
    
    ## Getter for property: (str) Title
    ##   the title name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
          the title name   
            
         
        """
        pass
    
    ## Setter for property: (str) Title

    ##   the title name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Title.setter
    def Title(self, titleName: str):
        """
        Setter for property: (str) Title
          the title name   
            
         
        """
        pass
    
    ##  Gets the column count 
    ##  @return numColumns (int): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetColumnCount(pMatrixPlotRecord: MatrixPlotRecord) -> int:
        """
         Gets the column count 
         @return numColumns (int): .
        """
        pass
    
    ##  Gets the column labels 
    ##  @return columnLabels (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetColumnLabels(pMatrixPlotRecord: MatrixPlotRecord) -> List[str]:
        """
         Gets the column labels 
         @return columnLabels (List[str]): .
        """
        pass
    
    ##   @brief  Gets real or complex data.  
    ## 
    ##  
    ##             
    ##                 To get real data, the parameter realData will be filled, but the parameter imagData will be empty.
    ##                 To get complex data, both the parameters realData and imagData will all be filled.
    ##             
    ##             
    ##  @return A tuple consisting of (realData, imagData). 
    ##  - realData is: List[float]. Real part of data .
    ##  - imagData is: List[float]. Imaginary part data .

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetData(pMatrixPlotRecord: MatrixPlotRecord) -> Tuple[List[float], List[float]]:
        """
          @brief  Gets real or complex data.  
        
         
                    
                        To get real data, the parameter realData will be filled, but the parameter imagData will be empty.
                        To get complex data, both the parameters realData and imagData will all be filled.
                    
                    
         @return A tuple consisting of (realData, imagData). 
         - realData is: List[float]. Real part of data .
         - imagData is: List[float]. Imaginary part data .

        """
        pass
    
    ##  Gets the row count 
    ##  @return numRows (int): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRowCount(pMatrixPlotRecord: MatrixPlotRecord) -> int:
        """
         Gets the row count 
         @return numRows (int): .
        """
        pass
    
    ##  Gets the row labels 
    ##  @return rowLabels (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRowLabels(pMatrixPlotRecord: MatrixPlotRecord) -> List[str]:
        """
         Gets the row labels 
         @return rowLabels (List[str]): .
        """
        pass
    
    ##  Sets the column labels 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="columnLabels"> (List[str]) </param>
    def SetColumnLabels(pMatrixPlotRecord: MatrixPlotRecord, columnLabels: List[str]) -> None:
        """
         Sets the column labels 
        """
        pass
    
    ##   @brief  Sets real or complex data.  
    ## 
    ##  
    ##             
    ##                 To set real data, the parameter realData must be given, but the parameter imagData can be empty.
    ##                 To set complex data, both the parameters realData and imagData must be given.
    ##             
    ##             
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  Real part of data 
    def SetData(pMatrixPlotRecord: MatrixPlotRecord, realData: List[float], imagData: List[float]) -> None:
        """
          @brief  Sets real or complex data.  
        
         
                    
                        To set real data, the parameter realData must be given, but the parameter imagData can be empty.
                        To set complex data, both the parameters realData and imagData must be given.
                    
                    
        """
        pass
    
    ##  Sets the row labels 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowLabels"> (List[str]) </param>
    def SetRowLabels(pMatrixPlotRecord: MatrixPlotRecord, rowLabels: List[str]) -> None:
        """
         Sets the row labels 
        """
        pass
    
import NXOpen
##   @brief  Provides methods to query the loaded OP2 files  
## 
##    <br> To obtain an instance of this class use @link NXOpen::CAE::FTK::DataManager::Op2FileManager NXOpen::CAE::FTK::DataManager::Op2FileManager@endlink .  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class Op2FileManager(NXOpen.Object): 
    """ <summary> Provides methods to query the loaded OP2 files </summary> """


    ##  Deletes an OP2 file 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="op2FileName"> (str) </param>
    @staticmethod
    def DeleteFile(op2FileName: str) -> None:
        """
         Deletes an OP2 file 
        """
        pass
    
    ##  Gets all dataset names in an OP2 file which must be loaded 
    ##  @return datasetNames (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="op2FileName"> (str) </param>
    @staticmethod
    def GetAllDatasetNamesInFile(op2FileName: str) -> List[str]:
        """
         Gets all dataset names in an OP2 file which must be loaded 
         @return datasetNames (List[str]): .
        """
        pass
    
    ##  Gets all record names in an OP2 dataset of an OP2 file which must be loaded 
    ##  @return recordNames (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="op2FileName"> (str) </param>
    ## <param name="datasetName"> (str) </param>
    def GetAllRecordNamesInDataset(op2FileName: str, datasetName: str) -> List[str]:
        """
         Gets all record names in an OP2 dataset of an OP2 file which must be loaded 
         @return recordNames (List[str]): .
        """
        pass
    
    ##  Gets all loaded OP2 files 
    ##  @return op2FileNames (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLoadedFiles() -> List[str]:
        """
         Gets all loaded OP2 files 
         @return op2FileNames (List[str]): .
        """
        pass
    
    ##  Gets an OP2 record in an OP2 dataset of an OP2 file which must be loaded 
    ##  @return op2Record (@link Op2Record NXOpen.CAE.FTK.Op2Record@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="op2FileName"> (str) </param>
    ## <param name="datasetName"> (str) </param>
    ## <param name="recordName"> (str) </param>
    def GetRecord(op2FileName: str, datasetName: str, recordName: str) -> Op2Record:
        """
         Gets an OP2 record in an OP2 dataset of an OP2 file which must be loaded 
         @return op2Record (@link Op2Record NXOpen.CAE.FTK.Op2Record@endlink): .
        """
        pass
    
    ##  Loads an OP2 file to the specified container.
    ##                 
    ##                 An OP2 file can be loaded under associated container, solution result container or user container.
    ##                 The container type indicates under which container the file is loaded.
    ##                 
    ##              
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="op2FileName"> (str) </param>
    ## <param name="containerType"> (@link DataManager.FileContainerType NXOpen.CAE.FTK.DataManager.FileContainerType@endlink) </param>
    def LoadFile(op2FileName: str, containerType: DataManager.FileContainerType) -> None:
        """
         Loads an OP2 file to the specified container.
                        
                        An OP2 file can be loaded under associated container, solution result container or user container.
                        The container type indicates under which container the file is loaded.
                        
                     
        """
        pass
    
    ##  Unloads an OP2 file from the specified container.
    ##                 
    ##                 An OP2 file can be loaded under associated container, solution result container or user container.
    ##                 The container type indicates under which container the file is unloaded.
    ##                 
    ##              
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="op2FileName"> (str) </param>
    ## <param name="containerType"> (@link DataManager.FileContainerType NXOpen.CAE.FTK.DataManager.FileContainerType@endlink) </param>
    def UnloadFile(op2FileName: str, containerType: DataManager.FileContainerType) -> None:
        """
         Unloads an OP2 file from the specified container.
                        
                        An OP2 file can be loaded under associated container, solution result container or user container.
                        The container type indicates under which container the file is unloaded.
                        
                     
        """
        pass
    
##  Represents the op2 record data  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Op2Record(BaseRecord): 
    """ Represents the op2 record data """


    ##  Calculates the RMS value for the PSD Record. 
    ##                 Error is returned if the input record is not a Power Spectral Density (PSD) record.
    ##  @return rmsValue (float): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def CalculateRMSOfPSD(op2Record: Op2Record) -> float:
        """
         Calculates the RMS value for the PSD Record. 
                        Error is returned if the input record is not a Power Spectral Density (PSD) record.
         @return rmsValue (float): .
        """
        pass
    
    ##  Lists the record information to a file or listing information window 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  if NULL, print information to listing information window. Otherwise write information to the file 
    def ListInformation(op2Record: Op2Record, fileName: str, listInfo: bool, listData: bool) -> None:
        """
         Lists the record information to a file or listing information window 
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Manager the options data for Data Record  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class OptionSetting(NXOpen.Object): 
    """ Manager the options data for Data Record """


    ## Getter for property: (@link NXOpen.CAE.AfuData.AbscissaType NXOpen.CAE.AfuData.AbscissaType@endlink) AbscissaSpacingType
    ##   the abscissa spacing type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CAE.AfuData.AbscissaType
    @property
    def AbscissaSpacingType(self) -> NXOpen.CAE.AfuData.AbscissaType:
        """
        Getter for property: (@link NXOpen.CAE.AfuData.AbscissaType NXOpen.CAE.AfuData.AbscissaType@endlink) AbscissaSpacingType
          the abscissa spacing type   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.AfuData.AbscissaType NXOpen.CAE.AfuData.AbscissaType@endlink) AbscissaSpacingType

    ##   the abscissa spacing type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AbscissaSpacingType.setter
    def AbscissaSpacingType(self, abscissa_type: NXOpen.CAE.AfuData.AbscissaType):
        """
        Setter for property: (@link NXOpen.CAE.AfuData.AbscissaType NXOpen.CAE.AfuData.AbscissaType@endlink) AbscissaSpacingType
          the abscissa spacing type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) AbscissaUnit
    ##   the abscissa unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CAE.XyFunctionUnit
    @property
    def AbscissaUnit(self) -> NXOpen.CAE.XyFunctionUnit:
        """
        Getter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) AbscissaUnit
          the abscissa unit   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) AbscissaUnit

    ##   the abscissa unit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AbscissaUnit.setter
    def AbscissaUnit(self, x_unit: NXOpen.CAE.XyFunctionUnit):
        """
        Setter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) AbscissaUnit
          the abscissa unit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.XyFunctionGeneralType NXOpen.CAE.XyFunctionGeneralType@endlink) FunctionType
    ##   the function type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CAE.XyFunctionGeneralType
    @property
    def FunctionType(self) -> NXOpen.CAE.XyFunctionGeneralType:
        """
        Getter for property: (@link NXOpen.CAE.XyFunctionGeneralType NXOpen.CAE.XyFunctionGeneralType@endlink) FunctionType
          the function type   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.XyFunctionGeneralType NXOpen.CAE.XyFunctionGeneralType@endlink) FunctionType

    ##   the function type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @FunctionType.setter
    def FunctionType(self, function_type: NXOpen.CAE.XyFunctionGeneralType):
        """
        Setter for property: (@link NXOpen.CAE.XyFunctionGeneralType NXOpen.CAE.XyFunctionGeneralType@endlink) FunctionType
          the function type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.AfuData.OrdinateType NXOpen.CAE.AfuData.OrdinateType@endlink) OrdinateDataType
    ##   the ordinate data type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CAE.AfuData.OrdinateType
    @property
    def OrdinateDataType(self) -> NXOpen.CAE.AfuData.OrdinateType:
        """
        Getter for property: (@link NXOpen.CAE.AfuData.OrdinateType NXOpen.CAE.AfuData.OrdinateType@endlink) OrdinateDataType
          the ordinate data type   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.AfuData.OrdinateType NXOpen.CAE.AfuData.OrdinateType@endlink) OrdinateDataType

    ##   the ordinate data type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OrdinateDataType.setter
    def OrdinateDataType(self, ordinate_type: NXOpen.CAE.AfuData.OrdinateType):
        """
        Setter for property: (@link NXOpen.CAE.AfuData.OrdinateType NXOpen.CAE.AfuData.OrdinateType@endlink) OrdinateDataType
          the ordinate data type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) OrdinateDenominatorUnit
    ##   the ordinate denominator unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CAE.XyFunctionUnit
    @property
    def OrdinateDenominatorUnit(self) -> NXOpen.CAE.XyFunctionUnit:
        """
        Getter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) OrdinateDenominatorUnit
          the ordinate denominator unit   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) OrdinateDenominatorUnit

    ##   the ordinate denominator unit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OrdinateDenominatorUnit.setter
    def OrdinateDenominatorUnit(self, y_denominator_unit: NXOpen.CAE.XyFunctionUnit):
        """
        Setter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) OrdinateDenominatorUnit
          the ordinate denominator unit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) OrdinateSecondNumeratorUnit
    ##   the ordinate second numerator unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CAE.XyFunctionUnit
    @property
    def OrdinateSecondNumeratorUnit(self) -> NXOpen.CAE.XyFunctionUnit:
        """
        Getter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) OrdinateSecondNumeratorUnit
          the ordinate second numerator unit   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) OrdinateSecondNumeratorUnit

    ##   the ordinate second numerator unit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OrdinateSecondNumeratorUnit.setter
    def OrdinateSecondNumeratorUnit(self, y_second_numerator_unit: NXOpen.CAE.XyFunctionUnit):
        """
        Setter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) OrdinateSecondNumeratorUnit
          the ordinate second numerator unit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) OrdinateUnit
    ##   the ordinate unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CAE.XyFunctionUnit
    @property
    def OrdinateUnit(self) -> NXOpen.CAE.XyFunctionUnit:
        """
        Getter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) OrdinateUnit
          the ordinate unit   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) OrdinateUnit

    ##   the ordinate unit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OrdinateUnit.setter
    def OrdinateUnit(self, y_unit: NXOpen.CAE.XyFunctionUnit):
        """
        Setter for property: (@link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink) OrdinateUnit
          the ordinate unit   
            
         
        """
        pass
    
    ## Getter for property: (str) RecordName
    ##   the record name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def RecordName(self) -> str:
        """
        Getter for property: (str) RecordName
          the record name   
            
         
        """
        pass
    
    ## Setter for property: (str) RecordName

    ##   the record name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RecordName.setter
    def RecordName(self, record_name: str):
        """
        Setter for property: (str) RecordName
          the record name   
            
         
        """
        pass
    
    ## Getter for property: (bool) SortValueType
    ##   the sort value flag.  
    ##   
    ##             Sorts the values in X direction when it is true. This option is only applicable for real only data.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def SortValueType(self) -> bool:
        """
        Getter for property: (bool) SortValueType
          the sort value flag.  
          
                    Sorts the values in X direction when it is true. This option is only applicable for real only data.   
         
        """
        pass
    
    ## Setter for property: (bool) SortValueType

    ##   the sort value flag.  
    ##   
    ##             Sorts the values in X direction when it is true. This option is only applicable for real only data.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SortValueType.setter
    def SortValueType(self, sort_value_type: bool):
        """
        Setter for property: (bool) SortValueType
          the sort value flag.  
          
                    Sorts the values in X direction when it is true. This option is only applicable for real only data.   
         
        """
        pass
    
    ##  Get the adding header flag when export to CSV file 
    ##  @return add_header (bool):  If want to add header when export to CSV file .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetHeaderFlag() -> bool:
        """
         Get the adding header flag when export to CSV file 
         @return add_header (bool):  If want to add header when export to CSV file .
        """
        pass
    
    ##  Get the record options data for the Data Record 
    ##  @return A tuple consisting of (record_name, function_type, abscissa_type, x_unit, ordinate_type, y_unit, y_denominator_unit, sort_value_type). 
    ##  - record_name is: str. The name of the Data Record .
    ##  - function_type is: @link NXOpen.CAE.XyFunctionGeneralType NXOpen.CAE.XyFunctionGeneralType@endlink. Usage type of Data Record used .
    ##  - abscissa_type is: @link NXOpen.CAE.AfuData.AbscissaType NXOpen.CAE.AfuData.AbscissaType@endlink. Abscissa specific data type .
    ##  - x_unit is: @link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink. Unit Code of data .
    ##  - ordinate_type is: @link NXOpen.CAE.AfuData.OrdinateType NXOpen.CAE.AfuData.OrdinateType@endlink. Ordinate data type .
    ##  - y_unit is: @link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink. Ordinate Numerator Unit Code of data .
    ##  - y_denominator_unit is: @link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink. Ordinate Denominator Unit Code of data .
    ##  - sort_value_type is: bool. If want to sort value in x direction .

    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRecordOptionData() -> Tuple[str, NXOpen.CAE.XyFunctionGeneralType, NXOpen.CAE.AfuData.AbscissaType, NXOpen.CAE.XyFunctionUnit, NXOpen.CAE.AfuData.OrdinateType, NXOpen.CAE.XyFunctionUnit, NXOpen.CAE.XyFunctionUnit, bool]:
        """
         Get the record options data for the Data Record 
         @return A tuple consisting of (record_name, function_type, abscissa_type, x_unit, ordinate_type, y_unit, y_denominator_unit, sort_value_type). 
         - record_name is: str. The name of the Data Record .
         - function_type is: @link NXOpen.CAE.XyFunctionGeneralType NXOpen.CAE.XyFunctionGeneralType@endlink. Usage type of Data Record used .
         - abscissa_type is: @link NXOpen.CAE.AfuData.AbscissaType NXOpen.CAE.AfuData.AbscissaType@endlink. Abscissa specific data type .
         - x_unit is: @link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink. Unit Code of data .
         - ordinate_type is: @link NXOpen.CAE.AfuData.OrdinateType NXOpen.CAE.AfuData.OrdinateType@endlink. Ordinate data type .
         - y_unit is: @link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink. Ordinate Numerator Unit Code of data .
         - y_denominator_unit is: @link NXOpen.CAE.XyFunctionUnit NXOpen.CAE.XyFunctionUnit@endlink. Ordinate Denominator Unit Code of data .
         - sort_value_type is: bool. If want to sort value in x direction .

        """
        pass
    
    ##  Set the adding header flag when export to CSV file 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  If want to add header when export to CSV file 
    @staticmethod
    def SetHeaderFlag(add_header: bool) -> None:
        """
         Set the adding header flag when export to CSV file 
        """
        pass
    
    ##  Set the record options data for the Data Record 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  The name of the Data Record 
    def SetRecordOptionData(record_name: str, function_type: NXOpen.CAE.XyFunctionGeneralType, abscissa_type: NXOpen.CAE.AfuData.AbscissaType, x_unit: NXOpen.CAE.XyFunctionUnit, ordinate_type: NXOpen.CAE.AfuData.OrdinateType, y_unit: NXOpen.CAE.XyFunctionUnit, y_denominator_unit: NXOpen.CAE.XyFunctionUnit, sort_value_type: bool) -> None:
        """
         Set the record options data for the Data Record 
        """
        pass
    
##  Represents a section based matrix record which has real data values.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class RealSectionBasedMatrixRecord(SectionBasedMatrixRecord): 
    """ Represents a section based matrix record which has real data values. """


    ##  Adds the real data values for each section. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  X-Coordinate data 
    def AddSectionData(matrixRecord: RealSectionBasedMatrixRecord, xCoordinatePoints: List[float], yCoordinatePoints: List[float], zCoordinatePoint: float) -> None:
        """
         Adds the real data values for each section. 
        """
        pass
    
    ##  Gets the real data values from specific section. 
    ##  @return A tuple consisting of (xCoordinatePoints, yCoordinatePoints, zCoordinatePoints). 
    ##  - xCoordinatePoints is: List[float]. X-Coordinate data .
    ##  - yCoordinatePoints is: List[float]. Y-Coordinate data .
    ##  - zCoordinatePoints is: float. Z-Coordinate data .

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Section index 
    @staticmethod
    def GetSectionData(matrixRecord: RealSectionBasedMatrixRecord, sectionIndex: int) -> Tuple[List[float], List[float], float]:
        """
         Gets the real data values from specific section. 
         @return A tuple consisting of (xCoordinatePoints, yCoordinatePoints, zCoordinatePoints). 
         - xCoordinatePoints is: List[float]. X-Coordinate data .
         - yCoordinatePoints is: List[float]. Y-Coordinate data .
         - zCoordinatePoints is: float. Z-Coordinate data .

        """
        pass
    
##  Represents a kind of record data could be displayed by 3D graphing.
##             The record is consist of multiple section data and each section
##             data repsresents a 2D record data.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class SectionBasedMatrixRecord(BaseRecord): 
    """ Represents a kind of record data could be displayed by 3D graphing.
            The record is consist of multiple section data and each section
            data repsresents a 2D record data. """


    ## Getter for property: (int) SectionCount
    ##   the section count   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def SectionCount(self) -> int:
        """
        Getter for property: (int) SectionCount
          the section count   
            
         
        """
        pass
    
    ## Getter for property: (str) Title
    ##   the title name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
          the title name   
            
         
        """
        pass
    
    ## Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) XCoordinateUnit
    ##   the X-Coordinate unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return BaseUnit
    @property
    def XCoordinateUnit(self) -> BaseUnit:
        """
        Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) XCoordinateUnit
          the X-Coordinate unit   
            
         
        """
        pass
    
    ## Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) XCoordinateUnit

    ##   the X-Coordinate unit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @XCoordinateUnit.setter
    def XCoordinateUnit(self, xCoordinateUnit: BaseUnit):
        """
        Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) XCoordinateUnit
          the X-Coordinate unit   
            
         
        """
        pass
    
    ## Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) YCoordinateUnit
    ##   the Y-Coordinate unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return BaseUnit
    @property
    def YCoordinateUnit(self) -> BaseUnit:
        """
        Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) YCoordinateUnit
          the Y-Coordinate unit   
            
         
        """
        pass
    
    ## Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) YCoordinateUnit

    ##   the Y-Coordinate unit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @YCoordinateUnit.setter
    def YCoordinateUnit(self, yCoordinateUnit: BaseUnit):
        """
        Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) YCoordinateUnit
          the Y-Coordinate unit   
            
         
        """
        pass
    
    ## Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) ZCoordinateUnit
    ##   the Z-Coordinate unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return BaseUnit
    @property
    def ZCoordinateUnit(self) -> BaseUnit:
        """
        Getter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) ZCoordinateUnit
          the Z-Coordinate unit   
            
         
        """
        pass
    
    ## Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) ZCoordinateUnit

    ##   the Z-Coordinate unit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ZCoordinateUnit.setter
    def ZCoordinateUnit(self, zCoordinateUnit: BaseUnit):
        """
        Setter for property: (@link BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) ZCoordinateUnit
          the Z-Coordinate unit   
            
         
        """
        pass
    
    ##  Removes the data values of the specific section. The section index must be greater than
    ##                 or equal to 0 and less than @link CAE::FTK::SectionBasedMatrixRecord::SectionCount  CAE::FTK::SectionBasedMatrixRecord::SectionCount @endlink . 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Section index 
    def RemoveSectionData(matrixRecord: SectionBasedMatrixRecord, sectionIndex: int) -> None:
        """
         Removes the data values of the specific section. The section index must be greater than
                        or equal to 0 and less than @link CAE::FTK::SectionBasedMatrixRecord::SectionCount  CAE::FTK::SectionBasedMatrixRecord::SectionCount @endlink . 
        """
        pass
    
## @package NXOpen.CAE.FTK
## Classes, Enums and Structs under NXOpen.CAE.FTK namespace

##  @link DataManagerAfuRecordZValue NXOpen.CAE.FTK.DataManagerAfuRecordZValue @endlink is an alias for @link DataManager.AfuRecordZValue NXOpen.CAE.FTK.DataManager.AfuRecordZValue@endlink
DataManagerAfuRecordZValue = DataManager.AfuRecordZValue


##  @link DataManagerFileContainerType NXOpen.CAE.FTK.DataManagerFileContainerType @endlink is an alias for @link DataManager.FileContainerType NXOpen.CAE.FTK.DataManager.FileContainerType@endlink
DataManagerFileContainerType = DataManager.FileContainerType


##  @link ExportFilesParameterHeaderOptions NXOpen.CAE.FTK.ExportFilesParameterHeaderOptions @endlink is an alias for @link ExportFilesParameter.HeaderOptions NXOpen.CAE.FTK.ExportFilesParameter.HeaderOptions@endlink
ExportFilesParameterHeaderOptions = ExportFilesParameter.HeaderOptions


##  @link ExportFilesParameterOverrideOption NXOpen.CAE.FTK.ExportFilesParameterOverrideOption @endlink is an alias for @link ExportFilesParameter.OverrideOption NXOpen.CAE.FTK.ExportFilesParameter.OverrideOption@endlink
ExportFilesParameterOverrideOption = ExportFilesParameter.OverrideOption


