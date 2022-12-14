#ifndef NXOpen_PREFERENCES_SMOOTHEDGESVIEWPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_SMOOTHEDGESVIEWPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_SmoothEdgesViewPreferences.ja
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
#include <NXOpen/Preferences_ISmoothEdgesViewPreferences.hxx>
#include <NXOpen/Preferences_ViewStylePreferencesData.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class SmoothEdgesViewPreferences;
    }
    namespace Preferences
    {
        class ViewPreferences;
    }
    namespace Preferences
    {
        class ISmoothEdgesViewPreferences;
    }
    namespace Preferences
    {
        /** Represents set of Smooth Edges View Preferences applicable to drafting views.
                Allows to control the display of smooth edges. Smooth edges are those whose adjacent 
                faces have the same surface tangent at the edge where they meet.
              <br> To obtain an instance of this class use @link Preferences::ViewPreferences::SmoothEdges Preferences::ViewPreferences::SmoothEdges@endlink  <br> */
        class NXOPENCPPEXPORT SmoothEdgesViewPreferences: public virtual Preferences::ISmoothEdgesViewPreferences
        {
            private: NXOpen::Preferences::ViewPreferences* m_owner;
            public: explicit SmoothEdgesViewPreferences(NXOpen::Preferences::ViewPreferences *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /**Sets  the status of smooth edge. If True then it enables the smooth edge options.  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSmoothEdge
            (
                bool smoothEdge /** smooth edge */ 
            );
            /**Returns  the status of smooth edge. If True then it enables the smooth edge options.  <br> License requirements : None */
            public: bool SmoothEdge
            (
            );
            /**Sets  the color of smooth edge. The value should be between 1 and 216. <br> License requirements : drafting ("DRAFTING") */
            public: void SetSmoothEdgeColor
            (
                int smoothEdgeColor /** smooth edge color */ 
            );
            /**Returns  the color of smooth edge. The value should be between 1 and 216. <br> License requirements : None */
            public: int SmoothEdgeColor
            (
            );
            /**Sets  the font of smooth edge. <br> License requirements : drafting ("DRAFTING") */
            public: void SetSmoothEdgeFont
            (
                NXOpen::Preferences::Font smoothEdgeFont /** smooth edge font */ 
            );
            /**Returns  the font of smooth edge. <br> License requirements : None */
            public: NXOpen::Preferences::Font SmoothEdgeFont
            (
            );
            /**Sets  the width of smooth edge. <br> License requirements : drafting ("DRAFTING") */
            public: void SetSmoothEdgeWidth
            (
                NXOpen::Preferences::Width smoothEdgeWidth /** smooth edge width */ 
            );
            /**Returns  the width of smooth edge. <br> License requirements : None */
            public: NXOpen::Preferences::Width SmoothEdgeWidth
            (
            );
            /**Sets  the status of smooth edge end gaps. If True, the visible ends are suppressed from the display.
                        The length of the suppressed end is in drawing units and is controlled by the value set in 
                        the End Gap field. If False, the visible ends are not suppressed from the display.
                      <br> License requirements : drafting ("DRAFTING") */
            public: void SetSmoothEdgeEndGaps
            (
                bool smoothEdgeEndGaps /** smooth edge end gaps */ 
            );
            /**Returns  the status of smooth edge end gaps. If True, the visible ends are suppressed from the display.
                        The length of the suppressed end is in drawing units and is controlled by the value set in 
                        the End Gap field. If False, the visible ends are not suppressed from the display.
                      <br> License requirements : None */
            public: bool SmoothEdgeEndGaps
            (
            );
            /**Sets  the value of smooth edge end gaps. <br> License requirements : drafting ("DRAFTING") */
            public: void SetSmoothEdgeEndGapsData
            (
                double smoothEdgeEndGapsData /** smooth edge end gaps data */ 
            );
            /**Returns  the value of smooth edge end gaps. <br> License requirements : None */
            public: double SmoothEdgeEndGapsData
            (
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
