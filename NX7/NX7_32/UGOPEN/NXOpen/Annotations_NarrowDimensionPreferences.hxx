#ifndef NXOpen_ANNOTATIONS_NARROWDIMENSIONPREFERENCES_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_NARROWDIMENSIONPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_NarrowDimensionPreferences.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Annotations.hxx>
#include <NXOpen/Dimensions.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class NarrowDimensionPreferences;
    }
    namespace Annotations
    {
    }
    namespace Annotations
    {
        /** Represents narrow dimension preferences */
        class NXOPENCPPEXPORT NarrowDimensionPreferences : public TransientObject
        {
            public: explicit NarrowDimensionPreferences(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~NarrowDimensionPreferences();
            /**Returns  the dimension display option  <br> License requirements : None */
            public: NXOpen::Annotations::NarrowDisplayOption DimensionDisplayOption
            (
            );
            /**Sets  the dimension display option  <br> License requirements : None */
            public: void SetDimensionDisplayOption
            (
                NXOpen::Annotations::NarrowDisplayOption option /** New display option */
            );
            /**Returns  the dimension text orientation  <br> License requirements : None */
            public: NXOpen::Annotations::NarrowTextOrientation DimensionTextOrientation
            (
            );
            /**Sets  the dimension text orientation  <br> License requirements : None */
            public: void SetDimensionTextOrientation
            (
                NXOpen::Annotations::NarrowTextOrientation textOrientation /** New text orientation */
            );
            /**Returns  the dimension leader angle  <br> License requirements : None */
            public: double DimensionLeaderAngle
            (
            );
            /**Sets  the dimension leader angle  <br> License requirements : None */
            public: void SetDimensionLeaderAngle
            (
                double leaderAngle /** New leader angle */
            );
            /**Returns  the dimension text offset  <br> License requirements : None */
            public: double DimensionTextOffset
            (
            );
            /**Sets  the dimension text offset  <br> License requirements : None */
            public: void SetDimensionTextOffset
            (
                double textOffset /** New text offset */
            );
            /**Returns  the dimension arrowhead type when no space for normal arrowheads   <br> License requirements : None */
            public: NXOpen::Annotations::ArrowheadType DimensionArrowheadType
            (
            );
            /**Sets  the dimension arrowhead type when no space for normal arrowheads   <br> License requirements : None */
            public: void SetDimensionArrowheadType
            (
                NXOpen::Annotations::ArrowheadType type /** New arrowhead type */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
