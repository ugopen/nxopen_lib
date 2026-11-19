/*****************************************************************************

             Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       



File description:
  
Prototypes for initialization of directory search path module.  Using the 
subroutines in this file you can:
.   Add the directories of one path to another path.
.   Add directories represented by strings to a path.
.   Add directories represented by environment variable strings to a path.
.   Retrieve the name of the current directory (with respect to an internal 
    index) in a path.
.   Return the number of directories in a path.
.   Return the index of the current directory in a path.
.   Extract the directories from a path.
.   Get the nth (as specified by index) directory from a path.
.   Retrieve the name of the previous directory (with respect to an internal 
    index) in a path.
.   Create a path from directories represented by strings.
.   Find the first file with a specific name in a path.
.   Prepare to index through each directory in a path.  

******************************************************************************/
#ifndef UF_DIRPATH_H_INCLUDED
#define UF_DIRPATH_H_INCLUDED

#include <uf_defs.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Creates a path from the value of an environment variable.


Environment: Internal  and  External

See Also: UF_DIRPATH_create_from_dirs 

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_create_from_env(
const char * env ,/* <I>
                  name of environment variable
                  */
tag_t * retval_tag  /* <O>
                    NULL_TAG or tag of path
                    */
);

/******************************************************************************
Creates a path from directories represented by strings.

Environment: Internal  and  External

See Also: UF_DIRPATH_create_from_env 



History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_create_from_dirs(
const int count ,/* <I>
                 number of directories
                 */
const char ** dirs ,/* <I,len:count>
                    directories
                    */
tag_t * retval_tag  /* <O>
                    NULL_TAG or tag of path
                    */
);


/******************************************************************************
 Adds the directories of one path to another path.

Environment: Internal  and  External
See Also: UF_DIRPATH_append_from_dirs  
         UF_DIRPATH_append_from_env 
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_append(
tag_t self ,/* <I>
            Original path which will be augmented.
            */
const tag_t append  /* <I>
                    Path to append from.
                    */
);

/******************************************************************************
Adds directories represented by environment variable strings to a path.

Environment: Internal  and  External

See Also: UF_DIRPATH_append  
         UF_DIRPATH_append_from_dirs 



History:
******************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_append_from_env(
tag_t self ,/* <I>
            Original path / augumented path.
            */
const char * env  /* <I>
                  Name of environment variable.
                  */
);


/******************************************************************************
adds directories represented by strings to a path.

Environment: Internal  and  External

See Also: UF_DIRPATH_append  
         UF_DIRPATH_append_from_env 



History:
******************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_append_from_dirs(
tag_t self ,/* <I>
            Original path / augmented path.
            */
const int count ,/* <I>
                 Number of directories to be appended.
                 */
const char ** dirs  /* <I,len:count>
                    Directories
                    */
);


/******************************************************************************
Extracts the directories from a path.

Environment: Internal  and  External

See Also:



History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_ask_dirs(
tag_t self ,/* <I>
            Path
            */
int * count ,/* <O>
             Number of directories
             */
char *** dirs  /* <OF,len:count>
               Array of directories.  This must be freed by the caller, using
               UF_free.
               */
);


/******************************************************************************
Returns the number of directories in a path.

Return:
         Number of directories

Environment: Internal  and  External

See Also:


History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_ask_dir_count(
tag_t self  /* <I>
            Path
            */
); /* <NEC> */

/******************************************************************************
Returns the index of the current directory in a path.
It is best to use UF_DIRPATH_start_dir_iteration before ever using 
UF_DIRPATH_ask_dir_index.

Return:
         index of current directory
 
Environment: Internal  and  External

See Also: UF_DIRPATH_start_dir_iteration 



History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_ask_dir_index(
tag_t self  /* <I>
            path
            */
); /* <NEC> */

/******************************************************************************
Gets the nth (as specified by index) directory from a path.

 
Environment: Internal  and  External

See Also: UF_DIRPATH_ask_prev_dir  
          UF_DIRPATH_ask_curr_dir 
          UF_DIRPATH_ask_next_dir 


 
History:
***************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_ask_nth_dir(
tag_t self ,/* <I>
            Path
            */
const int index ,/* <I>
                 >=0 : Index of directory to locate in path
                 */
char ** dir  /* <OF>
             nth directory.  This is dynamically allocated, and must be
             freed by the calling routine using UF_free.
             */
);

/******************************************************************************
 Finds the first file with a specific name in a path.

Environment: Internal  and  External

See Also:



History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_find_file(
tag_t self ,/* <I>
            Path
            */
char * name ,/* <I>
             Name of file to find
             */
char ** fpath  /* <OF>
               Path of file to find.  If the file is not found, then NULL is
               returned.  If the path is non-NULL, then the calling program
               must free this by calling UF_free.
               */
);


/******************************************************************************
This function is used to prepare to index through each directory in a path.

NOTE: This function should be called before using UF_DIRPATH_ask_next_dir,
      UF_DIRPATH_ask_prev_dir, or UF_DIRPATH_ask_curr_dir.


Environment: Internal  and  External

See Also:  UF_DIRPATH_ask_dir_index

History:
***************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_start_dir_iteration(
tag_t self  /* <I>
            path
            */
);


/******************************************************************************
Retrieves the name of the next directory (with respect to an internal
index) in a path.  You must call UF_DIRPATH_start_dir_iteration prior to
calling this routine.


Environment: Internal  and  External

See Also: UF_DIRPATH_ask_prev_dir  
          UF_DIRPATH_start_dir_iteration 
          UF_DIRPATH_ask_curr_dir 

History:
******************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_ask_next_dir(
tag_t self ,/* <I>
            Path
            */
char ** dir  /* <OF>
             Next directory.  This must be freed by the calling program using
             UF_free.
             */
);

/******************************************************************************
Retrieves the name of the previous directory (with respect to an internal 
index) in a path.  You must call UF_DIRPATH_start_dir_iteration prior to
calling this routine.

Environment: Internal  and  External

See Also: UF_DIRPATH_ask_curr_dir  
          UF_DIRPATH_ask_next_dir 
          UF_DIRPATH_start_dir_iteration 

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_ask_prev_dir(
tag_t self ,/* <I>
            Path
            */
char ** dir  /* <OF>
             Previous directory.  This must be freed by the caller using
             UF_free.
             */
);

/******************************************************************************
Retrieves the name of the current directory (with respect to an internal
index) in a path.  You must call UF_DIRPATH_start_dir_iteration prior to
calling this routine.


Environment: Internal  and  External

See Also: UF_DIRPATH_ask_prev_dir  
          UF_DIRPATH_ask_next_dir 
          UF_DIRPATH_start_dir_iteration 

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DIRPATH_ask_curr_dir(
tag_t self ,/* <I>
            path
            */
char ** dir  /* <OF>
             current directory.  This must be freed by the calling program
             using UF_free.
             */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif  /* UF_DIRPATH_H_INCLUDED */
