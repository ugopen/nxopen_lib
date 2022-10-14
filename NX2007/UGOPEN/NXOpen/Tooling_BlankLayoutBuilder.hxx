#ifndef NXOpen_TOOLING_BLANKLAYOUTBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_BLANKLAYOUTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_BlankLayoutBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class BlankLayoutBuilder;
    }
    class Builder;
    class Point;
    class SelectBody;
    namespace Tooling
    {
        class _BlankLayoutBuilderBuilder;
        class BlankLayoutBuilderImpl;
        /** Progressive Die Wizard blank layout builder <br> To create a new instance of this class, use @link NXOpen::Tooling::BlankLayoutCollection::CreateBlankLayoutBuilder  NXOpen::Tooling::BlankLayoutCollection::CreateBlankLayoutBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Bottom </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        LeftDistance </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        LeftRightSide </term> <description> 
         
        Average </description> </item> 

        <item><term> 
         
        LockPitch </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        LockPitchAndWidth </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        LockRotate </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        LockShiftX </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        LockShiftY </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        LockWidth </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        MinimumSpaceSize </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Pitch </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RightDistance </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Rotate </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        SideWeb </term> <description> 
         
        Average </description> </item> 

        <item><term> 
         
        SnapSize </term> <description> 
         
        One </description> </item> 

        <item><term> 
         
        ThreeBlanks </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Top </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Width </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        XShift </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        YShift </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  BlankLayoutBuilder : public NXOpen::Builder
        {
            /** Specifies the option of blank layout type. */
            public: enum Types
            {
                TypesCreateLayout/** the type of create blank layout */,
                TypesAddBlank/** the type of add multiple blank */,
                TypesCopyBlank/** the type of copy blank */,
                TypesRemoveBlank/** the type of remove blank */,
                TypesSetBasePoint/** the type of set the base point of the blank */,
                TypesFlipBlank/** the type of flip blank */
            };

            /** Specifies the option of side webs type. */
            public: enum SideWebOption
            {
                SideWebOptionAverage/** the side webs type of average */,
                SideWebOptionBottom/** the side webs type of bottom */,
                SideWebOptionTop/** the side webs type of top */
            };

            /** Specifies the option of left right side type. */
            public: enum LeftRightSideOption
            {
                LeftRightSideOptionAverage/** the left right side type of average */,
                LeftRightSideOptionLeft/** the left side type */,
                LeftRightSideOptionRight/** the right side type */
            };

            /** Specifies the option of snap size. */
            public: enum SnapSizeOption
            {
                SnapSizeOptionTenth/** the snap size is 0.1 */,
                SnapSizeOptionFifth/** the snap size is 0.2 */,
                SnapSizeOptionHalf/** the snap size is 1/2 */,
                SnapSizeOptionOne/** the snap size is 1 */,
                SnapSizeOptionTwo/** the snap size is 2 */,
                SnapSizeOptionFive/** the snap size is 5 */,
                SnapSizeOptionTen/** the snap size is 10 */
            };

            private: BlankLayoutBuilderImpl * m_blanklayoutbuilder_impl;
            private: friend class  _BlankLayoutBuilderBuilder;
            protected: BlankLayoutBuilder();
            public: ~BlankLayoutBuilder();
            /**Returns  the blank layout type.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::BlankLayoutBuilder::Types Type
            (
            );
            /**Sets  the blank layout type.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetType
            (
                NXOpen::Tooling::BlankLayoutBuilder::Types type /** type */ 
            );
            /**Returns  the selected blank name.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString BlankNameStr
            (
            );
            /**Sets  the selected blank name.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBlankNameStr
            (
                const NXString & blankNameStr /** Sets the blank name */
            );
            /**Sets  the selected blank name.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetBlankNameStr
            (
                const char * blankNameStr /** Sets the blank name */
            );
            /**Returns  the blank.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBody * Blank
            (
            );
            /**Returns  the base point. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * BasePoint
            (
            );
            /**Sets  the base point. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBasePoint
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns  the option to lock the x value or not.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool LockShiftX
            (
            );
            /**Sets  the option to lock the x value or not.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLockShiftX
            (
                bool lockShiftX /** lockshiftx */ 
            );
            /**Returns  the value to shift the blank in the X direction.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double XShift
            (
            );
            /**Sets  the value to shift the blank in the X direction.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetXShift
            (
                double xShift /** xshift */ 
            );
            /**Returns  the option to lock the y value or not.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool LockShiftY
            (
            );
            /**Sets  the option to lock the y value or not.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLockShiftY
            (
                bool lockShiftY /** lockshifty */ 
            );
            /**Returns  the value to shift the blank in the Y direction.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double YShift
            (
            );
            /**Sets  the value to shift the blank in the Y direction.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetYShift
            (
                double yShift /** yshift */ 
            );
            /**Returns  the option to lock the rotate value or not.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool LockRotate
            (
            );
            /**Sets  the option to lock the rotate value or not.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLockRotate
            (
                bool lockRotate /** lockrotate */ 
            );
            /**Returns  the value to rotate the blank around the base point.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double Rotate
            (
            );
            /**Sets  the value to rotate the blank around the base point.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetRotate
            (
                double rotate /** rotate */ 
            );
            /**Returns  the option to lock the pitch value or not.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool LockPitch
            (
            );
            /**Sets  the option to lock the pitch value or not.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLockPitch
            (
                bool lockPitch /** lockpitch */ 
            );
            /**Returns  the distance between the adjacent stations.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double Pitch
            (
            );
            /**Sets  the distance between the adjacent stations.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetPitch
            (
                double pitch /** pitch */ 
            );
            /**Returns  the option to lock the width value or not.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool LockWidth
            (
            );
            /**Sets  the option to lock the width value or not.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLockWidth
            (
                bool lockWidth /** lockwidth */ 
            );
            /**Returns  the width of the strip.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double Width
            (
            );
            /**Sets  the width of the strip.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetWidth
            (
                double width /** width */ 
            );
            /**Returns  the top boudary distance between blank and strip.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double Top
            (
            );
            /**Sets  the top boudary distance between blank and strip.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetTop
            (
                double top /** top */ 
            );
            /**Returns  the bottom boundary distance between blank and strip.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double Bottom
            (
            );
            /**Sets  the bottom boundary distance between blank and strip.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBottom
            (
                double bottom /** bottom */ 
            );
            /**Returns  the type of the overlap on the strip.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::BlankLayoutBuilder::SideWebOption SideWeb
            (
            );
            /**Sets  the type of the overlap on the strip.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSideWeb
            (
                NXOpen::Tooling::BlankLayoutBuilder::SideWebOption sideWeb /** sideweb */ 
            );
            /**Returns  the left boudary distance between blank and strip.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double LeftDistance
            (
            );
            /**Sets  the left boudary distance between blank and strip.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLeftDistance
            (
                double leftDistance /** leftdistance */ 
            );
            /**Returns  the right boundary distance between blank and strip.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double RightDistance
            (
            );
            /**Sets  the right boundary distance between blank and strip.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRightDistance
            (
                double rightDistance /** rightdistance */ 
            );
            /**Returns  the type of use left or right side to decide the distance between blank and strip.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::BlankLayoutBuilder::LeftRightSideOption LeftRightSide
            (
            );
            /**Sets  the type of use left or right side to decide the distance between blank and strip.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLeftRightSide
            (
                NXOpen::Tooling::BlankLayoutBuilder::LeftRightSideOption leftRightSide /** leftrightside */ 
            );
            /**Returns  the material utilization of the blank.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString MaterialUtilization
            (
            );
            /**Sets  the material utilization of the blank.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMaterialUtilization
            (
                const NXString & materialUtilization /** materialutilization */ 
            );
            /**Sets  the material utilization of the blank.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetMaterialUtilization
            (
                const char * materialUtilization /** materialutilization */ 
            );
            /**Returns  the option to report minimum space size or not.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool MinimumSpaceSize
            (
            );
            /**Sets  the option to report minimum space size or not.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMinimumSpaceSize
            (
                bool minimumSpaceSize /** minimumspacesize */ 
            );
            /**Returns  the minimum distance between the adjacent blanks.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString MinimumSpaceSizeValue
            (
            );
            /**Sets  the minimum distance between the adjacent blanks.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMinimumSpaceSizeValue
            (
                const NXString & minimumSpaceSizeValue /** minimumspacesizevalue */ 
            );
            /**Sets  the minimum distance between the adjacent blanks.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetMinimumSpaceSizeValue
            (
                const char * minimumSpaceSizeValue /** minimumspacesizevalue */ 
            );
            /**Returns  the option to set the increment of the scale bar.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::BlankLayoutBuilder::SnapSizeOption SnapSize
            (
            );
            /**Sets  the option to set the increment of the scale bar.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSnapSize
            (
                NXOpen::Tooling::BlankLayoutBuilder::SnapSizeOption snapSize /** snapsize */ 
            );
            /**Returns  the lock pitch and width values from being changed during processing. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool LockPitchAndWidth
            (
            );
            /**Sets  the lock pitch and width values from being changed during processing. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetLockPitchAndWidth
            (
                bool lockPitchAndWidth /** lockpitchandwidth */ 
            );
            /**Returns  the usage of three blanks or one blank. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool ThreeBlanks
            (
            );
            /**Sets  the usage of three blanks or one blank. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetThreeBlanks
            (
                bool threeBlanks /** threeblanks */ 
            );
            /** Method that reposition the blanks after bottom. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void RepositionBottom
            (
            );
            /** Method that reposition the blanks after modify left distance value. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void RepositionLeftDistance
            (
            );
            /** Method that reposition the blanks after change average, left, right types. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void RepositionLeftRightSide
            (
            );
            /** Method that repostion the blanks after pitch. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void RepositionPitch
            (
            );
            /** Method that reposition the blanks after modify right distance value. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void RepositionRightDistance
            (
            );
            /** Method that reposition the blanks after rotate. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void RepositionRotate
            (
            );
            /** Method that reposition the blanks after sideWeb. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void RepositionSideWeb
            (
            );
            /** Method that reposition the blanks after top. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void RepositionTop
            (
            );
            /** Method that repostion the blanks after width. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void RepositionWidth
            (
            );
            /** Method that reposition the blanks after shiftX. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void RepositionShiftX
            (
            );
            /** Method that reposition the blanks after shiftY. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void RepositionShiftY
            (
            );
            /** Method that update the blank layout. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void UpdateBlankLayout
            (
            );
            /** Method that set bounding box. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBoundingBox
            (
            );
            /** Method that set bounding box. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetItemValue
            (
            );
            /** Method that set bounding box. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetMaterialUtilization
            (
            );
            /** Method that insert a blank that has not been inserted under UP_NEST. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void InsertBlank
            (
                const NXString & blankName /** blankname */ 
            );
            /** Method that insert a blank that has not been inserted under UP_NEST. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void InsertBlank
            (
                const char * blankName /** blankname */ 
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