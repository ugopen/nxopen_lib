#ifndef NXOpen_GEOMETRICUTILITIES_FACESETOFFSET_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_FACESETOFFSET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_FaceSetOffset.ja
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
#include <NXOpen/ExpressionCollectorSet.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class FaceSetOffset;
    }
    class Expression;
    class ExpressionCollectorSet;
    class ScCollector;
    namespace GeometricUtilities
    {
        class _FaceSetOffsetBuilder;
        class FaceSetOffsetImpl;
        /** This class represents a face set (collector) offset data. As the name indicates, it is a
             *  combination of a face collector and an offset distance.
              <br> To create a new instance of this class, use @link GeometricUtilities::FaceSetOffsetCollection::CreateEmptyFaceSet GeometricUtilities::FaceSetOffsetCollection::CreateEmptyFaceSet@endlink  <br> */
        class NXOPENCPPEXPORT  FaceSetOffset : public ExpressionCollectorSet
        {
            private: FaceSetOffsetImpl * m_facesetoffset_impl;
            private: friend class  _FaceSetOffsetBuilder;
            protected: FaceSetOffset();
            public: ~FaceSetOffset();
            /**Sets  the face collector
                      <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFaceCollector
            (
                NXOpen::ScCollector * faceCollector /** Smart collector for the face set */
            );
            /**Returns  the face collector
                      <br> License requirements : None */
            public: NXOpen::ScCollector * FaceCollector
            (
            );
            /** Sets the offset distance
                      <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOffset
            (
                const NXString & offsetValue /** Input offset distance for the face set   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the offset distance
                      <br> License requirements : None */
            public: NXOpen::Expression * Offset
            (
            );
            /** Flip offset direction. This API flips the direction of offset keeping the offset distance same.
                      <br> License requirements : None */
            public: void FlipDirection
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif