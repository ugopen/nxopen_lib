/*******************************************************************************

             Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved


******************************************************************************




File Description:
This is the Open API interface to WEB related functions in NX.

The NX Web Author functions provide a programmatic interface to the NX
Web Express Authoring tool. The functions allow you to:
. Create a HTML document based on the contents of the NX HTML template.
. Write text to the current HTML output file specified with UF_WEB_author HTML.

NOTE:
      See the NX Online Help for details on template commands.

***************************************************************************/

#ifndef UF_WEB_INCLUDED
#define UF_WEB_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/***************************************************************************

  ***************************************************************************/

/*****************************************************************
Create an HTML document based on the contents of the NX
HTML template. The template allows you to customize the NX contents
of the HTML. See the NX Online Help for details of
the contents of the NX HTML template file.
NOTE: When using this function the UGSPREADSHEET command is not functional.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
*****************************************************************/
extern UFUNEXPORT int UF_WEB_author_html(
char * output_filename ,/* <I>
                        Output HTML file
                        */
char * template_filename ,/* <I>
                          Template file to use
                          */
int apply_to_each_component  /* <I>
                             FALSE = Template is applied once to the assembly
                             TRUE = Template is applied once to each
                             component of the assembly with the
                             work part being automatically changed.
                             */
);

/*****************************************************************
Writes text to the current HTML output file specified with
UF_WEB_author_html. This function is generally used with the
<@UGUF..> template command in order to write data into the
output HTML file from an internal Open API program.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.

 *****************************************************************/
extern UFUNEXPORT int UF_WEB_write_to_file(
char * output_string  /* <I>
                      Output HTML file
                      */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif    /*  END  UF_DISP_INCLUDED  */

