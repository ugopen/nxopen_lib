/*******************************************************************************

         Copyright (c) 1998-2000,2001 Unigraphics Solutions Inc.
                   Unpublished - All rights reserved



File Description :

This is the Open API interface to spreadsheet related functions in NX

The spreadsheet functions provide a programmatic interface for spreadsheet
data. The functions allow you to:
 . Read spreadsheet data from the work part and write
   spreadsheet data to the existing file name that you specify.
 . Store spreadsheet data into the work part.

NOTE: You have access to the two functions UF_XS_extract_spreadsheet and
UF_XS_store_spreadsheet. However, in order to use other Xess functions (such as
xess_read_file) you must have the Xess Development System.

See the NX Online Help for details on how to use the spreadsheet.
 *****************************************************************************/

#ifndef UF_XS_INCLUDED
#define UF_XS_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************

Reads spreadsheet data from the work part and writes spreadsheet data
to the existing file name that you specify.  The basic process used to
read data from the work part, would be to first establish the file
for the data, then call this Open API routine to create the file, then
read the data into the spreadsheet using an XESS routine, e.g.

This routine will extract either an XESS or Excel spreadsheet from the part.

NOTE: The Xess Developer's Library is required in order to access
the function xess_read_file.

Environment: Internal  and  External

See Also: 
History:
******************************************************************************/
extern UFUNEXPORT int UF_XS_extract_spreadsheet(
char * spreadsheet_name ,/* <I>
                         Spreadsheet object name:
                         "MODELING_SHEET" - modeling spreadsheet data
                         "DEFAULT_SHEET" - Gateway spreadsheet data
                         "PART_FAMILY_SHEET" - Part Family spreadsheet data
                         */
char * file_name  /* <I>
                  File name to write spreadsheet data to.
                  */
);

/*****************************************************************************

Store spreadsheet data into the work part. If the spreadsheet entity name does
not exist, it will be created.  The normal process for saving spreadsheet
data would be to establish a file for the data, write the data file using
the XESS programming call, then store that data into the spreadsheet with
this Open API routine.

This routine will store an XESS or Excel spreadsheet into the part.
Excel spreadsheets can only be stored on the Windows platform.
If it is not a valid spreadsheet the error UF_err_bad_parameter_number_2
is returned.

NOTE: The Xess Developer's Library is required in order to access
the function xess_write_file.

NOTE: Storing of the Part Family spreadsheet is not supported.

Environment: Internal  and  External

See Also: 
History:
*******************************************************************************/
extern UFUNEXPORT int UF_XS_store_spreadsheet(
char * spreadsheet_name ,/* <I>
                         Name of the spreadsheet object:
                         "MODELING_SHEET" - modeling spreadsheet data
                         "DEFAULT_SHEET" - Gateway spreadsheet data
                         */
char * file_name  /* <I>
                  Location of existing file name to read XESS spreadsheet
                  data from.
                  */
);



#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif    /*  END  UF_XS_INCLUDED  */
