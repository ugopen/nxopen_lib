#ifndef NXOpen_DRAFTING_DRAWINGCREATIONWIZARDBUILDER_HXX_INCLUDED
#define NXOpen_DRAFTING_DRAWINGCREATIONWIZARDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drafting_DrawingCreationWizardBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Drafting_DrawingCreationWizardBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_drafting_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drafting
    {
        class DrawingCreationWizardBuilder;
    }
    namespace Assemblies
    {
        class SelectComponentList;
    }
    class Builder;
    namespace Drafting
    {
        class AttributeItemBuilderList;
    }
    namespace Drafting
    {
        class PrimaryContentItemBuilderList;
    }
    class SelectNXObjectList;
    namespace Drafting
    {
        class _DrawingCreationWizardBuilderBuilder;
        class DrawingCreationWizardBuilderImpl;
        /**
            Represents a @link Drafting::DrawingCreationWizardBuilder Drafting::DrawingCreationWizardBuilder@endlink .  This class is
            used to create Booklets (i.e. a set of fully populated drawings).  The builder operates
            in both create and edit modes as well as in native and managed (Teamcenter) modes.  The
            following information is important when using this builder in edit mode:<br/>
            <ul>
                <li>
                Native Mode
                    <ul>
                        <li>
                        The @link Drafting::DrawingCreationWizardBuilder::SetFolder Drafting::DrawingCreationWizardBuilder::SetFolder@endlink  must be the first thing set after creating the builder.
                        Setting this will populate the builder with the booklet's information.
                        </li>
                    </ul>
                </li>
                <li>
                Managed Mode
                    <ul>
                        <li>
                        The @link Drafting::DrawingCreationWizardBuilder::SetNumber Drafting::DrawingCreationWizardBuilder::SetNumber@endlink  and @link Drafting::DrawingCreationWizardBuilder::SetRevision Drafting::DrawingCreationWizardBuilder::SetRevision@endlink  must be the first things set after
                        creating the builder (in that order).  The setting of the @link Drafting::DrawingCreationWizardBuilder::SetRevision Drafting::DrawingCreationWizardBuilder::SetRevision@endlink  will populate the builder with the booklet's information.
                        </li>
                    </ul>
                </li>
            </ul>
             <br> To create a new instance of this class, use @link Drafting::AutomationManager::CreateDrawingCreationWizardBuilderFromRule  Drafting::AutomationManager::CreateDrawingCreationWizardBuilderFromRule @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ApplyTemplateToAll </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_DRAFTINGEXPORT  DrawingCreationWizardBuilder : public Builder
        {
            private: DrawingCreationWizardBuilderImpl * m_drawingcreationwizardbuilder_impl;
            private: friend class  _DrawingCreationWizardBuilderBuilder;
            protected: DrawingCreationWizardBuilder();
            public: ~DrawingCreationWizardBuilder();
            /**Returns  the discipline. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Discipline
            (
            );
            /**Sets  the discipline. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetDiscipline
            (
                const NXString & discipline /** discipline */ 
            );
            /**Sets  the discipline. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            void SetDiscipline
            (
                const char * discipline /** discipline */ 
            );
            /**Returns  the drawing style. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DrawingStyle
            (
            );
            /**Sets  the drawing style. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetDrawingStyle
            (
                const NXString & drawingStyle /** drawingstyle */ 
            );
            /**Sets  the drawing style. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            void SetDrawingStyle
            (
                const char * drawingStyle /** drawingstyle */ 
            );
            /**Returns  the detail id. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DetailID
            (
            );
            /**Sets  the detail id. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetDetailID
            (
                const NXString & detailID /** detailid */ 
            );
            /**Sets  the detail id. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            void SetDetailID
            (
                const char * detailID /** detailid */ 
            );
            /**Returns  the name. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the number. This property is only used in managed mode and must be set before anything else.  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Number
            (
            );
            /**Sets  the number. This property is only used in managed mode and must be set before anything else.  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetNumber
            (
                const NXString & number /** number */ 
            );
            /**Sets  the number. This property is only used in managed mode and must be set before anything else.  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            void SetNumber
            (
                const char * number /** number */ 
            );
            /**Returns  the revision. This is only used in managed mode. In edit mode it must be set after the @link Drafting::DrawingCreationWizardBuilder::SetNumber Drafting::DrawingCreationWizardBuilder::SetNumber@endlink  and at the time
                        is set it will populate the builder with the booklet's information. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Revision
            (
            );
            /**Sets  the revision. This is only used in managed mode. In edit mode it must be set after the @link Drafting::DrawingCreationWizardBuilder::SetNumber Drafting::DrawingCreationWizardBuilder::SetNumber@endlink  and at the time
                        is set it will populate the builder with the booklet's information. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetRevision
            (
                const NXString & revision /** revision */ 
            );
            /**Sets  the revision. This is only used in managed mode. In edit mode it must be set after the @link Drafting::DrawingCreationWizardBuilder::SetNumber Drafting::DrawingCreationWizardBuilder::SetNumber@endlink  and at the time
                        is set it will populate the builder with the booklet's information. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            void SetRevision
            (
                const char * revision /** revision */ 
            );
            /**Returns  the folder. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Folder
            (
            );
            /**Sets  the folder. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetFolder
            (
                const NXString & foldername /** foldername */ 
            );
            /**Sets  the folder. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            void SetFolder
            (
                const char * foldername /** foldername */ 
            );
            /**Returns  the introductory template. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString IntroductoryTemplate
            (
            );
            /**Sets  the introductory template. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetIntroductoryTemplate
            (
                const NXString & introductoryTemplate /** introductorytemplate */ 
            );
            /**Sets  the introductory template. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            void SetIntroductoryTemplate
            (
                const char * introductoryTemplate /** introductorytemplate */ 
            );
            /**Returns  the primary content. Setting a component into @link Drafting::PrimaryContentItemBuilder::Content Drafting::PrimaryContentItemBuilder::Content@endlink  of an item in
                        @link Drafting::DrawingCreationWizardBuilder::PrimaryContent Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  will cause that component to be removed from 
                        @link Drafting::DrawingCreationWizardBuilder::SecondaryContent Drafting::DrawingCreationWizardBuilder::SecondaryContent@endlink  and 
                        @link Drafting::DrawingCreationWizardBuilder::ExcludedContent Drafting::DrawingCreationWizardBuilder::ExcludedContent@endlink  if they contain that component. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drafting::PrimaryContentItemBuilderList * PrimaryContent
            (
            );
            /**Returns  the flag which controls the behavior of setting @link Drafting::PrimaryContentItemBuilder::GeometryTemplate Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink 
                        on an item in @link Drafting::DrawingCreationWizardBuilder::PrimaryContent Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink . When set to true the builder
                        will respond to the setting of @link Drafting::PrimaryContentItemBuilder::GeometryTemplate Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink  on an item in
                        @link Drafting::DrawingCreationWizardBuilder::PrimaryContent Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  by setting the same value on
                        @link Drafting::PrimaryContentItemBuilder::GeometryTemplate Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink  on all of the other items in
                        @link Drafting::DrawingCreationWizardBuilder::PrimaryContent Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool ApplyTemplateToAll
            (
            );
            /**Sets  the flag which controls the behavior of setting @link Drafting::PrimaryContentItemBuilder::GeometryTemplate Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink 
                        on an item in @link Drafting::DrawingCreationWizardBuilder::PrimaryContent Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink . When set to true the builder
                        will respond to the setting of @link Drafting::PrimaryContentItemBuilder::GeometryTemplate Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink  on an item in
                        @link Drafting::DrawingCreationWizardBuilder::PrimaryContent Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  by setting the same value on
                        @link Drafting::PrimaryContentItemBuilder::GeometryTemplate Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink  on all of the other items in
                        @link Drafting::DrawingCreationWizardBuilder::PrimaryContent Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetApplyTemplateToAll
            (
                bool applyTemplateToAll /** applytemplatetoall */ 
            );
            /**Returns  the secondary content. Setting a component into @link Drafting::DrawingCreationWizardBuilder::SecondaryContent Drafting::DrawingCreationWizardBuilder::SecondaryContent@endlink  
                        will cause that component to be removed from @link Drafting::PrimaryContentItemBuilder::Content Drafting::PrimaryContentItemBuilder::Content@endlink 
                        of each item in @link Drafting::DrawingCreationWizardBuilder::PrimaryContent Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  and 
                        @link Drafting::DrawingCreationWizardBuilder::ExcludedContent Drafting::DrawingCreationWizardBuilder::ExcludedContent@endlink  if they contain that component. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponentList * SecondaryContent
            (
            );
            /**Returns  the excluded content. Setting a component into @link Drafting::DrawingCreationWizardBuilder::ExcludedContent Drafting::DrawingCreationWizardBuilder::ExcludedContent@endlink  
                        will cause that component to be removed from @link Drafting::PrimaryContentItemBuilder::Content Drafting::PrimaryContentItemBuilder::Content@endlink 
                        of each item in @link Drafting::DrawingCreationWizardBuilder::PrimaryContent Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  and 
                        @link Drafting::DrawingCreationWizardBuilder::SecondaryContent Drafting::DrawingCreationWizardBuilder::SecondaryContent@endlink  if they contain that component. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponentList * ExcludedContent
            (
            );
            /**Returns  the references. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * References
            (
            );
            /**Returns  the attributes. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drafting::AttributeItemBuilderList * Attributes
            (
            );
            /** Returns the summary.  This is in HTML format.  @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetSummary
            (
            );
            /** Sets the summary 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetSummary
            (
                const std::vector<NXString> & summary /** summary */ 
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
