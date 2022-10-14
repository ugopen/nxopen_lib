/*******************************************************************************

           Copyright (c) 1996-2003 Unigraphics Solutions Inc.
                        Unpublished - All rights reserved

********************************************************************************



File description:

These subroutines provide access to Clearance Analysis data within NX.
All Clearance Analysis data is maintained in an object called a Clearance
Analysis data set. The data set consists of two types of information, setup
data and analysis results. The setup data includes items such as the list of
objects available for analysis, the clearance zones for those objects, rules
used to exclude some object pairs from analysis, and analysis preferences. The
results are a list of interferences. The routines in this section allow you to:
      . manipulate clearance analysis data sets.
      . establish the lists of objects to be subject to clearance analysis.
      . define clearance zones around objects. These clearance
        zones define a volume in which no other objects can penetrate.
      . defines rules that exclude certain pairs from analysis.
      . create and query analysis results.
      . specify clearance analysis preferences.

Refer to the Assemblies User Manual for details on Clearance Analysis.

Note in routines where a user is expected to provide a valid pointer,
UF_CLEAR_err_null_pointer will be returned when a null pointer is detected.


*******************************************************************************/

#ifndef UF_CLEAR_H_INCLUDED
#define UF_CLEAR_H_INCLUDED

/***************************************************************************

  ***************************************************************************/

/*******************************************************************************
                                 ** Includes **
 ******************************************************************************/

#define ERROR_CLEAR_base       1185000
#include <uf_defs.h>                    /* For MAX_LINE_SIZE, TRUE/FALSE, etc.*/
#include <uf_retiring.h>
#include <libufun_exports.h>

#undef EXPORTLIBRARY

#endif /* UF_CLEAR_H_INCLUDED */

