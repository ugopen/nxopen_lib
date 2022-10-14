#ifndef NXOpen_GEOMETRICUTILITIES_BLENDLIMITSDATA_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_BLENDLIMITSDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_BlendLimitsData.ja
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
        class BlendLimitsData;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class TaggedObjectList;
    namespace GeometricUtilities
    {
        class _BlendLimitsDataBuilder;
        class BlendLimitsDataImpl;
        /**
            Represents a @link NXOpen::GeometricUtilities::BlendLimitsData NXOpen::GeometricUtilities::BlendLimitsData@endlink 
            
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  BlendLimitsData : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: BlendLimitsDataImpl * m_blendlimitsdata_impl;
            private: friend class  _BlendLimitsDataBuilder;
            protected: BlendLimitsData();
            public: ~BlendLimitsData();
            /**Returns  the caps list 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObjectList * CapsList
            (
            );
            /**Returns  the use plane cap blend 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool UserSelectedObjects
            (
            );
            /**Sets  the use plane cap blend 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetUserSelectedObjects
            (
                bool useSelectedObject /** useselectedobject */ 
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