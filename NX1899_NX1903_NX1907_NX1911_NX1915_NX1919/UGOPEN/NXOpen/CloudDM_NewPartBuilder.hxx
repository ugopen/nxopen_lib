#ifndef NXOpen_CLOUDDM_NEWPARTBUILDER_HXX_INCLUDED
#define NXOpen_CLOUDDM_NEWPARTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CloudDM_NewPartBuilder.ja
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
#include <NXOpen/Builder.hxx>
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
        class NewPartBuilder;
    }
    class Builder;
    class NXObject;
    namespace CloudDM
    {
        class _NewPartBuilderBuilder;
        class NewPartBuilderImpl;

        /// \cond NX_NO_DOC 
        /** A builder that holds specific parameters for a part being
                created and to be managed in Cloud  <br> To create a new instance of this class, use @link NXOpen::PartCollection::CreateCloudDMNewPartBuilder  NXOpen::PartCollection::CreateCloudDMNewPartBuilder @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_CLOUDDMEXPORT  NewPartBuilder : public NXOpen::Builder
        {
            private: NewPartBuilderImpl * m_newpartbuilder_impl;
            private: friend class  _NewPartBuilderBuilder;
            protected: NewPartBuilder();
            public: ~NewPartBuilder();

            /// \cond NX_NO_DOC 
            /**Returns the Cloud project where the part belongs. This is optional. If not specified,
                       the current session project will be used.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Project
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets the Cloud project where the part belongs. This is optional. If not specified,
                       the current session project will be used.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetProject
            (
                const NXString & project /** project */ 
            );
            /**Sets the Cloud project where the part belongs. This is optional. If not specified,
                       the current session project will be used.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            void SetProject
            (
                const char * project /** project */ 
            );

            /// \endcond 
            /**Returns the name of Folder inside the Project where the part will be saved.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Folder
            (
            );
            /**Sets the name of Folder inside the Project where the part will be saved.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFolder
            (
                const NXString & folder /** folder */ 
            );
            /**Sets the name of Folder inside the Project where the part will be saved.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            void SetFolder
            (
                const char * folder /** folder */ 
            );
            /**Returns the name of the part. It is also the name of the Dataset in Cloud.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DesignName
            (
            );
            /**Sets the name of the part. It is also the name of the Dataset in Cloud.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDesignName
            (
                const NXString & name /** name */ 
            );
            /**Sets the name of the part. It is also the name of the Dataset in Cloud.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            void SetDesignName
            (
                const char * name /** name */ 
            );

            /// \cond NX_NO_DOC 
            /**Returns the Design Number 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DesignNumber
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets the Design Number 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDesignNumber
            (
                const NXString & number /** number */ 
            );
            /**Sets the Design Number 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            void SetDesignNumber
            (
                const char * number /** number */ 
            );

            /// \endcond 
            /** Auto-generates a number and assigns it to the Design Number.
                        Note: If the Design Number has already a value assigned,
                        then that is not replaced.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void AutoAssignDesignNumber
            (
            );

            /// \cond NX_NO_DOC 
            /**Returns the Design Revision 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DesignRevision
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets the Design Revision 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDesignRevision
            (
                const NXString & revision /** revision */ 
            );
            /**Sets the Design Revision 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            void SetDesignRevision
            (
                const char * revision /** revision */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns the Design Description 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DesignDescription
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets the Design Description 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDesignDescription
            (
                const NXString & description /** description */ 
            );
            /**Sets the Design Description 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            void SetDesignDescription
            (
                const char * description /** description */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the Attribute holder to hold attributes before new part is created 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * AttributeHolder
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Synchronize attributes from attribute holder object to builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SynchronizeAttributes
            (
            );

            /// \endcond 
        };

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