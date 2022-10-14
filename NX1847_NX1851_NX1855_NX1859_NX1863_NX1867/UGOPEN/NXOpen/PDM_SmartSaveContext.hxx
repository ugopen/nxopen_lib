#ifndef NXOpen_PDM_SMARTSAVECONTEXT_HXX_INCLUDED
#define NXOpen_PDM_SMARTSAVECONTEXT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_SmartSaveContext.ja
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
#include <NXOpen/PDM_SmartSaveBuilder.hxx>
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
        class SmartSaveContext;
    }
    class TaggedObject;
    namespace PDM
    {
        class SmartSaveContextImpl;
        /** Represents smart save context  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreateSmartSaveContext  NXOpen::PDM::PdmSession::CreateSmartSaveContext @endlink  <br> 
         <br>  Created in NX11.0.1.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  SmartSaveContext : public NXOpen::TransientObject
        {
            private: SmartSaveContextImpl * m_smartsavecontext_impl;
            /// \cond NX_NO_DOC 
            public: explicit SmartSaveContext(void *ptr);
            /// \endcond 
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.  
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: virtual ~SmartSaveContext();
            /** Adds the given set of work object to root object pairs to the context 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetWorkObjectToRootObjectMap
            (
                const std::vector<NXOpen::TaggedObject *> & workObjects /** array of work objects to be saved */,
                const std::vector<NXOpen::TaggedObject *> & rootObjects /** array of root objects */
            );
            /** Returns the set of work object to root object pairs from the context 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void GetWorkObjectToRootObjectMap
            (
                std::vector<NXOpen::TaggedObject *> & workObjects /** array of work objects to be saved */,
                std::vector<NXOpen::TaggedObject *> & rootObjects /** array of root objects  */
            );
            /** Returns the save operation type  @return   
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::SmartSaveBuilder::SaveType GetSaveType
            (
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