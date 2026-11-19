/*******************************************************************************
            Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                     Unpublished - All rights reserved
******************************************************************************



File description:

   This module allows the programmer to interface with the UF_SETUP object that
   is associated with a part file. It is the UF_SETUP object that contains the
   4 Operation Groups: UF_NCGEOM, UF_NCPROG, UF_NCMCT and UF_NCMTHD. Any
   parameters set in the UF_SETUP object will be inherited by all the Groups
   and Operations in the part file associated with that UF_SETUP object.

   Note that each part file has exactly one UF_SETUP associated with it.

   The post, clsf and doc names referred to in the 'generate' functions:

                         UF_SETUP_generate_program,
                         UF_SETUP_generate_clsf and
                         UF_SHOPDOC_generate_doc

   are the names as found in the appropriate CAM resource file. These resource
   files can be read by:

                         UF_CAM_opt_ask_post_names,
                         UF_CAM_opt_ask_clsf_names and
                         UF_CAM_opt_ask_doc_names, resp.
****************************************************************************/
#ifndef UF_SETUP_H_INCLUDED
#define UF_SETUP_H_INCLUDED

/***************************** Include Files **********************************/
#include <uf_defs.h>
#include <uf_cam_errors.h>
#include <libufun_cam_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

/******************************** Defines *************************************/

/******************************** Typedefs ************************************/

/* Which units to use when generating output */
enum UF_SETUP_output_units_e
{
   UF_SETUP_OUTPUT_UNITS_INCH,
   UF_SETUP_OUTPUT_UNITS_METRIC,
   UF_SETUP_OUTPUT_UNITS_OUTPUT_DEFINED,
   UF_SETUP_OUTPUT_UNITS_LAST  /* Must be the last member */
};

typedef enum UF_SETUP_output_units_e UF_SETUP_output_units_t;

/******************************* Prototypes ***********************************/

/*******************************************************************************
 This function creates a UF_SETUP object in the part specified by 'part_tag'.
 It uses the part 'template_name' as its template. The setup, views, groups and
 operations of 'template_name' become the setup of 'part_tag'. No geometry
 is loaded and no attempt is made to map the geometry in 'template_name' to
 the geometry in 'part_tag'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_create
(
   tag_t         part_tag, /* <I> - see above */
   const char   *template_name /* <I> - see above */
);


/*******************************************************************************
 This function returns the current UF_SETUP object. This object is the setup
 in the current part.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_ask_setup
(
   tag_t   *setup_tag  /* <O> - the current setup object */
);


/*******************************************************************************
 Each UF_SETUP has four views: Program, Geometry, Machine Tool and Machining
 Method. This function returns the root of the Program view.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_ask_program_root
(
   tag_t    setup_tag,  /* <I> - the setup object to query */
   tag_t   *program_group  /* <O> - the root of the program view of the 
                                    specified setup object */
);


/*******************************************************************************
 Each UF_SETUP has four views: Program, Geometry, Machine Tool and Machining
 Method. This function returns the root of the Geometry view.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_ask_geom_root
(
   tag_t    setup_tag,  /* <I> - the setup object to query */
   tag_t   *geom_group  /* <O> - the root of the geometry view of the specified
                                 setup object */
);


/*******************************************************************************
 Each UF_SETUP has four views: Program, Geometry, Machine Tool and Machining
 Method. This function returns the root of the Machine Tool view.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_ask_mct_root
(
   tag_t    setup_tag,  /* <I> - the setup object to query */
   tag_t   *mct_group   /* <O> - the root of the machine tool view of the
                                 specified setup object */
);


/*******************************************************************************
 Each UF_SETUP has four views: Program, Geometry, Machine Tool and Machining
 Method. This function returns the root of the Machining Method view.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_ask_mthd_root
(
   tag_t    setup_tag,  /* <I> - the setup object to query */
   tag_t   *mthd_group  /* <O> - the root of the machining method view of the
                                 specified setup object */
);


/*******************************************************************************
 Each UF_SETUP has four views: Program, Geometry, Machine Tool and Machining
 Method. Each of these views has a special Group known as the NULL Group. In
 the Program view the NULL Group contains those operations for which no program
 should currently be generated. If one asks to generate all programs for the
 Program root, operations in the NULL Group will be ignored. This function
 returns the NULL Group of the Program view.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_ask_program_null
(
   tag_t    setup_tag,   /* <I> - the setup object to query */
   tag_t   *program_null /* <O> - the NULL Group of the program view */
);


/*******************************************************************************
 Each UF_SETUP has four views: Program, Geometry, Machine Tool and Machining
 Method. Each of these views has a special Group known as the NULL Group. In
 the Geometry view the NULL Group contains those operations for which no 
 geometry is currently assigned. This function returns the NULL Group of the 
 Geomtry view.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_ask_geom_null
(
   tag_t    setup_tag,  /* <I> - the setup object to query */
   tag_t   *geom_null   /* <O> - the NULL Group of the geometry view */
);


/*******************************************************************************
 Each UF_SETUP has four views: Program, Geometry, Machine Tool and Machining
 Method. Each of these views has a special Group known as the NULL Group. In
 the Machine Tool view the NULL Group contains those operations for which no 
 cutter is currently assigned. However, the operations in this Group are 
 assigned to the Machine Tool represented by the root of this view. This 
 function returns the NULL Group of the Machine Tool view.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_ask_mct_null
(
   tag_t    setup_tag,  /* <I> - the setup object to query */
   tag_t   *mct_null    /* <O> - the NULL Group of the machine tool view */
);


/*******************************************************************************
 Each UF_SETUP has four views: Program, Geometry, Machine Tool and Machining
 Method. Each of these views has a special Group known as the NULL Group.
 The NULL Group of the Machining Method has no specific use; it may be
 used anyway the user wishes.  This function returns the NULL Group of the 
 Machining Method view.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_ask_mthd_null
(
   tag_t    setup_tag,  /* <I> - the setup object to query */
   tag_t   *mthd_null   /* <O> - the NULL Group of the machining method view */
);


/*******************************************************************************
 This function generates the NC program for all the operations contained in
 the specified group of the specified setup. It will use the Post (i.e., the
 Definition File and Event Handler) specified by 'post_name'. It will write
 the generated NC Program to a file with name 'output_filename'. If 
 'output_filename' exists the output will be appended to the existing file.
 If the behavior wanted is to overwrite the exsiting file, then the user 
 has to delete the file before calling this function. 

 See the Note in the File Description regarding the relationship between the
 'post_name' and the CAM resource files.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_generate_program
(
   tag_t        setup,  /* <I> - the setup object to process */
   tag_t        group,  /* <I> - the program group to process */
   const char   *post_name, /* <I> - the name (as found in a resource file) of
                                     the post instructions to use. This name 
                                     specifies the Definition File and Event 
                                     Handler file to use */
   const char   *output_filename,    /* <I> - the name of the file to write the
                                              output to */
   UF_SETUP_output_units_t   output_units /* <I> - the output units for the 
                                                   Post to use  */
);


/*******************************************************************************
 This function generates the CLSF for all the operations contained in
 the specified group of the specified setup. It will use the instructions 
 (i.e., the Definition File and Event Handler) specified by 'clsf_name'. It 
 will write the generated CLSF to a file with name 'output_filename'. If 
 'output_filename' exists it will be erased before writing new data to it.

 See the Note in the File Description regarding the relationship between the
 'clsf_name' and the CAM resource files.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_generate_clsf
(
   tag_t        setup,  /* <I> - the setup object to process */
   tag_t        group,  /* <I> - the program group to process */
   const char   *clsf_name, /* <I> - the name (as found in a resource file) of
                                     the CLSF instructions to use. This name 
                                     specifies the Definition File and Event 
                                     Handler file to use */
   const char   *output_filename,    /* <I> - the name of the file to write the
                                              output to */
   UF_SETUP_output_units_t   output_units /* <I> - the output units for the Clsf
                                                   processor to use  */
);

/*******************************************************************************
 This function deletes the current UF_SETUP object. This object is the setup
 in the current part.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SETUP_delete_setup
(
 void
);


/*******************************************************************************
 This function generates Shop Floor Documentation based upon the Template file
 and Event Handler file specified by 'doc_name'. It will write the data
 generated by the Template file and Event Handler file to a file with name
 'output_filename'.  If 'output_filename' exists it will be erased before 
 writing new data to it.

 See the Note in the File Description regarding the relationship between the
 'doc_name' and the CAM resource files.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SHOPDOC_generate_doc
(
   const char   *doc_name, /* <I> - the name (as found in a resource file) of
                                    the documentation instructions to use. This
                                    name specifies the name of the Template
                                    file and Event Handler file to use. */
   const char   *output_filename,    /* <I> - the name of the file to write the
                                              output to */
   UF_SETUP_output_units_t   output_units /* <I> - the output units for the Shop
                                                   documentation to use  */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_SETUP_H_INCLUDED */
