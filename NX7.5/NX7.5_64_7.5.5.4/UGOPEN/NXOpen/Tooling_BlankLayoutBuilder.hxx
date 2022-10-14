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
#include <NXOpen/Tooling_BlankLayoutBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** Progressive Die Wizard blank layout builder <br> To create a new instance of this class, use @link Tooling::BlankLayoutCollection::CreateBlankLayoutBuilder Tooling::BlankLayoutCollection::CreateBlankLayoutBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Bottom </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        LockPitchAndWidth </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        MinimumSpaceSize </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Pitch </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Rotate </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SideWeb </td> <td> 
         
        Average </td> </tr> 

        <tr><td> 
         
        SnapSize </td> <td> 
         
        One </td> </tr> 

        <tr><td> 
         
        Top </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Width </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        XShift </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        YShift </td> <td> 
         
        0 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  BlankLayoutBuilder : public Builder
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
            /**Returns  the blank layout type. <br> License requirements : None */
            public: NXOpen::Tooling::BlankLayoutBuilder::Types Type
            (
            );
            /**Sets  the blank layout type. <br> License requirements : None */
            public: void SetType
            (
                NXOpen::Tooling::BlankLayoutBuilder::Types type /** type */ 
            );
            /**Returns  the selected blank name. <br> License requirements : None */
            public: NXString BlankNameStr
            (
            );
            /**Sets  the selected blank name. <br> License requirements : None */
            public: void SetBlankNameStr
            (
                const NXString & blankNameStr /** Sets the blank name */
            );
            /**Returns  the blank. <br> License requirements : None */
            public: NXOpen::SelectBody * Blank
            (
            );
            /**Returns  the base point.  <br> License requirements : None */
            public: NXOpen::Point * BasePoint
            (
            );
            /**Sets  the base point.  <br> License requirements : None */
            public: void SetBasePoint
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns  the value to shift the blank in the X direction. <br> License requirements : None */
            public: double XShift
            (
            );
            /**Sets  the value to shift the blank in the X direction. <br> License requirements : None */
            public: void SetXShift
            (
                double xShift /** xshift */ 
            );
            /**Returns  the value to shift the blank in the Y direction. <br> License requirements : None */
            public: double YShift
            (
            );
            /**Sets  the value to shift the blank in the Y direction. <br> License requirements : None */
            public: void SetYShift
            (
                double yShift /** yshift */ 
            );
            /**Returns  the value to rotate the blank around the base point. <br> License requirements : None */
            public: double Rotate
            (
            );
            /**Sets  the value to rotate the blank around the base point. <br> License requirements : None */
            public: void SetRotate
            (
                double rotate /** rotate */ 
            );
            /**Returns  the distance between the adjacent stations. <br> License requirements : None */
            public: double Pitch
            (
            );
            /**Sets  the distance between the adjacent stations. <br> License requirements : None */
            public: void SetPitch
            (
                double pitch /** pitch */ 
            );
            /**Returns  the width of the strip. <br> License requirements : None */
            public: double Width
            (
            );
            /**Sets  the width of the strip. <br> License requirements : None */
            public: void SetWidth
            (
                double width /** width */ 
            );
            /**Returns  the top boudary distance between blank and strip. <br> License requirements : None */
            public: double Top
            (
            );
            /**Sets  the top boudary distance between blank and strip. <br> License requirements : None */
            public: void SetTop
            (
                double top /** top */ 
            );
            /**Returns  the bottom boundary distance between blank and strip. <br> License requirements : None */
            public: double Bottom
            (
            );
            /**Sets  the bottom boundary distance between blank and strip. <br> License requirements : None */
            public: void SetBottom
            (
                double bottom /** bottom */ 
            );
            /**Returns  the type of the overlap on the strip. <br> License requirements : None */
            public: NXOpen::Tooling::BlankLayoutBuilder::SideWebOption SideWeb
            (
            );
            /**Sets  the type of the overlap on the strip. <br> License requirements : None */
            public: void SetSideWeb
            (
                NXOpen::Tooling::BlankLayoutBuilder::SideWebOption sideWeb /** sideweb */ 
            );
            /**Returns  the material utilization of the blank. <br> License requirements : None */
            public: NXString MaterialUtilization
            (
            );
            /**Sets  the material utilization of the blank. <br> License requirements : None */
            public: void SetMaterialUtilization
            (
                const NXString & materialUtilization /** materialutilization */ 
            );
            /**Returns  the option to report minimum space size or not. <br> License requirements : None */
            public: bool MinimumSpaceSize
            (
            );
            /**Sets  the option to report minimum space size or not. <br> License requirements : None */
            public: void SetMinimumSpaceSize
            (
                bool minimumSpaceSize /** minimumspacesize */ 
            );
            /**Returns  the minimum distance between the adjacent blanks. <br> License requirements : None */
            public: NXString MinimumSpaceSizeValue
            (
            );
            /**Sets  the minimum distance between the adjacent blanks. <br> License requirements : None */
            public: void SetMinimumSpaceSizeValue
            (
                const NXString & minimumSpaceSizeValue /** minimumspacesizevalue */ 
            );
            /**Returns  the option to set the increment of the scale bar. <br> License requirements : None */
            public: NXOpen::Tooling::BlankLayoutBuilder::SnapSizeOption SnapSize
            (
            );
            /**Sets  the option to set the increment of the scale bar. <br> License requirements : None */
            public: void SetSnapSize
            (
                NXOpen::Tooling::BlankLayoutBuilder::SnapSizeOption snapSize /** snapsize */ 
            );
            /**Returns  the lock pitch and width values from being changed during processing.  <br> License requirements : None */
            public: bool LockPitchAndWidth
            (
            );
            /**Sets  the lock pitch and width values from being changed during processing.  <br> License requirements : None */
            public: void SetLockPitchAndWidth
            (
                bool lockPitchAndWidth /** lockpitchandwidth */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif