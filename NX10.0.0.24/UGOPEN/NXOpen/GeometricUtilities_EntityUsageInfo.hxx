#ifndef NXOpen_GEOMETRICUTILITIES_ENTITYUSAGEINFO_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_ENTITYUSAGEINFO_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_EntityUsageInfo.ja
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
#include <NXOpen/GeometricUtilities_EntityUsageInfo.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class EntityUsageInfo;
    }
    class DisplayableObject;
    namespace Features
    {
        class Feature;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class NXObject;
    namespace GeometricUtilities
    {
        class _EntityUsageInfoBuilder;
        class EntityUsageInfoImpl;
        /**
            Represents a @link NXOpen::GeometricUtilities::EntityUsageInfo NXOpen::GeometricUtilities::EntityUsageInfo@endlink . An object of this class provides the
            dependency information for a single reparentable entity (edge or face). The creation of @link NXOpen::GeometricUtilities::EntityUsageInfo NXOpen::GeometricUtilities::EntityUsageInfo@endlink 
            is restricted for internal use (see @link NXOpen::GeometricUtilities::ReplAsstBuilder NXOpen::GeometricUtilities::ReplAsstBuilder@endlink ).
            
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  EntityUsageInfo : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** enum for usage status */
            public: enum Status
            {
                StatusUnused/** unused */,
                StatusIntraPart/** used in same part */,
                StatusInterPart/** used interpart */
            };

            private: EntityUsageInfoImpl * m_entityusageinfo_impl;
            private: friend class  _EntityUsageInfoBuilder;
            protected: EntityUsageInfo();
            public: ~EntityUsageInfo();
            /**Returns  the important entity. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DisplayableObject * Entity
            (
            );
            /** Query the dependent features of this entity. Use 'typeOfUsage' to restrict the query to
                        intra-part features or to include interpart features too. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void GetDependentFeatures
            (
                NXOpen::GeometricUtilities::EntityUsageInfo::Status typeOfUsage /** desired level of usage information */,
                std::vector<NXOpen::Features::Feature *> & dependentFeatures /** dependent features */,
                std::vector<NXString> & detailedUsageInfo /** detailed usage information for each dependent feature */
            );
            /** Query other dependents of this entity. Use 'typeOfUsage' to restrict the query to
                        intra-part dependents or to include interpart usage too. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void GetOtherDependents
            (
                NXOpen::GeometricUtilities::EntityUsageInfo::Status typeOfUsage /** desired level of usage information */,
                std::vector<NXOpen::NXObject *> & otherDependents /** dependent objects */,
                std::vector<NXString> & detailedUsageInfo /** detailed usage information for each dependent object */
            );
            /**Returns  the usage status of the corresponding entity 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::EntityUsageInfo::Status UsageStatus
            (
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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
