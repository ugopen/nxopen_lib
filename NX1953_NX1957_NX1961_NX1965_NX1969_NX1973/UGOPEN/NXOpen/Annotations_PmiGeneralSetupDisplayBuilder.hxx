#ifndef NXOpen_ANNOTATIONS_PMIGENERALSETUPDISPLAYBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIGENERALSETUPDISPLAYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiGeneralSetupDisplayBuilder.ja
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
#include <NXOpen/LineFontBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class PmiGeneralSetupDisplayBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class LineFontBuilder;
    class NXColor;
    namespace Annotations
    {
        class _PmiGeneralSetupDisplayBuilderBuilder;
        class PmiGeneralSetupDisplayBuilderImpl;
        /**
            Represents a NXOpen.Annotations.PmiGeneralSetupDisplayBuilder
            
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiGeneralSetupDisplayBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** the plane values which specify the annotation plane that will be used to display PMI.*/
            public: enum AnnotationPlaneType
            {
                AnnotationPlaneTypeXYPlaneofWCS/** the plane value which represents XY Plane of WCS type */,
                AnnotationPlaneTypeXZPlaneofWCS/** the plane value which represents XZ Plane of WCS type */,
                AnnotationPlaneTypeYZPlaneofWCS/** the plane value which represents YZ Plane of WCS type */,
                AnnotationPlaneTypeModelViewPlane/** the plane value which represents Model View Plane type */
            };

            /** the resize values which specify the method used to resize PMI.*/
            public: enum ResizeSettingsType
            {
                ResizeSettingsTypeRelativetoSavedViewScale/** the resize value which represents 'Settings Relative to Saved View Scale' type*/,
                ResizeSettingsTypeRelativetoViewZoomFactor/** the resize value which represents 'Settings Relative to View Zoom Factor' type*/,
                ResizeSettingsTypeIndependently/** the resize value which represents 'Independent of Settings' type*/,
                ResizeSettingsTypeRelativetoPartPreferences/** the resize value which represents 'Settings Relative to Part Preferences' type*/
            };

            /** the display values which determines whether or not Annotation planes will be displayed while creating and editing PMI.*/
            public: enum AnnotationPlaneDisplayType
            {
                AnnotationPlaneDisplayTypeAll/** the display value which allow "All Annotation planes to be displayed"  */,
                AnnotationPlaneDisplayTypeActivePlaneOnly/** the display value which allow "Only Active Annotation plane to be displayed"  */,
                AnnotationPlaneDisplayTypeNone/** the display value which do not allow "Annotation plane to be displayed"  */
            };

            private: PmiGeneralSetupDisplayBuilderImpl * m_pmigeneralsetupdisplaybuilder_impl;
            private: friend class  _PmiGeneralSetupDisplayBuilderBuilder;
            protected: PmiGeneralSetupDisplayBuilder();
            public: ~PmiGeneralSetupDisplayBuilder();
            /**Returns  the display in all views option which determines whether or not PMI should be displayed
                        in all views on create. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool DisplayInAllViews
            (
            );
            /**Sets  the display in all views option which determines whether or not PMI should be displayed
                        in all views on create. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDisplayInAllViews
            (
                bool displayInAllViews /** displayinallviews */ 
            );
            /**Returns  the option determines whether or not PMI should be displayed in all views on create 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiGeneralSetupDisplayBuilder::AnnotationPlaneDisplayType AnnotationPlaneDisplay
            (
            );
            /**Sets  the option determines whether or not PMI should be displayed in all views on create 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetAnnotationPlaneDisplay
            (
                NXOpen::Annotations::PmiGeneralSetupDisplayBuilder::AnnotationPlaneDisplayType displayType /** displaytype */ 
            );
            /**Returns  the annotation plane option which specifies the annotation plane that will be used to display PMI 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiGeneralSetupDisplayBuilder::AnnotationPlaneType AnnotationPlane
            (
            );
            /**Sets  the annotation plane option which specifies the annotation plane that will be used to display PMI 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetAnnotationPlane
            (
                NXOpen::Annotations::PmiGeneralSetupDisplayBuilder::AnnotationPlaneType annotationPlane /** annotationplane */ 
            );
            /**Returns  the option specifies translucency of the Annotation Plane preview. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: int AnnotationPlaneTranslucency
            (
            );
            /**Sets  the option specifies translucency of the Annotation Plane preview. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetAnnotationPlaneTranslucency
            (
                int annotationPlaneTranslucency /** annotationplanetranslucency */ 
            );
            /**Returns  the option specifies color of the Annotation Plane preview. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: int AnnotationPlaneColor
            (
            );
            /**Sets  the option specifies color of the Annotation Plane preview. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetAnnotationPlaneColor
            (
                int color /** color */ 
            );
            /**Returns  the option specifies line font for the Annotation Plane preview boundary line. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineFontBuilder * AnnotationPlaneFont
            (
            );
            /**Returns  the option to specifies project Annotation onto plane. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool ProjectOntoPlane
            (
            );
            /**Sets  the option to specifies project Annotation onto plane. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetProjectOntoPlane
            (
                bool projectOntoPlane /** projectontoplane */ 
            );
            /**Returns  the display pmi shaded model toggle option which determines how a PMI is displayed in a shaded model.
                        When turned on, PMI will show through the shaded model. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool DisplayPmiShadedModel
            (
            );
            /**Sets  the display pmi shaded model toggle option which determines how a PMI is displayed in a shaded model.
                        When turned on, PMI will show through the shaded model. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDisplayPmiShadedModel
            (
                bool displayPmiShadedModel /** displaypmishadedmodel */ 
            );
            /**Returns  the update reading direction toggle option which determines whether or not PMI text reading direction
                        should be updated in response to view rotation. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpdateReadingDirection
            (
            );
            /**Sets  the update reading direction toggle option which determines whether or not PMI text reading direction
                        should be updated in response to view rotation. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetUpdateReadingDirection
            (
                bool updateReadingDirection /** updatereadingdirection */ 
            );
            /**Returns  the enable resize toggle option which determines whether the resize function for PMI is enabled.
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool EnableResize
            (
            );
            /**Sets  the enable resize toggle option which determines whether the resize function for PMI is enabled.
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetEnableResize
            (
                bool enableResize /** enableresize */ 
            );
            /**Returns  the resize on create toggle option which determines whether the PMI are resized when they are created.
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool ResizeOnCreate
            (
            );
            /**Sets  the resize on create toggle option which determines whether the PMI are resized when they are created.
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetResizeOnCreate
            (
                bool resizeOnCreate /** resizeoncreate */ 
            );
            /**Returns  the resize on view save toggle option which determines whether the PMI are resized during a view save operation.
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool ResizeOnViewSave
            (
            );
            /**Sets  the resize on view save toggle option which determines whether the PMI are resized during a view save operation.
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetResizeOnViewSave
            (
                bool resizeOnViewSave /** resizeonviewsave */ 
            );
            /**Returns  the resize settings option specifies the method used to resize PMI.
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiGeneralSetupDisplayBuilder::ResizeSettingsType ResizeSettings
            (
            );
            /**Sets  the resize settings option specifies the method used to resize PMI.
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetResizeSettings
            (
                NXOpen::Annotations::PmiGeneralSetupDisplayBuilder::ResizeSettingsType resizeSettings /** resizesettings */ 
            );
            /**Returns  the option which determines whether or not to display supported PMI with background enabled.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool EnableBackground
            (
            );
            /**Sets  the option which determines whether or not to display supported PMI with background enabled.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetEnableBackground
            (
                bool enableBackground /** enablebackground */ 
            );
            /**Returns  the color of the PMI background. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * BackgroundColor
            (
            );
            /**Sets  the color of the PMI background. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetBackgroundColor
            (
                NXOpen::NXColor * backgroundColor /** backgroundcolor */ 
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not yet implemented
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
