#ifndef NXOpen_BLOCKSTYLER_WIZARD_HXX_INCLUDED
#define NXOpen_BLOCKSTYLER_WIZARD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BlockStyler_Wizard.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/BlockStyler_TreeListMenu.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace BlockStyler
    {
        class Wizard;
    }
    namespace BlockStyler
    {
        class PropertyList;
    }
    namespace BlockStyler
    {
        class TreeListMenu;
    }
    namespace BlockStyler
    {
        class UIBlock;
    }
    namespace BlockStyler
    {
        class _WizardBuilder;
        class WizardImpl;
        /** Represents a Wizard block 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENUICPPEXPORT  Wizard : public NXOpen::BlockStyler::UIBlock
        {
            /** Specifies an item in the Task Navigator.  */
            public: enum TaskNavigatorItem
            {
                TaskNavigatorItemStep/** step */ ,
                TaskNavigatorItemSubNode/** sub node */ ,
                TaskNavigatorItemBackground/** background */ 
            };

            /** Specifies the type of action performed on a sub-node in the Wizard Task Navigator.
                    The action is passed into the callback BlockStyler.Wizard.OnSubNodeCallback. */
            public: enum SubNodeAction
            {
                SubNodeActionSelect/** Sub-node has been selected. */,
                SubNodeActionDeselect/** Sub-node has been deselected. */,
                SubNodeActionCheck/** Sub-node has been checked if a checkbox was specified. */,
                SubNodeActionUncheck/** Sub-node has been unchecked if a checkbox was specified. */
            };

            public: /** The StepNotifyPre callback notifies a client before navigating to the next step 
                    in the Wizard.  The nextStep parameter for the callback is zero based and represents
                    the steps in the Wizard. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback2<int, NXOpen::BlockStyler::Wizard *, int> StepNotifyPreCallback;
            public: /** The StepNotifyPost callback notifies a client after navigating to the next step 
                    in the Wizard.  The nextStep parameter for the callback is zero based and represents
                    the steps in the Wizard. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback2<void, NXOpen::BlockStyler::Wizard *, int> StepNotifyPostCallback;
            public: /** The IsStepOkay callback allows the client to notify the Wizard that the step is okay
                    or not.  Returns true if the step is okay and false otherwise. The step parameter for the
                    callback is zero based and represents the steps in the Wizard.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback2<bool, NXOpen::BlockStyler::Wizard *, int> IsStepOkayCallback;
            public: /** The OnSubNode callback notifies a client of an action performed
                    on a sub-node in the Wizard Task Navigator.  The step
                    parameter for the callback is zero based and represents the steps in the Wizard.
                    The subNodeId parameter is the unique id returned by @link BlockStyler::Wizard::CreateStepSubNode BlockStyler::Wizard::CreateStepSubNode@endlink .  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback4<void, NXOpen::BlockStyler::Wizard *, int, int, NXOpen::BlockStyler::Wizard::SubNodeAction> OnSubNodeCallback;
            public: /** The OnMenu callback notifies a client prior to creating the popup menu in the Task
                    Navigator.  The item parameter specifies the popup menu was activated on a step,
                    sub-node or the background. The step parameter for the callback is zero based and
                    represents the steps in the Wizard.  The subNodeId parameter is the unique id returned
                    by @link BlockStyler::Wizard::CreateStepSubNode BlockStyler::Wizard::CreateStepSubNode@endlink .
                    If the popup menu is invoked on the background of the Task Navigator the step and
                    subNodeId parameters will be -1.  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback4<void, NXOpen::BlockStyler::Wizard *, NXOpen::BlockStyler::Wizard::TaskNavigatorItem, int, int> OnMenuCallback;
            public: /** The OnMenuSelection callback notifies a client of the menu item selection on the popup menu
                    in the Task Navigator.  The item parameter specifies the popup menu was activated on a step,
                    sub-node or the background. The step parameter for the callback is zero based and
                    represents the steps in the Wizard.  The subNodeId parameter is the unique id returned
                    by @link BlockStyler::Wizard::CreateStepSubNode BlockStyler::Wizard::CreateStepSubNode@endlink .  The menuItemIndex parameter will
                    be the unique id specified when creating menu items for the BlockStyler.TreeListMenu.
                    If the popup menu is invoked on the background of the Task Navigator the step and
                    subNodeId parameters will be -1.  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback5<void, NXOpen::BlockStyler::Wizard *, NXOpen::BlockStyler::Wizard::TaskNavigatorItem, int, int, int> OnMenuSelectionCallback;
            private: WizardImpl * m_wizard_impl;
            private: friend class  _WizardBuilder;
            protected: Wizard();
            public: ~Wizard();
            /** Create a sub-node for a step in the Task Navigator.  @return  Unique id for the sub-node. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int CreateStepSubNode
            (
                int step /** The step to add a sub-node. */,
                const NXString & text /** Text for the sub-node. */,
                const NXString & bitmap /** Optional bitmap for the sub-node. */,
                bool showCheckBox /** Associate an optional check box with the sub-node */,
                bool checkBoxChecked /** The initial state of the check box. */
            );
            /** Create a sub-node for a step in the Task Navigator.  @return  Unique id for the sub-node. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            int CreateStepSubNode
            (
                int step /** The step to add a sub-node. */,
                const char * text /** Text for the sub-node. */,
                const char * bitmap /** Optional bitmap for the sub-node. */,
                bool showCheckBox /** Associate an optional check box with the sub-node */,
                bool checkBoxChecked /** The initial state of the check box. */
            );
            /** Remove a sub-node in the Task Navigator. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void RemoveStepSubNode
            (
                int subNodeId /** The sub-node id. */
            );
            /** Creates a popup menu. Use @link BlockStyler::Wizard::SetMenu BlockStyler::Wizard::SetMenu@endlink  to set
                     the created menu.  See the @link BlockStyler::TreeListMenu BlockStyler::TreeListMenu@endlink  for
                     information on creating a menu.   @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::BlockStyler::TreeListMenu * CreateMenu
            (
            );
            /** Set the menu items for the popup menu for a step, sub-node or the background
                    in the Task Navigator.  See the @link BlockStyler::TreeListMenu BlockStyler::TreeListMenu@endlink  for
                    information on creating a menu.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMenu
            (
                NXOpen::BlockStyler::TreeListMenu * menu /** menu */ 
            );
            /** Sets the StepNotifyPre handler. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetStepNotifyPreHandler
            (
                const NXOpen::BlockStyler::Wizard::StepNotifyPreCallback&  cb /** cb */ 
            );
            /** Sets the StepNotifyPost handler. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetStepNotifyPostHandler
            (
                const NXOpen::BlockStyler::Wizard::StepNotifyPostCallback&  cb /** cb */ 
            );
            /** Sets the IsStepOkay handler. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetIsStepOkayHandler
            (
                const NXOpen::BlockStyler::Wizard::IsStepOkayCallback&  cb /** cb */ 
            );
            /** Sets the OnSubNode handler. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetOnSubNodeHandler
            (
                const NXOpen::BlockStyler::Wizard::OnSubNodeCallback&  cb /** cb */ 
            );
            /** Sets the OnMenu handler. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetOnMenuHandler
            (
                const NXOpen::BlockStyler::Wizard::OnMenuCallback&  cb /** cb */ 
            );
            /** Sets the OnMenuSelection handler. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetOnMenuSelectionHandler
            (
                const NXOpen::BlockStyler::Wizard::OnMenuSelectionCallback&  cb /** cb */ 
            );
            /**Returns  the CurrentStep. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int CurrentStep
            (
            );
            /**Sets  the CurrentStep. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetCurrentStep
            (
                int currentStep /** currentstep */ 
            );
            /**Returns  the HighQualityBitmap. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool HighQualityBitmap
            (
            );
            /**Sets  the HighQualityBitmap. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetHighQualityBitmap
            (
                bool highQuality /** highquality */ 
            );
            /**Returns  the Localize. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool Localize
            (
            );
            /**Sets  the Localize. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetLocalize
            (
                bool localize /** localize */ 
            );
            /**Returns  the Members
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::BlockStyler::PropertyList * Members
            (
            );
            /**Returns  the ShowTaskNavigator. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ShowTaskNavigator
            (
            );
            /**Sets  the ShowTaskNavigator. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetShowTaskNavigator
            (
                bool show /** show */ 
            );
            /** Gets the StepBannerBitmaps. Gets the list of bitmaps for the step bitmaps in the banner area. @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetStepBannerBitmaps
            (
            );
            /** Sets the StepBannerBitmaps. Sets the list of bitmaps for the step bitmaps in the banner area.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetStepBannerBitmaps
            (
                std::vector<NXString> & bitmaps /** bitmaps */ 
            );
            /** Gets the StepBitmaps. Gets the list of bitmaps for the node bitmaps in the Task Navigator. @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetStepBitmaps
            (
            );
            /** Sets the StepBitmaps. Sets the list of bitmaps for the node bitmaps in the Task Navigator.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetStepBitmaps
            (
                std::vector<NXString> & bitmaps /** bitmaps */ 
            );
            /** Gets the StepCues. Gets the list of cue lines for the wizard steps. @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetStepCues
            (
            );
            /** Sets the StepCues. Sets the list of cue lines for the wizard steps.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetStepCues
            (
                std::vector<NXString> & cues /** cues */ 
            );
            /** Gets the StepText. Gets the list of step descriptions for the banner area. @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetStepText
            (
            );
            /** Sets the StepText. Sets the list of step descriptions for the banner area.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetStepText
            (
                std::vector<NXString> & text /** text */ 
            );
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif