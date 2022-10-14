#ifndef NXOpen_DISPLAYMODIFICATION_HXX_INCLUDED
#define NXOpen_DISPLAYMODIFICATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DisplayModification.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class DisplayModification;
    class DisplayableObject;
    /** Represents changes to the display characteristics of an object */
    class NXOPENCPPEXPORT DisplayModification : public TransientObject
    {
        public: explicit DisplayModification(void *ptr);
        /**Sets  the apply to all faces flag. Specifies whether the modification should apply to 
            all faces of any bodies to which this is applied.  <br> License requirements : None */
        public: void SetApplyToAllFaces
        (
            bool apply /** true to apply the modification to all faces */
        );
        /**Returns  the apply to all faces flag. Specifies whether the modification should apply to 
            all faces of any bodies to which this is applied.  <br> License requirements : None */
        public: bool ApplyToAllFaces
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link ApplyToAllFaces() ApplyToAllFaces@endlink instead.
        @deprecated
        */
        public: bool GetApplyToAllFaces
        (
        ) { return this->ApplyToAllFaces(); }
        /**Sets  a new color for objects which will be modified. This is in the range from 1 to 216.
                 <br> 
                The methods in NXOpen.UF.UFObj can be used to convert RGB values to the NX color index.
                 <br> 
              <br> License requirements : None */
        public: void SetNewColor
        (
            int new_color /** new color value */
        );
        /**Returns  a new color for objects which will be modified. This is in the range from 1 to 216.
                 <br> 
                The methods in NXOpen.UF.UFObj can be used to convert RGB values to the NX color index.
                 <br> 
              <br> License requirements : None */
        public: int NewColor
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link NewColor() NewColor@endlink instead.
        @deprecated
        */
        public: int GetNewColor
        (
        ) { return this->NewColor(); }
        /**Sets  a new line width for objects which will be modified   <br> License requirements : None */
        public: void SetNewWidth
        (
            NXOpen::DisplayableObject::ObjectWidth new_width /** new line width */
        );
        /**Returns  a new line width for objects which will be modified   <br> License requirements : None */
        public: NXOpen::DisplayableObject::ObjectWidth NewWidth
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link NewWidth() NewWidth@endlink instead.
        @deprecated
        */
        public: NXOpen::DisplayableObject::ObjectWidth GetNewWidth
        (
        ) { return this->NewWidth(); }
        /**Sets  a new font (line style) for objects which will be modified  <br> License requirements : None */
        public: void SetNewFont
        (
            NXOpen::DisplayableObject::ObjectFont new_font /** new font */
        );
        /**Returns  a new font (line style) for objects which will be modified  <br> License requirements : None */
        public: NXOpen::DisplayableObject::ObjectFont NewFont
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link NewFont() NewFont@endlink instead.
        @deprecated
        */
        public: NXOpen::DisplayableObject::ObjectFont GetNewFont
        (
        ) { return this->NewFont(); }
        /** Set a new grid count for objects which will be modified.   <br> License requirements : None */
        public: void SetNewGrid
        (
            int u_grid /** number of grid lines in the u direction */,
            int v_grid /** number of grid lines in the v direction */
        );
        /** Get grid count for objects which will be modified. Only applies to faces.  <br> License requirements : None */
        public: void GetNewGrid
        (
            int* u_grid /** number of grid lines in the u direction */,
            int* v_grid /** number of grid lines in the v direction */
        );
        /**Sets  a new layer for objects which will be modified.  <br> License requirements : None */
        public: void SetNewLayer
        (
            int layer /** new layer, must be a valid layer number */
        );
        /**Returns  a new layer for objects which will be modified.  <br> License requirements : None */
        public: int NewLayer
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link NewLayer() NewLayer@endlink instead.
        @deprecated
        */
        public: int GetNewLayer
        (
        ) { return this->NewLayer(); }
        /**Sets  a new translucency value for objects which will be modified. Only applies to faces. <br> License requirements : None */
        public: void SetNewTranslucency
        (
            int translucency /** new translucency value in the range 0 to 100 */
        );
        /**Returns  a new translucency value for objects which will be modified. Only applies to faces. <br> License requirements : None */
        public: int NewTranslucency
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link NewTranslucency() NewTranslucency@endlink instead.
        @deprecated
        */
        public: int GetNewTranslucency
        (
        ) { return this->NewTranslucency(); }
        /**Sets  the partial shading flag. Only applies to faces.  <br> License requirements : None */
        public: void SetPartiallyShaded
        (
            bool on /** true for partial shading on */
        );
        /**Returns  the partial shading flag. Only applies to faces.  <br> License requirements : None */
        public: bool PartiallyShaded
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link PartiallyShaded() PartiallyShaded@endlink instead.
        @deprecated
        */
        public: bool GetPartiallyShaded
        (
        ) { return this->PartiallyShaded(); }
        /**Sets  the face analysis mode flag. Only applies to faces.  <br> License requirements : None */
        public: void SetFaceAnalysisMode
        (
            bool on /** true to enable face analysis mode */
        );
        /**Returns  the face analysis mode flag. Only applies to faces.  <br> License requirements : None */
        public: bool FaceAnalysisMode
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link FaceAnalysisMode() FaceAnalysisMode@endlink instead.
        @deprecated
        */
        public: bool GetFaceAnalysisMode
        (
        ) { return this->FaceAnalysisMode(); }
        /** Apply this display modification to a set of objects  <br> License requirements : None */
        public: void Apply
        (
            const std::vector<NXOpen::DisplayableObject *> & objects /** objects to be modified */
        );
        /** Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET, this method
            is automatically called when the object is deleted by the garbage
            collector.  <br> License requirements : None */
        public: virtual ~DisplayModification();
        /**Sets  the flag for knot display. Only applies to b-spline.  <br> License requirements : None */
        public: void SetKnotDisplayState
        (
            bool on /** true to enable knot display */
        );
        /**Returns  the flag for knot display. Only applies to b-spline.  <br> License requirements : None */
        public: bool KnotDisplayState
        (
        );
        /**Sets  the flag for pole display. Only applies to b-spline.  <br> License requirements : None */
        public: void SetPoleDisplayState
        (
            bool on /** true to enable pole display */
        );
        /**Returns  the flag for pole display. Only applies to b-spline.  <br> License requirements : None */
        public: bool PoleDisplayState
        (
        );
    };
}
#undef EXPORTLIBRARY
#endif