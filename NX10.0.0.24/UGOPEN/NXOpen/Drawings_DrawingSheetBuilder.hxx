#ifndef NXOpen_DRAWINGS_DRAWINGSHEETBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_DRAWINGSHEETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_DrawingSheetBuilder.ja
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
#include <NXOpen/Drawings_DrawingSheetBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class DrawingSheetBuilder;
    }
    class Builder;
    namespace Drawings
    {
        class _DrawingSheetBuilderBuilder;
        class DrawingSheetBuilderImpl;
        /**
            Represents a @link Drawings::DrawingSheetBuilder Drawings::DrawingSheetBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::Drawings::DrawingSheetCollection::DrawingSheetBuilder  NXOpen::Drawings::DrawingSheetCollection::DrawingSheetBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  DrawingSheetBuilder : public NXOpen::Builder
        {
            /** the options for specifying the attributes of the new drawing sheet to be created. */
            public: enum SheetOption
            {
                SheetOptionUseTemplate/** a drawing sheet template */,
                SheetOptionStandardSize/** a standard size drawing sheet */,
                SheetOptionCustomSize/** a custom size drawing sheet */
            };

            /** the standard Metric drawing sheet scales */
            public: enum SheetStandardMetricScale
            {
                SheetStandardMetricScaleS501/** a scale of 50:1 */,
                SheetStandardMetricScaleS201/** a scale of 20:1 */,
                SheetStandardMetricScaleS101/** a scale of 10:1 */,
                SheetStandardMetricScaleS51/** a scale of 5:1 */,
                SheetStandardMetricScaleS21/** a scale of 2:1 */,
                SheetStandardMetricScaleS11/** a scale of 1:1 */,
                SheetStandardMetricScaleS12/** a scale of 1:2 */,
                SheetStandardMetricScaleS15/** a scale of 1:5 */,
                SheetStandardMetricScaleS110/** a scale of 1:10 */,
                SheetStandardMetricScaleS120/** a scale of 1:20 */,
                SheetStandardMetricScaleS150/** a scale of 1:50 */,
                SheetStandardMetricScaleS1100/** a scale of 1:100 */,
                SheetStandardMetricScaleCustom/** a custom scale */
            };

            /** the standard English drawing sheet scales */
            public: enum SheetStandardEnglishScale
            {
                SheetStandardEnglishScaleS81/** a scale of 8:1 */,
                SheetStandardEnglishScaleS41/** a scale of 4:1 */,
                SheetStandardEnglishScaleS21/** a scale of 2:1 */,
                SheetStandardEnglishScaleS11/** a scale of 1:1 */,
                SheetStandardEnglishScaleS12/** a scale of 1:2 */,
                SheetStandardEnglishScaleS14/** a scale of 1:4 */,
                SheetStandardEnglishScaleS18/** a scale of 1:8 */,
                SheetStandardEnglishScaleCustom/** a custom scale */
            };

            /** the drawing sheet units */
            public: enum SheetUnits
            {
                SheetUnitsMetric/** a Metric units drawing sheet */,
                SheetUnitsEnglish/** an English units drawing sheet */
            };

            /** the drawing sheet projection angle */
            public: enum SheetProjectionAngle
            {
                SheetProjectionAngleFirst/** first angle projection */,
                SheetProjectionAngleThird/** third angle projection */
            };

            /** the drawing sheet dialog mode */
            public: enum SheetMode
            {
                SheetModeCreate/** create mode */,
                SheetModeEdit/** edit mode */
            };

            /** the base view or drawing view option */
            public: enum SheetBaseordrawingView
            {
                SheetBaseordrawingViewBase/** auto start base view */,
                SheetBaseordrawingViewDrawing/** auto start drawing view */
            };

            private: DrawingSheetBuilderImpl * m_drawingsheetbuilder_impl;
            private: friend class  _DrawingSheetBuilderBuilder;
            protected: DrawingSheetBuilder();
            public: ~DrawingSheetBuilder();
            /**Returns  the name of the drawing sheet to be created or edited 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name of the drawing sheet to be created or edited 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetName
            (
                const NXString & name /** drawing sheet name */
            );
            /**Sets  the name of the drawing sheet to be created or edited 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetName
            (
                const char * name /** drawing sheet name */
            );
            /**Returns  the number of the drawing sheet to be created or edited 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Number
            (
            );
            /**Sets  the number of the drawing sheet to be created or edited 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetNumber
            (
                const NXString & number /** the drawing sheet number */
            );
            /**Sets  the number of the drawing sheet to be created or edited 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetNumber
            (
                const char * number /** the drawing sheet number */
            );
            /**Returns  the secondary number of the drawing sheet to be created or edited 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString SecondaryNumber
            (
            );
            /**Sets  the secondary number of the drawing sheet to be created or edited 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetSecondaryNumber
            (
                const NXString & secondaryNumber /** the drawing sheet secondary number */
            );
            /**Sets  the secondary number of the drawing sheet to be created or edited 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetSecondaryNumber
            (
                const char * secondaryNumber /** the drawing sheet secondary number */
            );
            /**Returns  the option to be used to create the drawing sheet 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::DrawingSheetBuilder::SheetOption Option
            (
            );
            /**Sets  the option to be used to create the drawing sheet 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetOption
            (
                NXOpen::Drawings::DrawingSheetBuilder::SheetOption option /** the option to be used to create the drawing sheet */
            );
            /**Returns  the location of the metric drawing sheet template to be added to the part file 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString MetricSheetTemplateLocation
            (
            );
            /**Sets  the location of the metric drawing sheet template to be added to the part file 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetMetricSheetTemplateLocation
            (
                const NXString & metricSheetTemplateLocation /** metric drawing sheet template location */
            );
            /**Sets  the location of the metric drawing sheet template to be added to the part file 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetMetricSheetTemplateLocation
            (
                const char * metricSheetTemplateLocation /** metric drawing sheet template location */
            );
            /**Returns  the location of the english drawing sheet template to be added to the part file 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString EnglishSheetTemplateLocation
            (
            );
            /**Sets  the location of the english drawing sheet template to be added to the part file 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetEnglishSheetTemplateLocation
            (
                const NXString & englishSheetTemplateLocation /** english drawing sheet template location */
            );
            /**Sets  the location of the english drawing sheet template to be added to the part file 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetEnglishSheetTemplateLocation
            (
                const char * englishSheetTemplateLocation /** english drawing sheet template location */
            );
            /**Returns  the custom or standard height for the drawing sheet 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double Height
            (
            );
            /**Sets  the custom or standard height for the drawing sheet 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetHeight
            (
                double height /** the custom or standard height for the drawing sheet */
            );
            /**Returns  the custom or standard length to be used for the drawing to be created or edited. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double Length
            (
            );
            /**Sets  the custom or standard length to be used for the drawing to be created or edited. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetLength
            (
                double length /** the custom or standard length for the drawing sheet */
            );
            /**Returns  the standard Metric drawing scale 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::DrawingSheetBuilder::SheetStandardMetricScale StandardMetricScale
            (
            );
            /**Sets  the standard Metric drawing scale 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetStandardMetricScale
            (
                NXOpen::Drawings::DrawingSheetBuilder::SheetStandardMetricScale metricScale /** the standard Metric drawing scale */
            );
            /**Returns  the standard English drawing scale 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::DrawingSheetBuilder::SheetStandardEnglishScale StandardEnglishScale
            (
            );
            /**Sets  the standard English drawing scale 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetStandardEnglishScale
            (
                NXOpen::Drawings::DrawingSheetBuilder::SheetStandardEnglishScale englishScale /** the standard English drawing scale */
            );
            /**Returns  the numerator of a custom scale 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double ScaleNumerator
            (
            );
            /**Sets  the numerator of a custom scale 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetScaleNumerator
            (
                double scaleNumerator /** scale numerator */ 
            );
            /**Returns  the denominator of a custom scale 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double ScaleDenominator
            (
            );
            /**Sets  the denominator of a custom scale 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetScaleDenominator
            (
                double scaleDenominator /** the denominator of a custom scale */
            );
            /**Returns  the units for the drawing sheet 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::DrawingSheetBuilder::SheetUnits Units
            (
            );
            /**Sets  the units for the drawing sheet 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetUnits
            (
                NXOpen::Drawings::DrawingSheetBuilder::SheetUnits units /** the units for the drawing sheet */
            );
            /**Returns  the projection_angle option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::DrawingSheetBuilder::SheetProjectionAngle ProjectionAngle
            (
            );
            /**Sets  the projection_angle option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetProjectionAngle
            (
                NXOpen::Drawings::DrawingSheetBuilder::SheetProjectionAngle projectionAngle /** the projection_angle option */
            );
            /**Returns  the setting that controls whether or not the Add Base View command is automatically 
                        started after inserting a sheet that has no views on it.
                        This option does not appear for Edit Sheet. 
                        the toggle is changed to be auto start view creation in Nx7.0, obsolete.
                    
             <br>  @deprecated Deprecated in NX7.5.0.  Use @link Drawings::DrawingSheetBuilder::AutoStartViewCreation Drawings::DrawingSheetBuilder::AutoStartViewCreation@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0.  Use Drawings::DrawingSheetBuilder::AutoStartViewCreation instead.") bool AutoStartBaseView
            (
            );
            /**Sets  the setting that controls whether or not the Add Base View command is automatically 
                        started after inserting a sheet that has no views on it.
                        This option does not appear for Edit Sheet. 
                        the toggle is changed to be auto start view creation in Nx7.0, obsolete.
                    
             <br>  @deprecated Deprecated in NX7.5.0.  Use @link Drawings::DrawingSheetBuilder::SetAutoStartViewCreation Drawings::DrawingSheetBuilder::SetAutoStartViewCreation@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0.  Use Drawings::DrawingSheetBuilder::SetAutoStartViewCreation instead.") void SetAutoStartBaseView
            (
                bool autoStartBaseView /** the add base view automatic start toggle */
            );
            /**Returns  the setting that controls whether or not the Add View creation is automatically 
                        started after inserting a sheet that has no views on it.
                        This option does not appear for Edit Sheet.             
                    
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool AutoStartViewCreation
            (
            );
            /**Sets  the setting that controls whether or not the Add View creation is automatically 
                        started after inserting a sheet that has no views on it.
                        This option does not appear for Edit Sheet.             
                    
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAutoStartViewCreation
            (
                bool autoStartViewCreation /** the automatically start view creation */
            );
            /**Returns  the option of base view or drawing view 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::DrawingSheetBuilder::SheetBaseordrawingView BaseordrawingView
            (
            );
            /**Sets  the option of base view or drawing view 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetBaseordrawingView
            (
                NXOpen::Drawings::DrawingSheetBuilder::SheetBaseordrawingView option /** the type of view to automatically start creating */
            );
            /**Returns  the revision of the drawing sheet to be created or edited 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Revision
            (
            );
            /**Sets  the revision of the drawing sheet to be created or edited 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetRevision
            (
                const NXString & revision /** the drawing sheet revision */
            );
            /**Sets  the revision of the drawing sheet to be created or edited 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetRevision
            (
                const char * revision /** the drawing sheet revision */
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
