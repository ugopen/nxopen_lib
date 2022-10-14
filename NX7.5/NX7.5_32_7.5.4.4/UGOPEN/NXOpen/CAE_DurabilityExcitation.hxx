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
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** Represents a @link CAE::DurabilityExcitation CAE::DurabilityExcitation@endlink . 
                An excitation is essentially a variation of a loading in time. 
                @link CAE::DurabilityLoadPattern CAE::DurabilityLoadPattern@endlink  is one kind of excitation.
                Excitations can only be attached to static durability events.
            */
        class NXOPENCPPEXPORT  DurabilityExcitation : public NXObject
        {
            private: DurabilityExcitationImpl * m_durabilityexcitation_impl;
            private: friend class  _DurabilityExcitationBuilder;
            protected: DurabilityExcitation();
            public: ~DurabilityExcitation();
            /** Rename the excitation.  <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void Rename
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif