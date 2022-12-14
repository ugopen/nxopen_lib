#ifndef NXOpen_DIAGRAMMING_SHEETELEMENTBUILDER_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_SHEETELEMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_SheetElementBuilder.ja
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
#include <NXOpen/Diagramming_Annotation.hxx>
#include <NXOpen/Diagramming_DataType.hxx>
#include <NXOpen/Diagramming_LocationBuilder.hxx>
#include <NXOpen/Diagramming_Sheet.hxx>
#include <NXOpen/Diagramming_SheetElement.hxx>
#include <NXOpen/Diagramming_BaseObjectBuilder.hxx>
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
        class SheetElementBuilder;
    }
    namespace Diagramming
    {
        class Annotation;
    }
    namespace Diagramming
    {
        class BaseObjectBuilder;
    }
    namespace Diagramming
    {
        class LocationBuilder;
    }
    namespace Diagramming
    {
        class Sheet;
    }
    namespace Diagramming
    {
        class SheetElement;
    }
    namespace Diagramming
    {
        class _SheetElementBuilderBuilder;
        class SheetElementBuilderImpl;
        /**
            Represents a SheetElementBuilder.
             <br> This is an abstract class and cannot be directly instantiated  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  SheetElementBuilder : public NXOpen::Diagramming::BaseObjectBuilder
        {
            /** Represents the resize option 
                       for a @link NXOpen::Diagramming::SheetElementBuilder NXOpen::Diagramming::SheetElementBuilder@endlink .
                    
             <br>  Created in NX11.0.0.  <br>  
            */
            public: enum ResizeOptionType
            {
                ResizeOptionTypeAnyDirection/** any direction */ ,
                ResizeOptionTypeOnAnchor/** on anchor */ ,
                ResizeOptionTypeSameRatio/** same ratio */ ,
                ResizeOptionTypeSameRationOnCorner/** same ration on corner */ ,
                ResizeOptionTypeSameRatioOnEdge/** same ratio on edge */ 
            };

            private: SheetElementBuilderImpl * m_sheetelementbuilder_impl;
            private: friend class  _SheetElementBuilderBuilder;
            protected: SheetElementBuilder();
            public: ~SheetElementBuilder();
            /**Returns  the resize option of the sheet element 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::SheetElementBuilder::ResizeOptionType ResizeOption
            (
            );
            /**Sets  the resize option of the sheet element 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetResizeOption
            (
                NXOpen::Diagramming::SheetElementBuilder::ResizeOptionType resizeOption /** resizeoption */ 
            );
            /** Gets the minimum node size values 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void GetMinNodeSize
            (
                std::vector<double> & sizeValues /** Minimum node size values as output*/
            );
            /** Sets the minimum node size values 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMinNodeSize
            (
                const std::vector<double> & sizeValues /** Minimum node size values as input*/
            );
            /** Get the allowed transformations of the sheet element. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void GetAllowedTransformations
            (
                bool* isAllowedTranslation /** isallowedtranslation */ ,
                bool* isAllowedRotation /** isallowedrotation */ ,
                bool* isAllowedScale /** isallowedscale */ ,
                bool* isAllowedShear /** isallowedshear */ 
            );
            /**Returns  the height. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double Height
            (
            );
            /**Sets  the height. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetHeight
            (
                double height /** height */ 
            );
            /**Returns  the flag that indicates if the sheet element is internal. If false it is not part of the user's data model; for example, an Annotation is not part of the user's model of Nodes and Connections. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool Internal
            (
            );
            /**Returns  the location style. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::DiagrammingLocationstyle LocationStyle
            (
            );
            /**Sets  the location style. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLocationStyle
            (
                NXOpen::Diagramming::DiagrammingLocationstyle locationStyle /** locationstyle */ 
            );
            /**Returns  the absolute x coordinate. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double X
            (
            );
            /**Sets  the absolute x coordinate. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetX
            (
                double x /** x */ 
            );
            /**Returns  the absolute y coordinate. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double Y
            (
            );
            /**Sets  the absolute y coordinate. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetY
            (
                double y /** y */ 
            );
            /**Returns  the location of the sheet element relative to another sheet element. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::LocationBuilder * Location
            (
            );
            /**Returns  the label of this sheet element. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::Annotation * Label
            (
            );
            /**Returns  the label name of this sheet element. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXString LabelName
            (
            );
            /**Sets  the label name of this sheet element. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLabelName
            (
                const NXString & labelname /** labelname */ 
            );
            /**Sets  the label name of this sheet element. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            void SetLabelName
            (
                const char * labelname /** labelname */ 
            );
            /**Returns  the source element that records which sheet element it is a copy of. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::SheetElement * SourceElement
            (
            );
            /**Returns  the flag that indicates if the sheet element is up to date. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpToDate
            (
            );
            /**Returns  the flag that indicates if the sheet element is visible. If true it is visible. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool Visible
            (
            );
            /**Returns  the width. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double Width
            (
            );
            /**Sets  the width. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetWidth
            (
                double width /** width */ 
            );
            /**Returns  the rotation angle that is counter clockwise and relative to the owner. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double Rotation
            (
            );
            /**Sets  the rotation angle that is counter clockwise and relative to the owner. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRotation
            (
                double angle /** angle */ 
            );
            /**Returns  the Z depth. Higher values of the Z depth indicates that the object is rendered on top of objects with a lower value. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: int ZDepth
            (
            );
            /**Sets  the Z depth. Higher values of the Z depth indicates that the object is rendered on top of objects with a lower value. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetZDepth
            (
                int zDepth /** zdepth */ 
            );
            /**Returns  the owning sheet. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::Sheet * OwningSheet
            (
            );
            /** Set the owning sheet when the sheet element is created.
                    It is not allowed to change the owning sheet when editing the sheet element. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOwningSheet
            (
                NXOpen::Diagramming::Sheet * owningSheet /** owningsheet */ 
            );
            /**Returns  the owning sheet element. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::SheetElement * Owner
            (
            );
            /**Sets  the owning sheet element. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOwner
            (
                NXOpen::Diagramming::SheetElement * owner /** owner */ 
            );
            /**Returns  the height policy. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::DiagrammingSizingpolicy HeightPolicy
            (
            );
            /**Sets  the height policy. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetHeightPolicy
            (
                NXOpen::Diagramming::DiagrammingSizingpolicy heightPolicy /** heightpolicy */ 
            );
            /**Returns  the width policy. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::DiagrammingSizingpolicy WidthPolicy
            (
            );
            /**Sets  the width policy. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetWidthPolicy
            (
                NXOpen::Diagramming::DiagrammingSizingpolicy widthPolicy /** widthpolicy */ 
            );
            /**Returns  the sheet element to Mirror along the X axis. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool MirrorX
            (
            );
            /**Sets  the sheet element to Mirror along the X axis. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMirrorX
            (
                bool mirrorX /** mirrorx */ 
            );
            /**Returns  the sheet element to Mirror along the Y axis. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool MirrorY
            (
            );
            /**Sets  the sheet element to Mirror along the Y axis. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMirrorY
            (
                bool mirrorY /** mirrory */ 
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
