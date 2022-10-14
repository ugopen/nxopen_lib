/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_DISP_ask_work_plane_emphasis                                    *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part. The code prints the state   *
 *   of the work plane emphasis.                                              *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <uf_defs.h>
#include <uf.h>
#include <uf_disp.h>
#include <stdio.h>

/*ARGSUSED*/
void ufusr(char *param, int *retcod, int param_len)
{
	int emphasis, error;
	
	error = UF_initialize();
	if (error)
	{
		char err_string[133];
		UF_get_fail_message(error, err_string);
		printf("Unable to initialize: error code %d - %s\n",
				error, err_string);
		return;
	}
	error = UF_DISP_ask_work_plane_emphasis(&emphasis);
	if (error)
	{
		char err_string[133];
		UF_get_fail_message(error, err_string);
		printf("Unable to read emphasis value: error code %d -"
			  " %s\n", error, err_string);
		return;
	}
	printf("Work plane emphasis is %sabled\n",
		   (emphasis == UF_DISP_WORK_PLANE_EMPHASIS_ON) ? 
		   "en" : "dis");
	
	UF_terminate();
}
int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
