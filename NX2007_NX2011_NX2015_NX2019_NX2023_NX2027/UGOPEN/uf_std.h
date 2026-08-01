/*******************************************************************************

             Copyright (c) 1996-2004 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File Description:

Open C API interface to Rapid prototyping and GenConnect.

The standard functions provide routines exporting industry standard files. The
functions in this file enable you to:
.    Create a VRML output file from geometry definitions in the part.
.    Export geometry to an ICAD transfer file.

The Computer Graphics Metafile (CGM) routines enable you to:
.    Export a CGM from a drawing or layout
.    Import a CGM to one or more drawings.
.    Import an ICAD transfer file.
.    Import a VRML file.
.    Close an STL file.
.    Open an STL (Stereo Lithography) file for text output
.    Open an STL file for binary output and return its handle.
.    Put a facetized solid in an STL file.
.    Put a facetized set of sheets in an STL file.
.    Initialize the params data structure with the default VRML import
     parameter values.

The following CGM functions will be removed in NX5.

.    uc6410  (replaced by UF_CGM_export_cgm)
.    uc6411  (replaced by UF_CGM_import_cgm)
.    UF_STD_set_cgm_size_mode  (replaced by UF_CGM_set_session_export_options)

*******************************************************************************/

#ifndef UF_STD_INCLUDED_H
#define UF_STD_INCLUDED_H


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_retiring.h>
#include <libufun_exports.h>
/***************************************************************************

  ***************************************************************************/
#define ERROR_STD_base         1570000 /* standard file interfaces, like STL */

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Each standard output application has a subset of the error range allotted
 * to UF_STD. Each standard file gets 200 codes. This will allow 25 standard
 * output file types before having to allocate another major range.
 */

#define ERROR_UF_STD_base ERROR_STD_base      /* base for all UF_STD codes */

#define ERROR_UF_STD_stl_base (ERROR_UF_STD_base+0) /* base for STL files */


#define UF_STD_ERR_UNABLE_TO_FACETIZE   (ERROR_UF_STD_stl_base+1)
#define UF_STD_ERR_UNSUITABLE_ENTITY    (ERROR_UF_STD_stl_base+2)
#define UF_STD_ERR_USER_ABORT           (ERROR_UF_STD_stl_base+3)
#define UF_STD_ERR_INVALID_HANDLE       (ERROR_UF_STD_stl_base+4)
#define UF_STD_ERR_INVALID_CSYS         (ERROR_UF_STD_stl_base+5)

struct UF_STD_stl_error_s {
    int error_code;                    /* Error designation. */
    tag_t object;                      /* Edge or face with problem. */
    int related;                       /* Number of remaining related error entries. */
    double point1[3];                  /* Start point of problem range. */
    double point2[3];                  /* End point of problem range. */
} ;
typedef struct UF_STD_stl_error_s UF_STD_stl_error_t, *UF_STD_stl_error_p_t;

#define STL_STATE_base       ERROR_UF_STD_stl_base+100
#define UF_STD_STL_MULTADJ   (STL_STATE_base+1)
#define UF_STD_STL_NOADJ     (STL_STATE_base+2)
#define UF_STD_STL_DISJOINT  (STL_STATE_base+3)
#define UF_STD_STL_NOFACET   (STL_STATE_base+4)
#define UF_STD_STL_NEGSPACE  (STL_STATE_base+5)

/* For STL import */

#define UF_STD_STL_FILE_TYPE_ASCII      0
#define UF_STD_STL_FILE_TYPE_BINARY     1
#define UF_STD_STL_FILE_TYPE_UNSURE     2
#define UF_STD_STL_FILE_TYPE_NONE       3
#define UF_STD_STL_FILE_TYPE_EXT_BINARY 4

/* For ActiveWeb Output */
#define UF_STD_ACTIVEWEB_CREATE_ATTR (1)
#define UF_STD_ACTIVEWEB_ERASE_LOG   (2)
#define UF_STD_ACTIVEWEB_MOVE_FILES  (4)
#define UF_STD_ACTIVEWEB_RECURSIVE   (8)
#define UF_STD_ACTIVEWEB_NO_OPTIMIZE (16)

/* For VRML output */
#define UF_STD_OUTPUT_LIGHTS         (1)
#define UF_STD_OUTPUT_MATERIALS      (2)
#define UF_STD_OUTPUT_TEXTURES       (4)
#define UF_STD_OUTPUT_VRML_2         (8)
#define UF_STD_OUTPUT_BACKGROUND     (16)
#define UF_STD_OUTPUT_FLYTHRU        (32)
#define UF_STD_OUTPUT_MULTIFILE      (64)
#define UF_STD_OUTPUT_RECURSE        (128)
#define UF_STD_OUTPUT_ALLPARTS       (256)
#define UF_STD_OUTPUT_MOTION_RESULTS (512)

/* For VRML (import) and STL (import) input */

#define UF_STD_SMOOTH_COARSE    1.04
#define UF_STD_SMOOTH_MEDIUM    0.31
#define UF_STD_SMOOTH_FINE      0.10
#define UF_STD_UNITS_METER      1000
#define UF_STD_UNITS_MM            1
#define UF_STD_UNITS_INCH       25.4

struct UF_STD_vrml_params_s
  {
    double      angular_tolerance;      /* Angular tolerance to smooth edges.
                                        Angular tolerance (in radians) used
                                        to determine if an edge adjoining
                                        facets should be hidden. Use constants:
                                        UF_STD_SMOOTH_COARSE
                                        UF_STD_SMOOTH_MEDIUM
                                        UF_STD_SMOOTH_FINE
                                        Default value is UF_STD_SMOOTH_MEDIUM
                                        */
    float       unit_size;              /* The size of one VRML unit in
                                        millimeters.  Can be any value greater
                                        than zero, or use constants:
                                        UF_STD_UNITS_METER
                                        UF_STD_UNITS_MM
                                        UF_STD_UNITS_INCH
                                        Default value is UF_STD_UNITS_METER
                                        */
    logical     generate_all_lod;       /* Generate all Levels of Detail (LOD).
                                        TRUE = Generate all Levels of Detail
                                        FALSE = Generate only the highest Level
                                        of Detail
                                        */
    logical     hide_smooth_edges;      /* Hide smooth edges in facet models.
                                        TRUE = Hide smooth edges
                                        FALSE = Do not hide smooth edges
                                        Default value is TRUE.
                                        */
    logical     generate_one_model;     /* Generate only one facet model.
                                        Generate one facet model for all
                                        IndexedFaceSet nodes
                                        TRUE =  Generate only one facet model
                                        FALSE = Generate a facet model per
                                                IndexedFaceSet
                                        */
    logical     more_details;           /* Display more summary details.
                                        TRUE = Display more summary details
                                        FALSE =  Do not display more summary
                                                 details
                                        */
    logical     use_cache;              /* Use caching of global coordinate
                                        vertices and normal vectors.
                                        TRUE = Use caching
                                        FALSE = Do not use caching
                                        Default value is TRUE.
                                        */
    logical     suppress_warnings;      /* Suppress displaying of warning
                                        messages.
                                        TRUE = Suppress warning messages
                                        FALSE = Do not suppress warning messages
                                        */
  };

typedef struct UF_STD_vrml_params_s UF_STD_vrml_params_t;
typedef struct UF_STD_vrml_params_s *UF_STD_vrml_params_p_t;

struct UF_STD_stl_params_s
  {
    double      angular_tolerance;      /* Angular tolerance to smooth edges */
    float       unit_size;              /* Unit size in MM */
    logical     hide_smooth_edges;      /* Hide smooth edges? */
    logical     display_info;           /* Display information? */
    int         to_jt_body;             /* Convert to JT facet body */    
  };

typedef struct UF_STD_stl_params_s UF_STD_stl_params_t;
typedef struct UF_STD_stl_params_s *UF_STD_stl_params_p_t;

typedef int UF_STD_stl_file_type_t;
typedef UF_STD_stl_file_type_t *UF_STD_stl_file_type_p_t;

/****************************************************************************
Opens an STL file for text output and return its handle.

Environment: Internal  and  External

See Also: UF_STD_close_stl_file

History:
***************************************************************************/
extern UFUNEXPORT int UF_STD_open_text_stl_file(
char * file_name ,/* <I>
                  Name of STL file to be written
                  */
logical append ,/* <I>
                Append flag:
                TRUE = Append
                FALSE =  No append
                */
void ** file_handle  /* <O>
                     Handle of file
                     */
);

/****************************************************************************
Opens an STL file for binary output and return its handle.

Environment: Internal  and  External

See Also: UF_STD_close_stl_file

History:
***************************************************************************/
extern UFUNEXPORT int UF_STD_open_binary_stl_file(
char * file_name ,/* <I>
                  Name of STL file to be written
                  */
logical append ,/* <I>
                Append flag:
                TRUE = Append
                FALSE =  No append
                */
char * header ,/* <I>
               Header text for start of binary file
               */
void ** file_handle  /* <O>
                     Handle of file
                     */
);

/***************************************************************************
Closes an STL file.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUNEXPORT int UF_STD_close_stl_file(
void * file_handle  /* <I>
                    Handle of file
                    */
);

/****************************************************************************
Puts a facetized solid in an STL file.

Environment: Internal  and  External

See Also:

History:
***************************************************************************/
extern UFUNEXPORT int UF_STD_put_solid_in_stl_file(
void * file_handle ,/* <I>
                    Handle of file
                    */
tag_t csys ,/* <I>
            This argument is no longer used.  Set to NULL_TAG.
            */
tag_t body ,/* <I>
            Solid body to facetize for STL
            */
double min_edge_len ,/* <I>
                     This argument is not used, it for future
                     enhancements (Minimum facet edge length).
                     */
double max_edge_len ,/* <I>
                     Maximum facet edge length
                     */
double facet_toler ,/* <I>
                    Facet to surface tolerance (Interactive
                    Triangle Tolerance)
                    */
int * num_errors ,/* <O>
                  Number of errors
                  */
UF_STD_stl_error_p_t * error_info  /* <OF,len:num_errors>
                                   Error information - NULL if there is none.
                                   This must be free by calling UF_free.
                                   */
);

/****************************************************************************
Puts a facetized set of sheets in an STL file. The first sheet in the
sheets array must have its normal in the correct direction to indicate
the outside of the shell and it must have only one face.

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUNEXPORT int UF_STD_put_sheets_in_stl_file (
void * file_handle ,/* <I>
                    Handle of file
                    */
tag_t csys ,/* <I>
            Specifies the coordinate system with respect
            to which output data is to be made.  If specified
            as NULL_TAG, the current WCS is used.
            */
int num_sheets ,/* <I>
                Number of sheets in shell
                */
tag_t sheets[] ,/* <I,len:num_sheets>
                Solid bodies to facetize for STL
                */
double min_edge_len ,/* <I>
                     This argument is not used, it for future
                     enhancements (Minimum facet edge length).
                     */
double max_edge_len ,/* <I>
                     Maximum facet edge length
                     */
double facet_toler ,/* <I>
                    Facet to surface tolerance
                    */
double adj_toler ,/* <I>
                  Adjacency tolerance
                  */
int * num_negated ,/* <O>
                   Number of sheets with inverted normals
                   */
tag_p_t * negated ,/* <OF,len:num_negated>
                   Tags of sheets with inverted normals
                   */
int * num_errors ,/* <O>
                  Number of errors
                  */
UF_STD_stl_error_p_t * error_info  /* <OF,len:num_errors>
                                   Error information - NULL if there is none.
                                   This must be free by calling UF_free.
                                   */
);

/******************************************************************************
 *  This routine imports the specified binary STL file with the given STL
 *  parameters. The binary STL file cannot be in gzipped format, but can be
 *  an extended STL file.
 *
 * Environment: Internal  and  External
 *
 * See Also: UF_STD_import_stl_ascii_file
 *           UF_STD_ask_stl_file_type
 *           UF_STD_set_default_stl_params
 *
 * History: This function was originally released in V16.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_STD_import_stl_binary_file (
    char *                  filename,       /* <I>
                                            Name of binary STL file
                                            */
    UF_STD_stl_params_p_t   parameters,     /* <I>
                                            STL import parameters
                                            */
    int  *                  num_facets,     /* <O>
                                            Number of facets specified in
                                            the STL file
                                            */
    tag_t *                 topology        /* <O>
                                            Topology tag of new facet model
                                            */
);
/******************************************************************************
 *  This routine imports the specified ascii STL file with the given STL
 *  parameters. The ascii STL file can be in gzipped format.
 *
 * Environment: Internal  and  External
 *
 * See Also: UF_STD_import_stl_binary_file
 *           UF_STD_ask_stl_file_type
 *           UF_STD_set_default_stl_params
 *
 * History: This function was originally released in V16.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_STD_import_stl_ascii_file (
    char *                  filename,           /* <I>
                                                Name of ascii STL file
                                                */
    UF_STD_stl_params_p_t   parameters,         /* <I>
                                                STL input parameters
                                                */
    long *                  parser_line,        /* <O>
                                                Last line reached when parsing
                                                file
                                                */
    int *                   num_topologies,     /* <O>
                                                Number of topologies created
                                                */
    tag_t **                topologies,         /* <OF,len:num_topologies>
                                                Array of topology tags.  This
                                                array must be freed by calling
                                                UF_free.
                                                */
    int **                  facets_per_topol    /* <OF,len:num_topologies>
                                                Array of number of facets per
                                                topology.  This array must be
                                                freed by calling UF_free.
                                                */
);
/******************************************************************************
 *  This routine enquires the type of STL file for the specified filename.
 *  The type of files are
 *
 *  UF_STD_STL_FILE_TYPE_ASCII      -- Ascii STL file
 *  UF_STD_STL_FILE_TYPE_BINARY     -- Binary STL file
 *  UF_STD_STL_FILE_TYPE_EXT_BINARY -- Extended binary STL file
 *  UF_STD_STL_FILE_TYPE_UNSURE     -- Either ascii or binary STL file
 *  UF_STD_STL_FILE_TYPE_NONE       -- Not an STL file
 *
 *  Note: Binary files which aren't STL binary files may be identified
 *        incorrectly as extended binary STL files.
 *
 * Environment: Internal  and  External
 *
 * See Also:  UF_STD_import_stl_binary_file
 *           UF_STD_import_stl_ascii_file
 *           UF_STD_set_default_stl_params
 *
 * History: This function was originally released in V16.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_STD_ask_stl_file_type (
    char *          filename,       /* <I>
                                    Filename of potential STL file
                                    */
    UF_STD_stl_file_type_p_t    file_type  /* <O>
                                           STL file type
                                           */
);
/******************************************************************************
 *  This routine sets the given parameters to default.
 *
 * Environment: Internal  and  External
 *
 * See Also: UF_STD_import_stl_ascii_file
 *           UF_STD_import_stl_binary_file
 *           UF_STD_ask_stl_file_type
 *
 * History: This function was originally released in V16.0.
 *
 *****************************************************************************/
extern UFUNEXPORT int UF_STD_set_default_stl_params (
    UF_STD_stl_params_p_t       params   /* <O>
                                         Default STL parameters
                                         */
);

/*****************************************************************
 * Create an ActiveWeb output file from geometry definitions in the part.
 *
 *  NOTES:  This is a WNTI only function
 *   Most of the input parameters can be left as empty strings and
 *   appropriate values will be assigned from environment variables.
 *   The following environment variables are used:
 *
 *  Variable                  Default for Field
 *  UGII_ACTIVEWEB_GEOM_SERVER    Node name for geometry server
 *  UGII_ACTIVEWEB_ATTR_SERVER    Node name for attribute server
 *  UGII_ACTIVEWEB_SERVER_DIR     Relative path for amm files
 *  UGII_ACTIVEWEB_GEOM_DIR       Path for geometry files
 *  UGII_ACTIVEWEB_ATTR_DIR       Path to attribute database directory
 *  UGII_ACTIVEWEB_LOCAL_SERVER   Local path to amm directory
 *  UGII_ACTIVEWEB_LOCAL_GEOM     Local path to geometry directory
 *  UGII_ACTIVEWEB_LOCAL_WEB      Local path to web server directory
 *
 *
 *  EXAMPLE:
 *
 *  UF_STD_create_activeweb_file(
 *     "c:\temp", "cypci204", "AmGeombase", "c:\\GeomFiles\\",
 *     "phantom", "c:\\AttrDatabase\\",
 *     "", "", "", 1.0,
 *     UF_STD_ACTIVEWEB_CREATE_ATTR | UF_STD_ACTIVEWEB_ERASE_LOG );
 *
 * This command would generate files in the temp directory.
 * The geometry server is "cypci204" and the local directory for amm files
 * is "AmGeombase".  Attributes are on "phantom" under the directory
 * c:\\AttrDatabase.  No attempt will be made to move files to output
 * directories so all of the generated files will be in the working
 * directory.  The flags are set so that attributes are created and the
 * log files will be erased.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History: This function was originally released in V16.0.
 *
 *****************************************************************/
extern UFUNEXPORT int UF_STD_create_activeweb_file (
char * working_directory,      /* <I>
                               The working directory to be used for data files.
                               */
char * base_name,              /* <I>
                               The default root name for all the generated
                               files.
                               */
char * geom_server,            /* <I>
                               The node name or IP address of the geometry
                               server.
                               */
char * server_directory,       /* <I>
                               The relative directory path on the geometry
                               server for the .amm files.
                               */
char * geometry_directory,     /* <I>
                               The relative or absolute path on the geometry
                               server to the 3d data files (.3di or .3dd).
                               */
char * attribute_server,       /* <I>
                               The name or IP address for the attribute/
                               annotation database server.
                               */
char * attribute_directory,    /* <I>
                               The absolute path on the attribute serve to the
                               .mdb database files.
                               */
char * local_server_directory, /* <I>
                               The absolute directory path for the location of
                               the .amm files generated by the translator.
                               */
char * local_geom_directory,   /* <I>
                               The absolute directory path for the location
                               of the 3di and 3dd geometry data files.
                               */
char * local_web_directory,    /* <I>
                               The absolute directory path for the location of
                               the am3 web files.  This directory will probably
                               be the same location that other HTML, TIF or
                               VRML files are being written.
                               */
double tolerance,              /* <I>
                               Adjustment to facet tolerance.  Values larger
                               than 1.0 produce fewer output facets.  Values
                               less than 1.0 increase the number of facets
                               generated.
                               */
int    mode_flags              /* <I>
                               Bit field to control output contents.  Flags are:
                                  UF_STD_ACTIVEWEB_CREATE_ATTR
                                     Controls creation of attribute database.
                                  UF_STD_ACTIVEWEB_ERASE_LOG
                                     Erases log files after successful
                                     optimization.
                                  UF_STD_ACTIVEWEB_MOVE_FILES
                                     Moves generated files to the output
                                     directories as specified by the
                                     local_server_directory, the
                                     local_geom_directory, and the
                                     local_web_directory.   If the
                                     move flag is set and the directory spec for
                                     one of the local directories is blank, then
                                     that move will be ignored.
                                  UF_STD_ACTIVEWEB_RECURSIVE
                                     Apply translation to all components of an
                                     assembly.  For component parts the
                                     base_name will be the part name.
                                  UF_STD_ACTIVEWEB_NO_OPTIMIZE
                                     Generates the polygon data (.3dx) file but
                                     does not invoke the optimizer to create any
                                     of the other files.  This is useful if you
                                     desire to manually perform the optimization
                                     at another time.

                               */
);


/*****************************************************************
Create a Virtual Reality Modeling Language (VRML) output file
from geometry definitions in the part file. If no mode flags are
specified a file is produced that  contains only geometry and matches
the VRML 1.0 specification. You can OR mode_flags to obtain
different outputs.

This function can add Photo materials and textures to the export
file. Any lights or backgrounds set up by NX in the current view can
also be included in the VRML file. The file is in ASCII 3D data
format for geometry that is used by the World Wide Web.

To output a VRML 2.0 spec file with light sources but no materials,
textures, or backgrounds you could call this function as follows:
UF_STD_create_vrml_file( "test.wrl", 1.0,
UF_STD_OUTPUT_LIGHTS | UF_STD_OUTPUT_VRML_2 );

Environment: Internal  and  External

See Also:

History:
*****************************************************************/
extern UFUNEXPORT int UF_STD_create_vrml_file(
char * file_name ,/* <I>
                  Name for the output VRML file.
                  */
double tolerance ,/* <I>
                  adjustment to facet tolerance. Values larger than 1.0
                  produce fewer output facets. Values less than 1.0
                  increase the number of facets generated.
                  */
int mode_flags  /* <I>
                Control bit fields for controlling output facets. The
                following are valid flags:
                UF_STD_OUTPUT_LIGHTS - output light sources when set.
                UF_STD_OUTPUT_MATERIALS - output material properties
                                          if set.
                UF_STD_OUTPUT_TEXTURES - output image textures if set.
                UF_STD_OUTPUT_BACKGROUND - output background/foreground
                                           information
                UF_STD_OUTPUT_VRML_2  - use VRML 2.0 specification if set.
                */
);


/***************************************************************************
Imports a VRML file into the work part according to the specified
parameters.

Environment: Internal  and  External

See Also:  UF_STD_set_default_vrml_params.
 UF_STD_vrml_params_p_t


History: This function was originally released in V15.0.
 **************************************************************************/
extern UFUNEXPORT int UF_STD_import_vrml_file (
    char *   filename,  /* <I>
                        Name of file to import
                        */
    UF_STD_vrml_params_p_t  parameters,  /* <I>a
                                         Import parameters
                                         */
    int *    num_errors,  /* <O>
                          Number of errors found whilst parsing
                          */
    int *    num_warnings, /* <O>
                           Number of warnings found whilst parsing
                           */
    int *    n_topologies,  /* <O>
                            Number of new facet topologies created
                            */
    tag_p_t *  topologies    /* <OF,len:n_topologies>
                             Array of tags of the created facet
                             topologies. Must be freed by the caller.
                             */
);

/****************************************************************************
Initializes the params data structure with the default VRML import
parameter values.

Environment: Internal  and  External

See Also: UF_STD_import_vrml_file
 UF_STD_vrml_params_p_t


History: This function was originally released in V15.0.

****************************************************************************/
extern UFUNEXPORT int UF_STD_set_default_vrml_params(
    UF_STD_vrml_params_p_t      params  /* <O>
                                        Default VRML import parameters
                                        */
);

/***************************************************************************
import an icad transfer file

Environment: Internal  and  External

See Also:

History:
***************************************************************************/
extern UFUNEXPORT int UF_STD_import_icad_geometry(
const char * file_spec ,/* <I>
                  File specification of binary transfer file to import
                  */
double matrix[12] ,/* <I>
                   Orientation matrix of reference set:
                    [0-8]   Reference Set Orientation Matrix
                    [9-11]  Reference Set Origin
                   */
tag_t * ug_tag  /* <O> tag of reference set
                */
);

/**************************************************************************
Exports geometry to an ICAD transfer file.

Environment: Internal  and  External

See Also:

History:
*************************************************************************/
extern UFUNEXPORT int UF_STD_export_icad_geometry(
const char * file_spec ,/* <I>
                  File specification of binary transfer file to export
                  */
tag_t * objects ,/* <I,len:count>
                 Array of object tags to export
                 */
int count  /* <I>
           Number of objects
           */
);

/***************************************************************************
   This include file contains the prototypes and descriptions of the
   icadif functions that follow the old and new naming convention.  The
   prototypes for the old naming convention will be deleted when the move
   to using ONLY the new naming convention goes into effect.

                                   *NOTICE*

   The icadif functions are available on HP Risc & Sun Solaris.  These
   functions will simply return a zero status on all other platforms.
  ***************************************************************************/

/***************************************************************************
   Old naming convention prototypes - icadif functions
  ***************************************************************************/

/* uc5595 import icad binary report */
extern UFUNEXPORT int uc5595(const char *cp1/* <I> */, double *rp2, tag_t *nr3, char cr4[MAX_LINE_BUFSIZE] /* <O> */);
/* uc5596 export NX objects to an icad binary report */
extern UFUNEXPORT int uc5596(const char *cp1/* <I> */, tag_t *np2, int ip3, char cr4[MAX_LINE_BUFSIZE]/* <O> */);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif   /* END UF_STD_INCLUDED */
