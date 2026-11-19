from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Bearing Coefficients Import for Rotor Dynamics  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class BearingCoefficientsImport(NXOpen.Object): 
    """ Bearing Coefficients Import for Rotor Dynamics """


    ##  Bearing Coefficients Import 
    ##  @return A tuple consisting of (errorText, warningText). 
    ##  - errorText is: List[str].
    ##  - warningText is: List[str].

    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="csvFile"> (str) </param>
    ## <param name="bearingType"> (int) </param>
    ## <param name="unit"> (int) </param>
    def Apply(csvFile: str, bearingType: int, unit: int) -> Tuple[List[str], List[str]]:
        """
         Bearing Coefficients Import 
         @return A tuple consisting of (errorText, warningText). 
         - errorText is: List[str].
         - warningText is: List[str].

        """
        pass
    
import NXOpen
##  Energy Tables Display for Rotor Dynamics  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class EnergyTables(NXOpen.Object): 
    """ Energy Tables Display for Rotor Dynamics """


    ##  Energy Tables: Display on the Information Window 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="csvFile"> (str) </param>
    def Apply(csvFile: str) -> None:
        """
         Energy Tables: Display on the Information Window 
        """
        pass
    
import NXOpen
##  Results Merge for Rotor Dynamics  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Merge(NXOpen.Object): 
    """ Results Merge for Rotor Dynamics """


    ##  Merge the Results 
    ##  @return problemOut (str): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="u18Names"> (List[str]) </param>
    ## <param name="zoneValue"> (float) </param>
    ## <param name="executableFolderChoice"> (bool) </param>
    ## <param name="executableFolder"> (str) </param>
    ## <param name="configVar"> (str) </param>
    ## <param name="outputName"> (str) </param>
    def CompleteMerge(u18Names: List[str], zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, outputName: str) -> str:
        """
         Merge the Results 
         @return problemOut (str): .
        """
        pass
    
    ##  Merge the Results 
    ##  @return problemOut (str): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="u18Names"> (List[str]) </param>
    ## <param name="zoneValue"> (float) </param>
    ## <param name="executableFolderChoice"> (bool) </param>
    ## <param name="theAskQualification"> (bool) </param>
    ## <param name="executableFolder"> (str) </param>
    ## <param name="configVar"> (str) </param>
    ## <param name="outputName"> (str) </param>
    def CompleteMerge2(u18Names: List[str], zoneValue: float, executableFolderChoice: bool, theAskQualification: bool, executableFolder: str, configVar: str, outputName: str) -> str:
        """
         Merge the Results 
         @return problemOut (str): .
        """
        pass
    
import NXOpen
##  Cyclic Symmetry Recombination for Rotor Dynamics  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class RecombineAndMerge(NXOpen.Object): 
    """ Cyclic Symmetry Recombination for Rotor Dynamics """


    ##  Cyclic Symmetry: Merge the Results 2D-3D 
    ##  @return problemOut (str): .
    ## 
    ##   <br>  Created in NX1957.0.0  <br> 

    ## License requirements: None.
    ## <param name="isMergeOnly"> (bool) </param>
    ## <param name="u18"> (str) </param>
    ## <param name="zoneValue"> (float) </param>
    ## <param name="executableFolderChoice"> (bool) </param>
    ## <param name="executableFolder"> (str) </param>
    ## <param name="configVar"> (str) </param>
    ## <param name="problemIn"> (str) </param>
    def CompleteMerge(isMergeOnly: bool, u18: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, problemIn: str) -> str:
        """
         Cyclic Symmetry: Merge the Results 2D-3D 
         @return problemOut (str): .
        """
        pass
    
    ##  Cyclic Symmetry: Merge the Results 2D-3D 
    ##  @return problemOut (str): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="isMergeOnly"> (bool) </param>
    ## <param name="u18"> (str) </param>
    ## <param name="zoneValue"> (float) </param>
    ## <param name="executableFolderChoice"> (bool) </param>
    ## <param name="executableFolder"> (str) </param>
    ## <param name="configVar"> (str) </param>
    ## <param name="problemIn"> (str) </param>
    ## <param name="theAskQualification"> (bool) </param>
    def CompleteMerge2(isMergeOnly: bool, u18: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, problemIn: str, theAskQualification: bool) -> str:
        """
         Cyclic Symmetry: Merge the Results 2D-3D 
         @return problemOut (str): .
        """
        pass
    
    ##  Cyclic Symmetry: Get References 
    ##  @return A tuple consisting of (refList, isDoubleAnalysis, nalg, afterRecovery, ref2ListFirstColumn, ref2ListSecondColumn). 
    ##  - refList is: List[str].
    ##  - isDoubleAnalysis is: bool.
    ##  - nalg is: int.
    ##  - afterRecovery is: bool.
    ##  - ref2ListFirstColumn is: List[str].
    ##  - ref2ListSecondColumn is: List[str].

    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## <param name="resultSEUseFile"> (str) </param>
    ## <param name="samZone"> (int) </param>
    def GetReferences(resultSEUseFile: str, samZone: int) -> Tuple[List[str], bool, int, bool, List[str], List[str]]:
        """
         Cyclic Symmetry: Get References 
         @return A tuple consisting of (refList, isDoubleAnalysis, nalg, afterRecovery, ref2ListFirstColumn, ref2ListSecondColumn). 
         - refList is: List[str].
         - isDoubleAnalysis is: bool.
         - nalg is: int.
         - afterRecovery is: bool.
         - ref2ListFirstColumn is: List[str].
         - ref2ListSecondColumn is: List[str].

        """
        pass
    
    ##  Cyclic Symmetry: Merge the Results 2D-3D 
    ##  @return problem (str): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="isMergeOnly"> (bool) </param>
    ## <param name="u18"> (str) </param>
    ## <param name="zoneValue"> (float) </param>
    ## <param name="executableFolderChoice"> (bool) </param>
    ## <param name="executableFolder"> (str) </param>
    ## <param name="configVar"> (str) </param>
    ## <param name="theAskQualification"> (bool) </param>
    def Merge2(isMergeOnly: bool, u18: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, theAskQualification: bool) -> str:
        """
         Cyclic Symmetry: Merge the Results 2D-3D 
         @return problem (str): .
        """
        pass
    
    ##  Cyclic Symmetry: Recombine the Results 
    ##  @return problem (str): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="type"> (str) </param>
    ## <param name="u18"> (str) </param>
    ## <param name="zoneValue"> (float) </param>
    ## <param name="executableFolderChoice"> (bool) </param>
    ## <param name="executableFolder"> (str) </param>
    ## <param name="configVar"> (str) </param>
    def Recombine(type: str, u18: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str) -> str:
        """
         Cyclic Symmetry: Recombine the Results 
         @return problem (str): .
        """
        pass
    
    ##  Cyclic Symmetry: Recombine the Results 
    ##  @return problem (str): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="type"> (str) </param>
    ## <param name="u18"> (str) </param>
    ## <param name="zoneValue"> (float) </param>
    ## <param name="executableFolderChoice"> (bool) </param>
    ## <param name="executableFolder"> (str) </param>
    ## <param name="configVar"> (str) </param>
    ## <param name="theAskQualification"> (bool) </param>
    def Recombine2(type: str, u18: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, theAskQualification: bool) -> str:
        """
         Cyclic Symmetry: Recombine the Results 
         @return problem (str): .
        """
        pass
    
    ##  Cyclic Symmetry: Recombine the Results 
    ##  @return problem (str): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## <param name="type"> (str) </param>
    ## <param name="u18"> (str) </param>
    ## <param name="zoneValue"> (float) </param>
    ## <param name="executableFolderChoice"> (bool) </param>
    ## <param name="executableFolder"> (str) </param>
    ## <param name="configVar"> (str) </param>
    ## <param name="ref1Selected"> (List[str]) </param>
    ## <param name="ref2RotationSelected"> (List[str]) </param>
    ## <param name="ref2ModeSelected"> (List[str]) </param>
    ## <param name="theAskQualification"> (bool) </param>
    def Recombine3(type: str, u18: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, ref1Selected: List[str], ref2RotationSelected: List[str], ref2ModeSelected: List[str], theAskQualification: bool) -> str:
        """
         Cyclic Symmetry: Recombine the Results 
         @return problem (str): .
        """
        pass
    
    ##  Cyclic Symmetry: Recombine the Results 
    ##  @return problem (str): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="type"> (str) </param>
    ## <param name="u18"> (str) </param>
    ## <param name="theDesFile"> (str) </param>
    ## <param name="zoneValue"> (float) </param>
    ## <param name="executableFolderChoice"> (bool) </param>
    ## <param name="executableFolder"> (str) </param>
    ## <param name="configVar"> (str) </param>
    ## <param name="ref1Selected"> (List[str]) </param>
    ## <param name="ref2RotationSelected"> (List[str]) </param>
    ## <param name="ref2ModeSelected"> (List[str]) </param>
    ## <param name="theAskQualification"> (bool) </param>
    ## <param name="theComputeStress"> (bool) </param>
    ## <param name="theComputeEnergy"> (bool) </param>
    def Recombine4(type: str, u18: str, theDesFile: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, ref1Selected: List[str], ref2RotationSelected: List[str], ref2ModeSelected: List[str], theAskQualification: bool, theComputeStress: bool, theComputeEnergy: bool) -> str:
        """
         Cyclic Symmetry: Recombine the Results 
         @return problem (str): .
        """
        pass
    
    ##  Cyclic Symmetry: Recombine the Results 
    ##  @return problem (str): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="type"> (str) </param>
    ## <param name="u18"> (str) </param>
    ## <param name="theDesFile"> (str) </param>
    ## <param name="solution"> (str) </param>
    ## <param name="zoneValue"> (float) </param>
    ## <param name="executableFolderChoice"> (bool) </param>
    ## <param name="executableFolder"> (str) </param>
    ## <param name="configVar"> (str) </param>
    ## <param name="ref1Selected"> (List[str]) </param>
    ## <param name="ref2RotationSelected"> (List[str]) </param>
    ## <param name="ref2ModeSelected"> (List[str]) </param>
    ## <param name="theAskQualification"> (bool) </param>
    ## <param name="theComputeStress"> (bool) </param>
    ## <param name="theComputeEnergy"> (bool) </param>
    def Recombine5(type: str, u18: str, theDesFile: str, solution: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, ref1Selected: List[str], ref2RotationSelected: List[str], ref2ModeSelected: List[str], theAskQualification: bool, theComputeStress: bool, theComputeEnergy: bool) -> str:
        """
         Cyclic Symmetry: Recombine the Results 
         @return problem (str): .
        """
        pass
    
import NXOpen
##  Convert samcef result file to scd5 for Rotor Dynamics  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class SamcefToScd5(NXOpen.Object): 
    """ Convert samcef result file to scd5 for Rotor Dynamics """


    ##  Samcef To Scd5: Launch Conversion 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="theSamcefResultFile"> (str) </param>
    ## <param name="zoneValue"> (int) </param>
    ## <param name="executableChoice"> (bool) </param>
    ## <param name="executableFolderName"> (str) </param>
    ## <param name="configVarName"> (str) </param>
    def LaunchConversion(theSamcefResultFile: str, zoneValue: int, executableChoice: bool, executableFolderName: str, configVarName: str) -> None:
        """
         Samcef To Scd5: Launch Conversion 
        """
        pass
    
import NXOpen
##  Superelement Recovery for Rotor Dynamics  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class SuperelementRecovery(NXOpen.Object): 
    """ Superelement Recovery for Rotor Dynamics """


    ##  Superelement Recovery: Check Wave Number for cyclic symmetry 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## <param name="creaFile"> (str) </param>
    ## <param name="samZone"> (int) </param>
    def CheckWave(creaFile: str, samZone: int) -> None:
        """
         Superelement Recovery: Check Wave Number for cyclic symmetry 
        """
        pass
    
    ##  Superelement Recovery: Get nalg in use file 
    ##  @return nalg (int): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## <param name="resultSEUseFile"> (str) </param>
    ## <param name="samZone"> (int) </param>
    def GetAlgo(resultSEUseFile: str, samZone: int) -> int:
        """
         Superelement Recovery: Get nalg in use file 
         @return nalg (int): .
        """
        pass
    
    ##  Superelement Recovery: Get References 
    ##  @return A tuple consisting of (refList, ref2ListFirstColumn, ref2ListSecondColumn). 
    ##  - refList is: List[str].
    ##  - ref2ListFirstColumn is: List[str].
    ##  - ref2ListSecondColumn is: List[str].

    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="resultSEUseFile"> (str) </param>
    ## <param name="samZone"> (int) </param>
    def GetReferences(resultSEUseFile: str, samZone: int) -> Tuple[List[str], List[str], List[str]]:
        """
         Superelement Recovery: Get References 
         @return A tuple consisting of (refList, ref2ListFirstColumn, ref2ListSecondColumn). 
         - refList is: List[str].
         - ref2ListFirstColumn is: List[str].
         - ref2ListSecondColumn is: List[str].

        """
        pass
    
    ##  Superelement Recovery: Get References2 
    ##  @return A tuple consisting of (refList, isDoubleAnalysis, nalg, nWave, ref2ListFirstColumn, ref2ListSecondColumn). 
    ##  - refList is: List[str].
    ##  - isDoubleAnalysis is: bool.
    ##  - nalg is: int.
    ##  - nWave is: int.
    ##  - ref2ListFirstColumn is: List[str].
    ##  - ref2ListSecondColumn is: List[str].

    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## <param name="resultSEUseFile"> (str) </param>
    ## <param name="creaFile"> (str) </param>
    ## <param name="samZone"> (int) </param>
    def GetReferences2(resultSEUseFile: str, creaFile: str, samZone: int) -> Tuple[List[str], bool, int, int, List[str], List[str]]:
        """
         Superelement Recovery: Get References2 
         @return A tuple consisting of (refList, isDoubleAnalysis, nalg, nWave, ref2ListFirstColumn, ref2ListSecondColumn). 
         - refList is: List[str].
         - isDoubleAnalysis is: bool.
         - nalg is: int.
         - nWave is: int.
         - ref2ListFirstColumn is: List[str].
         - ref2ListSecondColumn is: List[str].

        """
        pass
    
    ##  Superelement Recovery: Get Superelements 
    ##  @return A tuple consisting of (seLabels, sePath, seNames, sePaths, filePresence). 
    ##  - seLabels is: List[int].
    ##  - sePath is: str.
    ##  - seNames is: List[str].
    ##  - sePaths is: List[str].
    ##  - filePresence is: List[int].

    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="resultSEUseFile"> (str) </param>
    ## <param name="samZone"> (int) </param>
    def GetSuperelementsInformation(resultSEUseFile: str, samZone: int) -> Tuple[List[int], str, List[str], List[str], List[int]]:
        """
         Superelement Recovery: Get Superelements 
         @return A tuple consisting of (seLabels, sePath, seNames, sePaths, filePresence). 
         - seLabels is: List[int].
         - sePath is: str.
         - seNames is: List[str].
         - sePaths is: List[str].
         - filePresence is: List[int].

        """
        pass
    
    ##  Superelement Recovery: Get Superelements 
    ##  @return A tuple consisting of (seLabels, sePath, seNames, sePaths, filePresence, seNxnIds). 
    ##  - seLabels is: List[int].
    ##  - sePath is: str.
    ##  - seNames is: List[str].
    ##  - sePaths is: List[str].
    ##  - filePresence is: List[int].
    ##  - seNxnIds is: List[int].

    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="resultSEUseFile"> (str) </param>
    ## <param name="samZone"> (int) </param>
    def GetSuperelementsInformation2(resultSEUseFile: str, samZone: int) -> Tuple[List[int], str, List[str], List[str], List[int], List[int]]:
        """
         Superelement Recovery: Get Superelements 
         @return A tuple consisting of (seLabels, sePath, seNames, sePaths, filePresence, seNxnIds). 
         - seLabels is: List[int].
         - sePath is: str.
         - seNames is: List[str].
         - sePaths is: List[str].
         - filePresence is: List[int].
         - seNxnIds is: List[int].

        """
        pass
    
    ##  Superelement Recovery: Get SE USe File Path 
    ##  @return sePath (str): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="resultSEUseFile"> (str) </param>
    def GetSuperelementsUseFilePath(resultSEUseFile: str) -> str:
        """
         Superelement Recovery: Get SE USe File Path 
         @return sePath (str): .
        """
        pass
    
    ##  Superelement Recovery: Launch Recovery 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="resultSEUseFile"> (str) </param>
    ## <param name="recoveryDeckFileName"> (str) </param>
    ## <param name="seLabel"> (int) </param>
    ## <param name="seName"> (str) </param>
    ## <param name="sePath"> (str) </param>
    ## <param name="zoneValue"> (float) </param>
    ## <param name="executableChoice"> (bool) </param>
    ## <param name="executableFolderName"> (str) </param>
    ## <param name="configVarName"> (str) </param>
    ## <param name="firstRow"> (str) </param>
    ## <param name="ref1Selected"> (List[str]) </param>
    ## <param name="ref2RotationSelected"> (List[str]) </param>
    ## <param name="ref2ModeSelected"> (List[str]) </param>
    def LaunchRecovery(resultSEUseFile: str, recoveryDeckFileName: str, seLabel: int, seName: str, sePath: str, zoneValue: float, executableChoice: bool, executableFolderName: str, configVarName: str, firstRow: str, ref1Selected: List[str], ref2RotationSelected: List[str], ref2ModeSelected: List[str]) -> None:
        """
         Superelement Recovery: Launch Recovery 
        """
        pass
    
    ##  Superelement Recovery: Launch Recovery 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="resultSEUseFile"> (str) </param>
    ## <param name="recoveryDeckFileName"> (str) </param>
    ## <param name="seLabel"> (int) </param>
    ## <param name="seName"> (str) </param>
    ## <param name="sePath"> (str) </param>
    ## <param name="zoneValue"> (float) </param>
    ## <param name="executableChoice"> (bool) </param>
    ## <param name="executableFolderName"> (str) </param>
    ## <param name="configVarName"> (str) </param>
    ## <param name="firstRow"> (str) </param>
    ## <param name="ref1Selected"> (List[str]) </param>
    ## <param name="ref2RotationSelected"> (List[str]) </param>
    ## <param name="ref2ModeSelected"> (List[str]) </param>
    ## <param name="theRequestStress"> (bool) </param>
    ## <param name="theRequestEnergy"> (bool) </param>
    ## <param name="theAskQualification"> (bool) </param>
    def LaunchRecovery2(resultSEUseFile: str, recoveryDeckFileName: str, seLabel: int, seName: str, sePath: str, zoneValue: float, executableChoice: bool, executableFolderName: str, configVarName: str, firstRow: str, ref1Selected: List[str], ref2RotationSelected: List[str], ref2ModeSelected: List[str], theRequestStress: bool, theRequestEnergy: bool, theAskQualification: bool) -> None:
        """
         Superelement Recovery: Launch Recovery 
        """
        pass
    
## @package NXOpen.CAE.RotorDynamics
## Classes, Enums and Structs under NXOpen.CAE.RotorDynamics namespace

