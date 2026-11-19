 EnvelopeResults.vb - Sort across load cases for Max/Min/Absolute Max

   Description:
   This program is used to sort for Min, Max and Absolute Max values across
   one or more loadcases.

   This program  prompt for the solver results file (.op2, .fil, etc.)

   Once the results file is successfully opened, it will propmt for load case(s)
   to sort across, and the results type and component to sort for, based on the
   data available in the results file.

   The sorted results will be written to an output file with the name of
   inputfile_inputextension.unv.

   NX 6.0.3 will recognize this naming convention and will append the dataset 2414
   results in the unv file to the results list from the solver ouptut file.

   The solution set ID, boundary condition set and load set fields in record 10
   are used to increment the Load Case container in the NX Post Processing Navigator.
   When the appended results file is loaded, 3 new load cases will show up. The
   first contains the maximum value, the second contains the minimum value and the
   third contains the absolute maximum value. Each load case will contain results
   for 2 iterations. The first is the result data component. The second is the 
   load case ID that the result data component occurred in.

   It is assumed that this program will be executed in a sim part.
 
   Instructions:
   1) Place a copy of envelopeResults.dlx in the %UGII_USER_DIR%\application folder
   2) Run this program from within a SIM file in NX Advanced Simulation
      - Use Tools > Journal > Play to execute EnvelopeResults.vb
   3) The program will prompt you for the existing results file to use.

   Known Issues:
   1) If multiple iterations exist, only the first one will be used

