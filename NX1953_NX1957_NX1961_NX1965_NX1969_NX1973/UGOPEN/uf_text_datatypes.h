/*******************************************************************************

            Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
                             Unpublished - All rights reserved

********************************************************************************



File description: 

  This module provides datatypes that deal with Localization or 
  Internationalization issues for the Open C API.

*******************************************************************************/
#ifndef UF_TEXT_DATATYPES_H_INCLUDED
#define UF_TEXT_DATATYPES_H_INCLUDED

/***************************************************************************

  ***************************************************************************/

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
    UF_TEXT_UTF8,              /* This mode means that the User function
                                  program will pass and receive character
                                  data using UTF-8 characters to certain
                                  NX Open functions.  This is for legacy
                                  programs only, new programs should use
                                  UF_TEXT_ALL_UTF8, as it switches the entire
                                  NX Open char * interface to UTF8.  
                               */
    UF_TEXT_ALL_UTF8           /* This mode means that the User function
                                  program will pass and receive character
                                  data using UTF-8 characters to all
                                  NX Open functions.
                               */
};

typedef enum UF_TEXT_mode_s UF_TEXT_mode_t;

#ifdef __cplusplus
}
#endif

#endif /* UF_TEXT_DATATYPES_H_INCLUDED */
