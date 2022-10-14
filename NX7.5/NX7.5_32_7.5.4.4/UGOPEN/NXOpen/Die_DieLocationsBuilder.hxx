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
#include <NXOpen/Die_DieLocationsBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
            Represents a @link Die::DieLocationsBuilder Die::DieLocationsBuilder@endlink . The Die 
            Locations is a helper to the main Die Design feature to gather the 
            location points for items such as hole center or clamping slot location.
            Note that a non-point is selected, such as a plane or coordinate system,
            the control point of the object will be used for the location.
             <br> To create a new instance of this class, use @link Die::DieCollection::CreateDieLocations Die::DieCollection::CreateDieLocations@endlink  <br> */
        class NXOPENCPPEXPORT  DieLocationsBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: DieLocationsBuilderImpl * m_dielocationsbuilder_impl;
            private: friend class  _DieLocationsBuilderBuilder;
            protected: DieLocationsBuilder();
            public: ~DieLocationsBuilder();
            /**Returns  the list containing the die location objects <br> License requirements : None */
            public: NXOpen::Die::DieLocationBuilderList * List
            (
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif