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

#define MAX_MD_SIZE                 64
#define MAX_KEY_LENGTH              32
#define MAX_IV_LENGTH               16
#define MAX_BLOCK_LENGTH            32
#define MAX_CRYPTO_SIZE             2000

#define TCCRYPTO_CIPHER_TYPE_aes_128_ecb     "aes-128-ecb"
#define TCCRYPTO_DIGEST_TYPE_sha1            "SHA1"
#ifdef  __cplusplus
extern "C" {
#endif

    typedef struct TcCryptoContext TcCryptoContext;

    /* <summary>
     Lists the error codes returned by the <c>TcCrypto</c> APIs.
     </summary>
     <seealso cref="TcCrypto.TcCrypto_System_GetLastError" />
    */
    typedef enum 
    {
        /* <summary>
         Indicates there no error has occurred
         </summary>
        */
        TcCryptoError_Ok    = 0,

        /* <summary>
        /// Indicates an SSL occurred in the underlying <c>OpenSSL</c> libraries.  
        /// Passing a buffer to <see cref="TcCrypto.TcCrypto_System_GetLastError"/>  will let 
        /// you see what the specific error occurred in the <c>OpenSSL</c> code.
        /// If this error code is returned, you can call the <c>OpenSsl</c> APIs to find out
        /// more details.  The interesting APIs are <c>ERR_get_error</c>, <c>ERR_peek_last_error</c>, etc.
        /// </summary>
        */
        TcCryptoError_SslInternal   = 1,

        /* <summary>
        /// Indicates the crypto system needs to be initialized with a call to 
        /// <see cref="TcCrypto.TcCrypto_System_Initialize"/> 
        /// </summary>
        */
        TcCryptoError_SystemNotInitialized = 2,

        /* <summary>
        /// Indicates the requested algorithm is not available, when calling 
        /// <see cref="TcCrypto.TcCrypto_Cipher_GetContext"/>, <see cref="TcCrypto.TcCrypto_Digest_GetContext"/> 
        /// <see cref="TcCrypto.TcCrypto_Hmac_GetContext"/>, <see cref="TcCrypto.TcCrypto_Signature_GetContext"/>.
        /// This can happen if a non-FIPS allowed algorithm (like MD5) is requested from a system initialized
        /// in FIPS mode.
        /// </summary>
        */
        TcCryptoError_AlgorithmNotAvailable = 3,

        /* <summary>
        /// Indicates a problem with the <see cref="TcCryptoContext"/>.  This may occur 
        /// when the context is <c>NULL</c> or if the context was created as one type (ie: Digest)
        /// and passed to a different type of method (ie: Signature)
        /// </summary>
        */
        TcCryptoError_InvalidContext = 4,

        /* <summary>
        /// Indicates the system type passed to <see cref="TcCrypto.TcCrypto_System_Initialize"/> is not recognized.
        /// System type must be one of <c>TcCrypto_SystemType_Domestic</c>) or <c>TcCrypto_SystemType_Fips</c>.
        /// </summary>
        */
        TcCryptoError_UnknownSystemType = 5,

        /* <summary>
        /// Indicates the crypto system has not been shut down by calling <see cref="TcCrypto.TcCrypto_System_Shutdown"/>
        /// before attempting to reinitialize it with <see cref="TcCrypto.TcCrypto_System_Initialize"/>).
        /// </summary>
        /// <seealso cref="TcCrypto.TcCrypto_System_Initialize" />
        */
        TcCryptoError_SystemAlreadyInitialized = 6,

        /* <summary>
        /// Indicates the operation failed because the system was unable to allocate sufficient memory
        /// </summary>
        */
        TcCryptoError_MemoryAllocationFailed = 7,

        /* <summary>
        /// Indicates the library hit a critical error during startup.  No crypto will be available.
        /// This is set if the FIPS self-tests fail.
        /// </summary>
        */
        TcCryptoError_FailedToInitialize = 8

    } TcCryptoError;

    /* <summary>
    /// Lists the different modes the system can be intitialized with.
    /// </summary>
    */
    typedef enum 
    {
        /* <summary>
        /// Represents the state that is returned before the library is configured.
        /// </summary>
        */
        TcCrypto_SystemType_Undefined = 0,

        /* <summary>
        /// Domestic mode provides the most security options, including some algorithms that are
        /// insecure or marginally secure, like <c>MD5</c>.  This mode is good for applications
        /// that don't require the higher <c>FIPS</c> security, or need to support interop with
        /// legacy applications that require these other algorithms.
        /// </summary>
        */
        TcCrypto_SystemType_Domestic  = 1,

        /* <summary>
        /// FIPS mode is the most secure, allowing only secure algorithms.  Some insecure algorithms
        /// like <c>MD5</c> will not be allowed in FIPS mode.
        /// </summary>
        */
        TcCrypto_SystemType_Fips      = 2

    } TcCryptoSystemType;

    int TcCrypto_System_Initialize(TcCryptoSystemType systemType);
    TcCryptoContext* TcCrypto_Cipher_GetContext(const char *);
    void TcCrypto_Cipher_Init(TcCryptoContext* context, const void* key, int keyLength, const  void* iv, int ivLength, int encrypt);
    void TcCrypto_Cipher_SetPadding(TcCryptoContext* context, int usePadding);
    int TcCrypto_Cipher_Update(TcCryptoContext* context, void* outbuf, int* outlenPtr, const void* inbuf, int inlen);
    int TcCrypto_Cipher_Final(TcCryptoContext* context, void*  outbuf, int* outlenPtr);
    void TcCrypto_System_FreeContext(TcCryptoContext* );
    TcCryptoContext* TcCrypto_Digest_GetContext(const char *);
    void TcCrypto_Digest_Init(TcCryptoContext*);
    int TcCrypto_Digest_Update(TcCryptoContext* context, const void* inbuf, int inlen);
    int TcCrypto_Digest_Final(TcCryptoContext* context, void*  outbuf, unsigned int* outlen);
    void TcCrypto_System_Shutdown();

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

/*
$  Function pointers for use with GetProcAddress and dynamic
$  loading of the library on NT. Need to match
$  with the actual entry points listed below.
*/
typedef int  (*TcCrypto_System_Initializefunc)(TcCryptoSystemType systemType);
typedef TcCryptoContext*  (*TcCrypto_Cipher_GetContextfunc)(const char *);
typedef void  (*TcCrypto_Cipher_Initfunc)(TcCryptoContext* context, const void* key, int keyLength, const  void* iv, int ivLength, int encrypt);
typedef void  (*TcCrypto_Cipher_SetPaddingfunc)(TcCryptoContext* context, int usePadding);
typedef int  (*TcCrypto_Cipher_Updatefunc)(TcCryptoContext* context, void* outbuf, int* outlenPtr, const void* inbuf, int inlen);
typedef int  (*TcCrypto_Cipher_Finalfunc)(TcCryptoContext* context, void*  outbuf, int* outlenPtr);
typedef void  (*TcCrypto_System_FreeContextfunc)(TcCryptoContext* );
typedef TcCryptoContext*  (*TcCrypto_Digest_GetContextfunc)(const char *);
typedef void  (*TcCrypto_Digest_Initfunc)(TcCryptoContext* );
typedef int  (*TcCrypto_Digest_Updatefunc)(TcCryptoContext* context, const void* inbuf, int inlen);
typedef int  (*TcCrypto_Digest_Finalfunc)(TcCryptoContext* context, void*  outbuf, unsigned int* outlen);
typedef void  (*TcCrypto_System_Shutdownfunc)();

#endif
