#ifndef NXOpen_GEOMETRICUTILITIES_SELECTIONLIST_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_SELECTIONLIST_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_SelectionList.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class SelectionList;
    }
    class NXObject;
    class SelectDisplayableObjectList;
    namespace GeometricUtilities
    {
        class _SelectionListBuilder;
        class SelectionListImpl;
        /** Represents a @link NXOpen::GeometricUtilities::SelectionList NXOpen::GeometricUtilities::SelectionList@endlink   <br> To create a new instance of this class, use @link NXOpen::Part::CreateSelectionList  NXOpen::Part::CreateSelectionList @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  SelectionList : public NXOpen::NXObject
        {
            private: SelectionListImpl * m_selectionlist_impl;
            private: friend class  _SelectionListBuilder;
            protected: SelectionList();
            public: ~SelectionList();
            /**Returns  the list of geometries  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectObjectList
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
