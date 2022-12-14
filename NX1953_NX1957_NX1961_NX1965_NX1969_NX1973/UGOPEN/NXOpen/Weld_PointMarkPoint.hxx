#ifndef NXOpen_WELD_POINTMARKPOINT_HXX_INCLUDED
#define NXOpen_WELD_POINTMARKPOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_PointMarkPoint.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/Weld_IFeature.hxx>
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
        class PointMarkPoint;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class Body;
    namespace Features
    {
        class BodyFeature;
    }
    class INXObject;
    class Point;
    class ReferenceSet;
    namespace Weld
    {
        class IFeature;
    }
    namespace Weld
    {
        class _PointMarkPointBuilder;
        class PointMarkPointImpl;
        /** Represents a Weld.PointMarkPoint Feature.  <br> To create or edit an instance of this class, use @link NXOpen::Weld::PointMarkBuilder  NXOpen::Weld::PointMarkBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  PointMarkPoint : public NXOpen::Features::BodyFeature, public virtual NXOpen::Weld::IFeature
        {
            private: PointMarkPointImpl * m_pointmarkpoint_impl;
            private: friend class  _PointMarkPointBuilder;
            protected: PointMarkPoint();
            public: ~PointMarkPoint();
            /** Gets the Symbol(Point Marker) information 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : None */
            public: int GetPointMarker
            (
            );

            /// \cond NX_NO_DOC 
            /** Checks if feature is a @link NXOpen::Weld::PointMarkPoint NXOpen::Weld::PointMarkPoint@endlink  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsPointMarkPoint
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Returns the reference point of a @link NXOpen::Weld::PointMarkPoint NXOpen::Weld::PointMarkPoint@endlink  feature
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * GetReferencePoint
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Returns the connected bodies of a @link NXOpen::Weld::PointMarkPoint NXOpen::Weld::PointMarkPoint@endlink  feature
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetConnectedBodies
            (
                std::vector<NXOpen::Body *> & connectedBodies /** connectedbodies */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Returns the output point of a @link NXOpen::Weld::PointMarkPoint NXOpen::Weld::PointMarkPoint@endlink  feature
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * GetOutputPoint
            (
            );

            /// \endcond 
            /** Returns the feature diagnostic information, warning, or error codes. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void GetFeatureDiagnostics
            (
                std::vector<int> & diagnosticCodes /** the information, warning, or error codes for this feature. */
            );
            /** Gets the feature icon name. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXString GetFeatureIconName
            (
            );
            /** Gets the feature layer. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual int GetFeatureLayer
            (
            );
            /** Gets the feature color. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual int GetFeatureObjectColor
            (
            );
            /** Gets all the reference sets that this feature is a member of. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void GetFeatureReferenceSets
            (
                std::vector<NXOpen::ReferenceSet *> & refSet /** refset */ 
            );
            /** Gets all the reference sets that this feature is a member of. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void GetFeatureReferenceSetStrings
            (
                std::vector<NXString> & refSet /** refset */ 
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
