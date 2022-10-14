#ifndef NXOpen_FEATURES_DATUMCSYSBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_DATUMCSYSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DatumCsysBuilder.ja
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
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class DatumCsysBuilder;
    }
    class CartesianCoordinateSystem;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class _DatumCsysBuilderBuilder;
        /** Represents a datum csys builder  <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateDatumCsysBuilder Features::FeatureCollection::CreateDatumCsysBuilder@endlink  <br> */
        class NXOPENCPPEXPORT DatumCsysBuilder : public Features::FeatureBuilder
        {
            private: friend class  _DatumCsysBuilderBuilder;
            protected: DatumCsysBuilder();
            /**Sets  the CSYS that defines a Datum CSYS  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCsys
            (
                NXOpen::CartesianCoordinateSystem * csys /** exisiting WCS This parameter may not be NULL.*/
            );
            /**Returns  the CSYS that defines a Datum CSYS  <br> License requirements : None */
            public: NXOpen::CartesianCoordinateSystem * Csys
            (
            );
            /**Sets  the scale factor of the input Datum Csys  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDisplayScaleFactor
            (
                double displayScaleFactor /** display scale factor */
            );
            /**Returns  the scale factor of the input Datum Csys  <br> License requirements : None */
            public: double DisplayScaleFactor
            (
            );
            /**Sets  the flag of the Datum Csys components creation  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetComponentsCreation
            (
                bool componentsCreation /** TRUE at creation and FALSE at edit */
            );
            /**Returns  the flag of the Datum Csys components creation  <br> License requirements : None */
            public: bool ComponentsCreation
            (
            );
            /**Sets  the fixed size flag of a created Datum Csys  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFixedSizeDatum
            (
                bool fixedSizeDatum /** always TRUE at both of creation and edit */
            );
            /**Returns  the fixed size flag of a created Datum Csys  <br> License requirements : None */
            public: bool FixedSizeDatum
            (
            );
            /** Prints wave browser type information about link  <br> License requirements : wave ("WAVE FUNCTIONALITY") */
            public: void GetWaveLinkInformation
            (
                NXString* info /** queried wave information */,
                bool* xformExists /** true if there is a transform */,
                NXOpen::Point3d* xformOrigin /** transformation origin */,
                NXOpen::Matrix3x3* xformOrientation /** transformation matrix */,
                double* xformScale /** transformation scale */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif