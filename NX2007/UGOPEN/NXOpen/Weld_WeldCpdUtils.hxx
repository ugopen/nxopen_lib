#ifndef NXOpen_WELD_WELDCPDUTILS_HXX_INCLUDED
#define NXOpen_WELD_WELDCPDUTILS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_WeldCpdUtils.ja
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
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class WeldCpdUtils;
    }
    class Session;
    class Curve;
    class NXObject;
    namespace Weld
    {
        class WeldCpdUtilsImpl;
        /**
            Provides methods for access a WeldCpdUtils class object in NX.
             <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  WeldCpdUtils
        {
            private: WeldCpdUtilsImpl * m_weldcpdutils_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit WeldCpdUtils(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~WeldCpdUtils();
            /** 
                    Return joint curves of a given welding joint feature.
                     @return  joint curves 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Curve *> GetJointCurvesFromWeldFeature
            (
                NXOpen::NXObject * featureTag /** weld feature */
            );
            /** 
                    Return Design Features of a given welding joint or surface weld feature.
                     @return  design features 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::NXObject *> GetDesignFeatureFromWeldFeature
            (
                NXOpen::NXObject * featureTag /** weld feature */
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