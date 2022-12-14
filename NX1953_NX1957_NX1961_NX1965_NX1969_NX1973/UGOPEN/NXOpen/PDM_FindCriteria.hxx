#ifndef NXOpen_PDM_FINDCRITERIA_HXX_INCLUDED
#define NXOpen_PDM_FINDCRITERIA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_FindCriteria.ja
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
#include <NXOpen/libnxopencpp_pdm_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PDM
    {
        class FindCriteria;
    }
    namespace PDM
    {
    }
    namespace PDM
    {
        class FindCriteriaImpl;
        /** Represents find criteria objects 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  FindCriteria : public NXOpen::TransientObject
        {
            private: FindCriteriaImpl * m_findcriteria_impl;
            /// \cond NX_NO_DOC 
            public: explicit FindCriteria(void *ptr);
            /// \endcond 
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~FindCriteria();
            /** This API sets the search query name, entries, and values. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCriteria
            (
                const NXString & queryName /** Search query name */,
                std::vector<NXString> & entries /** Search criteria entries */,
                std::vector<NXString> & values /** Search criteria values */
            );
            /** This API sets the search query name, entries, and values. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            void SetCriteria
            (
                const char * queryName /** Search query name */,
                std::vector<NXString> & entries /** Search criteria entries */,
                std::vector<NXString> & values /** Search criteria values */
            );
            /** This API returns the search query name, entries, and values. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void GetCriteria
            (
                NXString* queryName /** Search query name */,
                std::vector<NXString> & entries /** Search criteria entries */,
                std::vector<NXString> & values /** Search criteria values */
            );
        }; //lint !e1712 default constructor not defined for class  

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
