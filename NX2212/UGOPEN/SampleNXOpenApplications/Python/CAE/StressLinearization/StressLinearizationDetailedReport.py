#==================================================================================
#
# Copyright (c) 2021 Siemens
# All Rights Reserved.
#
#==================================================================================
#
'''This script shows various uses of the NXOpen API for Stress Linearization by
generating a report similar to that which is dumped to the information window,
but in a spreadsheet-ready (CSV: comma-separated value) format.

To load and execute the script, first load a .sim model into Simcenter3D.  To be
of any use, the .sim file must contain an FE solution which has Stress
Linearizations in it.  Use Play in the Journal section on the Tools ribbon
bar to navigate to this script.  Specify FE_SOLUTION_NAME to report a specific
FE solution, otherwise the active solution is used.

The script outputs CSV files, one per stress linearization, placed in the part
directory.  They are named to include the part file name and the stress
linearization name.
'''
import csv
import datetime
import math
import os
import sys
import time

import NXOpen
import NXOpen.CAE
SL = NXOpen.CAE.StressLinearization 

###Constants###
# Create 3 classes to define the extremum type
class MAX: pass
class MIN: pass
class WORST: pass

#Tensor Type
MEMBRANE = SL.TensorType.Membrane
BENDING = SL.TensorType.Bending
MEMBRANEPLUSBENDING = SL.TensorType.MembranePlusBending
PEAK = SL.TensorType.Peak
TOTAL = SL.TensorType.Total

# Tensor Component 
XX = SL.TensorComponent.Xx
YY = SL.TensorComponent.Yy
ZZ = SL.TensorComponent.Zz
XY = SL.TensorComponent.Xy
YZ = SL.TensorComponent.Yz
ZX = SL.TensorComponent.Zx
SIGMA11 = SL.TensorComponent.Sigma11
SIGMA22 = SL.TensorComponent.Sigma22
SIGMA33 = SL.TensorComponent.Sigma33
MAXSHEAR = SL.TensorComponent.MaxShear
INTENSITY = SL.TensorComponent.Intensity
VONMISES = SL.TensorComponent.VonMises

# Formatting for floating point values
TSV_FLOAT_FORMAT = "10.7g"
# Formatting for datetime values
TSV_DATE_FORMAT = "%Y-%b-%d %H:%M:%S"


### User Inputs ###
# Provide the name of the FE Solution whose SLs should be exported.
FE_SOLUTION_NAME = None # None means use Active Solution


# Provide the list of parameters for the extrema computation.
# Extremum Type: Compute MAX, MIN or WORST
# Tensor Type: Available options are: MEMBRANE, BENDING, MEMBRANEPLUSBENDING, PEAK, TOTAL 
# Component: Available options are: XX, YY, ZZ, XY, YZ, ZX, 
#                                   SIGMA11, SIGMA22, SIGMA33, MAXSHEAR, INTENSITY, VONMISES 
# Load case Selection: Name of the Loadcase to search for the extremum. 
#                      If the user wants to search among all loadcases, enter "AnyLoadCase"
# Location Selection: Location on the SCL. It is a number between 0 (start of the SCL) and 1 (end of the SCL). 
#                     If the user wants to search among all locations, enter "AnyLocation"
# Iteration Selection: Integer that provides the index of the iteration. 
#                      If the user wants to search among all iterations, enter "AnyIteration"
#
#                 Extremum Tensor Type,         Component, Load case Selection,             Location       Iteration Selection
#                 Type,                                                                     Selection,
LIST_OF_EXTREMA = [[MAX,   MEMBRANEPLUSBENDING, VONMISES,  "AnyLoadCase",                   0.5,           "AnyIteration"],
                   [MAX,   PEAK,                MAXSHEAR,  "Subcase - Nonlinear Statics 1", 0.0,           "AnyIteration"],
                   [MIN,   MEMBRANE,            XX,        "Subcase - Nonlinear Statics 2", "AnyLocation", "AnyIteration"],
                   [MIN,   TOTAL,               YY,        "Subcase - Nonlinear Statics 2", "AnyLocation", 1],
                   [WORST, BENDING,             SIGMA33,   "AnyLoadCase",                   "AnyLocation", 1],
                   [WORST, MEMBRANE,            INTENSITY, "Subcase - Nonlinear Statics 2", 1.0,           10]]

# Report output format
# Specifies which output format to use.   Value here must be equal to a key in
# SUPPORTED_OUTPUT_FORMATS.
REPORT_FORMAT = "CSV"




###############################################################################
# The remainder of the script shows how to recover Stress Linearization inputs,
# perform the calculation, retrieve the outputs, and place it all in files.
###############################################################################




# Obtain a reference to the current Simcenter3D application session.
Session = NXOpen.Session.GetSession()


# The current work part is where Stress Linearizations will be found, as well as
# providing other basic information (such as the file location.)
WorkPart = Session.Parts.BaseWork


# This is the entry point to the script.  It acquires a list of all Stress
# Linearizations in FE_SOLUTION_NAME, then exports them.
def main():
    SLs = GetStressLinearizations(FE_SOLUTION_NAME)
    ExportStressLinearizations(SLs)
    log("Operations completed.")


# Creates a list of all stress linearizations in the simulation which are
# in the specified solution.
# INPUT
#   solutionName [string] Name of the FE solution in which to find the
#       Stress Linearizations.  If this is None, finds stress linearizations
#       in the active solution.
# RETURNS
#   a list of stress linearizations
def GetStressLinearizations(solutionName = None):
    sim = WorkPart.FindObject("Simulation") # NXOpen.CAE.SimSimulation
    sol = sim.ActiveSolution if not solutionName else sim.FindObject("Solution[{0}]".format(solutionName))
    return list(sol.StressLinearizations)


# Generates files for stress linearizations in the specified list.  One
# file is created for each SL.  Files are generated in the same
# directory as the .sim, and are named {PartName}_{SLName}.csv.  A new file
# is created each time -- old files are deleted before being overwritten.
# INPUT
#   SLs [list of stress linearizations] the stress linearizations to export
# RETURNS
#   None
def ExportStressLinearizations(SLs):
    # Place all files in Part directory
    partdir = os.path.dirname(WorkPart.FullPath)
    partname = os.path.splitext(os.path.basename(WorkPart.FullPath))[0]

    extension, rpt_format = SUPPORTED_OUTPUT_FORMATS[REPORT_FORMAT]
    
    log("Part directory: ", partdir)
    if not SLs:
        log("No stress linearizations in solution.")
        return
    
    for sl in SLs:
        # Compute name for SL report file
        output_path = os.path.join(partdir, partname + "_" + sl.Name + extension)
        
        log("Exporting ", sl.Name, " to ", output_path)
        data = CollectStressLinearizationData(sl)
        data.write(output_path, rpt_format)


# Converts the stress linearization input and result data into a table object
# INPUT
#   sl [StressLinearization] The source of the input and output data
# RETURNS
#   [DataBlock] containing the semi-formatted input/result data
def CollectStressLinearizationData(sl):
    # Compute the Stress Linearization to obtain results
    log("Computing ", sl.Name)
    now = datetime.datetime.now()
    (params, iterationResults) = sl.ComputeAll()
    
    # General data

    table = DataBlock()
    table.add_row(["Name", sl.Name])
    table.add_row(["Description", sl.Description])
    table.add_row(["Date", tostr(now)])
    table.add_row(["Simulation", WorkPart.FullPath])
    table.add_row(["Load Case", sl.LoadCaseName])
    table.add_row(["Iteration Spec", IterSelToStr(sl.IterationSelection)])
    table.add_row(["Iteration Range", sl.IterationRange])
    table.add_row(["Result Type", ResultTypeToStr(sl.GetResultType())])
    table.add_row(["Length Units", UnitStr("LENGTH")])
    table.add_row(["Stress Units", UnitStr("STRESS")])
    if sl.ExtractTemperature:
        table.add_row(["Temperature Units",UnitStr("TEMPERATURE")])
    table.add_row(["Linearization Type",
                   "Axisymmetric" if NXOpen.CAE.StressLinearization.StructureTypes.Axisymmetric else "3D"])
    table.add_row(["SCL"])
    table.add_row(["  Start Point", params.A.X, params.A.Y, params.A.Z])
    table.add_row(["  End Point", params.B.X, params.B.Y, params.B.Z])
    table.add_row(["Length", Distance(params.A, params.B)])
    table.add_row(["Local CSYS"])
    table.add_row(["  X Dir",
                   params.LocalCsys.Xx,
                   params.LocalCsys.Xy,
                   params.LocalCsys.Xz])
    table.add_row(["  Y Dir",
                   params.LocalCsys.Yx,
                   params.LocalCsys.Yy,
                   params.LocalCsys.Yz])
    table.add_row(["  Z Dir",
                   params.LocalCsys.Zx,
                   params.LocalCsys.Zy,
                   params.LocalCsys.Zz])
    table.add_row(["Bending Components", BendingComponents(sl.BendingComponents)])
    table.add_row(["# Intervals", sl.NumIntervals])
    
    
    # Iterations

    # Each result is 1 iteration
    for result in iterationResults:
        table.add_section("Iteration {0}: {1}".format(
            result.IterationIndex,
            result.IterationName if result.IterationName else "-none-"))
        ExportResultDetails(table, result.GetBending(), "Bending")
        ExportResultDetails(table, result.GetMembranePlusBending(), "Membrane+Bending")
        ExportResultDetails(table, result.GetPeak(), "Peak")
        ExportResultDetails(table, result.GetTotal(), "Total")
        if sl.ExtractTemperature:
           ExportContextResultDetails(table,result)
    
    # Compute and Export Extrema
    ExportExtremaResults(table, sl, iterationResults, LIST_OF_EXTREMA)

    return table



# Exports the summary of the results, the different components of stress at the
# beginning, midpoint and end of the SCL.
# INPUT
#   db [DataBlock] data block to fill with output
#   result [NXOpen.CAE.StressLinearizationResult] The results of the stress
#      linearization calculation.
# RETURNS
#   None
def ExportResultSummary(db, result):
    db.add_subsection(result.IterationName)
    
    # Results at start, midpt, end

    membrane = result.GetMembrane()
    bending = result.GetBending()
    membend = result.GetMembranePlusBending()
    peak = result.GetPeak()
    total = result.GetTotal()
    contextResults = result.GetContext()

    titles = GetResultComponentsTitles()
    db.add_row(["", *titles])
    
    # Membrane value is constant along SCL, so only writing one value
    db.add_row(["Membrane", *GetResultComponents(membrane[0])])

    # list of first, middle, last indices into results
    indices = [0, len(membrane)//2, len(membrane)-1]

    for index in indices:
        db.add_row(["Bending" if index == 0 else "",
                    *GetResultComponents(bending[index])])
        
    for index in indices:
        db.add_row(["Membrane+Bending" if index==0 else "",
                    *GetResultComponents(membend[index])])
        
    for index in indices:
        db.add_row(["Peak" if index==0 else "",
                    *GetResultComponents(peak[index])])
        
    for index in indices:
        db.add_row(["Total" if index==0 else "",
                    *GetResultComponents(total[index])])

    #Print Temperature summary
    if sl.ExtractTemperature:
        db.add_row(["","X Local", "Temperature"])
        for index in indices:
            db.add_row(["Temperature" if index==0 else "",
                    contextResults[index].XLocal, contextResults[index].Temperature])


# Exports data at all SCL integration points for all stress components to
# the specified data block.
# INPUT
#   db [DataBlock] data block to fill with output
#   states list of StressLinearizationResult.StressState
#   title [string] Title for the section in the report
# RETURNS
#   None
def ExportResultDetails(db, states, title):
    db.add_subsection(title)
    db.add_row(["", *GetResultComponentsTitles()])

    for state in states:
        db.add_row(["", *GetResultComponents(state)])
        

# Exports data at all SCL integration points for the context results (temperature)
# INPUT
#   db [DataBlock] data block to fill with output
#   result [NXOpen.CAE.StressLinearizationResult] The results of the stress
#      linearization calculation.
# RETURNS
#   None
def ExportContextResultDetails(db, result):
    db.add_subsection("Temperature")
    db.add_row(["", "Average Temperature:", result.AverageTemperature])
    db.add_row([])  # add empty row
    db.add_row(["", "X Local", "Temperature"])
    for context in result.GetContext():
        db.add_row(["", context.XLocal, context.Temperature])


# Compute and Exports data for all the extrema in the list Of Extrema
# INPUT
#   db [DataBlock] data block to fill with output
#   sl [StressLinearization] The source of the input and output data
#   iterationResults  [NXOpen.CAE.StressLinearizationResult] The results of the stress
#      linearization calculation.
#   listOfExtrema: list of the extrema asked by the user.
# RETURNS
#   None
def ExportExtremaResults(db, sl, iterationResults, listOfExtrema):
    db.add_subsection("Extrema")
    db.add_row([])  # add empty row
    db.add_row(["", "Extremum Type", "Tensor", "Component", 
                "Loadcase Name", "Location",
               "X Local", "Iteration Name", 
               "Iteration Index", "Stress"])
    for extremumEntry in listOfExtrema:
        extremumResult = ComputeExtremum(sl, iterationResults, extremumEntry)
        if not extremumResult: continue
        extremumTypeName = GetExtremumTypeStr(extremumEntry[0])
        tensorTypeName = GetTensorTypeStr(extremumEntry[1])
        componentName = GetTensorComponentStr(extremumEntry[2])
        db.add_row(["", extremumTypeName, tensorTypeName, componentName,
                    extremumResult.Extras.LcName, extremumResult.Extras.Location, 
                    extremumResult.Extras.XLocal, extremumResult.Extras.IterName, 
                    extremumResult.Extras.IterIndex, extremumResult.Stress])

        
# Compute Extremum from the selection given as input
# INPUT
#   sl [StressLinearization] The source of the input and output data
#   iterationResults [NXOpen.CAE.StressLinearizationResult] The results of the stress
#      linearization calculation.
#   extremumEntry: list of user input parameter to compute an extremum
# RETURNS
#   [StressLinearization.ExtremumResult Struct] Structure containing the stress of the extremum and some context information 
def ComputeExtremum(sl, iterationResults, extremumEntry):
    tensorType = extremumEntry[1]
    tensorComponent = extremumEntry[2]
    loadCaseSelection = GetLoadCaseSelection(sl, extremumEntry[3])
    locationSelection = GetLocationSelection(sl, extremumEntry[4])
    iterationSelection = GetIterationSelection(sl, extremumEntry[5])

    try:
        if extremumEntry[0] == MAX:
            return sl.GetMax(iterationResults, tensorType, tensorComponent, 
                             loadCaseSelection, locationSelection, iterationSelection)
        elif extremumEntry[0] == MIN:
            return sl.GetMin(iterationResults, tensorType, tensorComponent, 
                             loadCaseSelection, locationSelection, iterationSelection)
        elif extremumEntry[0] == WORST:
            return sl.GetWorst(iterationResults, tensorType, tensorComponent, 
                               loadCaseSelection, locationSelection, iterationSelection)
        else:
            log(extremumEntry[0], "is not a supported type of extremum calculation.")
    except Exception as e:
            log(GetExtremumEntryStr(extremumEntry), " ", e)
            


# Converts a NXOpen.CAE.StressLinearization.ResultSelection into
# a user-friendly string.
# INPUT
#   itersel [ResultSelection] The enum value to convert
def IterSelToStr(itersel):
    ResultSelection = NXOpen.CAE.StressLinearization.ResultSelection
    
    if   itersel == ResultSelection.First: return "First"
    elif itersel == ResultSelection.Last: return "Last"
    elif itersel == ResultSelection.FirstToIndex: return "First to Index"
    elif itersel == ResultSelection.IndexToLast: return "Index to Last"
    elif itersel == ResultSelection.All: return "All"
    elif itersel == ResultSelection.ByName: return "From List"
    elif itersel == ResultSelection.Index: return "Specify Indices"
    return "n/a"


# Converts an NXOpen.CAE.StressLinearization.ResultType into a user-friendly
# string.
# INPUT
#   typ [ResultType] Enum value to convert
# RETURNS
#   The result type as a string.
def ResultTypeToStr(typ):
    ResultType = NXOpen.CAE.StressLinearization.ResultType
    
    if   typ == ResultType.StressElemental: return "Elemental"
    elif typ == ResultType.StressElementNodal: return "Element-Nodal"
    return "n/a"


# Converts a NXOpen.CAE.StressLinearization.BendingTensorComponents into
# a user-friendly string.
# INPUT
#   comps [BendingTensorComponents] to convert
# RETURNS
#   The components as a string.
def BendingComponents(comps):
    s = ""
    if comps.XX: s += "XX "
    if comps.YY: s += "YY "
    if comps.ZZ: s += "ZZ "
    if comps.XY: s += "XY "
    if comps.YZ: s += "YZ "
    if comps.ZX: s += "ZX "
    return s
    

# Returns the unit for the current work part given the measure.  So
# GetUnitStr("STRESS") might return "MPa".
def UnitStr(measureName):
    uc = WorkPart.UnitCollection
    unit = uc.GetBase(measureName)
    return unit.Symbol


# Provides the list of column headings for the exported tables.  The values
# in the list must match those in GetResultComponents.
# INPUT
#   None
# RETURNS
#   List of strings containing the headings.
def GetResultComponentsTitles():
    return [s for s in ["X Local",
                        "XX", "YY", "ZZ",
                        "XY", "YZ", "ZX",
                        "S1", "S2", "S3",
                        "TauMax", "SINT", "SVM"]]


# Retrieves the components of a StressState and returns them as a list
# INPUT
#   state [NXOpen.CAE.StressLinearizationResult+StressState] The state of
#      stress to convert
# RETURNS
#   list of double values for each component.
def GetResultComponents(state):
    return [v for v in [ state.XLocal,
                         state.XX, state.YY, state.ZZ,
                         state.XY, state.YZ, state.ZX,
                         state.Sigma11, state.Sigma22, state.Sigma33,
                         state.MaxShear, state.Intensity, state.VonMises ]]


#Converts the extremumEntry list of parameters into a user-friendly string.
# INPUT
#   extremumEntry to convert
# RETURNS
#   The extremum Entry as a list of strings.
def GetExtremumEntryStr(extremumEntry):
    return [GetExtremumTypeStr(extremumEntry[0]),
            GetTensorTypeStr(extremumEntry[1]),
            GetTensorComponentStr(extremumEntry[2]),
            extremumEntry[3],
            extremumEntry[4],
            extremumEntry[5]]



#Converts the extremum type into a user-friendly string.
# INPUT
#   extremumType to convert
# RETURNS
#   The extremum type as a string.
def GetExtremumTypeStr(extremumType):
    if   extremumType == MAX: return "Maximum"
    elif extremumType == MIN: return "Minimum"
    elif extremumType == WORST: return "Worst"
    else:
        log(extremumType, " is not a supported extremum Type")



# Converts a NXOpen.CAE.StressLinearization.TensorType Enumeration into
# a user-friendly string.
# INPUT
#   tensorType to convert
# RETURNS
#   The tensor type as a string.
def GetTensorTypeStr(tensorType):
    if   tensorType == MEMBRANE: return "Membrane"
    elif tensorType == BENDING: return "Bending"
    elif tensorType == MEMBRANEPLUSBENDING: return "Membrane+Bending"
    elif tensorType == PEAK: return "Peak"
    elif tensorType == TOTAL: return "Total"
    else:
        log(tensorType, " is not a supported tensor type")


# Converts a NXOpen.CAE.StressLinearization.TensorComponent Enumeration into
# a user-friendly string.
# INPUT
#   component to convert
# RETURNS
#   The component as a string.
def GetTensorComponentStr(component):
    if   component == XX: return  "XX"
    elif component == YY: return  "YY"
    elif component == ZZ: return  "ZZ"
    elif component == XY: return  "XY"
    elif component == YZ: return  "YZ"
    elif component == ZX: return  "ZX"
    elif component == SIGMA11: return "Sigma11"
    elif component == SIGMA22: return "Sigma22"
    elif component == SIGMA33: return "Sigma33"
    elif component == MAXSHEAR: return "MaxShear"
    elif component == INTENSITY: return "Intensity"
    elif component == VONMISES: return "VonMises"
    else: 
        log(component, " is not a supported tensor component")


# Retrieves the public property from NXOpen.CAE.StressLinearization object if "AnyLoadCase" is specified
# if not, the function simply returns the name of the Load case specified by the user
# INPUT
#   sl [StressLinearization] The source of the input and output data
#   loadCaseSelection  String entered by the user in the list of entry parameters used to compute the extrema
#   
# RETURNS
#   Name of the LoadCase or [NXOpen.CAE.StressLinearization.AnyLoadCase]
def GetLoadCaseSelection(sl, loadCaseSelection):
    if loadCaseSelection == "AnyLoadCase": return sl.AnyLoadCase
    else: return loadCaseSelection


# Retrieves the public property from NXOpen.CAE.StressLinearization object if "AnyLocation" is specified
# if not, the function simply returns the number representing the relative location on the SCL 
# (comprised between 0 and 1) where the extremum should be computed
# INPUT
#   sl [StressLinearization] The source of the input and output data
#   loadCaseSelection  number entered by the user in the list of entry parameters used to compute the extrema
#   
# RETURNS
#   Number representing the relative location on the SCL (comprised between 0 and 1) 
#       or [NXOpen.CAE.StressLinearization.AnyLocation]
def GetLocationSelection(sl, locationSelection):
    if locationSelection == "AnyLocation": return sl.AnyLocation
    else: return locationSelection


# Retrieves the public property from NXOpen.CAE.StressLinearization object if "AnyIteration" is specified
# if not, the function simply returns the index of the iteration specified by the user
# INPUT
#   sl [StressLinearization] The source of the input and output data
#   iterationSelection  index specified by the user in the list of entry parameters used to compute the extrema
#   
# RETURNS
#   Iteration Index or [NXOpen.CAE.StressLinearization.AnyLoadCase]
def GetIterationSelection(sl, iterationSelection):
    if iterationSelection == "AnyIteration": return sl.AnyIteration
    else: return iterationSelection


# Calculates distance between two points
# INPUT
#   a,b [NXOpen.Point3D] points to calculate distance
# RETURNS
#   Distance between the points as a floating point value.
def Distance(a, b):
    return math.sqrt((b.X - a.X)**2 + (b.Y - a.Y)**2 + (b.Z - a.Z)**2)
                  

# Writers for DataBlock.write

# Writer: CSV format for excel
def write_csv(path, rows):
    with open(path, 'w', newline='') as hfile:
        writer = csv.writer(hfile)
        for row in rows:
            writer.writerow(row)


def write_tsv(path, rows):
    with open(path, 'w') as hfile:
        for row in rows:
            hfile.write("\t".join([tostr(cell) for cell in row]))
            hfile.write("\n")


SUPPORTED_OUTPUT_FORMATS = {
    "CSV" : (".csv", write_csv),
    "TSV" : (".tsv", write_tsv)
}


# A "jagged" matrix containing the "cells" of output.  Each value
# need not be numeric, but should be convertible to a string.
class DataBlock:
    def __init__(self):
        # Store data by row, each row will contain a list.
        self.__rows = list()
        

    # Adds a row to the end of the data block
    def add_row(self, rowdata):
        assert type(rowdata) == list
        self.__rows.append(rowdata)

    def add_section(self, title):
        self.add_row([]) # add empty row
        self.add_row(["******** {0} ********".format(title)])
        self.add_row([]) # add empty row


    def add_subsection(self, title):
        self.add_row([]) # add empty row
        self.add_row(["**** {0} ****".format(title)])
        

    def nrows(self):
        return len(self.__rows)
    

    def ncols(self):
        # Return length of longest row
        return len(max(self.__rows, key = len))


    # Writes the content of this object to the specified file.
    def write(self, outpath, writer = write_csv):
        rv = writer(outpath, self.__rows)
        return rv

        

# Helper method to coerce values to str
def tostr(val, badchars = {}):
    s = None
    if type(val) == str:
        s = val
    elif type(val) == datetime.datetime:
        s = val.strftime(TSV_DATE_FORMAT)
    elif type(val) == float:
        s = ("{0:" + TSV_FLOAT_FORMAT + "}").format(val)
    else:
        s = str(val)
        
    for bad,good in badchars.items():
        s = s.replace(bad, good)
    return s



def log(*args):
    info = Session.ListingWindow
    info.Open()
    s = "Report| " + "".join([str(arg) for arg in args])
    info.WriteLine(s)
    Session.LogFile.WriteLine(s)


if __name__ == "__main__":
    main()
    
    
