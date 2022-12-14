#ifndef NXOpen_CLOUDDM_DOCUMENTIDENTIFIER_HXX_INCLUDED
#define NXOpen_CLOUDDM_DOCUMENTIDENTIFIER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CloudDM_DocumentIdentifier.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_clouddm_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CloudDM
    {
        class DocumentIdentifier;
    }
    namespace CloudDM
    {
        class DocumentIdentifierImpl;

        /// \cond NX_NO_DOC 
        /** JA interface for design document identifier 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CLOUDDMEXPORT  DocumentIdentifier : public NXOpen::TransientObject
        {

            /// \cond NX_NO_DOC 
             /** Represents the lock information */
            public:
            struct LockInformation
            {
                public: /** lockedat */ NXString LockedAt;
                public: /** lockexpires */ NXString LockExpires;
                public: /** lockedby */ NXString LockedBy;
                public: LockInformation() :
                    LockedAt(),
                    LockExpires(),
                    LockedBy()
                {
                }
                /** Constructor for the LockInformation struct. */ 
                public: LockInformation(const NXString &lockedAtInitial /** lockedat */ , 
                        const NXString &lockExpiresInitial /** lockexpires */ , 
                        const NXString &lockedByInitial /** lockedby */ ) :
                    LockedAt(lockedAtInitial),
                    LockExpires(lockExpiresInitial),
                    LockedBy(lockedByInitial)
                {
                }
            };


            /// \endcond 
            private: DocumentIdentifierImpl * m_documentidentifier_impl;
            /// \cond NX_NO_DOC 
            public: explicit DocumentIdentifier(void *ptr);
            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Frees the memory associated with this object. After invocation of this method, the object is no longer valid.  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~DocumentIdentifier();

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the document name 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the urn of the design revision 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString RevisionUrn
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the document last date modified 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DateModified
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the document owner 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Owner
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the document urn 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DocumentUrn
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the lock information 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CloudDM::DocumentIdentifier::LockInformation LockInfo
            (
            );

            /// \endcond 
        }; //lint !e1712 default constructor not defined for class  


        /// \endcond 
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
