#ifndef NXOpen_CAE_RESULTMEASURERESULTDIRECTIONOPTIONS_HXX_INCLUDED
#define NXOpen_CAE_RESULTMEASURERESULTDIRECTIONOPTIONS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResultMeasureResultDirectionOptions.ja
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
#include <NXOpen/CAE_Result.hxx>
#include <NXOpen/CAE_ResultMeasureResultOptions.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class ResultMeasureResultDirectionOptions;
    }
    namespace CAE
    {
        class ResultMeasureResultOptions;
    }
    namespace CAE
    {
    }
    namespace CAE
    {
        class ResultMeasureResultDirectionOptionsImpl;
        /**
            Represents the result directional options for result measure
             <br> To obtain an instance of this class use @link CAE::ResultMeasureCollection CAE::ResultMeasureCollection@endlink .  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ResultMeasureResultDirectionOptions : public NXOpen::CAE::ResultMeasureResultOptions
        {
            private: ResultMeasureResultDirectionOptionsImpl * m_resultmeasureresultdirectionoptions_impl;
            /// \cond NX_NO_DOC 
            public: explicit ResultMeasureResultDirectionOptions(void *ptr);
            /// \endcond 
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: virtual ~ResultMeasureResultDirectionOptions();
            /** Set the coordinate system for directional components 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCoordinateSystem
            (
                NXOpen::CAE::Result::CoordinateSystem eCsys /** ecsys */ 
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
