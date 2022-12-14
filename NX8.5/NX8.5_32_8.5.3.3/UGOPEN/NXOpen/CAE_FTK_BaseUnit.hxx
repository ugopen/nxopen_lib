#ifndef NXOpen_CAE_FTK_BASEUNIT_HXX_INCLUDED
#define NXOpen_CAE_FTK_BASEUNIT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FTK_BaseUnit.ja
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
#include <NXOpen/CAE_FTK_BaseUnit.hxx>
#include <NXOpen/NXObject.hxx>
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
        namespace FTK
        {
            class BaseUnit;
        }
    }
    class NXObject;
    namespace CAE
    {
        namespace FTK
        {
            class _BaseUnitBuilder;
            class BaseUnitImpl;
            /** Manages the base unit  <br> Not support KF.  <br> 
             <br>  Created in NX7.5.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  BaseUnit : public NXObject
            {
                private: BaseUnitImpl * m_baseunit_impl;
                private: friend class  _BaseUnitBuilder;
                protected: BaseUnit();
                public: ~BaseUnit();
                /** Sets measure name 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetMeasureName
                (
                    const NXString & measureName /** Measure name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** Sets measure name 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                void SetMeasureName
                (
                    const char * measureName /** Measure name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** Sets unit name 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetUnitName
                (
                    const NXString & unitName /** Unit name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** Sets unit name 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                void SetUnitName
                (
                    const char * unitName /** Unit name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
            };
        }
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
