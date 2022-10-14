#ifndef NXOpen_SKETCHEDITPARAMETERSBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHEDITPARAMETERSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchEditParametersBuilder.ja
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
#include <NXOpen/SketchOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class SketchEditParametersBuilder;
    namespace Annotations
    {
        class Dimension;
    }
    class SketchOperationBuilder;
    class _SketchEditParametersBuilderBuilder;
    class SketchEditParametersBuilderImpl;
    /** Represents a @link NXOpen::SketchEditParametersBuilder NXOpen::SketchEditParametersBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::SketchCollection::CreateEditParametersBuilder  NXOpen::SketchCollection::CreateEditParametersBuilder @endlink  <br> 
     <br>  Created in NX1926.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchEditParametersBuilder : public NXOpen::SketchOperationBuilder
    {
        private: SketchEditParametersBuilderImpl * m_sketcheditparametersbuilder_impl;
        private: friend class  _SketchEditParametersBuilderBuilder;
        protected: SketchEditParametersBuilder();
        public: ~SketchEditParametersBuilder();
        /** This function will solve the sketch based on the new data set in the builder 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void Evaluate
        (
            NXOpen::Annotations::Dimension * dimensionTag /** dimensiontag */ ,
            double newValue /** newvalue */ 
        );
    };
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif