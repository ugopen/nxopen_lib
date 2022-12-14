#ifndef NXOpen_DRAFTING_SETTINGSMANAGER_HXX_INCLUDED
#define NXOpen_DRAFTING_SETTINGSMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drafting_SettingsManager.ja
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
#include <NXOpen/Annotations_EditSettingsBuilder.hxx>
#include <NXOpen/Annotations_TableEditSettingsBuilder.hxx>
#include <NXOpen/Annotations_TableRowSortingBuilder.hxx>
#include <NXOpen/Drafting_BaseEditSettingsBuilder.hxx>
#include <NXOpen/Drafting_PreferencesBuilder.hxx>
#include <NXOpen/Drawings_EditSectionLineSettingsBuilder.hxx>
#include <NXOpen/Drawings_EditViewLabelSettingsBuilder.hxx>
#include <NXOpen/Drawings_EditViewSettingsBuilder.hxx>
#include <NXOpen/Layout2d_EditComponentSettingsBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class SettingsManager;
    }
    class Part;
    namespace Annotations
    {
        class EditSettingsBuilder;
    }
    namespace Annotations
    {
        class Table;
    }
    namespace Annotations
    {
        class TableEditSettingsBuilder;
    }
    namespace Annotations
    {
        class TableRowSortingBuilder;
    }
    class DisplayableObject;
    namespace Drafting
    {
        class BaseEditSettingsBuilder;
    }
    namespace Drafting
    {
        class PreferencesBuilder;
    }
    namespace Drawings
    {
        class EditSectionLineSettingsBuilder;
    }
    namespace Drawings
    {
        class EditViewLabelSettingsBuilder;
    }
    namespace Drawings
    {
        class EditViewSettingsBuilder;
    }
    namespace Drawings
    {
        class SectionLine;
    }
    namespace Layout2d
    {
        class Component;
    }
    namespace Layout2d
    {
        class EditComponentSettingsBuilder;
    }
    class View;
    namespace Drafting
    {
        class SettingsManagerImpl;
        /** Represents an object that manages drafting settings.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_DRAFTINGEXPORT  SettingsManager
        {
            private: SettingsManagerImpl * m_settingsmanager_impl;
            private: NXOpen::Part* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit SettingsManager(NXOpen::Part *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~SettingsManager();
            /** Creates a @link NXOpen::Drafting::PreferencesBuilder NXOpen::Drafting::PreferencesBuilder@endlink  
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drafting::PreferencesBuilder * CreatePreferencesBuilder
            (
            );
            /** Creates a @link NXOpen::Annotations::EditSettingsBuilder NXOpen::Annotations::EditSettingsBuilder@endlink 
                         <br> 
                        For multiple object settings, first create primary settings builder by passing all 
                        selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                        object starting from second selected object.
                        Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
                        after creating all settings builder for selected objects.  <br>  
                     @return  The annotations settings builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Annotations::EditSettingsBuilder * CreateAnnotationEditSettingsBuilder
            (
                const std::vector<NXOpen::DisplayableObject *> & objects /** the array of objects for style, NULL not allowed*/
            );
            /** Creates a @link NXOpen::Drawings::EditSectionLineSettingsBuilder NXOpen::Drawings::EditSectionLineSettingsBuilder@endlink 
                         <br> 
                        For multiple object settings, first create primary settings builder by passing all 
                        selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                        object starting from second selected object.
                        Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
                        after creating all settings builder for selected objects.  <br>  
                     @return  The section line settings builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::EditSectionLineSettingsBuilder * CreateDrawingEditSectionLineSettingsBuilder
            (
                const std::vector<NXOpen::Drawings::SectionLine *> & sectionLines /** The array of object for section line style, NULL is allowed. */
            );
            /** Creates a @link NXOpen::Drawings::EditViewSettingsBuilder NXOpen::Drawings::EditViewSettingsBuilder@endlink 
                         <br> 
                        For multiple object settings, first create primary settings builder by passing all 
                        selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                        object starting from second selected object.
                        Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
                        after creating all settings builder for selected objects.  <br> 
                     @return  The view settings builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::EditViewSettingsBuilder * CreateDrawingEditViewSettingsBuilder
            (
                const std::vector<NXOpen::View *> & views /** The array of objects for view style, NULL not allowed. */
            );
            /** Creates a @link NXOpen::Layout2d::EditComponentSettingsBuilder NXOpen::Layout2d::EditComponentSettingsBuilder@endlink  
                        This builder is the interface to edit the 2d component settings of layout
                         <br> 
                        For multiple object settings, first create primary settings builder by passing all 
                        selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                        object starting from second selected object.
                        Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
                        after creating all settings builder for selected objects.  <br> 
                     @return  The layout2d component settings builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_layout ("NX Layout") */
            public: NXOpen::Layout2d::EditComponentSettingsBuilder * CreateLayout2dEditComponentSettingsBuilder
            (
                const std::vector<NXOpen::Layout2d::Component *> & components /** The array of components to edit.  NULL is not allowed */
            );
            /** Creates a @link NXOpen::Drawings::EditViewLabelSettingsBuilder NXOpen::Drawings::EditViewLabelSettingsBuilder@endlink 
                         <br> 
                        For multiple object settings, first create primary settings builder by passing all 
                        selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                        object starting from second selected object.
                        Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
                        after creating all settings builder for selected objects.  <br> 
                     @return  The view label settings builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::EditViewLabelSettingsBuilder * CreateDrawingEditViewLabelSettingsBuilder
            (
                const std::vector<NXOpen::DisplayableObject *> & viewLabels /** the array of view labels to edit, NULL is not allowed. */
            );
            /** Creates a @link NXOpen::Annotations::TableEditSettingsBuilder NXOpen::Annotations::TableEditSettingsBuilder@endlink 
                         <br> 
                        For multiple object settings, first create primary settings builder by passing all 
                        selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                        object starting from second selected object.
                        Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
                        after creating all settings builder for selected objects.  <br> 
                     @return  The table settings builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Annotations::TableEditSettingsBuilder * CreateTableEditSettingsBuilder
            (
                const std::vector<NXOpen::DisplayableObject *> & objects /** the array of objects for style, If NULL, section or cell preferences for all sections or cells will be set. */
            );
            /** Process edit settings builders for mutiple objects
                    
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  instead. <br>  

             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use Drafting::SettingsManager::ProcessForMultipleObjectsSettings instead.") void ProcessForMutipleObjectsSettings
            (
                const std::vector<NXOpen::Drafting::BaseEditSettingsBuilder *> & editSettingsBuilders /** editsettingsbuilders */ 
            );
            /** Process edit settings builders for multiple objects
                        User must call this API for multiple object settings and pass all edit settings builders for selected objects
                    
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void ProcessForMultipleObjectsSettings
            (
                const std::vector<NXOpen::Drafting::BaseEditSettingsBuilder *> & editSettingsBuilders /** editsettingsbuilders */ 
            );
            /** Creates a @link Annotations::TableRowSortingBuilder Annotations::TableRowSortingBuilder@endlink   @return  The table sorting builder 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TableRowSortingBuilder * CreateTableRowSortingBuilder
            (
                const std::vector<NXOpen::DisplayableObject *> & objects /** the array of table row objects */
            );
            /** Creates a @link Annotations::TableRowSortingBuilder Annotations::TableRowSortingBuilder@endlink  from Table @return  The table sorting builder 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TableRowSortingBuilder * CreateTableRowSortingBuilder
            (
                NXOpen::Annotations::Table * tableObject /** the table object */
            );
        }; //lint !e1712 default constructor not defined for class  

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
