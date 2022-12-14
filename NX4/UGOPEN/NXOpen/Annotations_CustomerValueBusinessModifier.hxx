#ifndef NXOpen_ANNOTATIONS_CUSTOMERVALUEBUSINESSMODIFIER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_CUSTOMERVALUEBUSINESSMODIFIER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_CustomerValueBusinessModifier.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Annotations_ListBusinessModifier.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class CustomerValueBusinessModifier;
    }
    namespace Annotations
    {
        class ListBusinessModifier;
    }
    namespace Annotations
    {
        class _CustomerValueBusinessModifierBuilder;
        /** Represents business modifier that applies customer values such as CTQ (Critical To Quality), 
                KC (Key Characteristic) to a PMI. Please see ug_customer_value_bus_mod.dfa for attribute details.  */
        class NXOPENCPPEXPORT CustomerValueBusinessModifier : public Annotations::ListBusinessModifier
        {
            private: friend class  _CustomerValueBusinessModifierBuilder;
            protected: CustomerValueBusinessModifier();
        };
    }
}
#undef EXPORTLIBRARY
#endif
