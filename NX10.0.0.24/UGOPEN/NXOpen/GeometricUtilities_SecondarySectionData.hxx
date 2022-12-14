#ifndef NXOpen_GEOMETRICUTILITIES_SECONDARYSECTIONDATA_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_SECONDARYSECTIONDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_SecondarySectionData.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/GeometricUtilities_SecondarySectionData.hxx>
#include <NXOpen/NXObject.hxx>
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
        class SecondarySectionData;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class Extend;
    }
    class NXObject;
    namespace GeometricUtilities
    {
        class _SecondarySectionDataBuilder;
        class SecondarySectionDataImpl;
        /**
            Represents a @link NXOpen::GeometricUtilities::SecondarySectionData NXOpen::GeometricUtilities::SecondarySectionData@endlink 
            
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  SecondarySectionData : public NXOpen::NXObject
        {
            private: SecondarySectionDataImpl * m_secondarysectiondata_impl;
            private: friend class  _SecondarySectionDataBuilder;
            protected: SecondarySectionData();
            public: ~SecondarySectionData();
            /**Returns  the on path dim 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Extend * OnPathDimData
            (
            );
            /** Get the Secondary Sketch Expression Values @return  Dim Expressions 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetSecondarySectionValues
            (
            );
            /** Set the Secondary Sketch Expression Values. 
                        These values should be in the same sequence as the master sketch.
                        You can call @link NXOpen::Sketch::GetAllExpressions NXOpen::Sketch::GetAllExpressions@endlink  to get the exact
                        sequence of expression values.
                      
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSecondarySectionValues
            (
                std::vector<NXString> & expressions /**  Dim Expression */
            );
            /** Get the Master Sketch Expression Values @return  All the expressions in the sketch 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Expression *> GetMasterExpressionValues
            (
            );
            /** Set the Master Sketch Expression Values. 
                      
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMasterExpressionValues
            (
                const std::vector<NXOpen::Expression *> & expressions /** All the expressions in the sketch */
            );
            /**Sets  the Start Section  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStartSection
            (
                bool startSection /** startsection */ 
            );
            /**Returns  the Start Section  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsStartSection
            (
            );
            /**Sets  the End Section  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetEndSection
            (
                bool endSection /** endsection */ 
            );
            /**Returns  the End Section  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsEndSection
            (
            );
            /** Delete the secondary section object.
                      
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void Destroy
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
