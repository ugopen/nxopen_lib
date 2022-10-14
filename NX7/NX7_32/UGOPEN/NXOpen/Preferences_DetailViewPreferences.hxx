#ifndef NXOpen_PREFERENCES_DETAILVIEWPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_DETAILVIEWPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_DetailViewPreferences.ja
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
#include <NXOpen/Preferences_IDetailViewPreferences.hxx>
#include <NXOpen/Preferences_ViewStylePreferencesData.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class DetailViewPreferences;
    }
    namespace Preferences
    {
        class ViewPreferences;
    }
    class NXColor;
    namespace Preferences
    {
        class IDetailViewPreferences;
    }
    namespace Preferences
    {
        /** Represents set of Detail View Preferences applicable to drafting views.  <br> To obtain an instance of this class use @link Preferences::ViewPreferences::Detail Preferences::ViewPreferences::Detail@endlink  <br> */
        class NXOPENCPPEXPORT DetailViewPreferences: public virtual Preferences::IDetailViewPreferences
        {
            private: NXOpen::Preferences::ViewPreferences* m_owner;
            public: explicit DetailViewPreferences(NXOpen::Preferences::ViewPreferences *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Sets the circular boundary option. If True, circular boundary is displayed for detail 
                        view, else rectangular boundary is displayed.
                      <br> License requirements : drafting ("DRAFTING") */
            public: void SetCircularBoundary
            (
                bool circularBoundaryOption /** circular boundary option */ 
            );
            /**Returns  the view boundary color option  <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::NXColor * ViewBoundaryColor
            (
            );
            /**Sets  the view boundary color option  <br> License requirements : drafting ("DRAFTING") */
            public: void SetViewBoundaryColor
            (
                NXOpen::NXColor * color /** color */ 
            );
            /**Returns  the view boundary font option  <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Preferences::Font ViewBoundaryFont
            (
            );
            /**Sets  the view boundary font option  <br> License requirements : drafting ("DRAFTING") */
            public: void SetViewBoundaryFont
            (
                NXOpen::Preferences::Font font /** font */ 
            );
            /**Returns  the view boundary width option  <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Preferences::Width ViewBoundaryWidth
            (
            );
            /**Sets  the view boundary width option  <br> License requirements : drafting ("DRAFTING") */
            public: void SetViewBoundaryWidth
            (
                NXOpen::Preferences::Width width /** width */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif