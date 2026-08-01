/* 
===============================================================================

     Copyright (c) 1992 - 1998,2000 Electronic Data Systems Corporation
                       Unpublished - All rights reserved

===============================================================================

File description:
  
   This file demonstrates how to create a User Function Custom Application
   which provides a customised AutoTranslate function which will be used
   during clone based Import/Export.

   To include the Custom Application automatically into a dynamic load of NX
   the library created needs to be set up as described in the Open C Programmers
   Guild - Automatic Loading at NX Start-up.



===========================================================================*/

#include <stdio.h>
#include <uf.h>
#include <uf_ugmgr.h>
#include <uf_defs.h>
#include <uf_cfi.h>
#include <uf_exit.h>

/*
  Autotranslate function which translates @DB names to <Item_no>_<Rev>
  Native names, and Native names to @DB/<leafname>/A (Note that this is
  not a symmetrical translation).
*/
static int translate_name(const char old_name[ MAX_FSPEC_BUFSIZE ],
                         char new_name[ MAX_FSPEC_BUFSIZE ])
{
  if (old_name[0] == '@') /* export */
  {
    char *baseFileName = NULL;
    UF_UGMGR_generate_base_file_name (old_name, &baseFileName);

    if(baseFileName == NULL)
        return 5;

    sprintf(new_name,"%s.prt", baseFileName);
    return 0;
  }
  else /* import */
  {
    int file_type = 2;
    char simple_name[ UF_CFI_MAX_FILE_NAME_BUFSIZE ];
    if (uc4574((char *)old_name,file_type,simple_name) != 0)
      return 5;
    sprintf(new_name,"@DB/%s/A",simple_name);
    return 0;
  }
}

/*****************************************************************************
 * ufsta is a user exit added for the User Function Custom Application 
 * project. The library created from this program needs to be set up as
 * described in the Open C Programmers Guide - Automatic Loading at NX Start-up.
 *
*****************************************************************************/
void ufsta(char *param, int *retcod, int param_len)
{
  UF_initialize();
  UF_UGMGR_set_clone_auto_trans(translate_name);
  UF_terminate();
}
