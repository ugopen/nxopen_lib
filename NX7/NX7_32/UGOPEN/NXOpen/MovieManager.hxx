#ifndef NXOpen_MOVIEMANAGER_HXX_INCLUDED
#define NXOpen_MOVIEMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MovieManager.ja
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
#include <NXOpen/MovieSettingsBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>
namespace NXOpen
{
    class MovieManager;
    class UI;
    class MovieSettingsBuilder;
    /** Represents a @link MovieManager MovieManager@endlink  class. This class is used 
        for recording movies.
     <br> To obtain an instance of this class, refer to @link UI UI@endlink  <br> */
    class NXOPENUICPPEXPORT MovieManager
    {
        private: NXOpen::UI* m_owner;
        public: explicit MovieManager(NXOpen::UI *owner): m_owner(owner)
        {
        }
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        /** Creates a @link MovieSettingsBuilder MovieSettingsBuilder@endlink   @return   <br> License requirements : None */
        public: NXOpen::MovieSettingsBuilder * CreateMovieSettingsBuilder
        (
        );
        /** Starts movie recording  <br> License requirements : None */
        public: void Start
        (
            const NXString & filename /** Filename of the movie to be createed   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            bool userFrames /** If true, user will provide frames through @link MovieManager::CaptureFrame MovieManager::CaptureFrame@endlink . If false, system generates frames */
        );
        /** Pauses movie recording  <br> License requirements : None */
        public: void Pause
        (
        );
        /** Resumes movie recording  <br> License requirements : None */
        public: void Resume
        (
        );
        /** Stops movie recording  <br> License requirements : None */
        public: void End
        (
        );
        /** Use this method to capture a frame at a specified point. This is used when the
                movie recording was started with true as the second parameter of @link MovieManager::Start MovieManager::Start@endlink 
             <br> License requirements : None */
        public: void CaptureFrame
        (
        );
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif
