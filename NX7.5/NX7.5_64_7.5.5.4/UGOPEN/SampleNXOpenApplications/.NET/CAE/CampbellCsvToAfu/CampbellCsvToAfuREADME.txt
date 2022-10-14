 NX 6.0.2
 CampbellCsvToAfu.vb - Import Campbell .csv file to .afu file

   Description:
   This program is used to import Campbell diagram data from a .csv file generated
   by a NX Nastran Rotordynamics solution.

   Due to limitations with Nastran OP4 formatting, Campbell diagram data
   is written from NX Nastran to the .csv file 7 columns at a time. The 
   NX Function Toolkit can import a .csv file into an .afu file, but it
   expects that all data for each RPM is on the same row. This program
   will read the OUTPUT4 .csv file, reformat the data and import it into
   an .afu file. The records will be named using the column header in
   the .csv file

   Records for the 1P and 2P lines will also be generated. 

   The user will be prompted to select the .csv results file via a browser dialog

   The .afu output file will be named the same as the .csv input file

   This program can be executed in a fem or sim part.
 
   Instructions:
   1) Run this program from within a FEM or SIM file in NX Advanced Simulation
      - Use 'Tools > Journal > Play' to execute CampbellCsvToAfu.vb
   2) The program will prompt for the existing .csv results file to use.

   Known Issues:

