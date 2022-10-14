#ifndef NXOpen_GEOMETRICANALYSIS_SECTIONANALYSIS_ISOPARAMETRICBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_SECTIONANALYSIS_ISOPARAMETRICBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_SectionAnalysis_IsoparametricBuilder.ja
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
#include <NXOpen/GeometricAnalysis_SectionAnalysis_IsoparametricBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_geometricanalysis_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class IsoparametricBuilder;
        }
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class _IsoparametricBuilderBuilder;
            class IsoparametricBuilderImpl;
            /** Represents the Isoparametric specification for a @link GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder@endlink .
             <br>  Created in NX7.0.0.  <br>  
            */
            class NXOPENCPP_GEOMETRICANALYSISEXPORT  IsoparametricBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
            {
                private: IsoparametricBuilderImpl * m_isoparametricbuilder_impl;
                private: friend class  _IsoparametricBuilderBuilder;
                protected: IsoparametricBuilder();
                public: ~IsoparametricBuilder();
                /**Returns  a value indicating wheter the U direction is enabled 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsUEnabled
                (
                );
                /**Sets  a value indicating wheter the U direction is enabled 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetUEnabled
                (
                    bool isUEnabled /** isuenabled */ 
                );
                /**Returns  a value indicating wheter the V direction is enabled 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsVEnabled
                (
                );
                /**Sets  a value indicating wheter the V direction is enabled 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetVEnabled
                (
                    bool isVEnabled /** isvenabled */ 
                );
                /**Returns  a value indicating how many sections should be created 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : None */
                public: int Number
                (
                );
                /**Sets  a value indicating how many sections should be created 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetNumber
                (
                    int number /** number */ 
                );
                /**Returns  a value indicating whether the spacing is applied 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsSpacingEnabled
                (
                );
                /**Sets  a value indicating whether the spacing is applied 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetSpacingEnabled
                (
                    bool isSpacingEnabled /** isspacingenabled */ 
                );
                /**Returns  a value indicating the space between sections 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : None */
                public: double Spacing
                (
                );
                /**Sets  a value indicating the space between sections 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetSpacing
                (
                    double spacing /** spacing */ 
                );
                /** Validate whether the inputs to the component are sufficient for 
                            commit to be called.  If the component is not in a state to commit
                            then an exception is thrown.  For example, if the component requires
                            you to set some property, this method will throw an exception if
                            you haven't set it.  This method throws a not-yet-implemented
                            NXException for some components.
                         @return  Was self validation successful 
                 <br>  Created in NX3.0.1.  <br>  
                 <br> License requirements : None */
                public: virtual bool Validate
                (
                );
            };
        }
    }
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