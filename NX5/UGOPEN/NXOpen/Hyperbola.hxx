#ifndef NXOpen_HYPERBOLA_HXX_INCLUDED
#define NXOpen_HYPERBOLA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Hyperbola.ja
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
#include <NXOpen/Conic.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Hyperbola;
    class Conic;
    class _HyperbolaBuilder;
    /** Represents a hyperbola curve.   <br> To create a new instance of this class, use @link CurveCollection::CreateHyperbola CurveCollection::CreateHyperbola@endlink  <br> */
    class NXOPENCPPEXPORT Hyperbola : public Conic
    {
        private: friend class  _HyperbolaBuilder;
        protected: Hyperbola();
        /**Returns  the semi-transverse length.  <br> License requirements : None */
        public: double SemiTransverseLength
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link SemiTransverseLength() SemiTransverseLength@endlink instead.
        @deprecated
        */
        public: double GetSemiTransverseLength
        (
        ) { return this->SemiTransverseLength(); }
        /**Returns  the semi-conjugate length.  <br> License requirements : None */
        public: double SemiConjugateLength
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link SemiConjugateLength() SemiConjugateLength@endlink instead.
        @deprecated
        */
        public: double GetSemiConjugateLength
        (
        ) { return this->SemiConjugateLength(); }
        /**Returns  the minimum DY width.  <br> License requirements : None */
        public: double MinimumDY
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link MinimumDY() MinimumDY@endlink instead.
        @deprecated
        */
        public: double GetMinimumDY
        (
        ) { return this->MinimumDY(); }
        /**Returns  the maximum DY width.  <br> License requirements : None */
        public: double MaximumDY
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link MaximumDY() MaximumDY@endlink instead.
        @deprecated
        */
        public: double GetMaximumDY
        (
        ) { return this->MaximumDY(); }
    };
}
#undef EXPORTLIBRARY
#endif