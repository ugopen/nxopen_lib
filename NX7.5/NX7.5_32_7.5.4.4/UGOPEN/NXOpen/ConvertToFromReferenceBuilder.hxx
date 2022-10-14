#ifndef NXOpen_CONVERTTOFROMREFERENCEBUILDER_HXX_INCLUDED
#define NXOpen_CONVERTTOFROMREFERENCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ConvertToFromReferenceBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/ConvertToFromReferenceBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class ConvertToFromReferenceBuilder;
    class Builder;
    class Curve;
    class SelectNXObjectList;
    class _ConvertToFromReferenceBuilderBuilder;
    class ConvertToFromReferenceBuilderImpl;
    /**
        Represents a @link ConvertToFromReferenceBuilder ConvertToFromReferenceBuilder@endlink 
         <br> To create a new instance of this class, use @link SketchCollection::CreateConvertToFromReferenceBuilder SketchCollection::CreateConvertToFromReferenceBuilder@endlink  <br> */
    class NXOPENCPPEXPORT  ConvertToFromReferenceBuilder : public Builder
    {
        /** Represents the output type. */
        public: enum OutputType
        {
            OutputTypeReference/**Outputs become reference objects.*/,
            OutputTypeActive/**Outputs become active objects.*/
        };

        private: ConvertToFromReferenceBuilderImpl * m_converttofromreferencebuilder_impl;
        private: friend class  _ConvertToFromReferenceBuilderBuilder;
        protected: ConvertToFromReferenceBuilder();
        public: ~ConvertToFromReferenceBuilder();
        /**Returns  the input objects. The input objects must belong to the active sketch. Only curves and dimensions
                can be added to this list. <br> License requirements : None */
        public: NXOpen::SelectNXObjectList * InputObjects
        (
        );
        /**Returns  the projected curve flag. If this flag is ON and if at least one of the output curves
                of a sketch project feature are selected, all output curves of the sketch project feature will be selected.  <br> License requirements : None */
        public: bool SelectAllProjectFeatureCurves
        (
        );
        /**Sets  the projected curve flag. If this flag is ON and if at least one of the output curves
                of a sketch project feature are selected, all output curves of the sketch project feature will be selected.  <br> License requirements : None */
        public: void SetSelectAllProjectFeatureCurves
        (
            bool selectAllProjectFeatureCurves /** selectallprojectfeaturecurves */ 
        );
        /**Returns  the output type. If the output type is set to Active, all the selected curves and dimensions
                will get their reference status as active and if the output type is set to reference, they will
                get their reference status as reference. <br> License requirements : None */
        public: NXOpen::ConvertToFromReferenceBuilder::OutputType OutputState
        (
        );
        /**Sets  the output type. If the output type is set to Active, all the selected curves and dimensions
                will get their reference status as active and if the output type is set to reference, they will
                get their reference status as reference. <br> License requirements : None */
        public: void SetOutputState
        (
            NXOpen::ConvertToFromReferenceBuilder::OutputType outputState /** output state */ 
        );
        /** Adds all output entities belonging to the project feature that contains the input tag
                    to the input objects list of the command. The SelectAllProjectFeatureCurves flag must be
                    set to true before this function is called. <br> License requirements : None */
        public: void AddProjectFeatureCurves
        (
            NXOpen::Curve * entity /**The input curve tag.*/
        );
        /** Removes all output entities belonging to the project feature that contains the input tag
                    from the input objects list of the command. The SelectAllProjectFeatureCurves flag must be
                    set to true before this function is called. <br> License requirements : None */
        public: void RemoveProjectFeatureCurves
        (
            NXOpen::Curve * entity /**The input curve tag.*/
        );
    };
}
#undef EXPORTLIBRARY
#endif