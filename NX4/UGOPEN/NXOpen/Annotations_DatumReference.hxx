#ifndef NXOpen_ANNOTATIONS_DATUMREFERENCE_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DATUMREFERENCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DatumReference.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Gdts.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class DatumReference;
    }
    namespace Annotations
    {
    }
    namespace Annotations
    {
        /** Represents a datum reference */
        class NXOPENCPPEXPORT DatumReference : public TransientObject
        {
            public: explicit DatumReference(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~DatumReference();
            /**Returns  the datum label  <br> License requirements : None */
            public: NXString DatumLabel
            (
            );
            /**Sets  the datum label  <br> License requirements : None */
            public: void SetDatumLabel
            (
                const NXString & label /** New datum label */
            );
            /** Returns the material condition modifiers  @return  List of modifiers  <br> License requirements : None */
            public: std::vector<NXOpen::Annotations::MaterialConditionModifier> GetMaterialConditionModifiers
            (
            );
            /** Sets the material condition modifiers  <br> License requirements : None */
            public: void SetMaterialConditionModifiers
            (
                const std::vector<NXOpen::Annotations::MaterialConditionModifier> & modifiers /** List of modifiers */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif