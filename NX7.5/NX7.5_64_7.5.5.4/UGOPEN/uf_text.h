/*******************************************************************************

                  Copyright (c) 1998-2003 Unigraphics Solutions Incorporated
                             Unpublished - All rights reserved

********************************************************************************



File description: 

  This module provides routines that deal with Localization or 
  Internationalization issues for the Open C API.
  

*******************************************************************************/

#ifndef UF_TEXT_H_INCLUDED
#define UF_TEXT_H_INCLUDED
/***************************************************************************

  ***************************************************************************/

#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

enum UF_TEXT_mode_s
{
    UF_TEXT_LOCALE,            /* This mode means that the user function
                                  program will pass and receive character
                                  data using character strings in the current
                                  users locale.
                               */
    UF_TEXT_UTF8               /* This mode means that the User function
                                  program will pass and receive character
                                  data using UTF-8 characters.
                               */
};

typedef enum UF_TEXT_mode_s UF_TEXT_mode_t;


/**************************************************************************
 
This routine sets the text mode for a user function program.  UF_initialize 
defaults the text mode to UF_TEXT_LOCALE.  This routine is provided to let the 
user function programmer change the default behavior.  When text strings are 
returned in the locale, International characters may be lost, if they exist in 
the part.
 
Environment: Internal  and  External

See Also:

History:

****************************************************************************/
extern UFUNEXPORT int UF_TEXT_set_text_mode( 
UF_TEXT_mode_t mode  /* <I>
                        One of the following enumerated text mode constants: 
                            UF_TEXT_LOCALE
                            UF_TEXT_UTF8
                     */
);

/**************************************************************************
 
This routine allows the programmer to load a translation file that will be
used to translate strings from English into the users native language.  This
file will be used in addition to the standard ugii.lng that contains the
translations for NX messages and dialogs.

The Open API programmer is responsible for creating this file using the 
NLDMGR tool as described in the NX Internationalization and
Localization online help.
 
Environment: Internal  and  External

See Also:

History: Originally released in V18.0

****************************************************************************/
extern UFUNEXPORT int UF_TEXT_load_translation_file( 
const char *file  /* <I>
                  This is the complete path to the file to be loaded.  When
                  NX displays the user interface, it will use the 
                  contents of this file to try and translate strings into
                  the users language.
   
                  Translation strings that exist in the NX language
                  file found in $UGII_LANGUAGE/ugii.lng will always be used
                  first.  If a translation is not found in that file, then
                  this file will be searched.
                  */
);

/**************************************************************************
 
This routine allows the programmer to translate a C string
from English into the users native language.  The strings to translate
should be contained in the file loaded using UF_TEXT_load_translation_file.
If no translation is found the original string is used.
 
Environment: Internal  and  External

See Also:

History: Originally released in NX 2

****************************************************************************/
extern UFUNEXPORT int UF_TEXT_translate_string
(
    const char* source, /* <I>
                        This is the English source string to be translated.
                        */
    int         size,   /* <I> size in bytes of the xstring buffer */   
    char* const xstring /* <O>
                        This is the buffer to return the string
                        translated into the users native language.
                        If the source string is not translated
                        xstring receives the source string unchanged. 
                        This buffer must be allocated by the caller of
                        UF_TEXT_translate_string.
                        */
);
/**************************************************************************
 
This routine allows the programmer to translate a C string
from English into the users native language.  The strings to translate
should be contained in the file loaded using UF_TEXT_load_translation_file.
If no translation is found the original string is used. You must use UF_free 
to deallocate space used by xstring.
Environment: Internal  and  External

See Also:

History: Originally released in NX 602

****************************************************************************/
extern UFUNEXPORT int UF_TEXT_translate_string_2
(
    const char* source, /* <I>
                        This is the English source string to be translated.
                        */
     char** xstring /* <OF>
                        This returns the string translated into the users 
                        native language. If the source string is not translated
                        xstring receives the source string unchanged. 
                        Use UF_free to deallocate memory when done.
                        */
);
/*****************************************************************************
 *   
 * Initializes the system for native language support.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 *         Originally released in NX 602
 *****************************************************************************/
extern UFUNEXPORT int UF_TEXT_init_native_lang_support
(
    void
);
#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_TEXT_H_INCLUDED */
