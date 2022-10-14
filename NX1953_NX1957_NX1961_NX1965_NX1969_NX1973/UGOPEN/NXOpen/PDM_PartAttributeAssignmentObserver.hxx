#ifndef NXOpen_PDM_PARTATTRIBUTEASSIGNMENTOBSERVER_HXX_INCLUDED
#define NXOpen_PDM_PARTATTRIBUTEASSIGNMENTOBSERVER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_PartAttributeAssignmentObserver.ja
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
#include <NXOpen/TaggedObject.hxx>
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
        class PartAttributeAssignmentObserver;
    }
    namespace PDM
    {
        class PdmSession;
    }
    namespace PDM
    {
        class PartAttributeAssignmentObserverCallbackData;
    }
    namespace PDM
    {
        class PartAttributeAssignmentObserverImpl;
        /** This class is responsible for invoking user registered callback on attribute assignment in NX  <br> To obtain an instance of this class, refer to @link NXOpen::PDM::PdmSession  NXOpen::PDM::PdmSession @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  PartAttributeAssignmentObserver
        {
            public: /** User defined function which accepts logical objects and gets called on part attribute assignment
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback1<void, NXOpen::PDM::PartAttributeAssignmentObserverCallbackData *> UserFunctionHandler;
            private: PartAttributeAssignmentObserverImpl * m_partattributeassignmentobserver_impl;
            private: NXOpen::PDM::PdmSession* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit PartAttributeAssignmentObserver(NXOpen::PDM::PdmSession *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~PartAttributeAssignmentObserver();
            /** This function registers the user-defined function  @return  The indentifier of the method being registered. This can be used to unregister (using UnRegisterUserDefinedFunction()) if needed  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: int RegisterUserDefinedFunction
            (
                const NXOpen::PDM::PartAttributeAssignmentObserver::UserFunctionHandler&  handler /** method to register */
            );
            /** This function unregisters the user-defined function 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void UnRegisterUserDefinedFunction
            (
                int id /** identifier for method to unregister */
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