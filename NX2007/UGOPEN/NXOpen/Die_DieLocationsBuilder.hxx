#ifndef NXOpen_DIE_DIELOCATIONSBUILDER_HXX_INCLUDED
#define NXOpen_DIE_DIELOCATIONSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_DieLocationsBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/libnxopencpp_die_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Die
    {
        class DieLocationsBuilder;
    }
    namespace Die
    {
        class DieLocationBuilderList;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Die
    {
        class _DieLocationsBuilderBuilder;
        class DieLocationsBuilderImpl;
        /**
            Represents a @link NXOpen::Die::DieLocationsBuilder NXOpen::Die::DieLocationsBuilder@endlink . The Die 
            Locations is a helper to the main Die Design feature to gather the 
            location points for items such as hole center or clamping slot location.
            Note that a non-point is selected, such as a plane or coordinate system,
            the control point of the object will be used for the location.
             <br> To create a new instance of this class, use @link NXOpen::Die::DieCollection::CreateDieLocations  NXOpen::Die::DieCollection::CreateDieLocations @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  DieLocationsBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: DieLocationsBuilderImpl * m_dielocationsbuilder_impl;
            private: friend class  _DieLocationsBuilderBuilder;
            protected: DieLocationsBuilder();
            public: ~DieLocationsBuilder();
            /**Returns  the list containing the die location objects
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DieLocationBuilderList * List
            (
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not yet implemented
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