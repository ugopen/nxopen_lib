#ifndef NXOpen_CAE_DURABILITYEXCITATION_HXX_INCLUDED
#define NXOpen_CAE_DURABILITYEXCITATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurabilityExcitation.ja
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
        class DurabilityExcitation;
    }
    class NXObject;
    namespace CAE
    {
        class _DurabilityExcitationBuilder;
        class DurabilityExcitationImpl;
        /** Represents a @link NXOpen::CAE::DurabilityExcitation NXOpen::CAE::DurabilityExcitation@endlink . 
                An excitation is essentially a variation of a loading in time. 
                @link NXOpen::CAE::DurabilityLoadPattern NXOpen::CAE::DurabilityLoadPattern@endlink  is one kind of excitation.
                Excitations can only be attached to static durability events.
            
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurabilityExcitation : public NXOpen::NXObject
        {
            private: DurabilityExcitationImpl * m_durabilityexcitation_impl;
            private: friend class  _DurabilityExcitationBuilder;
            protected: DurabilityExcitation();
            public: ~DurabilityExcitation();
            /** Rename the excitation. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void Rename
            (
                const NXString & name /** name */ 
            );
            /** Rename the excitation. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            void Rename
            (
                const char * name /** name */ 
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
