/****************************************************************************
              Copyright (c) 1993-2002 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File Description:
      A set of Open C API subroutines is available for accessing files. These
      routines provide a "C" interface to NX Open C API routines and
      native files.

   CAUTION
      We recommend that you use standard C functions for file and directory
      manipulations in lieu of the cfi routines in this file.  These routines
      will all be impacted by the UGII_OPTION environment variable.  In
      particular file specifications returned by functions such as uc4576
      may be converted to lower case if UGII_OPTION=lower is set.

   NOTE
      These functions would not work with file names and folder names of
      NX Manager and Teamcenter Engineering.
      Use routines from  uf_ugmgr
      for this purpose.

      File types are used to identify the contents of a file and are also used
      to determine the default extension for a file. Note that for many cases
      several files will have different extensions but the same contents
      (e.g.  text files). Note that many types do not have a name. These are
      usually variations on a different file format but with a different
      extension.

      The following are the restrictions on the length  of various items:

          File Names are limited to UF_CFI_MAX_FILE_NAME_NCHARS characters
          File Extensions are limited to 4 characters
          Directory specifications are limited to MAX_FSPEC_NCHARS
          characters
          Full file specifications are limited to MAX_FSPEC_NCHARS
          characters

      Many of the Open C API CFI routines request a file type (ftype) as
      input. This type is used to determine the default extension for a file
      if none is supplied. The system does not add an extension if one is
      included in the filespec. A file type of zero does not use any
      extension.
      

      Many of the Open C API CFI routines return negative error numbers.
      
******************************************************************************/


#ifndef UF_CFI_INCLUDED
#define UF_CFI_INCLUDED
#define UF_MAXWORD 32768 /*value of UF_MAXWORD is same as MAXWORD.*/

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_cfi_types.h>

/* The following must be the last include file */
#include <libufun_exports.h>

/* */
#define UF_MAX_UNIQUE_FILE_NAME_NCHARS 16
#define UF_MAX_UNIQUE_FILE_NAME_BUFSIZE NX_BUFSIZE(UF_MAX_UNIQUE_FILE_NAME_NCHARS)

/*  */
#define UF_MAX_UNIQUE_FILE_NAME_SIZE        (UF_MAX_UNIQUE_FILE_NAME_BUFSIZE)  
/*  */

#ifdef __cplusplus
extern "C" {
#endif






/*******************************************************************************
The name returned is a unique name for a temporary file.  The resultant
filename is unique from other processes at the time.  From a single
process, filenames will begin duplicating after the first 1,679,615 calls
to uc4577.  Temporary files should be deleted when no longer needed by an
application.  If the files are not deleted, there is a chance that the same
name may come up again if the same user happens to get the same process id
on a later date.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc4577(
char fname[UF_MAX_UNIQUE_FILE_NAME_BUFSIZE]  /* <O>
              Unique filename
              */
);/* <WRAPAS:UF_CFI_get_unique_filename> */
/*******************************************************************************
Remove the file extension from a given file specification and
returns the resultant file specification.

Environment: Internal  and  External

See Also:


History:
*******************************************************************************/
extern UFUNEXPORT int uc4578(
const char * fspec ,/* <I>
              File specification
              */
int ftype ,/* <I>
           File type
           */
char dspec[MAX_FSPEC_BUFSIZE]  /* <O>
              Resultant file specification
              */
);
/*******************************************************************************
Form the full filespec, given a simple name of a file
in the UGII_UTIL directory.

Environment: Internal  and  External

See Also:


History:
*******************************************************************************/
extern UFUNEXPORT int uc4579(
const char * fname ,/* <I>
                    File name
                    */
int ftype ,/* <I>
           File type
           */
char fspec[MAX_FSPEC_BUFSIZE] /* <O>
              Resultant file specification
              */
);
/*******************************************************************************
return the four character symbolic name for a given ftype
code (e.g.: 'PART' for ftype code 2). Many ftype codes will return
'TEXT' which indicates the file's contents may be displayed as ascii
data. Unnamed ftypes will have their numeric code returned in ascii.

Return:
         Return code:
        < 0 = Error
        = 0 = Format Returned
        = 1 = Format Undefined

Environment: Internal  and  External

See Also:


History:
*******************************************************************************/
extern UFUNEXPORT int uc4580(
int ftype ,/* <I>
           File type
           */
char symb[5] /* <O>
             Symbolic name
             */
);

/******************************************************************************
Convert the symbolic character representation of a file type
into its numeric equivalent. For example, "PART" translates to a 2.

Return:
         Return code:
        = 0 = Unknown Symbolic Name
        > 0 = File Type

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc4581(
const char * symb  /* <I>
                   Symbolic file type
                   */
);
/*******************************************************************************
Convert NX computational time to display form. Two forms are available
for the date and two forms are available for the time.
A date or time of -1 returns the current date and/or time.

NOTE: In option 9 of the dtype argument, "formatted for the locale"
means that the date and time string is appropriate for the language in
which the user's operating system environment runs under.

Return:
         Return code:
        0 = No error
    not 0 = Error code

Environment: Internal  and  External

See Also:
 uc4583

History:The dtype argument was modified in V13.0 to
        increase the number of options from 4 to 9.

*******************************************************************************/
extern UFUNEXPORT int uc4582(
int date[2] ,/* <I>
             Computational time:
             [0]  Date
             [1]  Time
             */
int dtype ,/* <I>
           Date And time representation:
           1 = mm/dd/yy, hh:mm
           2 = mm/dd/yy, hh:mm xM
           3 = dd-mmm-yy, hh:mm
           4 = dd-mmm-yy, hh:mm xM
           5 = mm/dd/yyyy, hh:mm
           6 = mm/dd/yyyy, hh:mm xM
           7 = dd-mmm-yyyy, hh:mm
           8 = dd-mmm-yyyy, hh:mm xM
           9 = Formatted for the locale
           where 'mm' = numeric month,
           'dd' = day,
           'yy' = two digit year,
           'yyyy' = four digit year,
           'mmm' = symbolic month,
           'hh' = hour,
           'mm' = minute,
           'x' = 'A' or 'P'
           When a blank is passed in for 'x', dtype = 8 will default to
             12 hour time format where dtype = 7 will display a 24 hour time format.
           Note: On Windows any string can be specified as AM/PM by using
           Control Panel -> Regional and Language Options -> Customize -> Regional Options -> Time
           */
char date_string[21] ,/* <O>
                    Date (20 characters max)
                    */
char time[21] /* <O>
             Time (20 characters max)
             */
);
/*******************************************************************************
Convert a character date and time to NX computational date and time.

Return:
         Return Code:
         0 = Success
         1 = Failure

Environment: Internal  and  External

See Also:
 uc4582

History:
*******************************************************************************/
extern UFUNEXPORT int uc4583(
const char * date ,/* <I>
                   Date in any of the following forms
                   MM/DD/YY
                   DD-MMM-YY
                   DDMMMYY
                   MM/DD/YYYY
                   DD-MMM-YYYY
                   DDMMMYYYY
                   If date is blank, the current date is used
                   */
const char * time ,/* <I>
                   Time in either of the following forms
                   HH:MM
                   HH:MM xM (x = 'A' or 'P')
                   If time is blank, the current time is used
                   */
int* dandt  /* <O>
            Date And Time
            (1) = Computational Date
            (2) = Computational Time
            */
);
/******************************************************************************
Query the user name, String Result


Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc4595(
int qitem ,/* <I>
           Item to query:
           1 = Username
           */
char str[17] /* <O>
            Query result.  This must be a buffer big enough to hold the user
            name.
            */
);
/******************************************************************************
Query a set of characteristics. The result for each item code follows:
Login Status:   (qitem = 1)
        bit 0 = Login Status
                0       = NOT LOGGED IN
                1       = LOGGED IN
        bit 1 = Username Status
                0       = DO NOT NEED A USERNAME TO LOGIN
                1       = USERNAME NEEDED FOR LOGIN
        bit 2 = Password Status
                0       = DO NOT NEED A PASSWORD TO LOGIN
                1       = PASSWORD NEEDED FOR LOGIN
        bits 3-15       = *Reserved*
File Header Support:  (qitem = 2)
        bit 0 = Owner Supported
                0 = NO
                1 = YES
        bit 1 = Protection Classes Supported
                0 = NO
                1 = YES
        bit 2 = Status Word Supported
                0 = NO
                1 = YES
        bit 3-4  = *Reserved*
        bit 5 = Description Supported
                0 = NO
                1 = YES
        bit 6 = Customer Area Supported
                0 = NO
                1 = YES
        bit 7 =  Non-Native Files Supported
                0 = NO
                1 = YES
        bits 8-15 = *Reserved*

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc4596(
int qitem ,/* <I>
           Item to query
           1 = Login status
           2 = File header fields supported
           */
int * qreslt  /* <O>
              Query result
              */
);
/******************************************************************************
Translate an error code to the text associated with it.
Due to the way error handling is done in the file system routines, the
error text should be retrieved before another error occurs otherwise
the error message might be lost.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int uc4599(
int ug_errorno ,/* <I>
                Error Code
                */
char errstg[ MAX_LINE_BUFSIZE ] /* <O>
               Error Text
               */
);
/******************************************************************************
Return the simple file name of the last file read with uc4518 or uc4564..
To obtain the full file specification, including the directory use uc4519.

Environment: Internal  and  External

See Also:
 uc4518
 uc4564
 uc4519

History:
*******************************************************************************/
extern UFUNEXPORT int uc4600(
char fname[UF_CFI_MAX_FILE_NAME_BUFSIZE] /* <O>
              Filename
              */
);
/******************************************************************************
Return the file type of the last file read with uc4518 or uc4564..
You may use uc4581 to translate the file type to a character string.

Return:
         Return code:
        < 0  = error
        >= 0 = file type

Environment: Internal  and  External

See Also:
 uc4518
 uc4564
 uc4581

History:
*******************************************************************************/
extern UFUNEXPORT int uc4601( void );

/******************************************************************************
Return the status word of the last file read with uc4518 or uc4564..

Environment: Internal  and  External

See Also:
 uc4518
 uc4564

History:
*******************************************************************************/
extern UFUNEXPORT int uc4602(
int * fsts  /* <O>
            Status word
            */
);
/******************************************************************************
Return the owner of the last file read with uc4518 or uc4564..

Environment: Internal  and  External

See Also:
 uc4518
 uc4564

History:
*******************************************************************************/
extern UFUNEXPORT int uc4603(
char owner[17] /* <O>
              Owner of file (16 characters max)
              */
);
/******************************************************************************
Return the length of the last file read with uc4518 or uc4564..

Return:
         Return code:
        >= 0 = File Length In Bytes
        < 0  = error code

Environment: Internal  and  External

See Also:
 uc4518
 uc4564

History:
******************************************************************************/
extern UFUNEXPORT long uc4605( void );

/******************************************************************************
Return the creation, modification, and last access date/time
of the last file read with uc4518 or uc4564..
Use uc4582 to convert the date/time to character strings.

Environment: Internal  and  External

See Also:
 uc4518
 uc4564
 uc4582

History:
*******************************************************************************/
extern UFUNEXPORT int uc4606(
int * cdate ,/* <O>
                Two word array containing the creation date and time
                */
int * mdate ,/* <O>
                Two word array containing the modification date and time
                */
int * ldate  /* <O>
                Two word array containing the last access date and time
                */
);
/******************************************************************************
Return the descriptions area of the last file read with uc4518 or uc4564..

Environment: Internal  and  External

See Also:
 uc4518
 uc4564

History:
*******************************************************************************/
extern UFUNEXPORT int uc4607(
char darea[ MAX_LINE_BUFSIZE ] /* <O>
              Description Area (132 characters max)
              */
);
/******************************************************************************
Return the customer area of the last file read with uc4518 or uc4564..

Environment: Internal  and  External

See Also:
 uc4518
 uc4564

History:
*******************************************************************************/
extern UFUNEXPORT int uc4608(
char carea[ MAX_LINE_BUFSIZE ] /* <O>
              Customer area (132 characters max)
              */
);
/******************************************************************************
Return the machine field of the last file read with uc4518 or uc4564.
These values are available for part files only.  Parts filed in
V10.0 or earlier return unknown values.

Return:
        Return code:
        < 0 = error
        1 = APOLLO
        2 = DEC VAX/VMS
        3 = HP CISC
        4 = HP RISC
        5 = SUN 3
        6 = SUN SPARC
        7 = DEC RISC (ULTRIX)
        8 = SGI
        9 = DATA GENERAL
        10 = IBM MVS
        11 = IBM AIX
        12 = AXP/OSF
        13 = AXP/VMS

Environment: Internal  and  External

See Also:
 uc4518
 uc4564
History:
*******************************************************************************/
extern UFUNEXPORT int uc4609( void );

/******************************************************************************
Modify the status header field of a file. An error returns if the file
system does not support a status field or the user does not have the privilege
to change it.

Environment: Internal  and  External

See Also:


History:
*******************************************************************************/
extern UFUNEXPORT int uc4612(
const char * fname ,/* <I>
                    File name
                    */
int ftype ,/* <I>
           File type
           */
int fsts  /* <I>
          New status value
          */
);
/******************************************************************************
Modify the owner header field of a file. An error returns if the file system
does not support an owner field or the user does not have the privilege to
change it (some operating systems may require root privilege to change file
ownership).

Environment: Internal  and  External

See Also:


History:
*******************************************************************************/
extern UFUNEXPORT int uc4613(
const char * fname ,/* <I>
                    File name to change the owner of
                    */
int ftype ,/* <I>
           File type
           */
const char * owner  /* <I>
                    New owner value
                    */
);
/******************************************************************************
Change the description header field of a file. An
error is returned if the file system does not support a description field or
the user does not have the privilege to change it.

Environment: Internal  and  External

See Also:


History:
*******************************************************************************/
extern UFUNEXPORT int uc4617(
const char * fname ,/* <I>
                    File name to change description of
                    */
int ftype ,/* <I>
           File type
           */
const char * desc  /* <I>
                   New description value
                   */
);
/******************************************************************************
Change the customer area header field of a file.  An
error will be returned if the file system does not support a customer
area field or the user does not have the privilege to change it.
This function modifies the part file on disk and should not
be used on a part file that has already been opened in NX. If this
occurs, the part cannot be saved. Use UF_PART_set_customer_area to
modify the customer area of a loaded part.

Environment: Internal  and  External

See Also: UF_PART_set_customer_area


History:
*******************************************************************************/
extern UFUNEXPORT int uc4618(
const char * fname ,/* <I>
                    File name to change the  customers area of
                    */
int ftype ,/* <I>
           File type
           */
const char * carea  /* <I>
                    New customer area value
                    */
);
/******************************************************************************
Read a switch from the program command line given the name of the switch.
All switches are global switches; they may appear anywhere on the command line.
Switches may have a value or no value. For example:
/LIST=FOO.LIS   switch with a value
/LIST           switch with no value

The characters that must match should be specified using upper case characters.
The user entered switch must completely match, but matching is case insensitive.
So if the program passes:
    "PARTfile" 
as the switch, then the following user entries will match:
    -part=abc
    -partfi=abc
    -partfile=abc
    -PARTFILE=abc
And the following user entries will not match:
    -p=abc       // Not enough characters
    -parti=abc   // the i does not match the specified f

Under UNIX, switches take the form:
-name           no value
-name=value     switch with a value

Switches are separated by blanks on UNIX. For example:
ugraf -user=manager -pass=frogs

Under WNT, switches take the form:
-name           no value
-name:value     switch with a value
-name=value     switch with a value

NOTE: Use uc4624 in conjunction with this function. You must call
uc4624 before calling either uc4620 or uc4621.

Return:
         Return code:
         < 0 = Error
           0 = Switch Not Present
           1 = Switch Found With No Value
           3 = Switch Found With A Value

Environment: External

See Also:
 uc4624
 uc4621

History:
*******************************************************************************/
extern UFUNEXPORT int uc4620(
const char * sname ,/* <I>
                    Switch name
                    */
char swstg[ MAX_LINE_BUFSIZE ] /* <O>
              Switch value
              */
);
/******************************************************************************
Read arguments from the command line.  Each argument may be read only once.
NOTE: Use uc4624 in conjunction with this function. You must call
uc4624 before calling either uc4620 or uc4621.

Return:
         Return code:
        < 0 = Error
          0 = Argument Not Present
          1 = Argument Found

Environment: External

See Also:
 uc4624
 uc4620

History:
*******************************************************************************/
extern UFUNEXPORT int uc4621(
char nxtarg[MAX_FSPEC_BUFSIZE] /* <O>
               Argument Value
               */
);
/*******************************************************************************
Returns an argument list to the GRIP xspawn command.  The returned string
can not exceed 132 characters.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc4622(
       char *ip1 /* <I>
                 The return argument list
                 */
);

/******************************************************************************
Returns a pointer to a string which is the release number of the
specified part file. Some of the possible values are shown for the
description of cr2. You must allocate sufficient size for the relnum
array. For example, you could use  MAX_FSPEC_BUFSIZE (prototyped in
uf_defs.h) for the size of the array.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int uc4623(
const char * fspec ,/* <I>
              Part file name
              */
char relnum[133] /* <O>
               Release number
               An example of possible Return Values are: V8, V9,
               V10, V10.1, V10.2, V10.3 etc.
               */
);
/******************************************************************************
Save argument names for use with uc4620 and uc4621. The prog
parameter is not used. It is only present for backward compatibility.
You must use uc4624 before calling uc4620 or uc4621.

Note that uc4624 expects to receive the argc and argv values passed to the
program from main, and so the values in argv are assumed to be in the current
users locale not UTF8 data.  As such this routine does not honor the setting of the text
mode made by calling UF_TEXT_set_text_mode(). 

Environment: External

See Also:
 uc4620
 uc4621

History:
*******************************************************************************/
extern UFUNEXPORT int uc4624(
int prog ,/* <I>
          Not used
          */
int argc ,/* <I>
          Argument count
          */
char ** argv  /* <I>
              array of argument names.  This data is always assumed to be in
              the users current locale.
              */
);
/*******************************************************************************
Outputs a sorted directory listing to the Information Window if  it has
been opened. Use UF_UI_open_listing_window to open the
Information Window.  Dates in cbuf must be in the format
DD-MMM-YY (eg. 04-JUL-89).

Return:
         Return code:
        < 0 = Error code
        0 = No files listed
        > 0 = Number of files listed

Environment: UF_UI_open_listing_window

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc4650(
const char * dir ,/* <I>
                  Input directory
                  */
int fmode ,/* <I>
           File selection mode
           1 = Select all files
           2 = File template specified in cbuf
           3 = Select file created/modified/ accessed
                   after date specified in cbuf according to
                   field specified in ibuf
           4 = Select file created/modified/ accessed
                   before date specified in cbuf according to
                   field specified in ibuf
           5 = Select file by owner specified in cbuf
           6 = Select file by protection class specified in
                   cbuf
           7 = Select files of type specified in ibuf
           8 = Select files by status specified in ibuf
           */
int smode ,/* <I>
           Sort mode
           1 = Alphabetic
           2 = Creation date
           3 = Modified date
           4 = Access date
           5 = Owner
           */
int * pbuf ,/* <I>
            Print Field Selection Array,
            Set Array Element = 1 To Print Desired Field
             (1) = Print format
             (2) = Print owner
             (3) = Print pclass
             (4) = Print length
             (5) = Print status
             (6) = Print creation date
             (7) = Print creation time
             (8) = Print modification date
             (9) = Print modification time
            (10) = Print access date
            (11) = Print access time
            (12) = Print machine type
            (13) = Print description area
            (14-16) = Reserved
            */
int * ibuf ,/* <I>
            Integer Parameter Array
            IF fmode=3 or fmode=4, ibuf show date type
                    IF ibuf(1) = 1 : use file creation date
                    IF ibuf(1) = 2 : use file modified date
                    IF ibuf(1) = 3 : use file accessed date
            IF fmode=7, ibuf selects file type set array element
            = 1 to select desired file type
                    (1) = Part
                    (2) = Symbol
                    (3) = Text
                    (4) = GRIP
                    (5) = Customer
                    (6) = UNISOLIDS
                    (7) = UGI
                    (8) = Communications
                    (9) = Keystroke
                    (10) = Display
                    (11) = CL file
                    (12) = Directory
                    (13-16) = Reserved
            IF fmode=8, ibuf(1) = File Status
            */
const char * cbuf  /* <I>
                   Character Parameter
                   IF fmode=2, cbuf contains file template
                   IF fmode=3, cbuf contains file date
                   IF fmode=4, cbuf contains file date
                   IF fmode=5, cbuf contains owner name
                   IF fmode=6, cbuf contains protection class
                   */
);
/******************************************************************************
Return the language name stored in the native binary file.
You can use the returned language name string
to differentiate languages that use the same character set.
NOTE: If a Native Binary File has not been loaded then uc4901
returns "ENGLISH".

Return:
         Return code
        0 = No error
  not   0 = Error code

Environment: Internal  and  External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT int uc4901(
char lname[MAX_FSPEC_BUFSIZE] /* <O>
              Returns The Language Name Stored In The Native
              Binary File
              */
);

/******************************************************************************
Test if a file exists.

Note:  This function only works with files - not directories.  To check if a
       directory exists use uc4560 and pass a file type of 100.

Return:
      0 - No error
      Otherwise - Error Code

Environment: Internal  and  External
See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_CFI_ask_file_exist(
const char *file_spec , /* <I>
                    The file to check
                   */
int  *status       /* <O>
                     File existence status.
                     0 - file exists
                     1 - file does not exist
                    */
);

/******************************************************************************
Spawn a subprocess.  The return code will indicated the status of the
process creation.  If the status from the actual command is needed, use
UF_CFI_spawn_check_status.

Environment: Internal  and  External
See Also: UF_CFI_spawn_check_status

History: Originally released in V18.0
*******************************************************************************/
extern UFUNEXPORT int UF_CFI_spawn(
const char *program , /* <I>
                      The command to be executed.  This command must either be
                      a full path name, or the program must be found on the
                      path.
                      */
int num_args,         /* <I>
                      The number of arguments in the next array.  These
                      arguments will be passed to the command.
                      */
char *arguments[],    /* <I,len:num_args>
                      An array of character pointers for the arguments to
                      be passed to the program.  You may pass in a NULL if
                      there are not any arguments.  These arguments will be
                      added in the order they are stored, so the command
                      will be:
                         program argument[0] argument[1] ...
                      Switches must be formatted by the caller.  On NT,
                      switches take the form "-switch:value", where on Unix
                      switches take the form "-switch=value".
                      */
logical  is_concur,   /* <I>
                         If TRUE, the command will be run at the same time
                         as the NX Open program, if FALSE, then UF_CFI_spawn
                         will wait for the completion of the command prior
                         to returning to the caller.
                      */
int *process_id       /* <O>
                         The process ID of the spawned process.
                         This process ID can be used to check the status of
                         the spawned process using UF_CFI_spawn_check_status.
                      */


);

/******************************************************************************
Check the status of a spawned subprocess.

Environment: Internal  and  External
See Also:  UF_CFI_spawn

History: Originally released in V18.0
*******************************************************************************/
extern UFUNEXPORT int UF_CFI_spawn_check_status(
int  process_id , /* <I>
                     The process id returned by UF_CFI_spawn for the
                     command that was run.  Note that this is only returned
                     for processes that are run concurrently.
                  */
logical  *still_running, /* <O>
                            If TRUE, the command is still running.  If FALSE,
                            the command has completed.
                         */
int *return_status    /* <O>
                         If still_running is FALSE, then this is the return
                         status from the child process.  If still_running
                         is TRUE, then this will be set to zero.  A
                         return_status of 127 is set when the spawned
                         command could not be found.
                      */


);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif
