from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AfuFileManager(NXOpen.Object): 
    """  Provides methods to query the loaded AFU files  """
    def DeleteFile(afuFileName: str) -> None:
        """
         Deletes an AFU file 
        """
        pass
    def GetAllRecordNamesInFile(afuFileName: str) -> List[str]:
        """
         Gets all record names in an AFU file which must be loaded 
         Returns recordNames (List[str]): .
        """
        pass
    def GetLoadedFiles() -> List[str]:
        """
         Gets all loaded AFU files 
         Returns afuFileNames (List[str]): .
        """
        pass
    def GetRecord(afuFileName: str, recordName: str) -> BaseRecord:
        """
         Gets an AFU record in an AFU file which must be loaded 
         Returns afuRecord ( BaseRecord NXOpen): .
        """
        pass
    def LoadFile(afuFileName: str, containerType: DataManager.FileContainerType) -> None:
        """
         Loads an AFU file to the specified container.
                        
                        An AFU file can be loaded under associated container, solution result container or user container.
                        The container type indicates under which container the file is loaded.
                        
                     
        """
        pass
    def UnloadFile(afuFileName: str, containerType: DataManager.FileContainerType) -> None:
        """
         Unloads an AFU file from the specified container.
                        
                        An AFU file can be loaded under associated container, solution result container or user container.
                        The container type indicates under which container the file is unloaded.
                        
                     
        """
        pass
class ArrayRecord2DEvenWithZValue(ArrayRecord2DEven): 
    """ Manages the CAE.FTK.ArrayRecord2DEven with Z value """
    @property
    def Unit(self) -> BaseUnit:
        """
        Getter for property: ( BaseUnit NXOpen) Unit
         Returns the Z unit   
            
         
        """
        pass
    @Unit.setter
    def Unit(self, zValueUnit: BaseUnit):
        """
        Setter for property: ( BaseUnit NXOpen) Unit
         Returns the Z unit   
            
         
        """
        pass
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
         Returns the Z value   
            
         
        """
        pass
    @Value.setter
    def Value(self, zValue: float):
        """
        Setter for property: (float) Value
         Returns the Z value   
            
         
        """
        pass
class ArrayRecord2DEven(ArrayRecord2D): 
    """ Manages the 2d array record with even abscissa data """
    def GetEvenComplexData(self) -> Tuple[List[float], float, float, List[float]]:
        """
         Gets even complex data 
         Returns A tuple consisting of (y_coordinate_real, x_minimum, x_increment, y_coordinate_imag). 
         - y_coordinate_real is: List[float]. Real part of Y-Coordinate data .
         - x_minimum is: float. Minimum abscissa data value .
         - x_increment is: float. Abscissa increment .
         - y_coordinate_imag is: List[float]. Imaginary part of Y-Coordinate data .

        """
        pass
    def GetEvenRealData(self) -> Tuple[List[float], float, float]:
        """
         Gets even real data 
         Returns A tuple consisting of (y_coordinate_points, x_minimum, x_increment). 
         - y_coordinate_points is: List[float]. Y-Coordinate data .
         - x_minimum is: float. Minimum abscissa data value .
         - x_increment is: float. Abscissa increment .

        """
        pass
    def SetEvenComplexData(self, x_minimum: float, x_increment: float, y_coordinate_real: List[float], y_coordinate_imag: List[float]) -> None:
        """
         Sets even complex data 
        """
        pass
    def SetEvenRealData(self, x_minimum: float, x_increment: float, y_coordinate_points: List[float]) -> None:
        """
         Sets even real data 
        """
        pass
class ArrayRecord2DWithZValue(ArrayRecord2D): 
    """ Manages the CAE.FTK.ArrayRecord2D with Z value """
    @property
    def Unit(self) -> BaseUnit:
        """
        Getter for property: ( BaseUnit NXOpen) Unit
         Returns the Z unit   
            
         
        """
        pass
    @Unit.setter
    def Unit(self, zValueUnit: BaseUnit):
        """
        Setter for property: ( BaseUnit NXOpen) Unit
         Returns the Z unit   
            
         
        """
        pass
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
         Returns the Z value   
            
         
        """
        pass
    @Value.setter
    def Value(self, zValue: float):
        """
        Setter for property: (float) Value
         Returns the Z value   
            
         
        """
        pass
class ArrayRecord2D(BaseRecord): 
    """ Manages the 2d array record """
    def GetComplexData(self) -> Tuple[List[float], List[float], List[float]]:
        """
         Gets complex points data 
         Returns A tuple consisting of (x_coordinate_points, y_coordinate_real, y_coordinate_imag). 
         - x_coordinate_points is: List[float]. X-Coordinate data .
         - y_coordinate_real is: List[float]. Real part of Y-Coordinate data .
         - y_coordinate_imag is: List[float]. Imaginary part of Y-Coordinate data .

        """
        pass
    def GetRealData(self) -> Tuple[List[float], List[float]]:
        """
         Gets real points data 
         Returns A tuple consisting of (x_coordinate_points, y_coordinate_points). 
         - x_coordinate_points is: List[float]. X-Coordinate data .
         - y_coordinate_points is: List[float]. Y-Coordinate data .

        """
        pass
    def GetTitle(self) -> str:
        """
         Gets the title 
         Returns title (str): .
        """
        pass
    def GetXCoordinateUnit(self) -> BaseUnit:
        """
         Gets X-Coordinate unit 
         Returns x_coordinate_unit ( BaseUnit NXOpen):  X-Coordinate unit .
        """
        pass
    def GetYCoordinateUnit(self) -> BaseUnit:
        """
         Gets Y-Coordinate unit 
         Returns y_coordinate_unit ( BaseUnit NXOpen):  Y-Coordinate unit .
        """
        pass
    def SetComplexData(self, x_coordinate_points: List[float], y_coordinate_real: List[float], y_coordinate_imag: List[float]) -> None:
        """
         Sets complex points data 
        """
        pass
    def SetPointLabels(self, pointLabels: List[str]) -> None:
        """
         Sets the point labels 
        """
        pass
    def SetRealData(self, x_coordinate_points: List[float], y_coordinate_points: List[float]) -> None:
        """
         Sets real points data 
        """
        pass
    def SetXCoordinateUnit(self, x_coordinate_unit: BaseUnit) -> None:
        """
         Sets X-Coordinate unit 
        """
        pass
    def SetYCoordinateUnit(self, y_coordinate_unit: BaseUnit) -> None:
        """
         Sets Y-Coordinate unit 
        """
        pass
class ArrayRecord3D(ArrayRecord2D): 
    """ Manages the 3d array record """
    def EditZCoordinateUnit(self, measureOrQuantityName: str, unitName: str) -> None:
        """
         Edits Z-Coordinate units.
                        If the input units are different with the old units, the units are updated with new ones, and the data are also converted to new units.
                        
                        At least one of names must be provided.
                        
                        
                        If the units is a Unitless related measure or quantity, measure name or quantity name must be provided, unit type name is not needed.
                        
                        
                        If the units is a measure but not a Unitless related measure, measure name is optional, unit type name must be provided.
                        
                        
                        If the units is a quantity but not a Unitless related quantity, both quantity name and unit type name must be provided.
                        
                        
                        
                    
        """
        pass
    def GetZCoordinateUnit(self) -> BaseUnit:
        """
         Gets Z-Coordinate unit 
         Returns z_coordinate_unit ( BaseUnit NXOpen):  Z-Coordinate unit .
        """
        pass
    def SetZCoordinatePoints(self, z_coordinate_points: List[float]) -> None:
        """
         Sets Z-Coordinate points 
        """
        pass
    def SetZCoordinateUnit(self, z_coordinate_unit: BaseUnit) -> None:
        """
         Sets Z-Coordinate unit 
        """
        pass
import NXOpen
class BaseRecord(NXOpen.NXObject): 
    """ Manages the base record. """
    @property
    def LegendName(self) -> str:
        """
        Getter for property: (str) LegendName
         Returns the legend name   
            
         
        """
        pass
    @property
    def ResultInformation(self) -> str:
        """
        Getter for property: (str) ResultInformation
         Returns the result information of a record  
            
         
        """
        pass
    @ResultInformation.setter
    def ResultInformation(self, resultInformation: str):
        """
        Setter for property: (str) ResultInformation
         Returns the result information of a record  
            
         
        """
        pass
    def GetAbscissaUnit(self) -> BaseUnit:
        """
         Gets the abscissa unit 
         Returns abscissaUnit ( BaseUnit NXOpen): .
        """
        pass
    def GetDescription(self) -> List[str]:
        """
         Gets the description 
         Returns description (List[str]): .
        """
        pass
    def GetOrdinateUnit(self) -> BaseUnit:
        """
         Gets the ordinate unit 
         Returns ordinateUnit ( BaseUnit NXOpen): .
        """
        pass
    def GetPointLabels(self) -> List[str]:
        """
         Gets the point labels 
         Returns pointLabels (List[str]): .
        """
        pass
    def SetDescription(self, description: List[str]) -> None:
        """
         Sets the description 
        """
        pass
import NXOpen
class BaseUnit(NXOpen.NXObject): 
    """ Manages the base unit """
    def GetConstituentUnit(self, nthConstituentUnitIndex: int) -> BaseUnit:
        """
         Gets constituent unit by index
         Returns constituentUnit ( BaseUnit NXOpen):  constituent unit .
        """
        pass
    def GetConstituentUnitsCount(self) -> int:
        """
         Gets the count of constituent units 
         Returns constituentUnitsCount (int):  constituent units count .
        """
        pass
    def SetMeasureName(self, measure_name: str) -> None:
        """
         Sets measure name 
        """
        pass
    def SetNxUnit(self, nxUnit: NXOpen.Unit) -> None:
        """
         Sets nx unit.
                    
                        To make sure the base unit could be changed successfully,two conditions must be satisfied:
                    
                        The measure of input nx unit must be same as the nx unit saved in BaseUnit.
                        The BaseUnit must be created by method CAE.FTK.DataManager.CreateArrayUnit,but except for the method which creates
                            unit by numerator and denominator unit.
                    
                    
        """
        pass
    def SetUnitName(self, unit_name: str) -> None:
        """
         Sets unit name 
        """
        pass
class ComplexSectionBasedMatrixRecord(SectionBasedMatrixRecord): 
    """ Represents a section based matrix record which has complex data values. """
    def AddSectionData(self, xCoordinatePoints: List[float], yCoordinateReal: List[float], yCoordinateImag: List[float], zCoordinatePoint: float) -> None:
        """
         Adds the complex data values for each section. 
        """
        pass
    def GetSectionData(self, sectionIndex: int) -> Tuple[List[float], List[float], List[float], float]:
        """
         Gets the complex data values from specific section. 
         Returns A tuple consisting of (xCoordinatePoints, yCoordinateReal, yCoordinateImag, zCoordinatePoints). 
         - xCoordinatePoints is: List[float]. X-Coordinate data .
         - yCoordinateReal is: List[float]. Real part of Y-Coordinate data .
         - yCoordinateImag is: List[float]. Imaginary part of Y-Coordinate data .
         - zCoordinatePoints is: float. Z-Coordinate data .

        """
        pass
import NXOpen
class DataManager(NXOpen.Object): 
    """ Ftk data manager """
    class AfuRecordZValue(Enum):
        """
        Members Include: 
         |SelectionOrder|  The Z value is selection order 
         |General|  The Z value is attribute of General field in an afu record  
         |Rpm|  The z value is attribute of RPM field in an afu record 
         |Time|  The z value is attribute of Time field in an afu record 
         |Order|  The z value is attribute of Order field in an afu record 

        """
        SelectionOrder: int
        General: int
        Rpm: int
        Time: int
        Order: int
        @staticmethod
        def ValueOf(value: int) -> DataManager.AfuRecordZValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FileContainerType(Enum):
        """
        Members Include: 
         |NotSet|  Not any container 
         |AssociatedContainer|  Part associated container which has the same simple name with the part 
         |ResultContainer|  Solution result container which has the same name with the solution 
         |UserContainer|  User container 
         |All|  All containers 

        """
        NotSet: int
        AssociatedContainer: int
        ResultContainer: int
        UserContainer: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> DataManager.FileContainerType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AfuFileManager() -> AfuFileManager:
        """
         Returns the  NXOpen::CAE::FTK::AfuFileManager  belonging to FTK data manager 
        """
        pass
    @property
    def Op2FileManager() -> Op2FileManager:
        """
         Returns the  NXOpen::CAE::FTK::Op2FileManager  belonging to FTK data manager 
        """
        pass
    def CreateArrayRecord2d(title_name: str, legend_name: str, num_points: int) -> ArrayRecord2D:
        """
         Creates 2d array record 
         Returns array_record ( ArrayRecord2D NXOpen):  2D array record .
        """
        pass
    def CreateArrayRecord2dEvenSpacing(title_name: str, legend_name: str) -> ArrayRecord2DEven:
        """
         Creates 2d array record with even spacing 
         Returns array_record ( ArrayRecord2DEven NXOpen):  2D even array record .
        """
        pass
    def CreateArrayRecord2dEvenSpacingWithZValue(titleName: str, legendName: str) -> ArrayRecord2DEvenWithZValue:
        """
         Creates 2d array record with even spacing and data attributes 
         Returns arrayRecord ( ArrayRecord2DEvenWithZValue NXOpen):  2D array record with even spacing and data attributes .
        """
        pass
    def CreateArrayRecord2dWithZValue(titleName: str, legendName: str, numPoints: int) -> ArrayRecord2DWithZValue:
        """
         Creates 2d array record with data attributes 
         Returns arrayRecord ( ArrayRecord2DWithZValue NXOpen):  2D array record with data attributes .
        """
        pass
    def CreateArrayRecord3d(title_name: str, legend_name: str, num_points: int) -> ArrayRecord3D:
        """
         Creates 3d array record 
         Returns array_record ( ArrayRecord3D NXOpen):  3D array record .
        """
        pass
    @overload
    def CreateArrayUnit(nx_unit: NXOpen.Unit) -> BaseUnit:
        """
         Creates array unit by nx system unit 
         Returns array_unit ( BaseUnit NXOpen):  Array unit .
        """
        pass
    @overload
    def CreateArrayUnit(nxUnit: NXOpen.Unit, aliasMeasureName: str, localizedAliasMeasureName: str) -> BaseUnit:
        """
          Creates the object NXOpen.CAE.FTK.BaseUnit by NXOpen.Unit
                    with alias measure name and localized alias measure name. 
                    
                    Please use the method NXOpen.CAE.FTK.DataManager.CreateArrayUnit which has two arguments
                    if alias measure name is not needed.
                    
                    
         Returns arrayUnit ( BaseUnit NXOpen): .
        """
        pass
    @overload
    def CreateArrayUnit(numerator_unit: BaseUnit, denominator_unit: BaseUnit) -> BaseUnit:
        """
         Creates array unit by numerator and denominator unit 
         Returns array_unit ( BaseUnit NXOpen):  Array unit .
        """
        pass
    def CreateComplexMatrixRecord(title_name: str, legend_name: str) -> ComplexSectionBasedMatrixRecord:
        """
         Creates an empty complex matrix record which section data is complex data. 
         Returns matrix_record ( ComplexSectionBasedMatrixRecord NXOpen):  Complex matrix record .
        """
        pass
    def CreateMatrixPlotRecord(titleName: str, legendName: str) -> MatrixPlotRecord:
        """
         Creates an empty record for matrix plot. 
         Returns pMatrixPlotRecord ( MatrixPlotRecord NXOpen): .
        """
        pass
    def CreateRealMatrixRecord(title_name: str, legend_name: str) -> RealSectionBasedMatrixRecord:
        """
         Creates an empty real matrix record which section data is real data. 
         Returns matrix_record ( RealSectionBasedMatrixRecord NXOpen):  Real matrix record .
        """
        pass
    def CreateUnitlessUnit(measureName: str, localizedMeasureName: str) -> BaseUnit:
        """
         Creates unitless unit 
         Returns arrayUnit ( BaseUnit NXOpen): .
        """
        pass
    def DeleteArrayUnit(deleted_unit: BaseUnit) -> None:
        """
         Deletes array unit 
        """
        pass
    def DeleteRecord(deleted_record: BaseRecord) -> None:
        """
         Deletes record 
        """
        pass
import NXOpen
import NXOpen.CAE
class ExportFilesParameter(NXOpen.TransientObject): 
    """ Represents the parameter settings for exporting data to external files. """
    class HeaderOptions(Enum):
        """
        Members Include: 
         |FileDescription| 
         |General| 
         |Abscissa| 
         |Ordinate| 
         |AbscissaZ| 
         |ApplicationSpecific| 

        """
        FileDescription: int
        General: int
        Abscissa: int
        Ordinate: int
        AbscissaZ: int
        ApplicationSpecific: int
        @staticmethod
        def ValueOf(value: int) -> ExportFilesParameter.HeaderOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OverrideOption(Enum):
        """
        Members Include: 
         |Rename|  Rename the file name with number postfix, like A - A1 
         |Append|  Append data to the end of the given file 
         |Replace|  Replace the whole data in the given file 
         |Skip|  Skip to write data 

        """
        Rename: int
        Append: int
        Replace: int
        Skip: int
        @staticmethod
        def ValueOf(value: int) -> ExportFilesParameter.OverrideOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IsHeaderExportRequired(self) -> bool:
        """
        Getter for property: (bool) IsHeaderExportRequired
         Returns the full header print required.  
           If the setting is true, all header options are required for export.   
         
        """
        pass
    @IsHeaderExportRequired.setter
    def IsHeaderExportRequired(self, hasHeader: bool):
        """
        Setter for property: (bool) IsHeaderExportRequired
         Returns the full header print required.  
           If the setting is true, all header options are required for export.   
         
        """
        pass
    @property
    def NumberFormat(self) -> NXOpen.CAE.NumberFormat:
        """
        Getter for property: ( NXOpen.CAE.NumberFormat) NumberFormat
         Returns the number format options.  
          
                    
                    The NumberFormat object will be deleted along with the file parameter object.
                    
                      
         
        """
        pass
    @property
    def OverrideSetting(self) -> ExportFilesParameter.OverrideOption:
        """
        Getter for property: ( ExportFilesParameter.OverrideOption NXOpen) OverrideSetting
         Returns the file override option   
            
         
        """
        pass
    @OverrideSetting.setter
    def OverrideSetting(self, overrideOption: ExportFilesParameter.OverrideOption):
        """
        Setter for property: ( ExportFilesParameter.OverrideOption NXOpen) OverrideSetting
         Returns the file override option   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object 
        """
        pass
    def GetCustomRecordNames(self) -> List[str]:
        """
         Gets the custom record names for export 
         Returns customRecordNames (List[str]): .
        """
        pass
    def GetFileNames(self) -> List[str]:
        """
         Gets the external files for export 
         Returns fileNames (List[str]): .
        """
        pass
    def GetIsCertainHeaderExportRequired(self, whichHeader: ExportFilesParameter.HeaderOptions) -> bool:
        """
         Asks whether to export the specified header option 
         Returns required (bool): .
        """
        pass
    def SetCustomRecordNames(self, customRecordNames: List[str]) -> None:
        """
         Sets the custom record names for export 
        """
        pass
    def SetFileNames(self, fileNames: List[str]) -> None:
        """
         Sets the external files for export 
        """
        pass
    def SetIsCertainHeaderExportRequired(self, whichHeader: ExportFilesParameter.HeaderOptions, required: bool) -> None:
        """
         Sets whether or not a specific header is required 
        """
        pass
import NXOpen
class FTKManager(NXOpen.Object): 
    """ FTK function data manager """
    @property
    def OptionSetting() -> OptionSetting:
        """
         Returns the  NXOpen::CAE::FTK::OptionSetting  belonging to this session 
        """
        pass
import NXOpen
class IApplicationDataOwner(NXOpen.Object): 
    """ Represents the interface for  application specific data owner"""
    @abstractmethod
    def GetApplicationData(self) -> IApplicationData:
        """
         Gets the application specific data associated with the record 
         Returns applicationData ( IApplicationData NXOpen): .
        """
        pass
    @abstractmethod
    def SetApplicationData(self, applicationData: IApplicationData) -> None:
        """
         Sets the application specific data to the record 
        """
        pass
import NXOpen
class IApplicationData(NXOpen.Object): 
    """ Represents the interface for  application specific data class"""
    @abstractmethod
    def AskNthDisplayableAttributeName(self, nth: int) -> str:
        """
         Asks the name of a displayable attribute 
         Returns attributeName (str): .
        """
        pass
    @abstractmethod
    def AskNthDisplayableAttributeValue(self, nth: int) -> str:
        """
         Asks the value of a displayable attribute 
         Returns attributeValue (str): .
        """
        pass
    @abstractmethod
    def AskNumberOfDisplayableAttributes(self) -> int:
        """
         Asks the count of attributes which could be showed on legend table 
         Returns count (int): .
        """
        pass
import NXOpen
class IRecordWithZValue(NXOpen.Object): 
    """ Represents the interface for a record with Z value"""
    @property
    @abstractmethod
    def Unit(self) -> BaseUnit:
        """
        Getter for property: ( BaseUnit NXOpen) Unit
         Returns the Z unit   
            
         
        """
        pass
    @Unit.setter
    def Unit(self, zValueUnit: BaseUnit):
        """
        Setter for property: ( BaseUnit NXOpen) Unit
         Returns the Z unit   
            
         
        """
        pass
    @property
    @abstractmethod
    def Value(self) -> float:
        """
        Getter for property: (float) Value
         Returns the Z value   
            
         
        """
        pass
    @Value.setter
    def Value(self, zValue: float):
        """
        Setter for property: (float) Value
         Returns the Z value   
            
         
        """
        pass
class MatrixPlotRecord(BaseRecord): 
    """ Represents record data for matrix plot. """
    @property
    def DataUnit(self) -> BaseUnit:
        """
        Getter for property: ( BaseUnit NXOpen) DataUnit
         Returns the data unit   
            
         
        """
        pass
    @DataUnit.setter
    def DataUnit(self, pDataUnit: BaseUnit):
        """
        Setter for property: ( BaseUnit NXOpen) DataUnit
         Returns the data unit   
            
         
        """
        pass
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the title name   
            
         
        """
        pass
    @Title.setter
    def Title(self, titleName: str):
        """
        Setter for property: (str) Title
         Returns the title name   
            
         
        """
        pass
    def GetColumnCount(self) -> int:
        """
         Gets the column count 
         Returns numColumns (int): .
        """
        pass
    def GetColumnLabels(self) -> List[str]:
        """
         Gets the column labels 
         Returns columnLabels (List[str]): .
        """
        pass
    def GetData(self) -> Tuple[List[float], List[float]]:
        """
          Gets real or complex data. 
                    
                        To get real data, the parameter realData will be filled, but the parameter imagData will be empty.
                        To get complex data, both the parameters realData and imagData will all be filled.
                    
                    
         Returns A tuple consisting of (realData, imagData). 
         - realData is: List[float]. Real part of data .
         - imagData is: List[float]. Imaginary part data .

        """
        pass
    def GetRowCount(self) -> int:
        """
         Gets the row count 
         Returns numRows (int): .
        """
        pass
    def GetRowLabels(self) -> List[str]:
        """
         Gets the row labels 
         Returns rowLabels (List[str]): .
        """
        pass
    def SetColumnLabels(self, columnLabels: List[str]) -> None:
        """
         Sets the column labels 
        """
        pass
    def SetData(self, realData: List[float], imagData: List[float]) -> None:
        """
          Sets real or complex data. 
                    
                        To set real data, the parameter realData must be given, but the parameter imagData can be empty.
                        To set complex data, both the parameters realData and imagData must be given.
                    
                    
        """
        pass
    def SetRowLabels(self, rowLabels: List[str]) -> None:
        """
         Sets the row labels 
        """
        pass
import NXOpen
class Op2FileManager(NXOpen.Object): 
    """  Provides methods to query the loaded OP2 files and 
            export the records in the OP2 file to specified AFU file  """
    def DeleteFile(op2FileName: str) -> None:
        """
         Deletes an OP2 file 
        """
        pass
    def ExportOp2RecordsToAfuFile(op2Record: List[Op2Record], afuFileName: str) -> None:
        """
         Exports Op2 records to Afu file. 
        """
        pass
    def ExportRecordsOfOp2DatasetToAfuFile(op2FileName: str, datasetsNames: List[str], afuFileName: str) -> None:
        """
          Exports the records of OP2 Datasets to an AFU file 
        """
        pass
    def ExportRecordsOfOp2FileToAfuFile(op2FileName: str, afuFileName: str) -> None:
        """
          Exports the records of an OP2 file to an AFU file 
        """
        pass
    def GetAllDatasetNamesInFile(op2FileName: str) -> List[str]:
        """
         Gets all dataset names in an OP2 file which must be loaded 
         Returns datasetNames (List[str]): .
        """
        pass
    def GetAllRecordNamesInDataset(op2FileName: str, datasetName: str) -> List[str]:
        """
         Gets all record names in an OP2 dataset of an OP2 file which must be loaded 
         Returns recordNames (List[str]): .
        """
        pass
    def GetLoadedFiles() -> List[str]:
        """
         Gets all loaded OP2 files 
         Returns op2FileNames (List[str]): .
        """
        pass
    def GetRecord(op2FileName: str, datasetName: str, recordName: str) -> Op2Record:
        """
         Gets an OP2 record in an OP2 dataset of an OP2 file which must be loaded 
         Returns op2Record ( Op2Record NXOpen): .
        """
        pass
    def LoadFile(op2FileName: str, containerType: DataManager.FileContainerType) -> None:
        """
         Loads an OP2 file to the specified container.
                        
                        An OP2 file can be loaded under associated container, solution result container or user container.
                        The container type indicates under which container the file is loaded.
                        
                     
        """
        pass
    def UnloadFile(op2FileName: str, containerType: DataManager.FileContainerType) -> None:
        """
         Unloads an OP2 file from the specified container.
                        
                        An OP2 file can be loaded under associated container, solution result container or user container.
                        The container type indicates under which container the file is unloaded.
                        
                     
        """
        pass
class Op2Record(BaseRecord): 
    """ Represents the op2 record data """
    def CalculateRMSOfPSD(self) -> float:
        """
         Calculates the RMS value for the PSD Record. 
                        Error is returned if the input record is not a Power Spectral Density (PSD) record.
         Returns rmsValue (float): .
        """
        pass
    def ListInformation(self, fileName: str, listInfo: bool, listData: bool) -> None:
        """
         Lists the record information to a file or listing information window 
        """
        pass
import NXOpen
import NXOpen.CAE
class OptionSetting(NXOpen.Object): 
    """ Manager the options data for Data Record """
    @property
    def AbscissaSpacingType(self) -> NXOpen.CAE.AfuData.AbscissaType:
        """
        Getter for property: ( NXOpen.CAE.AfuData.AbscissaType) AbscissaSpacingType
         Returns the abscissa spacing type   
            
         
        """
        pass
    @AbscissaSpacingType.setter
    def AbscissaSpacingType(self, abscissa_type: NXOpen.CAE.AfuData.AbscissaType):
        """
        Setter for property: ( NXOpen.CAE.AfuData.AbscissaType) AbscissaSpacingType
         Returns the abscissa spacing type   
            
         
        """
        pass
    @property
    def AbscissaUnit(self) -> NXOpen.CAE.XyFunctionUnit:
        """
        Getter for property: ( NXOpen.CAE.XyFunctionUnit) AbscissaUnit
         Returns the abscissa unit   
            
         
        """
        pass
    @AbscissaUnit.setter
    def AbscissaUnit(self, x_unit: NXOpen.CAE.XyFunctionUnit):
        """
        Setter for property: ( NXOpen.CAE.XyFunctionUnit) AbscissaUnit
         Returns the abscissa unit   
            
         
        """
        pass
    @property
    def FunctionType(self) -> NXOpen.CAE.XyFunctionGeneralType:
        """
        Getter for property: ( NXOpen.CAE.XyFunctionGeneralType) FunctionType
         Returns the function type   
            
         
        """
        pass
    @FunctionType.setter
    def FunctionType(self, function_type: NXOpen.CAE.XyFunctionGeneralType):
        """
        Setter for property: ( NXOpen.CAE.XyFunctionGeneralType) FunctionType
         Returns the function type   
            
         
        """
        pass
    @property
    def OrdinateDataType(self) -> NXOpen.CAE.AfuData.OrdinateType:
        """
        Getter for property: ( NXOpen.CAE.AfuData.OrdinateType) OrdinateDataType
         Returns the ordinate data type   
            
         
        """
        pass
    @OrdinateDataType.setter
    def OrdinateDataType(self, ordinate_type: NXOpen.CAE.AfuData.OrdinateType):
        """
        Setter for property: ( NXOpen.CAE.AfuData.OrdinateType) OrdinateDataType
         Returns the ordinate data type   
            
         
        """
        pass
    @property
    def OrdinateDenominatorUnit(self) -> NXOpen.CAE.XyFunctionUnit:
        """
        Getter for property: ( NXOpen.CAE.XyFunctionUnit) OrdinateDenominatorUnit
         Returns the ordinate denominator unit   
            
         
        """
        pass
    @OrdinateDenominatorUnit.setter
    def OrdinateDenominatorUnit(self, y_denominator_unit: NXOpen.CAE.XyFunctionUnit):
        """
        Setter for property: ( NXOpen.CAE.XyFunctionUnit) OrdinateDenominatorUnit
         Returns the ordinate denominator unit   
            
         
        """
        pass
    @property
    def OrdinateSecondNumeratorUnit(self) -> NXOpen.CAE.XyFunctionUnit:
        """
        Getter for property: ( NXOpen.CAE.XyFunctionUnit) OrdinateSecondNumeratorUnit
         Returns the ordinate second numerator unit   
            
         
        """
        pass
    @OrdinateSecondNumeratorUnit.setter
    def OrdinateSecondNumeratorUnit(self, y_second_numerator_unit: NXOpen.CAE.XyFunctionUnit):
        """
        Setter for property: ( NXOpen.CAE.XyFunctionUnit) OrdinateSecondNumeratorUnit
         Returns the ordinate second numerator unit   
            
         
        """
        pass
    @property
    def OrdinateUnit(self) -> NXOpen.CAE.XyFunctionUnit:
        """
        Getter for property: ( NXOpen.CAE.XyFunctionUnit) OrdinateUnit
         Returns the ordinate unit   
            
         
        """
        pass
    @OrdinateUnit.setter
    def OrdinateUnit(self, y_unit: NXOpen.CAE.XyFunctionUnit):
        """
        Setter for property: ( NXOpen.CAE.XyFunctionUnit) OrdinateUnit
         Returns the ordinate unit   
            
         
        """
        pass
    @property
    def RecordName(self) -> str:
        """
        Getter for property: (str) RecordName
         Returns the record name   
            
         
        """
        pass
    @RecordName.setter
    def RecordName(self, record_name: str):
        """
        Setter for property: (str) RecordName
         Returns the record name   
            
         
        """
        pass
    @property
    def SortValueType(self) -> bool:
        """
        Getter for property: (bool) SortValueType
         Returns the sort value flag.  
          
                    Sorts the values in X direction when it is true. This option is only applicable for real only data.   
         
        """
        pass
    @SortValueType.setter
    def SortValueType(self, sort_value_type: bool):
        """
        Setter for property: (bool) SortValueType
         Returns the sort value flag.  
          
                    Sorts the values in X direction when it is true. This option is only applicable for real only data.   
         
        """
        pass
    def GetHeaderFlag() -> bool:
        """
         Get the adding header flag when export to CSV file 
         Returns add_header (bool):  If want to add header when export to CSV file .
        """
        pass
    def GetRecordOptionData() -> Tuple[str, NXOpen.CAE.XyFunctionGeneralType, NXOpen.CAE.AfuData.AbscissaType, NXOpen.CAE.XyFunctionUnit, NXOpen.CAE.AfuData.OrdinateType, NXOpen.CAE.XyFunctionUnit, NXOpen.CAE.XyFunctionUnit, bool]:
        """
         Get the record options data for the Data Record 
         Returns A tuple consisting of (record_name, function_type, abscissa_type, x_unit, ordinate_type, y_unit, y_denominator_unit, sort_value_type). 
         - record_name is: str. The name of the Data Record .
         - function_type is:  NXOpen.CAE.XyFunctionGeneralType. Usage type of Data Record used .
         - abscissa_type is:  NXOpen.CAE.AfuData.AbscissaType. Abscissa specific data type .
         - x_unit is:  NXOpen.CAE.XyFunctionUnit. Unit Code of data .
         - ordinate_type is:  NXOpen.CAE.AfuData.OrdinateType. Ordinate data type .
         - y_unit is:  NXOpen.CAE.XyFunctionUnit. Ordinate Numerator Unit Code of data .
         - y_denominator_unit is:  NXOpen.CAE.XyFunctionUnit. Ordinate Denominator Unit Code of data .
         - sort_value_type is: bool. If want to sort value in x direction .

        """
        pass
    def SetHeaderFlag(add_header: bool) -> None:
        """
         Set the adding header flag when export to CSV file 
        """
        pass
    def SetRecordOptionData(record_name: str, function_type: NXOpen.CAE.XyFunctionGeneralType, abscissa_type: NXOpen.CAE.AfuData.AbscissaType, x_unit: NXOpen.CAE.XyFunctionUnit, ordinate_type: NXOpen.CAE.AfuData.OrdinateType, y_unit: NXOpen.CAE.XyFunctionUnit, y_denominator_unit: NXOpen.CAE.XyFunctionUnit, sort_value_type: bool) -> None:
        """
         Set the record options data for the Data Record 
        """
        pass
class RealSectionBasedMatrixRecord(SectionBasedMatrixRecord): 
    """ Represents a section based matrix record which has real data values. """
    def AddSectionData(self, xCoordinatePoints: List[float], yCoordinatePoints: List[float], zCoordinatePoint: float) -> None:
        """
         Adds the real data values for each section. 
        """
        pass
    def GetSectionData(self, sectionIndex: int) -> Tuple[List[float], List[float], float]:
        """
         Gets the real data values from specific section. 
         Returns A tuple consisting of (xCoordinatePoints, yCoordinatePoints, zCoordinatePoints). 
         - xCoordinatePoints is: List[float]. X-Coordinate data .
         - yCoordinatePoints is: List[float]. Y-Coordinate data .
         - zCoordinatePoints is: float. Z-Coordinate data .

        """
        pass
class SectionBasedMatrixRecord(BaseRecord): 
    """ Represents a kind of record data could be displayed by 3D graphing.
            The record is consist of multiple section data and each section
            data repsresents a 2D record data. """
    @property
    def SectionCount(self) -> int:
        """
        Getter for property: (int) SectionCount
         Returns the section count   
            
         
        """
        pass
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the title name   
            
         
        """
        pass
    @property
    def XCoordinateUnit(self) -> BaseUnit:
        """
        Getter for property: ( BaseUnit NXOpen) XCoordinateUnit
         Returns the X-Coordinate unit   
            
         
        """
        pass
    @XCoordinateUnit.setter
    def XCoordinateUnit(self, xCoordinateUnit: BaseUnit):
        """
        Setter for property: ( BaseUnit NXOpen) XCoordinateUnit
         Returns the X-Coordinate unit   
            
         
        """
        pass
    @property
    def YCoordinateUnit(self) -> BaseUnit:
        """
        Getter for property: ( BaseUnit NXOpen) YCoordinateUnit
         Returns the Y-Coordinate unit   
            
         
        """
        pass
    @YCoordinateUnit.setter
    def YCoordinateUnit(self, yCoordinateUnit: BaseUnit):
        """
        Setter for property: ( BaseUnit NXOpen) YCoordinateUnit
         Returns the Y-Coordinate unit   
            
         
        """
        pass
    @property
    def ZCoordinateUnit(self) -> BaseUnit:
        """
        Getter for property: ( BaseUnit NXOpen) ZCoordinateUnit
         Returns the Z-Coordinate unit   
            
         
        """
        pass
    @ZCoordinateUnit.setter
    def ZCoordinateUnit(self, zCoordinateUnit: BaseUnit):
        """
        Setter for property: ( BaseUnit NXOpen) ZCoordinateUnit
         Returns the Z-Coordinate unit   
            
         
        """
        pass
    def RemoveSectionData(self, sectionIndex: int) -> None:
        """
         Removes the data values of the specific section. The section index must be greater than
                        or equal to 0 and less than CAE.FTK.SectionBasedMatrixRecord.SectionCount . 
        """
        pass
