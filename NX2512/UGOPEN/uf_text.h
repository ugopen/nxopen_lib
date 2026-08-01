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

#include <uf_defs.h>
#include <uf_text_datatypes.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/**************************************************************************
 
This routine sets the text mode for a user function program.  UF_initialize 
defaults the text mode to UF_TEXT_LOCALE.  This routine is provided to let the 
user function programmer change the default behavior.  When text strings are 
returned in the locale, International characters may be lost, if they exist in 
the part.
 
Environment: Internal  and  External

See Also:  UF_TEXT_ask_text_mode

History:

****************************************************************************/
extern UFUNEXPORT int UF_TEXT_set_text_mode( 
UF_TEXT_mode_t mode  /* <I>
                        One of the following enumerated text mode constants: 
                            UF_TEXT_LOCALE
                            UF_TEXT_UTF8
                            UF_TEXT_ALL_UTF8 
                     */
);/*<RETIRE_NXOPEN>*/

/**************************************************************************

This routine returns the current text mode for a user function program.
This routine is provided to let the user function programmer know what the mode is
so that it can be changed temporarily and then reset as needed.

Environment: Internal  and  External

See Also:  UF_TEXT_set_text_mode

History:

****************************************************************************/
extern UFUNEXPORT UF_TEXT_mode_t UF_TEXT_ask_text_mode ( );

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

/****************************************************************************
*   Count the number of characters in a string.  This is designed to work
*   with multibyte characters to support all languages.  If passed a NULL
*   string the count will be returned as zero, same as if the string was empty.
*
*   Environment: Internal and External
*
*   History: Released in NX 9.0
****************************************************************************/
extern UFUNEXPORT int UF_TEXT_count_characters
(
    const char * string_to_check,/* <I>  The string to look at */
    int *num_characters          /* <O> The count of characters (not bytes) in the string */
);

/****************************************************************************
*   Truncate a string to a given byte count and a number of characters based
*   on the internal NX encoding for strings.  This will ensure the string is
*   appropriately sized for calls to other UF function calls.
*
*   This is designed to work with multibyte characters to support all languages.
*   If passed a NULL it will return success.  If the string is shorter than 
*   the number of characters passed and the number of bytes passed then no 
*   action will be taken and success will be returned.  If the internal NX
*   string representation exceeds either the number of bytes or the number of 
*   characters, the string will be terminated after the last full character 
*   that ensures the string is both less than the number of bytes and less 
*   than the number of characters.  The logical returned will indicate whether
*   the input string was changed or not.
* 
*   This routine is designed to work with the new UF definitions that now
*   specify a character and byte count limitation, e.g.
*
*   error = UF_TEXT_truncate(filespec, MAX_FSPEC_BUFSIZE, MAX_FSPEC_NCHARS, &trunc);
*   will make sure a filespec is appropriately sized for UF_CFI calls.
*
*   Environment: Internal and External
*
*   History: Released in NX 9.0
****************************************************************************/
extern UFUNEXPORT int UF_TEXT_truncate
(
    char * string_to_truncate,  /* <I/O,len:num_characters>  The string to look at */
    int num_bytes,              /* <I> The maximum number of bytes allowed in
                                       the output string.
                                */
    int num_characters,         /* <I> The maximum number of characters allowed
                                       in the output string
                                 */
    logical *truncated          /* <O> True if the string was truncated */
);

/****************************************************************************
*   Copy a string to a given byte count and a number of characters based
*   on the internal NX encoding for strings.  This will ensure the string is
*   appropriately sized for calls to other UF function calls.
*
*   This is designed to work with multibyte characters to support all languages.
*   If passed a NULL it will return an error.  If the internal NX
*   string representation exceeds either the number of bytes or the number of 
*   characters, the string will be terminated after the last full character 
*   that ensures the string is both less than the number of bytes and less 
*   than the number of characters.  The value returned will indicate whether
*   the copy was successful or not.
* 
*   This routine is designed to work with the new UF definitions that now
*   specify a character and byte count limitation.
*
*   Environment: Internal and External
*
*   History: Released in NX 10.0
****************************************************************************/
extern UFUNEXPORT int UF_TEXT_copy_nchars
(
    const char *input_buffer,    /* <I>  The string to look at */
    unsigned int output_buffer_length, /* <I> The maximum number of bytes allowed in
                                       the output string including the trailing NULL.
                                  */
    unsigned int nchars,               /* <I> The maximum number of characters allowed
                                       in the output string
                                  */
    char *output_buffer          /* <O,len:output_buffer_length>
                                    The copied string */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_TEXT_H_INCLUDED */
