#ifndef NXOpen_ANNOTATIONS_LETTERINGPREFERENCES_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_LETTERINGPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_LetteringPreferences.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Annotations.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class LetteringPreferences;
    }
    namespace Annotations
    {
    }
    namespace Annotations
    {
        /** Represents lettering preferences.
             <br>  When setting the property, changes are not applied to object until
            @link Annotation::SetLetteringPreferences Annotation::SetLetteringPreferences@endlink  is called  <br>  */
        class NXOPENCPPEXPORT LetteringPreferences : public TransientObject
        {
            public: explicit LetteringPreferences(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~LetteringPreferences();
            /**Returns  the align position  <br> License requirements : None */
            public: NXOpen::Annotations::AlignmentPosition AlignmentPosition
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link AlignmentPosition() AlignmentPosition@endlink instead.
            @deprecated
            */
            public: NXOpen::Annotations::AlignmentPosition GetAlignmentPosition
            (
            ) { return this->AlignmentPosition(); }
            /**Sets  the align position  <br> License requirements : None */
            public: void SetAlignmentPosition
            (
                NXOpen::Annotations::AlignmentPosition align_position /** align position */ 
            );
            /**Returns  the horizontal text justification  <br> License requirements : None */
            public: NXOpen::Annotations::TextJustification HorizTextJust
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link HorizTextJust() HorizTextJust@endlink instead.
            @deprecated
            */
            public: NXOpen::Annotations::TextJustification GetHorizTextJust
            (
            ) { return this->HorizTextJust(); }
            /**Sets  the horizontal text justification  <br> License requirements : None */
            public: void SetHorizTextJust
            (
                NXOpen::Annotations::TextJustification horiz_text_just /** horiz text just */ 
            );
            /**Returns  the gdt frame height factor  <br> License requirements : None */
            public: double GdtFrameHeightFactor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link GdtFrameHeightFactor() GdtFrameHeightFactor@endlink instead.
            @deprecated
            */
            public: double GetGdtFrameHeightFactor
            (
            ) { return this->GdtFrameHeightFactor(); }
            /**Sets  the gdt frame height factor  <br> License requirements : None */
            public: void SetGdtFrameHeightFactor
            (
                double gdt_frame_height_factor /** gdt frame height factor */ 
            );
            /**Returns  the angle  <br> License requirements : None */
            public: double Angle
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link Angle() Angle@endlink instead.
            @deprecated
            */
            public: double GetAngle
            (
            ) { return this->Angle(); }
            /**Sets  the angle  <br> License requirements : None */
            public: void SetAngle
            (
                double angle /** angle */ 
            );
            /**Returns  the dimension/dimension line space factor  <br> License requirements : None */
            public: double DimDimLineSpaceFactor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DimDimLineSpaceFactor() DimDimLineSpaceFactor@endlink instead.
            @deprecated
            */
            public: double GetDimDimLineSpaceFactor
            (
            ) { return this->DimDimLineSpaceFactor(); }
            /**Sets  the dimension/dimension line space factor  <br> License requirements : None */
            public: void SetDimDimLineSpaceFactor
            (
                double dim_dim_line_space_factor /** dim dim line space factor */ 
            );
            /**Returns  the dimension/appended text space factor  <br> License requirements : None */
            public: double DimAppendedTextSpaceFactor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DimAppendedTextSpaceFactor() DimAppendedTextSpaceFactor@endlink instead.
            @deprecated
            */
            public: double GetDimAppendedTextSpaceFactor
            (
            ) { return this->DimAppendedTextSpaceFactor(); }
            /**Sets  the dimension/appended text space factor  <br> License requirements : None */
            public: void SetDimAppendedTextSpaceFactor
            (
                double dim_app_text_space_factor /** dim app text space factor */ 
            );
            /**Returns  the dimension/tolerance text space factor  <br> License requirements : None */
            public: double DimToleranceTextSpaceFactor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DimToleranceTextSpaceFactor() DimToleranceTextSpaceFactor@endlink instead.
            @deprecated
            */
            public: double GetDimToleranceTextSpaceFactor
            (
            ) { return this->DimToleranceTextSpaceFactor(); }
            /**Sets  the dimension/tolerance text space factor  <br> License requirements : None */
            public: void SetDimToleranceTextSpaceFactor
            (
                double dim_tol_text_space_factor /** dim tol text space factor */ 
            );
            /** Returns the dimension text  @return   <br> License requirements : None */
            public: NXOpen::Annotations::Lettering GetDimensionText
            (
            );
            /** Sets the dimension text  <br> License requirements : None */
            public: void SetDimensionText
            (
                const NXOpen::Annotations::Lettering & dimension_text /** dimension text */ 
            );
            /** Returns the appended text  @return   <br> License requirements : None */
            public: NXOpen::Annotations::Lettering GetAppendedText
            (
            );
            /** Sets the appended text  <br> License requirements : None */
            public: void SetAppendedText
            (
                const NXOpen::Annotations::Lettering & appended_text /** appended text */ 
            );
            /** Returns the tolerance text  @return   <br> License requirements : None */
            public: NXOpen::Annotations::Lettering GetToleranceText
            (
            );
            /** Sets the tolerance text  <br> License requirements : None */
            public: void SetToleranceText
            (
                const NXOpen::Annotations::Lettering & tolerance_text /** tolerance text */ 
            );
            /** Returns the general text  @return   <br> License requirements : None */
            public: NXOpen::Annotations::Lettering GetGeneralText
            (
            );
            /** Sets the general text  <br> License requirements : None */
            public: void SetGeneralText
            (
                const NXOpen::Annotations::Lettering & general_text /** general text */ 
            );
            /**Returns  the stack vertical(above/below) alignment option  <br> License requirements : None */
            public: NXOpen::Annotations::StackVerticalAlignment StackVerticalAlignment
            (
            );
            /**Sets  the stack vertical(above/below) alignment option  <br> License requirements : None */
            public: void SetStackVerticalAlignment
            (
                NXOpen::Annotations::StackVerticalAlignment vertical_alignment /** vertical alignment */ 
            );
            /**Returns  the stack horizontal(left/right) alignment option  <br> License requirements : None */
            public: NXOpen::Annotations::StackHorizontalAlignment StackHorizontalAlignment
            (
            );
            /**Sets  the stack horizontal(left/right) alignment option  <br> License requirements : None */
            public: void SetStackHorizontalAlignment
            (
                NXOpen::Annotations::StackHorizontalAlignment horizontal_alignment /** horizontal alignment */ 
            );
            /**Returns  the stack above spacing factor for space buffer above annotation in stack. <br> License requirements : None */
            public: double StackAboveSpaceFactor
            (
            );
            /**Sets  the stack above spacing factor for space buffer above annotation in stack. <br> License requirements : None */
            public: void SetStackAboveSpaceFactor
            (
                double stack_above_space_factor /** stack above space factor */ 
            );
            /**Returns  the stack below spacing factor for space buffer below annotation in stack. <br> License requirements : None */
            public: double StackBelowSpaceFactor
            (
            );
            /**Sets  the stack below spacing factor for space buffer below annotation in stack. <br> License requirements : None */
            public: void SetStackBelowSpaceFactor
            (
                double stack_below_space_factor /** stack below space factor */ 
            );
            /**Returns  the stack left spacing factor for space buffer left annotation in stack. <br> License requirements : None */
            public: double StackLeftSpaceFactor
            (
            );
            /**Sets  the stack left spacing factor for space buffer left annotation in stack. <br> License requirements : None */
            public: void SetStackLeftSpaceFactor
            (
                double stack_left_space_factor /** stack left space factor */ 
            );
            /**Returns  the stack right spacing factor for space buffer right annotation in stack. <br> License requirements : None */
            public: double StackRightSpaceFactor
            (
            );
            /**Sets  the stack right spacing factor for space buffer right annotation in stack. <br> License requirements : None */
            public: void SetStackRightSpaceFactor
            (
                double stack_right_space_factor /** stack right space factor */ 
            );
            /**Returns  the flag indicating whether to inherit the associated objects of a stack when 
                        an annotation is inserted into a stack.  <br> License requirements : None */
            public: bool StackInheritAssociatedObjects
            (
            );
            /**Sets  the flag indicating whether to inherit the associated objects of a stack when 
                        an annotation is inserted into a stack.  <br> License requirements : None */
            public: void SetStackInheritAssociatedObjects
            (
                bool stack_inherit_associated_objects /** Flag to whether inherit associated objects of stack*/
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif