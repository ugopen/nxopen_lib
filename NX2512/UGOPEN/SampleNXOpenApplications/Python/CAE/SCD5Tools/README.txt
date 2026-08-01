------------------------------------------------------------------------------------
------------------------------------------------------------------------------------

                            Copyright 2022 Siemens

------------------------------------------------------------------------------------
                                SCD5 Tools
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
Prerequisites
------------------------------------------------------------------------------------

-h5repack utility from HDF utilities included with hdf5 library
-python 3.9 or newer
-Python libraries:
	-h5py: 3.5 or newer
	-numpy
	-matplotlib (FileContent.py)
	-prettytable (QueryNode.py only)

------------------------------------------------------------------------------------
Assumptions and Limitations
------------------------------------------------------------------------------------

- The scripts that are using h5repack utilities for copying hdf5 assume the path of
the HDF5 utilities is in the PATH environment variable (%PATH% on Windows, 
$PATH on Linux).

If the path to h5repack is not in the PATH, scripts should me modified to specify 
the full path to h5repack. For example, on windows change getH5Repack() method to 
return "C:\\Program Files\\HDF_Group\\HDF5\\1.12.2\\bin\\ h5repack.exe".

- The python scripts that split a scd5 file into multiple files create a new scd5 
  file referencing the actual data for the result data sets as links in Virtual Data 
  Sets. Pithos library used by Simcenter to read scd5 files is not able to return 
  the external files referenced by Virtual Data Sets. The library reads the actual 
  data if the linked files are available and an array of zeros if they are missing. 
  
  To allow the detection of missing result files, they are also stored in an 
  additional attribute called "ResultFiles" on the "__attribute__" group 
  corresponding to the result data set. If a distributed file is merged back into a
  single file, all attributes storing the result files should be removed, otherwise 
  they might still be considered as merged files by Simcenter. 
  This is implemented in MergeScd5.py script.

- The distributed scd5 file and all the companion files storing the actual data of a
  result data sets must be stored in the same directory. 
  The virtual data sets should reference the companion result files by relative path 
  (file name only, since they are stored in the same directory). 
  The hdf5 library allows referencing files in external files by absolute path or by 
  relative path from a different directory but this is not supported by the Simcenter
  for checking file availability. 

------------------------------------------------------------------------------------
Split scd5 by Measure (Result Type)
------------------------------------------------------------------------------------

Script Name: SplitByMeasure.py

Description:
Splits a scd5 file into multiple hdf5 files by creating a new scd5 file and a new h5 
file for every measure (result type) from the file. Each h5 file stores the data for a
single measure for all load cases and all iterations (time steps, modes or frequencies).

Split by measure is recommended if the user is interested in post processing the 
results of a single measure across multiple load cases and iterations (Contour plots,
Function plots, Envelope for one measure).

Usage:
SplitByMeasure.py input.scd5

The script will create a new file input_m_byMeasure.scd5 and a new file h5 file for 
every measure from the file named input_m_<MeasureName>.h5

Example:
SplitByMeasure.py Sol101_Static.scd5

Will create a new scd5 file Sol101_Static_m_byMeasure.scd5 and new h5 files: 
Sol101_m_Displacement.h5, Sol101_m_Stress.h5, Sol101_m_Force_Reaction_GridPoint.h5, 
etc.

------------------------------------------------------------------------------------
Split scd5 by Subcase (Solution Step)
------------------------------------------------------------------------------------

Script Name: SplitBySubcase.py

Description:
Splits a scd5 file into multiple hdf5 files by creating a new scd5 file and a new h5 
file for every subcase (solution step) from the file. Each h5 file stores the data for a
single solution step for all measures and all iterations (time steps, modes or frequency).

Usage:
SplitBySubcase.py input.scd5

The script will create a new file input_s_byStep.scd5 and a new file h5 file for 
every subcase from the file named input_s_<Step>.h5

Example:
SplitBySubcase.py Sol101_Static.scd5

Will create a new scd5 file Sol101_Static_s_byStep.scd5 and new h5 files: 
Sol101_Static_s_Static_Step1.h5, Sol101_Static_s_Static_Step2.h5, Sol101_Static_s_Static_Step3.h5.

------------------------------------------------------------------------------------
Split scd5 by Iteration
------------------------------------------------------------------------------------

Script Name: SplitByIteration.py

Description:
Splits a scd5 file into multiple hdf5 files by creating a new scd5 file and a new h5 
file for every iteration from the file. Each h5 file stores the data for a single 
iteration (time steps, modes or frequency) for all load cases and all measure
(result types)

Usage:
SplitByIteration.py input.scd5
The script will create a new file input_byIteration.scd5 and a new file h5 file 
for every iteration from the file named input_s_IterationResult_<iteration number>.h5

Example:
SplitByIteration.py Sol103_Modes.scd5
Will create a new scd5 file Sol103_Modes_byIteration.scd5 and new h5 files:
Sol103_Modes_IterationResult_00.h5,..., Sol103_Modes_IterationResult_09.h5 .

Limitations:
Because the h5py library currently does not support nested compound types, the 
script can be used only for data sets containing real values of type scalar, vector, 
symmetric tensor and tensor. The script does not support data sets containing 
complex values of type vector, tensors and symmetric tensor because they are stored 
as compound data of compound data in scd5 files.

------------------------------------------------------------------------------------
Split scd5 by Measure and Iteration
------------------------------------------------------------------------------------

Script Name: SplitByMeasureAndIteration.py

Description:
Splits a scd5 file into multiple hdf5 files by creating a new scd5 file and a new h5 
file for every measure and every iteration from the file. Each h5 file stores the data
for a single iteration (time steps, modes or frequency) and a single measure 
(result types) for all load cases.

Usage:
SplitByMeasureAndIteration.py input.scd5
The script will create a new file input_byIteration.scd5 and a new file h5 file for
every iteration from the file named input_s_IterationResult_<iteration number>.h5

Example:
SplitByMeasureAndIteration.py Sol103_Modes.scd5
Will create a new scd5 file Sol103_Modes_s1.scd5 and new h5 files for every measure 
and iteration: Sol103_Modes_s1_Displacement_00.h5,..., Sol103_Modes_s1_Displacement_09.h5,
Sol103_Modes_s1_Stress_00.h5,..., Sol103_Modes_s1_Stress_09.h5, etc.

Limitations:
Because the h5py library currently does not support nested compound types, the 
script can be used only for data sets containing real values of type scalar, vector,
symmetric tensor and tensor. The script does not support data sets containing
complex values of type vector, tensors and symmetric tensor because they are stored
as compound data of compound data in scd5 files.

------------------------------------------------------------------------------------
Merge a distributed scd5 with virtual data sets
------------------------------------------------------------------------------------

Script Name: MergeScd5.py

Description:
Merges a distributed scd5 file referencing result data sets from external hdf5 files
into a single scd5 file.

Usage:
MergeScd5.py input.scd5 output.scd5
The script will merge input.scd5 and all the other hdf5 files referenced by it into
one single file having the name specified by user(output.scd5). 

Example:
Suppose we have the following files: Sol103_Modes_byIteration.scd5, 
Sol103_Modes_IterationResult_00.h5, Sol103_Modes_IterationResult_01.h5, ... 
Sol103_Modes_09.h5 and they were obtained by using the script SplitByIteration.py.

MergeScd5.py Sol103_Modes_byIteration.scd5 Sol103_Modes_merged.scd5

Will merge all the files back together in a file named Sol103_Modes_merged.scd5.

Limitations:
We expect the script to work properly on any files split by one of the above scripts
(SplitByMeasure.py, SplitByIteration.py, SplitByMeasureAndIteration.py).

------------------------------------------------------------------------------------
Query and extract data on mesh node as function of iteration (frequency or time)
------------------------------------------------------------------------------------

Script Name: QueryNode.py

Description:
Extracts results data from a mesh node as a function of iteration (Time Step, 
Frequency or Mode Frequency) and writes it into a separate h5 file. The script also 
plots the extracted data values as a graphical plot by using matplotlib library.

Usage:
QueryNode.py input.scd5 NodeId ResultName/QuantityName output.h5

input.scd5: name of input scd5 file from which data should be extracted

NodeId: the node id (user number) for which data should be extracted. 

ResultName/QuantityName: an identifier for the data set from which data should be 
extracted. Can be specified as a data set name (without path) or as quantity name. 
Available result names and quantities names can be queried by using FileContent.py
script. 

output.h5: the name of the output file where the extracted data should be written.
The result file will contain a data set with the iteration values (time steps or 
frequencies) and one or more data sets containing the extracted data values for the
input node and result name or quantity name. The id of the node for which the values
where extracted is not stored in the output file. 

Example:
QueryNode.py Sol401_Time.scd5 10 Acceleration a.h5 
Extracts result values for mesh node having user number 10 from the data set
containing Acceleration data by specifying quantity name. 

QueryNode.py Sol401_Time.scd5 10 "Acceleration Nodal" a.h5 
Extracts result values for mesh node having user number 10 from the data set named
"Acceleration Nodal".

The script also plots the extracted data values.

Limitations:
The script plots real data of type Scalar, Vector and Symmetric Tensor.
The script can extract only data sets data sets with two legends (two dimensional 
data sets): Iteration legend (Time Step, Frequency Step, Mode) and Node.
The script plots the data as it is stored in the file, without taking into account 
the file unit system. 

------------------------------------------------------------------------------------
List scd5 file content
------------------------------------------------------------------------------------

Script Name: FileContent.py

Description:
Displays information about the result available in a scd5 file:
- Available Solution Steps (Load Cases)
- Available iterations: Time Step, Frequency, Modes
- Results available for every iteration 
- For every available, result displays the following information
- The name of the HDF5 Group storing the result data set
- The quantity (measure) of the result (Displacement, Force, Stress, etc.)
- The result display name, if available
- The result quantity qualifiers (sub measure). For example, for Force or Moment, 
  can be: Applied, Reaction, Grid Point, etc.
- The Component of the result data 
- The type of result data: Scalar, Vector, Symmetric Tensor
- Available data legends. For example, Iteration legends: Time, Frequency Mode and 
  location legends: Node, Element, Node Of Element, Shell Location
- Flag indicating if the result is stored as a virtual data set (meaning that result
  data is stored in separate file(s) )

Usage:
FileContent.py input.scd5

Example:
SplitByMeasureAndIteration.py Sol401_Time.scd5

Will display a table with the results of the data sets from the file.

------------------------------------------------------------------------------------
Exports function results from a scd5 file to a csv file
------------------------------------------------------------------------------------

Script Name: ExportSCD5FunctionResultsToCSV.py

Description:
Exports function results from a scd5 file to a csv file:
- The names of the function result types
- The names of the function records
- The names of abscissa and ordinate quantities
- The symbols of abscissa and ordinate units
- The complex types of the function records
- The values of data points

Usage:
run_journal ExportSCD5FunctionResultsToCSV.py -args [-h] [input scd5 file name] [output csv file name]

Arguments:
[-h]: Print help documentation
[input scd5 file name]: Required. Specifies the name of the scd5 file containing function results. If the file path is not specified, it is same as the current working directory.
[output csv file name]: Optional. Specifies the name of the csv file function to which results will be written. If no specified output file, the default output file would be <path of input file>/<input_file_name>.csv

Example:
run_journal ExportSCD5FunctionResultsToCSV.py -args SampleFunctionResults.scd5 SampleFunctionResultsExport.csv
