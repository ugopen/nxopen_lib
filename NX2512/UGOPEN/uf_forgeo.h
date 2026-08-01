/*******************************************************************************


             Copyright (c) 1997-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved




File description:
       The structures, functions, and macros in the UF_FORGEO module allow you
       to define your own surfaces for use inside NX. You can use this
       module in conjuction with the UF_BREP module to aid in the creation an
       inquiry of foreign surfaces. The functionality of this module is for
       users who have proprietary surface definitions which cannot be duplicated
       using NX modeling techniques.

       To use this functionality you must first register a set of functions,
       like a UDO (see the uf_udobj.h chapter or header file), which is called
       when your foreign surface is processed. You then create the surface using
       the routines in the UF_BREP module.

       The mechanism for loading the foreign surface library is identical to
       that used to load and initialize User Defined Objects. You will build a
       library containing everything you need to process your foreign surfaces.
       This library will also contain the function ufsta(). You will put your
       foreign surface library in your $UGII_SITE_DIR/udo directory.  During
       NX startup this library will be loaded and ufsta will be
       invoked. Your ufsta function must call UF_FORGEO_register_surface() to
       register the functions required to process foreign surfaces. The
       functions you register will be called when NX needs to process
       a foreign surface. You must call UF_initialize before the call to
       register your callbacks and UF_terminate after. If your callbacks call
       Open API functions then they too must UF_initialize and UF_terminate.

       



*******************************************************************************/

#ifndef UF_FORGEO_H_INCLUDED
#define UF_FORGEO_H_INCLUDED

/*******************************************************************************

*******************************************************************************/

#include <uf_defs.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

#define UF_FORGEO_EVALUATOR_MISSING  1
#define UF_FORGEO_INCOMPLETE  2
#define UF_FORGEO_TRIANGULAR  1
#define UF_FORGEO_RECTANGULAR 2

/*******************************************************************************

   Macros to help in the loading of the results array during evaluation
   of surfaces.

   For each macro:
     num_derivs_in_u and num_derivs_in_v are the requested number of
                     derivatives in each direction.
     triang   is the request for triangular array status input to the evaluator.

     The macro will return true if that particular derivative is required.
          false otherwise.

     index    is the position in the results array to put the answer if it is
              needed.

*******************************************************************************/

/*
   Position.
*/
#define UF_FORGEO_SRF_POSITION(index) (index = 0, TRUE)

/*
   First partial in u.
*/
#define UF_FORGEO_SRF_FIRST_PARTIAL_IN_U(num_derivs_in_u,index) \
            ((num_derivs_in_u) > 0 ? (index = 3), TRUE : FALSE)

/*
   Second partial in u.
*/
#define UF_FORGEO_SRF_SECOND_PARTIAL_IN_U(num_derivs_in_u,index) \
             ((num_derivs_in_u) > 1 ? (index = 6), TRUE : FALSE)

/*
   First partial in v.
*/
#define UF_FORGEO_SRF_FIRST_PARTIAL_IN_V(num_derivs_in_u,num_derivs_in_v,index)\
 ((num_derivs_in_v) > 0 ? (index = (3 * ((num_derivs_in_u) + 1))), TRUE : FALSE)

/*
   Second partial in v.
*/
#define UF_FORGEO_SRF_SECOND_PARTIAL_IN_V(num_derivs_in_u,num_derivs_in_v, \
 triang,index) ((num_derivs_in_v) > 1 ? (index = (6 *(num_derivs_in_u) + 3 *(2 \
 - ((triang) == UF_FORGEO_RECTANGULAR ? 0 : 1)))), TRUE : FALSE)

/*
   Mixed partial.
*/
#define UF_FORGEO_SRF_MIXED_PARTIAL(num_derivs_in_u,num_derivs_in_v, \
triang,index) ((((num_derivs_in_u) > 0 && (num_derivs_in_v) > 0 && (triang) == \
                UF_FORGEO_RECTANGULAR) || ((num_derivs_in_u) > 1 && (triang)\
                != UF_FORGEO_RECTANGULAR)) ? \
                (index = (3*((num_derivs_in_u) + 2))), TRUE : FALSE)


/*******************************************************************************

   Data structure for foreign surface.

*******************************************************************************/

/*
   Structure defining the foreign surface.

   In the foreign surface structure, the transformation matrix operates as a
   post-multiplier on row vectors containing homogenous coordinates as:

   (x',y',z',s') = (x,y,z,s)T

   where the conventional 3D coordinates are

   (x/s,y/s,z/s).

   The matrix consists of

             0
       R     0
             0
    Tx Ty Tz S

    R = a non singular transformation matrix. This matrix contains the rotation,
        reflection, local scaling and shearing components.

    T = a translation vector

    S = a scaling factor that has to be greater than zero.

    The subscripts of "transform" corresponding to the above form are:

     [0][0]   [1][0]   [2][0]   [3][0]
     [0][1]   [1][1]   [2][1]   [3][1]
     [0][2]   [1][2]   [2][2]   [3][2]
     [0][3]   [1][3]   [2][3]   [3][3]

     After initializing the foreign surface data structure you will use

     UF_BREP functions to create a body from the surface data.

See Also: 

*/
struct UF_FORGEO_forsurf_s {
   char   *char_data ;        /* character string data for surface */
   int     nspace ;           /* space required by surface loader, in doubles
                                 used to define length of "fg_data"
                                 input to registered functions */
   int     num_ints ;         /* number of integers defining surface */
   int    *int_array ;        /* array of integers for surface */
   int     num_doubles ;      /* number of doubles defining surface */
   double *double_array ;     /* array of doubles for surface */
   double  transform[4][4] ;  /* 4x4 transformation array
                                 the "perspective" elements must be 0.0 */
};

typedef struct UF_FORGEO_forsurf_s  UF_FORGEO_forsurf_t,
                                   *UF_FORGEO_forsurf_p_t;

/*
   Definitions of registered functions for foreign surface use.
*/

/*******************************************************************************

   This function will be called when a foreign surface is created. This will
   occur either during new surface creations or during load of existing models.
   NX will ask you to prepare to process this surface.  You need to prepare to
   evaluate this surface and return whether or not evaluation is possible.  The
   fg_data array can be used any way you wish.  You may want to store
   information to make the evaluation faster or you could store the address of
   the evaluation function for this surface if multiple surface types are
   supported and you want to remove a switch between surface types during each
   evaluation.

*******************************************************************************/
typedef int (*UF_FORGEO_create_surface_f_t) (
    char   *char_data,        /* <I>  - character string data for surface */
    int     num_ints,         /* <I>  - number of integers defining surface */
    int    *int_array,        /* <I,len:num_ints> num_ints  - array of integers for surface */
    int     num_doubles,      /* <I>  - number of doubles defining surface */
    double *double_array,     /* <I,len:num_doubles> num_doubles  - array of doubles for surface */
    int     num_data,         /* <I>  - FG data length */
    double *fg_data           /* <I/O,len:num_data> num_data - FG data array
                                 R  - 0 = NO_ERROR
                                      UF_FORGEO_EVALUATOR_NOT_AVAILABLE */
);

/******************************************************************************

   This function is used to define the valid parameter range for the surface.
   A place is saved to handle periodic surfaces but this is not yet supported.

******************************************************************************/
typedef void (*UF_FORGEO_ask_surface_params_f_t) (
    int    int_array[],        /* <I> - array of integers for surface */
    double double_array[],     /* <I> - array of doubles for surface */
    double fg_data[],          /* <I> - FG data array */
    double *uvbox,            /* <O> - uv parameter box for surface */
    int     period[2]         /* <O> - u and v periodicity flags for surface
                                     [0] = u, [1] = v
                                     UF_MODL_NON_PERIODIC or
                                     UF_MODL_PERIODIC (not yet supported) */
);

/******************************************************************************

   This function will be called when evaluation of the foreign surface is
   needed.  You need to support up to second derivatives.

******************************************************************************/
typedef int (*UF_FORGEO_evaluate_surface_f_t) (
    int    int_array[],        /* <I> - array of integers for surface */
    double double_array[],     /* <I> - array of doubles for surface */
    double fg_data[],          /* <I> - FG data array */
    double  u,                /* <I> - u parameter value at which to evaluate */
    double  v,                /* <I> - v parameter value at which to evaluate */
    int     num_derivs_in_u,  /* <I> - number of derivatives in u direction */
    int     num_derivs_in_v,  /* <I> - number of derivatives in u direction */
    int     triang,           /* <I> - request for triangular array of
                                     derivatives.  UF_MODL_RECTANGULAR or
                                                 UF_MODL_TRIANGULAR  */
    double *results         /* <O> - evaluation results
                                 R - NO_ERROR
                                     UF_FORGEO_EVALUATOR_NOT_AVAILABLE
                                     UF_FORGEO_INCOMPLETE */
);

 /*****************************************************************************

  Register the callbacks for foreign surface processing.

*******************************************************************************/

/******************************************************************************
Registers the functions required to process foreign surfaces.
NOTE: It is not possible for NX to validate the function
pointers you pass in. However, if any of them are NULL, then an
error code of UF_FORGEO_FUNCTION_MISSING is returned

Environment: Internal and External

See Also:

History: This function was originally released in V15.0.

******************************************************************************/
extern UFUNEXPORT int UF_FORGEO_register_surface(
  UF_FORGEO_create_surface_f_t      create_function,     /* <I> - function to
                                                                invoke for
                                                                surface create
                                                         */
  UF_FORGEO_ask_surface_params_f_t  ask_params_function, /* <I> - function to
                                                                invoke for
                                                                initializing
                                                                the surface
                                                                parameterization
                                                         */
  UF_FORGEO_evaluate_surface_f_t    evaluate_function  /* <I> - function to
                                                                invoke to
                                                                evaluate the
                                                                surface
                                                         */

  );
#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif  /* UF_FORGEO_H_INCLUDED */
