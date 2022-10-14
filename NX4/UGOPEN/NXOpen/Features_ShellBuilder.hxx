#ifndef NXOpen_FEATURES_SHELLBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHELLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShellBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ShellBuilder;
    }
    class Body;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ObjectList;
    class ScCollector;
    namespace Features
    {
        class _ShellBuilderBuilder;
        /** Represents the Shell feature builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateShellBuilder Features::FeatureCollection::CreateShellBuilder@endlink  <br> */
        class NXOPENCPPEXPORT ShellBuilder : public Features::FeatureBuilder
        {
            private: friend class  _ShellBuilderBuilder;
            protected: ShellBuilder();
            /**Returns  the tolerance for the Shell operation.
                     <br> License requirements : None */
            public: double Tolerance
            (
            );
            /**Sets  the tolerance for the Shell operation.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTolerance
            (
                double tolerance /** */
            );
            /**Returns  the option to use approximate surfaces for the Shell operation.
                     <br> License requirements : None */
            public: bool UseSurfaceApproximation
            (
            );
            /**Sets  the option to use approximate surfaces for the Shell operation.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetUseSurfaceApproximation
            (
                bool approximation_option /** */
            );
            /**Returns  the option to process tangent remove faces for the Shell operation.
                     <br> License requirements : None */
            public: bool TgtPierceOption
            (
            );
            /**Sets  the option to process tangent remove faces for the Shell operation.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTgtPierceOption
            (
                bool tgt_pierce_option /** */
            );
            /**Returns  the body to be shelled.
                     <br> License requirements : None */
            public: NXOpen::Body * Body
            (
            );
            /**Sets  the body to be shelled.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetBody
            (
                NXOpen::Body * body /** */
            );
            /**Returns  the default thickness for the shelled body.
                     <br> License requirements : None */
            public: NXOpen::Expression * DefaultThickness
            (
            );
            /** Sets the default thickness for the shelled body.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDefaultThickness
            (
                const NXString & default_thickness_value /** default thickness expression   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the flip direction option for default thickness.
                     <br> License requirements : None */
            public: bool DefaultThicknessFlip
            (
            );
            /**Sets  the flip direction option for default thickness.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDefaultThicknessFlip
            (
                bool flip /** */
            );
            /**Returns  the set of faces to be removed from the shelled body.
                     <br> License requirements : None */
            public: NXOpen::ScCollector * RemovedFacesCollector
            (
            );
            /**Sets  the set of faces to be removed from the shelled body.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRemovedFacesCollector
            (
                NXOpen::ScCollector * sc_collector /** */
            );
            /**Returns  the list of faces and corresponding alternate thickness for each.
                     <br> License requirements : None */
            public: NXOpen::ObjectList * FaceThicknessList
            (
            );
            /**Sets  the list of faces and corresponding alternate thickness for each.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFaceThicknessList
            (
                NXOpen::ObjectList * seldimlist /** */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif