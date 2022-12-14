#ifndef NXOpen_FEATURES_EMBOSSTAPER_HXX_INCLUDED
#define NXOpen_FEATURES_EMBOSSTAPER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_EmbossTaper.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Features_EmbossTaper.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class EmbossTaper;
    }
    class Expression;
    namespace Features
    {
        class _EmbossTaperBuilder;
        /** Represents taper of an emboss feature 
              --Taper Angle
            */
        class NXOPENCPPEXPORT EmbossTaper : public TaggedObject
        {
            private: friend class  _EmbossTaperBuilder;
            protected: EmbossTaper();
            /** Set the emboss taper angle  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAngle
            (
                const NXString & taper_angle /**Taper angle value or expression formula string  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns   <br> License requirements : None */
            public: NXOpen::Expression * Angle
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
