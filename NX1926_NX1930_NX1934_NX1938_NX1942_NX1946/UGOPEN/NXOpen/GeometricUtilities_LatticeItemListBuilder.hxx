#ifndef NXOpen_GEOMETRICUTILITIES_LATTICEITEMLISTBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_LATTICEITEMLISTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_LatticeItemListBuilder.ja
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
#include <NXOpen/GeometricUtilities_LatticeItemBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ObjectList.hxx>
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
        class LatticeItemListBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class LatticeItemBuilder;
    }
    namespace GeometricUtilities
    {
        class LatticeItemBuilderList;
    }
    namespace GeometricUtilities
    {
        class _LatticeItemListBuilderBuilder;
        class LatticeItemListBuilderImpl;
        /** Represents a LatticeItemList 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  LatticeItemListBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: LatticeItemListBuilderImpl * m_latticeitemlistbuilder_impl;
            private: friend class  _LatticeItemListBuilderBuilder;
            protected: LatticeItemListBuilder();
            public: ~LatticeItemListBuilder();
            /**Returns  the section defining the lattice body options. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LatticeItemBuilderList * LatticeItemList
            (
            );
            /** Creates a GeometricUtilities.LatticeItemBuilder 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_additive_design (" NX Additive Design") */
            public: NXOpen::GeometricUtilities::LatticeItemBuilder * CreateLatticeItemBuilder
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