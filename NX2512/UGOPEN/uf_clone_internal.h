/*==================================================================================================

             Copyright 2009 UGS Corp.
             All rights reserved.
 ====================================================================================================
File description:

    Definitions and functions for encryption methods used by uf_clone.

*
===================================================================================================*/

#ifndef UF_CLONE_INTERNAL_INCLUDE
#define UF_CLONE_INTERNAL_INCLUDE

#include <libufun_exports.h>

#define MAX_CRYPTO_SIZE             2000

#ifdef  __cplusplus
extern "C" {
#endif


/************************************************************************

This routine loads a specific library

Environment : Internal  and  External
See Also:
History : Originally released in NX5.0.7
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_load_crypt();

/************************************************************************

This routine can be used to decode a value if the encryption method
and other values are known.

Environment : Internal  and  External
See Also:
History : Originally released in NX5.0.7
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_decode(unsigned const char *aesKey, /* <I> */
                                       const char *inp_string,      /* <I> */
                                       int str_length,              /* <I> */
                                       char *decoded_str            /* <O> */
                                       );

/************************************************************************

This routine converts a base64 string to bytes.

Environment : Internal  and  External
See Also:
History : Originally released in NX5.0.7
***********************************************************************/
extern UFUNEXPORT int  UF_CLONE_base_64_to_bytes( unsigned char *bytes,  /* <O> */
                                              int *nbytes,            /* <O> */
                                              char  *data,            /* <I> */
                                              int offset,             /* <I> */
                                              int length              /* <I> */
                                              );

/************************************************************************

This routine returns a key.

Environment : Internal  and  External
See Also:
History : Originally released in NX5.0.7
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_get_key(unsigned char* aesKey /* <O> */
                                        );
#ifdef __cplusplus
}
#endif



#endif
