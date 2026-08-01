' CampbellCsvToAfu.vb - Import Campbell .csv file to .afu file
'
' 
'
'   Description:
'   This program is used to import Campbell diagram data from a .csv file generated
'   by a NX Nastran Rotordynamics solution.
'
'   MODTRK=1:
'    - Due to limitations with Nastran OP4 formatting, Campbell diagram data
'   is written from NX Nastran to the .csv file 7 columns at a time. The 
'   NX Function Toolkit can import a .csv file into an .afu file, but it
'   expects that all data for each RPM is on the same row. This program
'   will read the OUTPUT4 .csv file, reformat the data and import it into
'   an .afu file. The records will be named using the column header in
'   the .csv file
'
'    - Records for the 1P and 2P lines may also be generated. 
'
'   MODTRK=2/3:
'    - Updated format containing 10 columns of data for each mode
'
'   The user will be prompted to select the .csv results file and the
'   units for the ordinate and abscissa via a Block Styler dialog
'
'   The .afu output file will be named the same as the .csv input file
'
'   This program can be executed in a fem or sim part.
' 
' 
'
'   Instructions:
'   1) A copy of CampbellCsvToAfu.dlx must be in one of the following locations:
'        1.) In the same folder as CampbellCsvToAfu.vb
'        2.) From where NX session is launched
'        3.) $UGII_USER_DIR/application
'        4.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
'            recommended. This variable is set to a full directory path to a file 
'            containing a list of root directories for all custom applications.
'            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
'
'   2) Run this program from within a FEM or SIM file in NX Advanced Simulation
'      - Use 'Tools > Journal > Play' to run CampbellCsvToAfu.vb
'
'   3) The program will prompt for the existing .csv results file to use and the units of
'      the data in that file.
'
'   Known Issues:
'
