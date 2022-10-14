#ifndef NXOpen_CAE_AEROSTRUCTURES_LAMINATEHELPER_HXX_INCLUDED
#define NXOpen_CAE_AEROSTRUCTURES_LAMINATEHELPER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AeroStructures_LaminateHelper.ja
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
#include <NXOpen/CAE_AeroStructures_Laminate.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        namespace AeroStructures
        {
            class LaminateHelper;
        }
    }
    class Session;
    namespace CAE
    {
        namespace AeroStructures
        {
            class LocalLaminate;
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            class LaminateHelperImpl;
            /** Represents a @link NXOpen::CAE::AeroStructures::LaminateHelper NXOpen::CAE::AeroStructures::LaminateHelper@endlink  object.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  LaminateHelper
            {
                private: LaminateHelperImpl * m_laminatehelper_impl;
                private: NXOpen::Session* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit LaminateHelper(NXOpen::Session *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                private: static LaminateHelper* theLaminateHelper;
                /** Returns the LaminateHelper object for the running session which serves as the 'gateway' class for the application API.  
                    References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                    Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
                */
                public: static LaminateHelper* GetLaminateHelper(NXOpen::Session *owner);
                public: ~LaminateHelper();
                /** Create an empty local laminate 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: NXOpen::CAE::AeroStructures::LocalLaminate * NewLocalLaminate
                (
                );
            }; //lint !e1712 default constructor not defined for class  

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