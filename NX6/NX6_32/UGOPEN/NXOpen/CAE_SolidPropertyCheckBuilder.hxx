#ifndef NXOpen_CAE_SOLIDPROPERTYCHECKBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SOLIDPROPERTYCHECKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SolidPropertyCheckBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
#include <NXOpen/CAE_SolidPropertyCheckBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class SolidPropertyCheckBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectElementsBuilder;
    }
    class CoordinateSystem;
    class Expression;
    namespace CAE
    {
        class _SolidPropertyCheckBuilderBuilder;
        /**
            Represents a @link CAE::SolidPropertyCheckBuilder CAE::SolidPropertyCheckBuilder@endlink 
             <br> To create a new instance of this class, use @link CAE::ModelCheckManager::CreateSolidPropertyCheckBuilder CAE::ModelCheckManager::CreateSolidPropertyCheckBuilder@endlink  <br> */
        class NXOPENCPPEXPORT SolidPropertyCheckBuilder : public Builder
        {
            /** User Specified output unit */
            public: enum UserUnit
            {
                UserUnitDefaultUnit/** Load unit = same as system default unit*/,
                UserUnitKgMilli/** mass = kg, cg = mm, volume = mm^3 mmoi = kg-mm^2*/,
                UserUnitLbmIn/** mass = lbm, cg = in, volume = in^3 mmoi = lbm-in^2*/,
                UserUnitLbfInSec/** mass = lbf-sec^2/in, cg = in, volume = in^3 mmoi = lbf-in-sec^2*/
            };

            private: friend class  _SolidPropertyCheckBuilderBuilder;
            protected: SolidPropertyCheckBuilder();
            /**Returns  the reference csys  <br> License requirements : None */
            public: NXOpen::CoordinateSystem * ReferenceCsys
            (
            );
            /**Sets  the reference csys  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetReferenceCsys
            (
                NXOpen::CoordinateSystem * referenceCsys /** referencecsys */ 
            );
            /**Returns  the output result unit   <br> License requirements : None */
            public: NXOpen::CAE::SolidPropertyCheckBuilder::UserUnit UserSpecifiedUnit
            (
            );
            /**Sets  the output result unit   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetUserSpecifiedUnit
            (
                NXOpen::CAE::SolidPropertyCheckBuilder::UserUnit userSpecifiedUnit /** userspecifiedunit */ 
            );
            /**Returns  the output mass split option option  <br> License requirements : None */
            public: bool DisplayCgOption
            (
            );
            /**Sets  the output mass split option option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetDisplayCgOption
            (
                bool displayCG /** displaycg */ 
            );
            /**Returns  the selected elements  <br> License requirements : None */
            public: NXOpen::CAE::SelectElementsBuilder * Elements
            (
            );
            /**Returns  the output mass split option option  <br> License requirements : None */
            public: bool SplitMass
            (
            );
            /**Sets  the output mass split option option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetSplitMass
            (
                bool splitMass /** splitmass */ 
            );
            /**Returns  the output mass split option option  <br> License requirements : None */
            public: bool DefaultTemperatureOption
            (
            );
            /**Sets  the output mass split option option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetDefaultTemperatureOption
            (
                bool defaultTemperatureOption /** defaulttemperatureoption */ 
            );
            /**Returns  the output temperature option in C <br> License requirements : None */
            public: NXOpen::Expression * EvaluationTemparature
            (
            );
            /**Returns  the detail output option  <br> License requirements : None */
            public: bool OutputOption
            (
            );
            /**Sets  the detail output option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetOutputOption
            (
                bool outputOpt /** outputopt */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
