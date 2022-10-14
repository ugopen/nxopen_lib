#ifndef NXOpen_ROUTING_COMPONENTNAMEPLUGINDATA_HXX_INCLUDED
#define NXOpen_ROUTING_COMPONENTNAMEPLUGINDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_ComponentNamePluginData.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        class ComponentNamePluginData;
    }
    class NXObject;
    namespace Routing
    {
        class _ComponentNamePluginDataBuilder;
        class ComponentNamePluginDataImpl;
        /** Data object created by Routing just before creating stock or cut elbow components.
                Routing expects the plugin you write to fill in the required information for the
                component name.

                For more information, see @link Routing::CustomManager Routing::CustomManager@endlink  and the
                @link Routing::CustomManager::SetStockComponentNamePlugin Routing::CustomManager::SetStockComponentNamePlugin@endlink  or
                @link Routing::CustomManager::SetCutElbowComponentNamePlugin Routing::CustomManager::SetCutElbowComponentNamePlugin@endlink .
             <br> An instance of this object will be sent to the Component Name plugin.  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  ComponentNamePluginData : public NXOpen::TaggedObject
        {
            private: ComponentNamePluginDataImpl * m_componentnameplugindata_impl;
            private: friend class  _ComponentNamePluginDataBuilder;
            protected: ComponentNamePluginData();
            public: ~ComponentNamePluginData();
            /**Returns  the stock or the elbow's template part for which Routing needs to create a new component. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::NXObject * TemplateObject
            (
            );
            /**Returns  the flag that tells Routing to use the information in this data object to
                        rename the stock's or cut elbow's part. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool RenameComponentPartFlag
            (
            );
            /**Sets  the flag that tells Routing to use the information in this data object to
                        rename the stock's or cut elbow's part. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetRenameComponentPartFlag
            (
                bool shouldRenamePart /** Should Routing rename the part using the information provided by your plugin? */
            );
            /**Returns  the name Routing will use for the component in the NX assembly. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString ComponentName
            (
            );
            /**Sets  the name Routing will use for the component in the NX assembly. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetComponentName
            (
                const NXString & componentName /** The component name. */
            );
            /**Sets  the name Routing will use for the component in the NX assembly. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetComponentName
            (
                const char * componentName /** The component name. */
            );
            /**Returns  the path under which to place the component part when in native mode.
                        An empty string means use the current directory.
                        This may be a relative path from the current directory or an absolute path.
                    
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString NativePath
            (
            );
            /**Sets  the path under which to place the component part when in native mode.
                        An empty string means use the current directory.
                        This may be a relative path from the current directory or an absolute path.
                    
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetNativePath
            (
                const NXString & nativePath /** The path under which to create the component part. */
            );
            /**Sets  the path under which to place the component part when in native mode.
                        An empty string means use the current directory.
                        This may be a relative path from the current directory or an absolute path.
                    
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetNativePath
            (
                const char * nativePath /** The path under which to create the component part. */
            );
            /**Returns  the customer's plugin gives us the name for the component part when in native mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString NativeFileName
            (
            );
            /**Sets  the customer's plugin gives us the name for the component part when in native mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetNativeFileName
            (
                const NXString & fileName /** The file name for the component part . */
            );
            /**Sets  the customer's plugin gives us the name for the component part when in native mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetNativeFileName
            (
                const char * fileName /** The file name for the component part . */
            );
            /**Returns  the folder in which to show the component part in managed mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString ManagedModeFolderName
            (
            );
            /**Sets  the folder in which to show the component part in managed mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetManagedModeFolderName
            (
                const NXString & folderName /** The folder in which to show the component part. */
            );
            /**Sets  the folder in which to show the component part in managed mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetManagedModeFolderName
            (
                const char * folderName /** The folder in which to show the component part. */
            );
            /**Returns  the item name for the component part when in managed mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString ManagedModeItemName
            (
            );
            /**Sets  the item name for the component part when in managed mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetManagedModeItemName
            (
                const NXString & itemName /** The item name for the component part. */
            );
            /**Sets  the item name for the component part when in managed mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetManagedModeItemName
            (
                const char * itemName /** The item name for the component part. */
            );
            /**Returns  the item revision for the component part when in managed mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString ManagedModeItemRevision
            (
            );
            /**Sets  the item revision for the component part when in managed mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetManagedModeItemRevision
            (
                const NXString & itemRevision /** The item revision for the component part. */
            );
            /**Sets  the item revision for the component part when in managed mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetManagedModeItemRevision
            (
                const char * itemRevision /** The item revision for the component part. */
            );
            /**Returns  the item type for the component part when in managed mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString ManagedModeItemType
            (
            );
            /**Sets  the item type for the component part when in managed mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetManagedModeItemType
            (
                const NXString & itemType /** The item type for the component part. */
            );
            /**Sets  the item type for the component part when in managed mode. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetManagedModeItemType
            (
                const char * itemType /** The item type for the component part. */
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