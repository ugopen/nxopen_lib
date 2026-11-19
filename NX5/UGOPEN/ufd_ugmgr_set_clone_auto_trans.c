/* 
===============================================================================

     Copyright (c) 1992 - 1998,2000 Electronic Data Systems Corporation
                       Unpublished - All rights reserved

===============================================================================

File description:
  
   This file demonstrates how to create a User Function Custom Application
   which provides a customised AutoTranslate function which will be used
   during clone based Import/Export.

To compile and link on HP (This assumes that headers specific to the
application are in current directory):
   cc -c -Aa -D_HPUX_SOURCE +Z \
      -I/usr/include/X11R5 -I/usr/include/Motif1.2 -I/usr/include -I. \
      ufd_ugmgr_set_clone_auto_trans.c
   /usr/eds/ufunc/uflink -r -c ufd_ugmgr_set_clone_auto_trans
   mv ufd_ugmgr_set_clone_auto_trans ufd_ugmgr_set_clone_auto_trans.hpp

To include the Custom Application automatically into a dynamic load of UG
on HP, before starting UG type:
   export USER_STARTUP=/full_path_name/ufd_ugmgr_set_clone_auto_trans.hpp

To compile and link on SGI:
   cc -O2 -KPIC -common -mips2 -c \
      -I/usr/include/X11R5 -I/usr/include/Motif1.2 -I/usr/include -I. \
      ufd_ugmgr_set_clone_auto_trans.c
   /usr/eds/ufunc/uflink -r -c ufd_ugmgr_set_clone_auto_trans
   mv ufd_ugmgr_set_clone_auto_trans ufd_ugmgr_set_clone_auto_trans.sgi
   export USER_STARTUP=/full_path_name/ufd_ugmgr_set_clone_auto_trans.sgi

To compile and link on OSF:
   cc -c -Aa +Z -std1 \
      -I/usr/include/X11R5 -I/usr/include/Motif1.2 -I/usr/include -I. \
      ufd_ugmgr_set_clone_auto_trans.c
   /usr/eds/ufunc/uflink -r -c ufd_ugmgr_set_clone_auto_trans

To compile and link on SUN:
   cc -KPIC -c \
      -I/usr/include/X11R5 -I/usr/include/Motif1.2 -I/usr/include -I. \
      ufd_ugmgr_set_clone_auto_trans.c
   /usr/eds/ufunc/uflink -r -c ufd_ugmgr_set_clone_auto_trans
   export USER_STARTUP=/full_path_name/libufd_ugmgr_set_clone_auto_trans.so



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
static int translate_name(const char old_name[MAX_FSPEC_SIZE +1],
                         char new_name[MAX_FSPEC_SIZE + 1])
{
  if (old_name[0] == '@') /* export */
  {
    char no[UF_UGMGR_PARTNO_SIZE+1];
    char rev[UF_UGMGR_PARTREV_SIZE+1];
    char ftype[UF_UGMGR_FTYPE_SIZE+1];
    char fname[UF_UGMGR_FNAME_SIZE+1];
    if (UF_UGMGR_decode_part_filename((char *)old_name,
                                      no,rev,ftype,fname) != 0)

        return 5;
    sprintf(new_name,"%s_%s.prt",no,rev);
    return 0;
  }
  else /* import */
  {
    int file_type = 2;
    char simple_name[UF_CFI_MAX_FILE_NAME_SIZE];
    if (uc4574((char *)old_name,file_type,simple_name) != 0)
      return 5;
    sprintf(new_name,"@DB/%s/A",simple_name);
    return 0;
  }
}

/*****************************************************************************
 * ufsta is a user exit added for the User Function Custom Application 
 * project. This user exit is activated when the environment variable 
 * USER_STARTUP is defined. USER_STARTUP must point to the path of the user
 * function that you want to execute, and this user function program must 
 * have the ufsta entry.
 *
 * For example: export USER_STARTUP=/ui1/ui_v104/ufun_test/ufd_ugmgr_set_clone_auto_trans.hpp
 *
*****************************************************************************/
void ufsta(char *param, int *retcod, int param_len)
{
  UF_initialize();
  UF_UGMGR_set_clone_auto_trans(translate_name);
  UF_terminate();
}
