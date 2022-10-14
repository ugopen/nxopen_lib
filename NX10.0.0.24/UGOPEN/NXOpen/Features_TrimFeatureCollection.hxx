#ifndef NXOpen_FEATURES_TRIMFEATURECOLLECTION_HXX_INCLUDED
#define NXOpen_FEATURES_TRIMFEATURECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TrimFeatureCollection.ja
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
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class TrimFeatureCollection;
    }
    namespace Features
    {
        class FeatureCollection;
    }
    namespace Features
    {
        class ExtendSheet;
    }
    namespace Features
    {
        class ExtendSheetBuilder;
    }
    namespace Features
    {
        class TrimAndExtend;
    }
    namespace Features
    {
        class TrimAndExtendBuilder;
    }
    namespace Features
    {
        class TrimFeatureCollectionImpl;
        /** Manages design features.  <br> To obtain an instance of this class, refer to @link NXOpen::Features::FeatureCollection  NXOpen::Features::FeatureCollection @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  TrimFeatureCollection
        {
            private: TrimFeatureCollectionImpl * m_trimfeaturecollection_impl;
            private: NXOpen::Features::FeatureCollection* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit TrimFeatureCollection(NXOpen::Features::FeatureCollection *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~TrimFeatureCollection();
            /** Creates a @link Features::ExtendSheetBuilder Features::ExtendSheetBuilder@endlink   @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::ExtendSheetBuilder * CreateExtendSheetBuilder
            (
                NXOpen::Features::ExtendSheet * extendSheet /** @link Features::ExtendSheet Features::ExtendSheet@endlink  to be edited */
            );
            /** Creates a @link Features::TrimAndExtendBuilder Features::TrimAndExtendBuilder@endlink   @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::TrimAndExtendBuilder * CreateTrimAndExtendBuilder
            (
                NXOpen::Features::TrimAndExtend * trimAndExtendSheet /** @link Features::TrimAndExtend Features::TrimAndExtend@endlink  to be edited */
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