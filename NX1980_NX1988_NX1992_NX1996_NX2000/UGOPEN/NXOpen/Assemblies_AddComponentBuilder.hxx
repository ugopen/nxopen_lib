#ifndef NXOpen_ASSEMBLIES_ADDCOMPONENTBUILDER_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_ADDCOMPONENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_AddComponentBuilder.ja
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
#include <NXOpen/ErrorList.hxx>
#include <NXOpen/FileNew.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/IAttributeSourceObjectBuilder.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_assemblies_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Assemblies
    {
        class AddComponentBuilder;
    }
    namespace Assemblies
    {
        namespace ProductInterface
        {
            class InterfaceObject;
        }
    }
    class BasePart;
    class Builder;
    class ConfiguredPart;
    class CoordinateSystem;
    class ErrorList;
    class FileNew;
    class IAttributeSourceObjectBuilder;
    class NXObject;
    namespace PDM
    {
        class LogicalObject;
    }
    class Point;
    namespace Assemblies
    {
        class _AddComponentBuilderBuilder;
        class AddComponentBuilderImpl;
        /**
            Represents a builder class that performs add existing component operation in current context.
            Context can be Assembly or 4GD.   
             <br> To create a new instance of this class, use @link NXOpen::Assemblies::AssemblyManager::CreateAddComponentBuilder  NXOpen::Assemblies::AssemblyManager::CreateAddComponentBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  AddComponentBuilder : public NXOpen::Builder, public virtual NXOpen::IAttributeSourceObjectBuilder
        {
            /** Represents initial location type that can be present during add component */
            public: enum LocationType
            {
                LocationTypeSnap/** Snap as initial location type */,
                LocationTypeWorkPartAbsolute/** Absolute of work part as initial location type */,
                LocationTypeDisplayedPartAbsolute/** Absolute of displayed part as initial location type */,
                LocationTypeDisplayedPartWCS/** WCS as initial location type */
            };

            /** Represents CAM component type that can be present during add component in manufacturing mode */
            public: enum CamComponentType
            {
                CamComponentTypeTarget/** Target type */,
                CamComponentTypeResource/** Resource type */,
                CamComponentTypeWorkpiece/** Workpiece type */
            };

            private: AddComponentBuilderImpl * m_addcomponentbuilder_impl;
            private: friend class  _AddComponentBuilderBuilder;
            protected: AddComponentBuilder();
            public: ~AddComponentBuilder();
            /**Returns  the type of a add component
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DesignElementType
            (
            );
            /**Sets  the type of a add component
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void SetDesignElementType
            (
                const NXString & deType /** detype */ 
            );
            /**Sets  the type of a add component
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            void SetDesignElementType
            (
                const char * deType /** detype */ 
            );
            /**Returns  the component name for added components.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ComponentName
            (
            );
            /**Sets  the component name for added components.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetComponentName
            (
                const NXString & componentName /** componentname */ 
            );
            /**Sets  the component name for added components.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            void SetComponentName
            (
                const char * componentName /** componentname */ 
            );
            /**Returns  the reference set for added components.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ReferenceSet
            (
            );
            /**Sets  the reference set for added components.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetReferenceSet
            (
                const NXString & referenceSet /** referenceset */ 
            );
            /**Sets  the reference set for added components.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            void SetReferenceSet
            (
                const char * referenceSet /** referenceset */ 
            );
            /**Returns  the layer for added components.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int Layer
            (
            );
            /**Sets  the layer for added components.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetLayer
            (
                int layer /** layer */ 
            );
            /** Returns the parts to be used for adding components
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void GetPartsToAdd
            (
                std::vector<NXOpen::BasePart *> & partsToUse /** partstouse */ 
            );
            /** Sets the parts to be used for adding components
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetPartsToAdd
            (
                const std::vector<NXOpen::BasePart *> & partsToUse /** partstouse */ 
            );
            /** Removes the specified parts from the selected parts list
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void RemovePartsFromSelection
            (
                const std::vector<NXOpen::BasePart *> & partsToRemove /** partstoremove */ 
            );

            /// \cond NX_NO_DOC 
            /** Returns the configured parts to be used for adding components
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetConfiguredPartsToAdd
            (
                std::vector<NXOpen::ConfiguredPart *> & configuredPartsToUse /** configuredpartstouse */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Sets the configured parts to be used for adding components
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetConfiguredPartsToAdd
            (
                const std::vector<NXOpen::ConfiguredPart *> & configuredParts /** configuredparts */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Removes the specified configured parts from the selected parts list
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void RemoveConfiguredPartsFromSelection
            (
                const std::vector<NXOpen::ConfiguredPart *> & configuredPartsToRemove /** configuredpartstoremove */ 
            );

            /// \endcond 
            /** Removes the components added through add component
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void RemoveAddedComponents
            (
            );
            /**Returns  the file new descriptor to identify an added component in 4GD 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::FileNew * FileNewDescriptor
            (
            );
            /** Gets the number of components to be added.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int GetCount
            (
            );
            /** Sets the number of components to be added.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetCount
            (
                int count /** count */ 
            );
            /** Get the initial location type during add component.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::AddComponentBuilder::LocationType GetInitialLocationType
            (
            );
            /** Set the initial location type during add component.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetInitialLocationType
            (
                NXOpen::Assemblies::AddComponentBuilder::LocationType locationType /** locationtype */ 
            );
            /** Returns the location and orientation used for adding component
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void GetInitialLocationAndOrientation
            (
                NXOpen::Point ** initialLocation /** initiallocation */ ,
                NXOpen::CoordinateSystem ** initialOrientation /** initialorientation */ 
            );
            /** Sets the location and orientation to be used for adding component. Orientation is optional and user can pass NULL.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetInitialLocationAndOrientation
            (
                NXOpen::Point * initialLocation /** initiallocation */ ,
                NXOpen::CoordinateSystem * initialOrientation /** initialorientation */ 
            );
            /** Sets the location and orientation to be used for add component. Orientation is optional and user can pass NULL.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetInitialLocationAndOrientation
            (
                const NXOpen::Point3d & point /** point */ ,
                const NXOpen::Matrix3x3 & orientation /** orientation */ 
            );
            /** Gets the scatter option for added components.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetScatterOption
            (
            );
            /** Sets the scatter option for added components.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetScatterOption
            (
                bool scatterOption /** scatteroption */ 
            );
            /** Gets allow multiple assembly location option for adding components.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: bool AllowMultipleAssemblyLocations
            (
            );
            /** Sets allow multiple assembly location option for adding components.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetAllowMultipleAssemblyLocations
            (
                bool allow /** allow */ 
            );
            /** Gets the keep constraints option for added components.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetKeepConstraintsOption
            (
            );
            /** Sets the keep constraints option for added components.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetKeepConstraintsOption
            (
                bool keepConstraintsOption /** keepconstraintsoption */ 
            );
            /** Returns the component anchor used for adding component
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::ProductInterface::InterfaceObject * GetComponentAnchor
            (
            );
            /** Sets the component anchor to be used for adding component
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetComponentAnchor
            (
                NXOpen::Assemblies::ProductInterface::InterfaceObject * componentAnchor /** componentanchor */ 
            );
            /** Returns all product interface objects available, one of these can be used as component anchor
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void GetAllProductInterfaceObjects
            (
                std::vector<NXOpen::Assemblies::ProductInterface::InterfaceObject *> & productInterfaceObjects /** productinterfaceobjects */ 
            );
            /** Returns the pre-creation objects 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void GetLogicalObjects
            (
                std::vector<NXOpen::PDM::LogicalObject *> & logicalObjects /** logicalobjects */ 
            );
            /** Returns the pre-creation objects which have unassign required attributes
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void GetLogicalObjectsHavingUnassignedRequiredAttributes
            (
                std::vector<NXOpen::PDM::LogicalObject *> & logicalObjects /** logicalobjects */ 
            );
            /** Returns add component operation failures 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ErrorList * GetOperationFailures
            (
            );
            /** Resets the component to snapped position and orientation 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void ResetToSnapped
            (
            );
            /** Orient added components to the WCS 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void OrientToWCS
            (
            );
            /** Reverse the Z direction of added components 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void ReverseZDirection
            (
            );
            /** Rotate added components along Z direction by 90 degrees 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void RotateAlongZDirection
            (
            );
            /** Sets the option to synchronize display properties with the component to be added 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetSynchDisplayProperties
            (
                bool synchDisplayProperties /** synchdisplayproperties */ 
            );
            /** Get the CAM component type during add component.
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::AddComponentBuilder::CamComponentType GetCamComponentType
            (
            );
            /** Set the CAM component type during add component.
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetCamComponentType
            (
                NXOpen::Assemblies::AddComponentBuilder::CamComponentType camCompType /** camcomptype */ 
            );
            /** Sets the allocate pending instance at time of instance creation for manage pending component.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetPendingInstance
            (
                NXOpen::NXObject * pendingInstance /** pendinginstance */ 
            );
            /**  Auto assigns the attributes for a given array of objects and returns an array of objects that failed to auto assign.
               
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: virtual NXOpen::ErrorList * AutoAssignAttributes
            (
                const std::vector<NXOpen::NXObject *> & objects /** objects */ 
            );
            /**  Auto assigns the attributes for a given object and returns an array of objects that failed to auto assign.
                    properties needs to be created using @link CreateAttributeTitleToNamingPatternMap CreateAttributeTitleToNamingPatternMap@endlink 
               
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXOpen::ErrorList * AutoAssignAttributesWithNamingPattern
            (
                const std::vector<NXOpen::NXObject *> & objects /** objects */ ,
                const std::vector<NXOpen::NXObject *> & properties /** properties */ 
            );
            /** Creates a map object of attribute titles to their corresponding naming pattern 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXOpen::NXObject * CreateAttributeTitleToNamingPatternMap
            (
                std::vector<NXString> & attributeTitles /** attributetitles */ ,
                std::vector<NXString> & titlePatterns /** titlepatterns */ 
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
