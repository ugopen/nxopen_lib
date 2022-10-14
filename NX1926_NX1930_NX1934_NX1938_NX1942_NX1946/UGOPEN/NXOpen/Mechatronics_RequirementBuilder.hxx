#ifndef NXOpen_MECHATRONICS_REQUIREMENTBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_REQUIREMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_RequirementBuilder.ja
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
#include <NXOpen/Mechatronics_ObjectInformationBuilder.hxx>
#include <NXOpen/Mechatronics_SystemObjectBuilder.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class RequirementBuilder;
    }
    namespace Mechatronics
    {
        class ObjectInformationBuilder;
    }
    namespace Mechatronics
    {
        class SystemObjectBuilder;
    }
    class NXObject;
    namespace Mechatronics
    {
        class _RequirementBuilderBuilder;
        class RequirementBuilderImpl;
        /** Represents a @link NXOpen::Mechatronics::Requirement NXOpen::Mechatronics::Requirement@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Mechatronics::RequirementCollection::CreateRequirementBuilder  NXOpen::Mechatronics::RequirementCollection::CreateRequirementBuilder @endlink  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  RequirementBuilder : public NXOpen::Mechatronics::SystemObjectBuilder
        {
            private: RequirementBuilderImpl * m_requirementbuilder_impl;
            private: friend class  _RequirementBuilderBuilder;
            protected: RequirementBuilder();
            public: ~RequirementBuilder();
            /**Returns  the parent object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::NXObject * ParentFunction
            (
            );
            /**Sets  the parent object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetParentFunction
            (
                NXOpen::NXObject * parent /** Parent function object */
            );
            /**Returns  the object information builder, used to specify the information of requirement object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Mechatronics::ObjectInformationBuilder * ObjectInformation
            (
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