#ifndef NXOpen_PREFERENCES_SESSIONASSEMBLIES_HXX_INCLUDED
#define NXOpen_PREFERENCES_SESSIONASSEMBLIES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_SessionAssemblies.ja
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
    namespace Preferences
    {
        class SessionAssemblies;
    }
    namespace Preferences
    {
        class SessionPreferences;
    }
    class NXColor;
    namespace Preferences
    {
        /** Represents the set of Assemblies Preferences applicable to entire session  <br> To obtain an instance of this class, refer to @link Preferences::SessionPreferences Preferences::SessionPreferences@endlink  <br> */
        class NXOPENCPPEXPORT SessionAssemblies
        {
            /** Describe whether the part name style is file name or description or specified */
            public: enum PartNameOption
            {
                PartNameOptionFileName/** file name */ ,
                PartNameOptionDescription/** description */ ,
                PartNameOptionSpecifiedAttributes/** specified attributes */ 
            };

            private: NXOpen::Preferences::SessionPreferences* m_owner;
            public: explicit SessionAssemblies(NXOpen::Preferences::SessionPreferences *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /**Returns  the emphasize for work part   <br> License requirements : None */
            public: bool WorkPartEmphasize
            (
            );
            /**Sets  the emphasize for work part   <br> License requirements : None */
            public: void SetWorkPartEmphasize
            (
                bool workPartEmphasize /** work part emphasize */ 
            );
            /**Returns  the work part maintain option  <br> License requirements : None */
            public: bool WorkPartMaintain
            (
            );
            /**Sets  the work part maintain option  <br> License requirements : None */
            public: void SetWorkPartMaintain
            (
                bool workPartMaintain /** work part maintain */ 
            );
            /**Returns  the work part display as entire part option  <br> License requirements : None */
            public: bool WorkPartDisplayAsEntirePart
            (
            );
            /**Sets  the work part display as entire part option  <br> License requirements : None */
            public: void SetWorkPartDisplayAsEntirePart
            (
                bool workPartDisplayAsEntirePart /** work part display as entire part */ 
            );
            /**Returns  the warn on automatic change for work part option  <br> License requirements : None */
            public: bool WorkPartWarnOnAutomaticChange
            (
            );
            /**Sets  the warn on automatic change for work part option  <br> License requirements : None */
            public: void SetWorkPartWarnOnAutomaticChange
            (
                bool workPartWarnOnAutomaticChange /** work part warn on automatic change */ 
            );
            /**Returns  the product interface display emphasis setting  <br> License requirements : None */
            public: bool ProductInterfaceEmphasize
            (
            );
            /**Sets  the product interface display emphasis setting  <br> License requirements : None */
            public: void SetProductInterfaceEmphasize
            (
                bool productInterfaceEmphasize /** product interface emphasize */ 
            );
            /**Returns  the dim color for product interface display emphasis 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : None */
            public: NXOpen::NXColor * ProductInterfaceDimColor
            (
            );
            /**Sets  the dim color for product interface display emphasis 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : None */
            public: void SetProductInterfaceDimColor
            (
                NXOpen::NXColor * productInterfaceDimColor /** product interface dim color */ 
            );
            /**Returns  the check for newer revisions of template part option  <br> License requirements : None */
            public: bool CheckNewerRevisionsOfTemplatePart
            (
            );
            /**Sets  the check for newer revisions of template part option  <br> License requirements : None */
            public: void SetCheckNewerRevisionsOfTemplatePart
            (
                bool checkNewerRevisionsOfTemplatePart /** check newer revisions of template part */ 
            );
            /**Returns  the display update report option  <br> License requirements : None */
            public: bool DisplayUpdateReport
            (
            );
            /**Sets  the display update report option  <br> License requirements : None */
            public: void SetDisplayUpdateReport
            (
                bool displayUpdateReport /** display update report */ 
            );
            /**Returns  the warn on drag and drop  <br> License requirements : None */
            public: bool WarnOnDragDrop
            (
            );
            /**Sets  the warn on drag and drop  <br> License requirements : None */
            public: void SetWarnOnDragDrop
            (
                bool warnOnDragDrop /** warn on drag drop */ 
            );
            /**Returns  the component member select option  <br> License requirements : None */
            public: bool ComponentMemberSelect
            (
            );
            /**Sets  the component member select option  <br> License requirements : None */
            public: void SetComponentMemberSelect
            (
                bool componentMemberSelect /** component member select */ 
            );
            /**Returns  the preview component on add option  <br> License requirements : None */
            public: bool PreviewComponentOnAdd
            (
            );
            /**Sets  the preview component on add option  <br> License requirements : None */
            public: void SetPreviewComponentOnAdd
            (
                bool previewComponentOnAdd /** preview component on add */ 
            );
            /**Returns  the true shape filtering option  <br> License requirements : None */
            public: bool TrueShapeFiltering
            (
            );
            /**Sets  the true shape filtering option  <br> License requirements : None */
            public: void SetTrueShapeFiltering
            (
                bool trueShapeFiltering /** true shape filtering */ 
            );
            /**Returns  the part name style  <br> License requirements : None */
            public: NXOpen::Preferences::SessionAssemblies::PartNameOption PartNameStyle
            (
            );
            /**Sets  the part name style  <br> License requirements : None */
            public: void SetPartNameStyle
            (
                NXOpen::Preferences::SessionAssemblies::PartNameOption partNameStyle /** part name style */ 
            );
            /**Returns  the part name attribute  <br> License requirements : None */
            public: NXString PartNameAttribute
            (
            );
            /**Sets  the part name attribute  <br> License requirements : None */
            public: void SetPartNameAttribute
            (
                const NXString & partNameAttribute /** part name attribute */ 
            );
            /**Returns  the color for non work part 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : None */
            public: int NonWorkPartColor
            (
            );
            /**Sets  the color for non work part 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : None */
            public: void SetNonWorkPartColor
            (
                int nonWorkPartColor /** non work part color */ 
            );
            /**Returns  the update structure on assembly tree expand option  <br> License requirements : None */
            public: bool UpdateStructureOnExpand
            (
            );
            /**Sets  the update structure on assembly tree expand option  <br> License requirements : None */
            public: void SetUpdateStructureOnExpand
            (
                bool updateStructure /** update structure */ 
            );
            /**Returns  the option to allow tolerant (imprecise) geometry selection for assembly positioning  <br> License requirements : None */
            public: bool TolerantPositioning
            (
            );
            /**Sets  the option to allow tolerant (imprecise) geometry selection for assembly positioning  <br> License requirements : None */
            public: void SetTolerantPositioning
            (
                bool allowTolerantPositioning /** allow tolerant positioning */ 
            );
            /**Returns  the option to allow interpart geometry selection in the assembly constraints dialog  <br> License requirements : None */
            public: bool InterpartPositioning
            (
            );
            /**Sets  the option to allow interpart geometry selection in the assembly constraints dialog  <br> License requirements : None */
            public: void SetInterpartPositioning
            (
                bool allowInterpartPositioning /** allow interpart positioning */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif