#ifndef NXOpen_PDM_PARTATTRIBUTEASSIGNMENTOBSERVERCALLBACKDATA_HXX_INCLUDED
#define NXOpen_PDM_PARTATTRIBUTEASSIGNMENTOBSERVERCALLBACKDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_PartAttributeAssignmentObserverCallbackData.ja
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
        class PartAttributeAssignmentObserverCallbackData;
    }
    namespace PDM
    {
        class LogicalObject;
    }
    namespace PDM
    {
        class _PartAttributeAssignmentObserverCallbackDataBuilder;
        class PartAttributeAssignmentObserverCallbackDataImpl;
        /** JA interface for PartAttributeAssignmentObserverCallbackData object  <br> This cannot be created  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  PartAttributeAssignmentObserverCallbackData : public NXOpen::TaggedObject
        {
            private: PartAttributeAssignmentObserverCallbackDataImpl * m_partattributeassignmentobservercallbackdata_impl;
            private: friend class  _PartAttributeAssignmentObserverCallbackDataBuilder;
            protected: PartAttributeAssignmentObserverCallbackData();
            public: ~PartAttributeAssignmentObserverCallbackData();
            /** Gets the @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  for NX Objects participating in attribute assignment operation 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetLogicalObjects
            (
                std::vector<NXOpen::PDM::LogicalObject *> & logicalObjects /** logicalobjects */ 
            );
        };
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