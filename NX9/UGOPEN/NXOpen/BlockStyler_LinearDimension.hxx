#ifndef NXOpen_BLOCKSTYLER_LINEARDIMENSION_HXX_INCLUDED
#define NXOpen_BLOCKSTYLER_LINEARDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BlockStyler_LinearDimension.ja
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
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_LinearDimension.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace BlockStyler
    {
        class LinearDimension;
    }
    namespace BlockStyler
    {
        class UIBlock;
    }
    class TaggedObject;
    namespace BlockStyler
    {
        class _LinearDimensionBuilder;
        class LinearDimensionImpl;
        /** Represents a Linear Dimension block
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENUICPPEXPORT  LinearDimension : public BlockStyler::UIBlock
        {
            private: LinearDimensionImpl * m_lineardimension_impl;
            private: friend class  _LinearDimensionBuilder;
            protected: LinearDimension();
            public: ~LinearDimension();
            /**Returns  the BalloonTooltipImage
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString BalloonTooltipImage
            (
            );
            /**Sets  the BalloonTooltipImage
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBalloonTooltipImage
            (
                const NXString & imageString /** image string */ 
            );
            /**Sets  the BalloonTooltipImage
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetBalloonTooltipImage
            (
                const char * imageString /** image string */ 
            );
            /**Returns  the BalloonTooltipLayout as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString BalloonTooltipLayoutAsString
            (
            );
            /**Sets  the BalloonTooltipLayout as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBalloonTooltipLayoutAsString
            (
                const NXString & enumString /** enumstring */ 
            );
            /**Sets  the BalloonTooltipLayout as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetBalloonTooltipLayoutAsString
            (
                const char * enumString /** enumstring */ 
            );
            /** Gets the BalloonTooltipLayout members  @return Values to get from the property. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetBalloonTooltipLayoutMembers
            (
            );
            /**Returns  the BalloonTooltipText
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString BalloonTooltipText
            (
            );
            /**Sets  the BalloonTooltipText
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBalloonTooltipText
            (
                const NXString & balloonTooltipText /** balloon tooltip text */ 
            );
            /**Sets  the BalloonTooltipText
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetBalloonTooltipText
            (
                const char * balloonTooltipText /** balloon tooltip text */ 
            );
            /**Returns  the ExpressionObject
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObject * ExpressionObject
            (
            );
            /**Sets  the ExpressionObject
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetExpressionObject
            (
                NXOpen::TaggedObject * expressionObj /** expression obj */ 
            );
            /**Returns  the Formula
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Formula
            (
            );
            /**Sets  the Formula
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetFormula
            (
                const NXString & formula /** formula */ 
            );
            /**Sets  the Formula
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetFormula
            (
                const char * formula /** formula */ 
            );
            /**Returns  the HandleOrigin
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d HandleOrigin
            (
            );
            /**Sets  the HandleOrigin
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetHandleOrigin
            (
                const NXOpen::Point3d & handleOrogin /** handle orogin */ 
            );
            /**Returns  the MaximumValue
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: double MaximumValue
            (
            );
            /**Sets  the MaximumValue
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMaximumValue
            (
                double maxValue /** max value */ 
            );
            /**Returns  the MaxInclusive
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool MaxInclusive
            (
            );
            /**Sets  the MaxInclusive
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMaxInclusive
            (
                bool maxInclusive /** max inclusive */ 
            );
            /**Returns  the MinimumValue
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: double MinimumValue
            (
            );
            /**Sets  the MinimumValue
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMinimumValue
            (
                double minValue /** min value */ 
            );
            /**Returns  the MinInclusive
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool MinInclusive
            (
            );
            /**Sets  the MinInclusive
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMinInclusive
            (
                bool minInclusive /** min inclusive */ 
            );
            /**Returns  the ShowFocusHandle
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ShowFocusHandle
            (
            );
            /**Sets  the ShowFocusHandle
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetShowFocusHandle
            (
                bool showFocus /** show focus */ 
            );
            /**Returns  the ShowHandle. If true, linear dimension handle is visible
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ShowHandle
            (
            );
            /**Sets  the ShowHandle. If true, linear dimension handle is visible
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetShowHandle
            (
                bool showHandle /** show handle */ 
            );
            /**Returns  the SnapPointTypesOnByDefault
             <br>  @deprecated Deprecated in NX9.0.0.  This call can be safely removed as this is now a no-op. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  This call can be safely removed as this is now a no-op.") int SnapPointTypesOnByDefault
            (
            );
            /**Sets  the SnapPointTypesOnByDefault
             <br>  @deprecated Deprecated in NX9.0.0.  This call can be safely removed as this is now a no-op. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  This call can be safely removed as this is now a no-op.") void SetSnapPointTypesOnByDefault
            (
                int pointType /** point type */ 
            );
            /**Returns  the Units
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObject * Units
            (
            );
            /**Sets  the Units
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetUnits
            (
                NXOpen::TaggedObject * units /** units */ 
            );
            /**Returns  the Value.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: double Value
            (
            );
            /**Sets  the Value.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetValue
            (
                double dimensionValue /** dimension value */ 
            );
            /**Returns  the WithScale. If true, the slider bar is shown.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool WithScale
            (
            );
            /**Sets  the WithScale. If true, the slider bar is shown.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetWithScale
            (
                bool withScale /** with scale */ 
            );
            /**Returns  the HandleOrientation
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Vector3d HandleOrientation
            (
            );
            /**Sets  the HandleOrientation
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetHandleOrientation
            (
                const NXOpen::Vector3d & orientation /** orientation */ 
            );
            /**Returns  the AutoReverseDuringDrag. If true, the linear dimension handle reverses its direction when it is dragged through the 0 value.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool AutoReverseDuringDrag
            (
            );
            /**Sets  the AutoReverseDuringDrag. If true, the linear dimension handle reverses its direction when it is dragged through the 0 value.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAutoReverseDuringDrag
            (
                bool autoReverse /** auto reverse */ 
            );
            /**Returns the AdaptiveScaleLimits.
                    If true, indicates that the scale should be adaptive.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool AdaptiveScaleLimits
            (
            );
            /**Sets the AdaptiveScaleLimits.
                    If true, indicates that the scale should be adaptive.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAdaptiveScaleLimits
            (
                bool scaleLimits /** scale limits */ 
            );
            /**Returns the PageIncrement value.
                    Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
                    Only available when PresentationStyle  is set to Scale or ScaleKeyin.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double PageIncrement
            (
            );
            /**Sets the PageIncrement value.
                    Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
                    Only available when PresentationStyle  is set to Scale or ScaleKeyin.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPageIncrement
            (
                double pageIncrement /** page increment */ 
            );
            /**Returns the LineIncrement value.
                    Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
                    Only available when PresentationStyle  is set to Scale or ScaleKeyin.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double LineIncrement
            (
            );
            /**Sets the LineIncrement value.
                    Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
                    Only available when PresentationStyle  is set to Scale or ScaleKeyin.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLineIncrement
            (
                double lineIncrement /** line increment */ 
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
