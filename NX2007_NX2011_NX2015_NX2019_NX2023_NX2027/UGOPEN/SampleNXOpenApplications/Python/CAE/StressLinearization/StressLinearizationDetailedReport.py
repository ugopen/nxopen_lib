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

# Provide the name of the FE Solution whose SLs should be exported.
FE_SOLUTION_NAME = None # None means use Active Solution

# Report output format
# Specifies which output format to use.   Value here must be equal to a key in
# SUPPORTED_OUTPUT_FORMATS.
REPORT_FORMAT = "CSV"

# Formatting for floating point values
TSV_FLOAT_FORMAT = "10.7g"
# Formatting for datetime values
TSV_DATE_FORMAT = "%Y-%b-%d %H:%M:%S"


###############################################################################
# The remainder of the script shows how to recover Stress Linearization inputs,
# perform the calculation, retrieve the outputs, and place it all in files.
###############################################################################

import csv
import datetime
import math
import os
import sys
import time

import NXOpen
import NXOpen.CAE


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
        db.add_row(["","X local", "Temperature"])
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
#   states list of StressLinearizationResult.StressState
# RETURNS
#   None
def ExportContextResultDetails(db, result):
    db.add_subsection("Temperature")
    db.add_row(["", "Average Temperature:", result.AverageTemperature])
    db.add_row([])  # add empty row
    db.add_row(["", "X local", "Temperature"])
    for context in result.GetContext():
        db.add_row(["", context.XLocal, context.Temperature])
        


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
    
    
