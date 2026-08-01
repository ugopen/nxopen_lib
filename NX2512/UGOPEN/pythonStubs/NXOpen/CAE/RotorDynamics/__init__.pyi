from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class BearingCoefficientsImport(NXOpen.Object): 
    """ Bearing Coefficients Import for Rotor Dynamics """
    def Apply(csvFile: str, bearingType: int, unit: int) -> Tuple[List[str], List[str]]:
        """
         Bearing Coefficients Import 
         Returns A tuple consisting of (errorText, warningText). 
         - errorText is: List[str].
         - warningText is: List[str].

        """
        pass
import NXOpen
class EnergyTables(NXOpen.Object): 
    """ Energy Tables Display for Rotor Dynamics """
    def Apply(csvFile: str) -> None:
        """
         Energy Tables: Display on the Information Window 
        """
        pass
import NXOpen
class Merge(NXOpen.Object): 
    """ Results Merge for Rotor Dynamics """
    def CompleteMerge(u18Names: List[str], zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, outputName: str) -> str:
        """
         Merge the Results 
         Returns problemOut (str): .
        """
        pass
    def CompleteMerge2(u18Names: List[str], zoneValue: float, executableFolderChoice: bool, theAskQualification: bool, executableFolder: str, configVar: str, outputName: str) -> str:
        """
         Merge the Results 
         Returns problemOut (str): .
        """
        pass
import NXOpen
class RecombineAndMerge(NXOpen.Object): 
    """ Cyclic Symmetry Recombination for Rotor Dynamics """
    def CompleteMerge(isMergeOnly: bool, u18: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, problemIn: str) -> str:
        """
         Cyclic Symmetry: Merge the Results 2D-3D 
         Returns problemOut (str): .
        """
        pass
    def CompleteMerge2(isMergeOnly: bool, u18: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, problemIn: str, theAskQualification: bool) -> str:
        """
         Cyclic Symmetry: Merge the Results 2D-3D 
         Returns problemOut (str): .
        """
        pass
    def GetReferences(resultSEUseFile: str, samZone: int) -> Tuple[List[str], bool, int, bool, List[str], List[str]]:
        """
         Cyclic Symmetry: Get References 
         Returns A tuple consisting of (refList, isDoubleAnalysis, nalg, afterRecovery, ref2ListFirstColumn, ref2ListSecondColumn). 
         - refList is: List[str].
         - isDoubleAnalysis is: bool.
         - nalg is: int.
         - afterRecovery is: bool.
         - ref2ListFirstColumn is: List[str].
         - ref2ListSecondColumn is: List[str].

        """
        pass
    def Merge2(isMergeOnly: bool, u18: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, theAskQualification: bool) -> str:
        """
         Cyclic Symmetry: Merge the Results 2D-3D 
         Returns problem (str): .
        """
        pass
    def Recombine(type: str, u18: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str) -> str:
        """
         Cyclic Symmetry: Recombine the Results 
         Returns problem (str): .
        """
        pass
    def Recombine2(type: str, u18: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, theAskQualification: bool) -> str:
        """
         Cyclic Symmetry: Recombine the Results 
         Returns problem (str): .
        """
        pass
    def Recombine3(type: str, u18: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, ref1Selected: List[str], ref2RotationSelected: List[str], ref2ModeSelected: List[str], theAskQualification: bool) -> str:
        """
         Cyclic Symmetry: Recombine the Results 
         Returns problem (str): .
        """
        pass
    def Recombine4(type: str, u18: str, theDesFile: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, ref1Selected: List[str], ref2RotationSelected: List[str], ref2ModeSelected: List[str], theAskQualification: bool, theComputeStress: bool, theComputeEnergy: bool) -> str:
        """
         Cyclic Symmetry: Recombine the Results 
         Returns problem (str): .
        """
        pass
    def Recombine5(type: str, u18: str, theDesFile: str, solution: str, zoneValue: float, executableFolderChoice: bool, executableFolder: str, configVar: str, ref1Selected: List[str], ref2RotationSelected: List[str], ref2ModeSelected: List[str], theAskQualification: bool, theComputeStress: bool, theComputeEnergy: bool) -> str:
        """
         Cyclic Symmetry: Recombine the Results 
         Returns problem (str): .
        """
        pass
import NXOpen
class SamcefToScd5(NXOpen.Object): 
    """ Convert samcef result file to scd5 for Rotor Dynamics """
    def LaunchConversion(theSamcefResultFile: str, zoneValue: int, executableChoice: bool, executableFolderName: str, configVarName: str) -> None:
        """
         Samcef To Scd5: Launch Conversion 
        """
        pass
import NXOpen
class SuperelementRecovery(NXOpen.Object): 
    """ Superelement Recovery for Rotor Dynamics """
    def CheckWave(creaFile: str, samZone: int) -> None:
        """
         Superelement Recovery: Check Wave Number for cyclic symmetry 
        """
        pass
    def GetAlgo(resultSEUseFile: str, samZone: int) -> int:
        """
         Superelement Recovery: Get nalg in use file 
         Returns nalg (int): .
        """
        pass
    def GetReferences(resultSEUseFile: str, samZone: int) -> Tuple[List[str], List[str], List[str]]:
        """
         Superelement Recovery: Get References 
         Returns A tuple consisting of (refList, ref2ListFirstColumn, ref2ListSecondColumn). 
         - refList is: List[str].
         - ref2ListFirstColumn is: List[str].
         - ref2ListSecondColumn is: List[str].

        """
        pass
    def GetReferences2(resultSEUseFile: str, creaFile: str, samZone: int) -> Tuple[List[str], bool, int, int, List[str], List[str]]:
        """
         Superelement Recovery: Get References2 
         Returns A tuple consisting of (refList, isDoubleAnalysis, nalg, nWave, ref2ListFirstColumn, ref2ListSecondColumn). 
         - refList is: List[str].
         - isDoubleAnalysis is: bool.
         - nalg is: int.
         - nWave is: int.
         - ref2ListFirstColumn is: List[str].
         - ref2ListSecondColumn is: List[str].

        """
        pass
    def GetSuperelementsInformation(resultSEUseFile: str, samZone: int) -> Tuple[List[int], str, List[str], List[str], List[int]]:
        """
         Superelement Recovery: Get Superelements 
         Returns A tuple consisting of (seLabels, sePath, seNames, sePaths, filePresence). 
         - seLabels is: List[int].
         - sePath is: str.
         - seNames is: List[str].
         - sePaths is: List[str].
         - filePresence is: List[int].

        """
        pass
    def GetSuperelementsInformation2(resultSEUseFile: str, samZone: int) -> Tuple[List[int], str, List[str], List[str], List[int], List[int]]:
        """
         Superelement Recovery: Get Superelements 
         Returns A tuple consisting of (seLabels, sePath, seNames, sePaths, filePresence, seNxnIds). 
         - seLabels is: List[int].
         - sePath is: str.
         - seNames is: List[str].
         - sePaths is: List[str].
         - filePresence is: List[int].
         - seNxnIds is: List[int].

        """
        pass
    def GetSuperelementsUseFilePath(resultSEUseFile: str) -> str:
        """
         Superelement Recovery: Get SE USe File Path 
         Returns sePath (str): .
        """
        pass
    def LaunchRecovery(resultSEUseFile: str, recoveryDeckFileName: str, seLabel: int, seName: str, sePath: str, zoneValue: float, executableChoice: bool, executableFolderName: str, configVarName: str, firstRow: str, ref1Selected: List[str], ref2RotationSelected: List[str], ref2ModeSelected: List[str]) -> None:
        """
         Superelement Recovery: Launch Recovery 
        """
        pass
    def LaunchRecovery2(resultSEUseFile: str, recoveryDeckFileName: str, seLabel: int, seName: str, sePath: str, zoneValue: float, executableChoice: bool, executableFolderName: str, configVarName: str, firstRow: str, ref1Selected: List[str], ref2RotationSelected: List[str], ref2ModeSelected: List[str], theRequestStress: bool, theRequestEnergy: bool, theAskQualification: bool) -> None:
        """
         Superelement Recovery: Launch Recovery 
        """
        pass
