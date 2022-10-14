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
    namespace Preferences
    {
        /** Represents the set of Assemblies Preferences applicable to entire session  <br> To obtain an instance of this class, refer to @link SessionPreferences SessionPreferences@endlink  <br> */
        class NXOPENCPPEXPORT SessionAssemblies
        {
            /** Describe whether the part name style is file name or description or specified */
            public: enum PartNameOption
            {
                PartNameOptionFileName/** */,
                PartNameOptionDescription/** */,
                PartNameOptionSpecifiedAttributes/** */
            };

            private: NXOpen::Preferences::SessionPreferences* m_owner;
            public: explicit SessionAssemblies(NXOpen::Preferences::SessionPreferences *owner): m_owner(owner)
            {
            }
            public: tag_t Tag() const;
            /**Returns  the emphasize for work part   <br> License requirements : None */
            public: bool WorkPartEmphasize
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link WorkPartEmphasize() WorkPartEmphasize@endlink instead.
            @deprecated
            */
            public: bool GetWorkPartEmphasize
            (
            ) { return this->WorkPartEmphasize(); }
            /**Sets  the emphasize for work part   <br> License requirements : None */
            public: void SetWorkPartEmphasize
            (
                bool work_part_emphasize /**  */
            );
            /**Returns  the work part maintain option  <br> License requirements : None */
            public: bool WorkPartMaintain
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link WorkPartMaintain() WorkPartMaintain@endlink instead.
            @deprecated
            */
            public: bool GetWorkPartMaintain
            (
            ) { return this->WorkPartMaintain(); }
            /**Sets  the work part maintain option  <br> License requirements : None */
            public: void SetWorkPartMaintain
            (
                bool work_part_maintain /**  */
            );
            /**Returns  the work part display as entire part option  <br> License requirements : None */
            public: bool WorkPartDisplayAsEntirePart
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link WorkPartDisplayAsEntirePart() WorkPartDisplayAsEntirePart@endlink instead.
            @deprecated
            */
            public: bool GetWorkPartDisplayAsEntirePart
            (
            ) { return this->WorkPartDisplayAsEntirePart(); }
            /**Sets  the work part display as entire part option  <br> License requirements : None */
            public: void SetWorkPartDisplayAsEntirePart
            (
                bool work_part_display_as_entire_part /**  */
            );
            /**Returns  the warn on automatic change for work part option  <br> License requirements : None */
            public: bool WorkPartWarnOnAutomaticChange
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link WorkPartWarnOnAutomaticChange() WorkPartWarnOnAutomaticChange@endlink instead.
            @deprecated
            */
            public: bool GetWorkPartWarnOnAutomaticChange
            (
            ) { return this->WorkPartWarnOnAutomaticChange(); }
            /**Sets  the warn on automatic change for work part option  <br> License requirements : None */
            public: void SetWorkPartWarnOnAutomaticChange
            (
                bool work_part_warn_on_automatic_change /**  */
            );
            /**Returns  the check for newer revisions of template part option  <br> License requirements : None */
            public: bool CheckNewerRevisionsOfTemplatePart
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link CheckNewerRevisionsOfTemplatePart() CheckNewerRevisionsOfTemplatePart@endlink instead.
            @deprecated
            */
            public: bool GetCheckNewerRevisionsOfTemplatePart
            (
            ) { return this->CheckNewerRevisionsOfTemplatePart(); }
            /**Sets  the check for newer revisions of template part option  <br> License requirements : None */
            public: void SetCheckNewerRevisionsOfTemplatePart
            (
                bool check_newer_revisions_of_template_part /**  */
            );
            /**Returns  the display update report option  <br> License requirements : None */
            public: bool DisplayUpdateReport
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DisplayUpdateReport() DisplayUpdateReport@endlink instead.
            @deprecated
            */
            public: bool GetDisplayUpdateReport
            (
            ) { return this->DisplayUpdateReport(); }
            /**Sets  the display update report option  <br> License requirements : None */
            public: void SetDisplayUpdateReport
            (
                bool display_update_report /**  */
            );
            /**Returns  the warn on drag and drop  <br> License requirements : None */
            public: bool WarnOnDragDrop
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link WarnOnDragDrop() WarnOnDragDrop@endlink instead.
            @deprecated
            */
            public: bool GetWarnOnDragDrop
            (
            ) { return this->WarnOnDragDrop(); }
            /**Sets  the warn on drag and drop  <br> License requirements : None */
            public: void SetWarnOnDragDrop
            (
                bool warn_on_drag_drop /**  */
            );
            /**Returns  the component member select option  <br> License requirements : None */
            public: bool ComponentMemberSelect
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link ComponentMemberSelect() ComponentMemberSelect@endlink instead.
            @deprecated
            */
            public: bool GetComponentMemberSelect
            (
            ) { return this->ComponentMemberSelect(); }
            /**Sets  the component member select option  <br> License requirements : None */
            public: void SetComponentMemberSelect
            (
                bool component_member_select /**  */
            );
            /**Returns  the preview component on add option  <br> License requirements : None */
            public: bool PreviewComponentOnAdd
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link PreviewComponentOnAdd() PreviewComponentOnAdd@endlink instead.
            @deprecated
            */
            public: bool GetPreviewComponentOnAdd
            (
            ) { return this->PreviewComponentOnAdd(); }
            /**Sets  the preview component on add option  <br> License requirements : None */
            public: void SetPreviewComponentOnAdd
            (
                bool preview_component_on_add /**  */
            );
            /**Returns  the true shape filtering option  <br> License requirements : None */
            public: bool TrueShapeFiltering
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link TrueShapeFiltering() TrueShapeFiltering@endlink instead.
            @deprecated
            */
            public: bool GetTrueShapeFiltering
            (
            ) { return this->TrueShapeFiltering(); }
            /**Sets  the true shape filtering option  <br> License requirements : None */
            public: void SetTrueShapeFiltering
            (
                bool true_shape_filtering /**  */
            );
            /**Returns  the part name style  <br> License requirements : None */
            public: NXOpen::Preferences::SessionAssemblies::PartNameOption PartNameStyle
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link PartNameStyle() PartNameStyle@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::SessionAssemblies::PartNameOption GetPartNameStyle
            (
            ) { return this->PartNameStyle(); }
            /**Sets  the part name style  <br> License requirements : None */
            public: void SetPartNameStyle
            (
                NXOpen::Preferences::SessionAssemblies::PartNameOption part_name_style /**  */
            );
            /**Returns  the part name attribute  <br> License requirements : None */
            public: NXString PartNameAttribute
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link PartNameAttribute() PartNameAttribute@endlink instead.
            @deprecated
            */
            public: NXString GetPartNameAttribute
            (
            ) { return this->PartNameAttribute(); }
            /**Sets  the part name attribute  <br> License requirements : None */
            public: void SetPartNameAttribute
            (
                const NXString & part_name_attribute /**  */
            );
            /**Returns  the color for non work part  <br> License requirements : None */
            public: int NonWorkPartColor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link NonWorkPartColor() NonWorkPartColor@endlink instead.
            @deprecated
            */
            public: int GetNonWorkPartColor
            (
            ) { return this->NonWorkPartColor(); }
            /**Sets  the color for non work part  <br> License requirements : None */
            public: void SetNonWorkPartColor
            (
                int non_work_part_color /**  */
            );
            /**Returns  the update structure on assembly tree expand option  <br> License requirements : None */
            public: bool UpdateStructureOnExpand
            (
            );
            /**Sets  the update structure on assembly tree expand option  <br> License requirements : None */
            public: void SetUpdateStructureOnExpand
            (
                bool update_structure /**  */
            );
            /**Returns  the option to allow tolerant (imprecise) geometry selection for assembly positioning  <br> License requirements : None */
            public: bool TolerantPositioning
            (
            );
            /**Sets  the option to allow tolerant (imprecise) geometry selection for assembly positioning  <br> License requirements : None */
            public: void SetTolerantPositioning
            (
                bool allow_tolerant_positioning /**  */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif