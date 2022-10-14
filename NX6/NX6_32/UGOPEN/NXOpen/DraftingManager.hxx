#ifndef NXOpen_DRAFTINGMANAGER_HXX_INCLUDED
#define NXOpen_DRAFTINGMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DraftingManager.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class DraftingManager;
    class Part;
    namespace Drawings
    {
        class SectionLineCollection;
    }
    class NXObject;
    /** Represents an object that manages drafting objects and member views.  <br> To obtain an instance of this class, refer to @link Part Part@endlink  <br> */
    class NXOPENCPPEXPORT DraftingManager
    {
        private: NXOpen::Part* m_owner;
        public: explicit DraftingManager(NXOpen::Part *owner): m_owner(owner)
        {
        }
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        /** Converts all older drafting objects (including member views) in the part to the latest version.  <br> License requirements : None */
        public: void VersionUpAllDraftingObjects
        (
        );
        /** Converts selected drafting objects (including member views) in the part to the latest version.  <br> License requirements : None */
        public: void VersionUpSelectedDraftingObjects
        (
            const std::vector<NXOpen::NXObject *> & draftingObjects /** drafting objects */ 
        );


        private: NXOpen::Drawings::SectionLineCollection *sectionLines;
        /** Section Line Collection */
        public: NXOpen::Drawings::SectionLineCollection *SectionLines()
        {
            return sectionLines;
        }
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif