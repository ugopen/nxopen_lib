#ifndef NXOpen_ROUTINGCOMMON_ASSIGNCOMPONENTNAMEBUILDER_HXX_INCLUDED
#define NXOpen_ROUTINGCOMMON_ASSIGNCOMPONENTNAMEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     RoutingCommon_AssignComponentNameBuilder.ja
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
#include <NXOpen/libnxopencpp_routingcommon_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace RoutingCommon
    {
        class AssignComponentNameBuilder;
    }
    class Builder;
    namespace PDM
    {
        class LogicalObject;
    }
    namespace RoutingCommon
    {
        class _AssignComponentNameBuilderBuilder;
        class AssignComponentNameBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Represents @link NXOpen::RoutingCommon::AssignComponentNameBuilder NXOpen::RoutingCommon::AssignComponentNameBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::RoutingCommon::BuilderFactory::CreateAssignComponentNameBuilder  NXOpen::RoutingCommon::BuilderFactory::CreateAssignComponentNameBuilder @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGCOMMONEXPORT  AssignComponentNameBuilder : public NXOpen::Builder
        {
            private: AssignComponentNameBuilderImpl * m_assigncomponentnamebuilder_impl;
            private: friend class  _AssignComponentNameBuilderBuilder;
            protected: AssignComponentNameBuilder();
            public: ~AssignComponentNameBuilder();
            /** Sets part spec on logical object
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetPartSpecOnLogicalObject
            (
                NXOpen::PDM::LogicalObject * logicalObject /** This parameter may not be NULL.*/,
                const NXString & partSpec /** part spec to set on logical object This parameter may not be NULL.*/
            );
            /** Sets part spec on logical object
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetPartSpecOnLogicalObject
            (
                NXOpen::PDM::LogicalObject * logicalObject /** This parameter may not be NULL.*/,
                const char * partSpec /** part spec to set on logical object This parameter may not be NULL.*/
            );
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
