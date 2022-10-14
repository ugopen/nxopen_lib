#ifndef NXOpen_SKETCHASSOCIATIVETRIMBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHASSOCIATIVETRIMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchAssociativeTrimBuilder.ja
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
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/SketchAssociativeTrimBuilder.hxx>
#include <NXOpen/ugmath.hxx>
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
    class SketchAssociativeTrimBuilder;
    class Builder;
    class Section;
    class SelectNXObjectList;
    class _SketchAssociativeTrimBuilderBuilder;
    class SketchAssociativeTrimBuilderImpl;
    /**
        Represents a @link SketchAssociativeTrimBuilder SketchAssociativeTrimBuilder@endlink 
         <br> To create a new instance of this class, use @link SketchCollection::CreateSketchAssociativeTrimBuilder  SketchCollection::CreateSketchAssociativeTrimBuilder @endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    TrimType </td> <td> 
     
    Keep </td> </tr> 

    </table>  

     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchAssociativeTrimBuilder : public Builder
    {
        /** Represents the keep discard options for selected region */
        public: enum TrimOption
        {
            TrimOptionKeep/** Selected region will be kept. Default set. */,
            TrimOptionDiscard/** Selected region will be discarded. */
        };

        private: SketchAssociativeTrimBuilderImpl * m_sketchassociativetrimbuilder_impl;
        private: friend class  _SketchAssociativeTrimBuilderBuilder;
        protected: SketchAssociativeTrimBuilder();
        public: ~SketchAssociativeTrimBuilder();
        /** The function creates a new empty section object and adds it to the builder  @return  New section object 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Section * CreateSection
        (
        );
        /** The function removes the given section from the builder 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveSection
        (
            NXOpen::Section * section /** Section object to remove */
        );
        /** This function gets all sections of the trim constraint during create/edit  @return  All the sections associated with the builder 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: std::vector<NXOpen::Section *> GetSections
        (
        );
        /**Returns  the input curves. These curves must be a part of a single continuous recipe chain. 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectNXObjectList * RecipeCurves
        (
        );
        /**Returns  the trim region type - if the region needs to be kept/discarded 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SketchAssociativeTrimBuilder::TrimOption TrimType
        (
        );
        /**Sets  the trim region type - if the region needs to be kept/discarded 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetTrimType
        (
            NXOpen::SketchAssociativeTrimBuilder::TrimOption option /** option */ 
        );
        /** The function sets help point for region select. The region corresponding to help point will be 
                kept/discarded depending on trim type 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SelectRegion
        (
            const NXOpen::Point3d & helpPoint /** Help point for region selection */
        );
        /** The region corresponding to help point will be delsected from being kept/discarded depending 
                on trim type 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void DeselectRegion
        (
            const NXOpen::Point3d & helpPoint /** Help point for region selection */
        );
        /** The regions are recreated and updated to reflect the change in the boundary curves 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void UpdateRegions
        (
        );
        /** The regions are forced to be deselected 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void ResetRegions
        (
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