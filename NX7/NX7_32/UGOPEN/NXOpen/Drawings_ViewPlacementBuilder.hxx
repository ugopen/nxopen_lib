#ifndef NXOpen_DRAWINGS_VIEWPLACEMENTBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWPLACEMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewPlacementBuilder.ja
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
#include <NXOpen/Drawings_ViewPlacementBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class ViewPlacementBuilder;
    }
    class Direction;
    namespace Drawings
    {
        class SelectDraftingView;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class SelectTaggedObject;
    namespace Drawings
    {
        class _ViewPlacementBuilderBuilder;
        /**
            Represents a @link Drawings::ViewPlacementBuilder Drawings::ViewPlacementBuilder@endlink .  This class
            is used to define the origin of a view.
            */
        class NXOPENCPPEXPORT ViewPlacementBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** view method */
            public: enum Method
            {
                MethodInfer/** Infer the view position */,
                MethodHorizontal/** Align the view horizontally to another view */,
                MethodVertical/** Align the view vertically to another view */,
                MethodPerpendicularToLine/** Align the view along some line to another view */,
                MethodOverlay/** Align the view on top of another view */
            };

            /** view option */
            public: enum Option
            {
                OptionToView/** Align to the view centers */,
                OptionModelPoint/** Align to the same point in the alignment view and the view being edited */,
                OptionPointToPoint/** Align a point in the alignment view to another point in the view being edited */
            };

            private: friend class  _ViewPlacementBuilderBuilder;
            protected: ViewPlacementBuilder();
            /**Returns  the placement location.  The location is not necessarily the
                        position of the view.  The location provides a hint point that
                        helps determine the view's position based on the alignment
                        method and alignment point specified.  <br> License requirements : None */
            public: NXOpen::Drawings::SelectDraftingView * Placement
            (
            );
            /**Returns  the alignment method  <br> License requirements : None */
            public: NXOpen::Drawings::ViewPlacementBuilder::Method AlignmentMethod
            (
            );
            /**Sets  the alignment method  <br> License requirements : drafting ("DRAFTING") */
            public: void SetAlignmentMethod
            (
                NXOpen::Drawings::ViewPlacementBuilder::Method alignmentMethod /** alignmentmethod */ 
            );
            /**Returns  the vector to align along.  The vector is only required for the
                        JA_VIEW_PLACEMENT_BUILDER_Method_perpendicular_to_line alignment
                        method.  The vector must be set regardless of the alignment option.  <br> License requirements : None */
            public: NXOpen::Direction * AlignmentVector
            (
            );
            /**Sets  the vector to align along.  The vector is only required for the
                        JA_VIEW_PLACEMENT_BUILDER_Method_perpendicular_to_line alignment
                        method.  The vector must be set regardless of the alignment option.  <br> License requirements : drafting ("DRAFTING") */
            public: void SetAlignmentVector
            (
                NXOpen::Direction * alignmentVector /** alignmentvector */ 
            );
            /**Returns  the alignment option used to indicate what points in the views to align.
                        The alignment option is not used when the alignment method is set
                        to @link Drawings::ViewPlacementBuilder::MethodInfer Drawings::ViewPlacementBuilder::MethodInfer@endlink .  <br> License requirements : None */
            public: NXOpen::Drawings::ViewPlacementBuilder::Option AlignmentOption
            (
            );
            /**Sets  the alignment option used to indicate what points in the views to align.
                        The alignment option is not used when the alignment method is set
                        to @link Drawings::ViewPlacementBuilder::MethodInfer Drawings::ViewPlacementBuilder::MethodInfer@endlink .  <br> License requirements : drafting ("DRAFTING") */
            public: void SetAlignmentOption
            (
                NXOpen::Drawings::ViewPlacementBuilder::Option alignmentOption /** alignmentoption */ 
            );
            /**Returns  the view to align to.  The view is required for all alignment
                        options.  The view is required for all alignment methods except for
                        @link Drawings::ViewPlacementBuilder::MethodInfer Drawings::ViewPlacementBuilder::MethodInfer@endlink .  <br> License requirements : None */
            public: NXOpen::Drawings::SelectDraftingView * AlignmentView
            (
            );
            /**Returns  the point to align to.  This point is only required for the
                        @link Drawings::ViewPlacementBuilder::OptionModelPoint Drawings::ViewPlacementBuilder::OptionModelPoint@endlink  and
                        @link Drawings::ViewPlacementBuilder::OptionPointToPoint Drawings::ViewPlacementBuilder::OptionPointToPoint@endlink  alignment options.
                        The point is required for all alignment methods except for
                        @link Drawings::ViewPlacementBuilder::MethodInfer Drawings::ViewPlacementBuilder::MethodInfer@endlink   <br> License requirements : None */
            public: NXOpen::SelectTaggedObject * AlignmentPoint
            (
            );
            /**Returns  the point to align in the view being edited.  This point is only
                        required for the @link Drawings::ViewPlacementBuilder::OptionPointToPoint Drawings::ViewPlacementBuilder::OptionPointToPoint@endlink 
                        alignment option.  The point is required for all alignment methods
                        except @link Drawings::ViewPlacementBuilder::MethodInfer Drawings::ViewPlacementBuilder::MethodInfer@endlink .  <br> License requirements : None */
            public: NXOpen::SelectTaggedObject * CandidatePoint
            (
            );
            /**Returns  the lock offset flag.  Use the offset property if this flag is set
                        to true.  <br> License requirements : None */
            public: bool LockOffset
            (
            );
            /**Sets  the lock offset flag.  Use the offset property if this flag is set
                        to true.  <br> License requirements : drafting ("DRAFTING") */
            public: void SetLockOffset
            (
                bool lockOffset /** lockoffset */ 
            );
            /**Returns  the offset.  If the lock offset flag is set to true then the offset
                        will be applied.  The offset has no meaning when used with the
                        @link Drawings::ViewPlacementBuilder::MethodOverlay Drawings::ViewPlacementBuilder::MethodOverlay@endlink .  If the
                        @link Drawings::ViewPlacementBuilder::MethodInfer Drawings::ViewPlacementBuilder::MethodInfer@endlink  method is set, then the offset
                        is defined as the distance from the view to its parent view.
                        For all other methods, the offset is defined as the distance along
                        the line being aligned to.  <br> License requirements : None */
            public: double Offset
            (
            );
            /**Sets  the offset.  If the lock offset flag is set to true then the offset
                        will be applied.  The offset has no meaning when used with the
                        @link Drawings::ViewPlacementBuilder::MethodOverlay Drawings::ViewPlacementBuilder::MethodOverlay@endlink .  If the
                        @link Drawings::ViewPlacementBuilder::MethodInfer Drawings::ViewPlacementBuilder::MethodInfer@endlink  method is set, then the offset
                        is defined as the distance from the view to its parent view.
                        For all other methods, the offset is defined as the distance along
                        the line being aligned to.  <br> License requirements : drafting ("DRAFTING") */
            public: void SetOffset
            (
                double offset /** offset */ 
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
