#ifndef NXOpen_DRAWINGS_THREADSVIEWSTYLE_HXX_INCLUDED
#define NXOpen_DRAWINGS_THREADSVIEWSTYLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ThreadsViewStyle.ja
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
#include <NXOpen/Preferences_IThreadsViewPreferences.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class ThreadsViewStyle;
    }
    namespace Drawings
    {
        class ViewStyle;
    }
    namespace Preferences
    {
        class IThreadsViewPreferences;
    }
    namespace Drawings
    {
        /** Represents set of Threads View Style Preferences applicable to drafting views. 
                Allows to create ANSI and ISO thread representations for both internal 
                and external threads in drawing member views.
              <br> To obtain an instance of this class, refer to @link Drawings::ViewStyle Drawings::ViewStyle@endlink  <br> */
        class NXOPENCPPEXPORT ThreadsViewStyle: public virtual Preferences::IThreadsViewPreferences
        {
            private: NXOpen::Drawings::ViewStyle* m_owner;
            public: explicit ThreadsViewStyle(NXOpen::Drawings::ViewStyle *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /**Returns  the threads standard option  <br> License requirements : None */
            public: int ThreadsStandardOptionData
            (
            );
            /**Sets  the threads standard option  <br> License requirements : drafting ("DRAFTING") */
            public: void SetThreadsStandardOptionData
            (
                int threads_standard_option_data /** threads standard option data */ 
            );
            /**Returns  the minimum pitch field. Allows to control the minimum distance (in drawing coordinates) 
            		    to which two points which represent crests of a thread are drawn. It is also used to control 
            		    the minimum distance between a thread and it's defining geometry such as edges, silhouettes or 
            		    section edges of the cylindrical face or chamfered face. This can be used to help prevent lines 
            		    from running together, when threads with a small pitch are plotted at a small scale.
                      <br> License requirements : None */
            public: double MinimumPitchField
            (
            );
            /**Sets  the minimum pitch field. Allows to control the minimum distance (in drawing coordinates) 
            		    to which two points which represent crests of a thread are drawn. It is also used to control 
            		    the minimum distance between a thread and it's defining geometry such as edges, silhouettes or 
            		    section edges of the cylindrical face or chamfered face. This can be used to help prevent lines 
            		    from running together, when threads with a small pitch are plotted at a small scale.
                      <br> License requirements : drafting ("DRAFTING") */
            public: void SetMinimumPitchField
            (
                double minimum_pitch_field /** minimum pitch field */ 
            );
            /**Returns  the status of render true hidden line  <br> License requirements : None */
            public: bool RenderTrueHiddenLine
            (
            );
            /**Sets  the status of render true hidden line  <br> License requirements : drafting ("DRAFTING") */
            public: void SetRenderTrueHiddenLine
            (
                bool render_true_hidden_line /** render true hidden line */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
