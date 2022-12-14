#ifndef NXOpen_DIAGRAMMING_SHEETZONESETTINGSBUILDER_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_SHEETZONESETTINGSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_SheetZoneSettingsBuilder.ja
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
#include <NXOpen/Diagramming_BordersAndZones.hxx>
#include <NXOpen/Diagramming_SheetZoneSettingsBuilder.hxx>
#include <NXOpen/LineColorFontWidthBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_diagramming_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Diagramming
    {
        class SheetZoneSettingsBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class LineColorFontWidthBuilder;
    namespace Diagramming
    {
        class _SheetZoneSettingsBuilderBuilder;
        class SheetZoneSettingsBuilderImpl;
        /** The SheetZoneSettings builder 
         <br>  Created in NX11.0.1.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  SheetZoneSettingsBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: SheetZoneSettingsBuilderImpl * m_sheetzonesettingsbuilder_impl;
            private: friend class  _SheetZoneSettingsBuilderBuilder;
            protected: SheetZoneSettingsBuilder();
            public: ~SheetZoneSettingsBuilder();
            /**Returns  the flag indicates to create zones or not. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool CreateZones
            (
            );
            /**Sets  the flag indicates to create zones or not. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetCreateZones
            (
                bool createZones /** createzones */ 
            );
            /**Returns  the size of the horizontal zone. It must be greater than zero. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: double HorizontalSize
            (
            );
            /**Sets  the size of the horizontal zone. It must be greater than zero. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetHorizontalSize
            (
                double horizontalSize /** horizontalsize */ 
            );
            /**Returns  the size of the vertical zone. It must be greater than zero. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: double VerticalSize
            (
            );
            /**Sets  the size of the vertical zone. It must be greater than zero. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetVerticalSize
            (
                double verticalSize /** verticalsize */ 
            );
            /**Returns  the type of zone origin like TopLeft/BottomRight. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::ZoneOrigin Origin
            (
            );
            /**Sets  the type of zone origin like TopLeft/BottomRight. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetOrigin
            (
                NXOpen::Diagramming::ZoneOrigin origin /** origin */ 
            );
            /**Returns  the flag indicates whether the index for horizontal numeric zone labels will continue onto the next sheet or not. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool ContinueZoneIndexingAcrossSheets
            (
            );
            /**Sets  the flag indicates whether the index for horizontal numeric zone labels will continue onto the next sheet or not. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetContinueZoneIndexingAcrossSheets
            (
                bool continueZoneIndexingAcrossSheets /** continuezoneindexingacrosssheets */ 
            );
            /**Returns  the flag indicates to create zone markings or not. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool CreateZoneMarkings
            (
            );
            /**Sets  the flag indicates to create zone markings or not. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetCreateZoneMarkings
            (
                bool createZoneMarkings /** createzonemarkings */ 
            );
            /**Returns  the height of the marking. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: double MarkingHeight
            (
            );
            /**Sets  the height of the marking. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetMarkingHeight
            (
                double markingHeight /** markingheight */ 
            );
            /**Returns  the color and width of marking line. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * MarkingLineColorWidth
            (
            );
            /**Returns  the flag indicates to create zone labels or not. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool CreateZoneLabels
            (
            );
            /**Sets  the flag indicates to create zone labels or not. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetCreateZoneLabels
            (
                bool createZoneLabels /** createzonelabels */ 
            );
            /**Returns  the height of the label(text). 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: double LabelHeight
            (
            );
            /**Sets  the height of the label(text). 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetLabelHeight
            (
                double labelHeight /** labelheight */ 
            );
            /**Returns  the color of the label(text). 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: int LabelColor
            (
            );
            /**Sets  the color of the label(text). 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetLabelColor
            (
                int labelColor /** labelcolor */ 
            );
            /**Returns  the font of the label(text). 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: int LabelFont
            (
            );
            /**Sets  the font of the label(text). 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetLabelFont
            (
                int labelFont /** labelfont */ 
            );
            /**Returns  the width of the label(text) like Regular, Bold. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: int LabelWidth
            (
            );
            /**Sets  the width of the label(text) like Regular, Bold. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetLabelWidth
            (
                int labelWidth /** labelwidth */ 
            );
            /**Returns  the flag indicates the label(text) is italic or not. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool LabelItalicized
            (
            );
            /**Sets  the flag indicates the label(text) is italic or not. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetLabelItalicized
            (
                bool italic /** italic */ 
            );
            /**Returns  the characters to skip in label(text). 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXString LabelsToSkip
            (
            );
            /**Sets  the characters to skip in label(text). 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetLabelsToSkip
            (
                const NXString & labelsToSkip /** labelstoskip */ 
            );
            /**Sets  the characters to skip in label(text). 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            void SetLabelsToSkip
            (
                const char * labelsToSkip /** labelstoskip */ 
            );
            /**Returns  the corner zone modification used as determine the size of the corner zone. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: double CornerZoneModification
            (
            );
            /**Sets  the corner zone modification used as determine the size of the corner zone. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetCornerZoneModification
            (
                double cornerZoneModification /** cornerzonemodification */ 
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
