#ifndef NXOpen_DIE_FACESHEETBUILDER_HXX_INCLUDED
#define NXOpen_DIE_FACESHEETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_FaceSheetBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class FaceSheetBuilder;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Die
    {
        class _FaceSheetBuilderBuilder;
        /** Represents a Face Sheet feature  <br> This is an abstract class, and cannot be created. <br> */
        class NXOPENCPPEXPORT FaceSheetBuilder : public Features::FeatureBuilder
        {
            private: friend class  _FaceSheetBuilderBuilder;
            protected: FaceSheetBuilder();
            /**Returns  the stamping output feature of the Face Sheet  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Features::Feature * StampingOutput
            (
            );
            /**Sets  the stamping output feature of the Face Sheet  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetStampingOutput
            (
                NXOpen::Features::Feature * object /** object */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif