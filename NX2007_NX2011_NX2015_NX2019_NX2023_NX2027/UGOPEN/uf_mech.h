/***************************************************************************
             Copyright (c) 1993-2003 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       



File Description :

The Open API interface to mechanisms.
The routines in this file  offer access to the NX
database.
The routines are used to 
.    Create a gear joint.
.    reate a point curve joint.
.    Create mechanism and setup the common.
.    Retrieve a mechanism.
.    Read and edit mechanism gravitational constants.
.    Read and edit mechanism parameter values.
.    Read count value and add or edit count to object.
.    Delete objects of a mechanism.
.    Cycle by mechanism object type.
.    Add a joint to a mechanism.
.    Read and edit joint origin and matrix.
.    Read and edit joint real data.
.    Add, edit or delete joint motion input.
.    Add a link to a mechanism.
.    Read link weight, inertias, and COG.
.    Read Object ID of requested type attached to link
.    Return the number of geometry object identifier's attached
     to a link.
.    Read the geometry that is associated with a link.
.    Edit or add link weight.
.    Delete weight from link.
.    Edit or add link inertias.
.    Delete inertias from link.
.    Add, edit or delete a link COG.
.    Add a spring to a mechanism.
.    Read and edit spring values.
.    Read number and object identifier for link/joints attached to
     spring.
.    Add a force to a mechanism.
.    Read the link object identifier's attached to force.
.    Read force magnitude and location.
.    Edit or add force magnitude and location.
.    Read marker link object identifier.
.    Edit marker location.
.    Add a motion vector to a mechanism.
.    Read and edit motion vector values.
.    Add a damper to a mechanism.
.    Read and edit damper values.
.    Read damper attachments.
.    Add a torque to a mechanism.
.    Read torque object identifier's.
.    Read torque magnitude and location.
.    Edit torque magnitude.
       
 

***************************************************************************/

#ifndef UF_MECH_INCLUDED 
#define UF_MECH_INCLUDED 

#include <uf_defs.h>
#include <libufun_exports.h>
#include <uf_retiring.h>


/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif

