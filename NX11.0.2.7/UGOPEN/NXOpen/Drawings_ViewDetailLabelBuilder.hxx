#ifndef NXOpen_DRAWINGS_VIEWDETAILLABELBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWDETAILLABELBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewDetailLabelBuilder.ja
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
#include <NXOpen/Drawings_ViewDetailLabelBuilder.hxx>
#include <NXOpen/Drawings_ViewLabelPreferencesData.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class ViewDetailLabelBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Drawings
    {
        class _ViewDetailLabelBuilderBuilder;
        class ViewDetailLabelBuilderImpl;
        /**
            Represents a @link NXOpen::Drawings::ViewDetailLabelBuilder NXOpen::Drawings::ViewDetailLabelBuilder@endlink 
            
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  ViewDetailLabelBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Label on Parent Display type*/
            public: enum LabelParentDisplayTypes
            {
                LabelParentDisplayTypesNone/** none */ ,
                LabelParentDisplayTypesCircle/** circle */ ,
                LabelParentDisplayTypesNote/** note */ ,
                LabelParentDisplayTypesLabel/** label */ ,
                LabelParentDisplayTypesEmbedded/** embedded */ ,
                LabelParentDisplayTypesBoundary/** boundary */ ,
                LabelParentDisplayTypesLabelOnBoundary/** label on boundary */ 
            };

            /** Label on Parent Text Placement type*/
            public: enum LabelParentTextPlacement
            {
                LabelParentTextPlacementBeforeOrAfterStub/** before or after stub */ ,
                LabelParentTextPlacementAboveStub/** above stub */ 
            };

            private: ViewDetailLabelBuilderImpl * m_viewdetaillabelbuilder_impl;
            private: friend class  _ViewDetailLabelBuilderBuilder;
            protected: ViewDetailLabelBuilder();
            public: ~ViewDetailLabelBuilder();
            /**Returns  the show view label 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowViewLabel
            (
            );
            /**Sets  the show view label 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetShowViewLabel
            (
                bool showViewLabel /** showviewlabel */ 
            );
            /**Returns  the view label option 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewLabelTypes ViewLabelOption
            (
            );
            /**Sets  the view label option 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetViewLabelOption
            (
                NXOpen::Drawings::ViewLabelTypes viewLabelOption /** viewlabeloption */ 
            );
            /**Returns  the label position 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::LabelPositionTypes LabelPosition
            (
            );
            /**Sets  the label position 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetLabelPosition
            (
                NXOpen::Drawings::LabelPositionTypes labelPosition /** labelposition */ 
            );
            /**Returns  the label prefix 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString LabelPrefix
            (
            );
            /**Sets  the label prefix 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetLabelPrefix
            (
                const NXString & labelPrefix /** labelprefix */ 
            );
            /**Sets  the label prefix 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetLabelPrefix
            (
                const char * labelPrefix /** labelprefix */ 
            );
            /**Returns  the letter format 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::LetterFormatTypes LetterFormat
            (
            );
            /**Sets  the letter format 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetLetterFormat
            (
                NXOpen::Drawings::LetterFormatTypes letterFormat /** letterformat */ 
            );
            /**Returns  the section vw label letter size factor 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double LabelCharacterHeightFactor
            (
            );
            /**Sets  the section vw label letter size factor 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetLabelCharacterHeightFactor
            (
                double labelCharacterHeightFactor /** labelcharacterheightfactor */ 
            );
            /**Returns  the reference to show 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ReferenceShowTypes ReferenceToShow
            (
            );
            /**Sets  the reference to show 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetReferenceToShow
            (
                NXOpen::Drawings::ReferenceShowTypes referenceToShow /** referencetoshow */ 
            );
            /**Returns  the label parent display 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewDetailLabelBuilder::LabelParentDisplayTypes LabelParentDisplay
            (
            );
            /**Sets  the label parent display 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetLabelParentDisplay
            (
                NXOpen::Drawings::ViewDetailLabelBuilder::LabelParentDisplayTypes labelParentDisplay /** labelparentdisplay */ 
            );
            /**Returns  the text placement 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewDetailLabelBuilder::LabelParentTextPlacement TextPlacement
            (
            );
            /**Sets  the text placement 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetTextPlacement
            (
                NXOpen::Drawings::ViewDetailLabelBuilder::LabelParentTextPlacement textPlacement /** textplacement */ 
            );
            /**Returns  the text gap factor 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double TextGapFactor
            (
            );
            /**Sets  the text gap factor 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetTextGapFactor
            (
                double textGapFactor /** textgapfactor */ 
            );
            /**Returns  the parent label prefix 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ParentLabelPrefix
            (
            );
            /**Sets  the parent label prefix 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetParentLabelPrefix
            (
                const NXString & parentLabelPrefix /** parentlabelprefix */ 
            );
            /**Sets  the parent label prefix 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetParentLabelPrefix
            (
                const char * parentLabelPrefix /** parentlabelprefix */ 
            );
            /**Returns  the show view scale 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowViewScale
            (
            );
            /**Sets  the show view scale 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetShowViewScale
            (
                bool showViewScale /** showviewscale */ 
            );
            /**Returns  the scale position 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ScalePositionTypes ScalePosition
            (
            );
            /**Sets  the scale position 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetScalePosition
            (
                NXOpen::Drawings::ScalePositionTypes scalePosition /** scaleposition */ 
            );
            /**Returns  the scale prefix 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ScalePrefix
            (
            );
            /**Sets  the scale prefix 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetScalePrefix
            (
                const NXString & scalePrefix /** scaleprefix */ 
            );
            /**Sets  the scale prefix 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetScalePrefix
            (
                const char * scalePrefix /** scaleprefix */ 
            );
            /**Returns  the prefix character height factor 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double PrefixCharacterHeightFactor
            (
            );
            /**Sets  the prefix character height factor 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetPrefixCharacterHeightFactor
            (
                double prefixCharacterHeightFactor /** prefixcharacterheightfactor */ 
            );
            /**Returns  the value format 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ScaleValueFormatTypes ValueFormat
            (
            );
            /**Sets  the value format 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetValueFormat
            (
                NXOpen::Drawings::ScaleValueFormatTypes valueFormat /** valueformat */ 
            );
            /**Returns  the scale character height factor 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double ScaleCharacterHeightFactor
            (
            );
            /**Sets  the scale character height factor 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetScaleCharacterHeightFactor
            (
                double scaleCharacterHeightFactor /** scalecharacterheightfactor */ 
            );
            /**Returns  the include parentheses 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool IncludeParentheses
            (
            );
            /**Sets  the include parentheses 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetIncludeParentheses
            (
                bool includeParentheses /** includeparentheses */ 
            );
            /**Returns  the customized view label 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool CustomizedViewLabel
            (
            );
            /**Sets  the customized view label 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetCustomizedViewLabel
            (
                bool customizedViewLabel /** customizedviewlabel */ 
            );
            /** Returns the customized view label text  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: std::vector<NXString> GetCustomizedViewLabelText
            (
            );
            /** Sets the customized view label text 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetCustomizedViewLabelText
            (
                const std::vector<NXString> & customizedText /** customizedtext */ 
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
