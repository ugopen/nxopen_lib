#ifndef NXOpen_ASSEMBLIES_SUBSET_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_SUBSET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_Subset.ja
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
#include <NXOpen/Assemblies_PositioningTask.hxx>
#include <NXOpen/Assemblies_Subset.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/PDM_DesignElementRevision.hxx>
#include <NXOpen/PDM_DesignSubordinateRevision.hxx>
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
        class Subset;
    }
    namespace Assemblies
    {
        class Component;
    }
    namespace Assemblies
    {
        class PositioningTask;
    }
    class NXObject;
    namespace PDM
    {
        class DesignElementRevision;
    }
    namespace PDM
    {
        class DesignSubordinateRevision;
    }
    namespace Assemblies
    {
        class _SubsetBuilder;
        class SubsetImpl;
        /**
                A subset is a set of design elements within a collaborative design.
             <br> To create or edit an instance of this class, use @link NXOpen::Assemblies::SubsetBuilder  NXOpen::Assemblies::SubsetBuilder @endlink  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  Subset : public NXOpen::NXObject
        {
            /** Represents the type of partition view style to show for a subset.
                    */
            public: enum PartitionViewStyleType
            {
                PartitionViewStyleTypeNone/** Show no partition view style for subset */,
                PartitionViewStyleTypeFlat/** Show flat partition view style for subset */,
                PartitionViewStyleTypeHierarchical/** Show hierachical view style for subset */
            };

            private: SubsetImpl * m_subset_impl;
            private: friend class  _SubsetBuilder;
            protected: Subset();
            public: ~Subset();
            /**Returns  the description of this subset.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: NXString Description
            (
            );
            /** Replay this subset.  This will perform a search using the current subset recipe 
                        and configuration.  The contents of the subset will be changed accordingly.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void ReplayRecipe
            (
            );
            /**Returns  the @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink  that corresponds to this subset in 
                        the workset @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink .
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: NXOpen::Assemblies::Component * ComponentInWorkset
            (
            );
            /** Removes the design elements from this subset. This will not delete the design element from the
                        owning @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void RemoveDesignElements
            (
                const std::vector<NXOpen::NXObject *> & designElements /** designelements */ 
            );
            /** Deletes the design elements from the owning @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void DeleteFromCollaborativeDesign
            (
                const std::vector<NXOpen::NXObject *> & designElement /** designelement */ 
            );
            /** Add sources of interpart relationships (wave links in the subset and Connected To relationships for design features)
                        that are not in the specified subset to the subset recipe. 
                        The recipe will be modified and explicit include terms will be added for each parent.
                        The modified recipe will be replayed at the end of the operation. 
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void AddInterpartParents
            (
            );
            /** Add Elements to a subset that reference the existing Design Elements in it by a Connection relation.
                        A typical example will be to add Weld Design Features that reference any of the Design Elements in this subset.
                        The recipe will be modified and explicit include terms will be added for each Element.
                        The modified recipe will be replayed at the end of the operation. 
                        See @link JA_SUBSET_AddInterpartParents JA_SUBSET_AddInterpartParents@endlink " 
                    
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void AddConnectedByElements
            (
            );
            /** Adds all the child components of the selected Reuse Design Element to the owning subset.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void AddAllChildrenToSubset
            (
                const std::vector<NXOpen::Assemblies::Component *> & reuseDesignElements /** reusedesignelements */ 
            );
            /**  If the Reuse Design Elements in the subset contain any new components which were not added
                         to the subset because its owning workset was not the displayed part at the time of creation,
                         then add those new components to the subset now. 
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void AddNewChildrenToSubset
            (
            );
            /** The @link NXOpen::PDM::DesignElementRevision NXOpen::PDM::DesignElementRevision@endlink s that are members of this subset.
                        Note that this does not include elements that have been loaded only because they contain
                        a @link NXOpen::PDM::DesignSubordinateRevision NXOpen::PDM::DesignSubordinateRevision@endlink  that belongs to this subset.
                        See @link GetDesignElementRevisionParents GetDesignElementRevisionParents@endlink 
                     @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: std::vector<NXOpen::PDM::DesignElementRevision *> GetDesignElementRevisionMembers
            (
            );
            /** The @link NXOpen::PDM::DesignElementRevision NXOpen::PDM::DesignElementRevision@endlink s that have been loaded because they contain
                        a @link NXOpen::PDM::DesignSubordinateRevision NXOpen::PDM::DesignSubordinateRevision@endlink  that belongs to this subset.
                     @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: std::vector<NXOpen::PDM::DesignElementRevision *> GetDesignElementRevisionParents
            (
            );
            /** The @link NXOpen::PDM::DesignSubordinateRevision NXOpen::PDM::DesignSubordinateRevision@endlink s that are members of this subset.
                        Note that this does not include elements that have been loaded only because they contain
                        a @link NXOpen::PDM::DesignSubordinateRevision NXOpen::PDM::DesignSubordinateRevision@endlink  that belongs to this subset.
                        See @link GetDesignSubordinateRevisionParents GetDesignSubordinateRevisionParents@endlink 
                     @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: std::vector<NXOpen::PDM::DesignSubordinateRevision *> GetDesignSubordinateRevisionMembers
            (
            );
            /** The @link NXOpen::PDM::DesignSubordinateRevision NXOpen::PDM::DesignSubordinateRevision@endlink s that have been loaded because they contain
                        a @link NXOpen::PDM::DesignSubordinateRevision NXOpen::PDM::DesignSubordinateRevision@endlink  that belongs to this subset.
                     @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: std::vector<NXOpen::PDM::DesignSubordinateRevision *> GetDesignSubordinateRevisionParents
            (
            );
            /** Displays the preview for the Collaborative Design in the graphics window.
                        The preview is stored as a JT dataset on the Collaborative Design. 
                        Any transformation specific to this subset will also be applied to the preview. 
                        isPreviewAvailable will be false if no JT dataset could be found. 
                        See @link HideCollaborativeDesignPreview HideCollaborativeDesignPreview@endlink . 
                     @return  
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: bool ShowCollaborativeDesignPreview
            (
            );
            /** Hides the preview for the Collaborative Design in the graphics window if it was 
                        already displayed. 
                        See @link ShowCollaborativeDesignPreview ShowCollaborativeDesignPreview@endlink . 
                    
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void HideCollaborativeDesignPreview
            (
            );
            /** Is the preview for the Collaborative Design being displayed in the Graphics window.
                     @return  
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: bool IsCollaborativeDesignPreviewDisplayed
            (
            );
            /**Returns  the design elements excluded from spatial search to be displayed or not
                    
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: bool DisplayExcludedDesignElements
            (
            );
            /**Sets  the design elements excluded from spatial search to be displayed or not
                    
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void SetDisplayExcludedDesignElements
            (
                bool displayExcluded /** displayexcluded */ 
            );
            /**Returns  
                        the partition view style to show.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: NXOpen::Assemblies::Subset::PartitionViewStyleType PartitionViewStyle
            (
            );
            /**Sets  
                        the partition view style to show.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void SetPartitionViewStyle
            (
                NXOpen::Assemblies::Subset::PartitionViewStyleType partitionViewStyle /** partitionviewstyle */ 
            );
            /**Returns  
                        the subset structure to be shown or not.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: bool ShowSubsetStructure
            (
            );
            /**Sets  
                        the subset structure to be shown or not.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void SetShowSubsetStructure
            (
                bool showSubsetStructure /** showsubsetstructure */ 
            );
            /** Gets all @link NXOpen::Assemblies::PositioningTask NXOpen::Assemblies::PositioningTask@endlink  
                        that belong to this subset.
                     @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Assemblies::PositioningTask *> GetAllPositioningTasks
            (
            );
            /** Deletes the @link NXOpen::Assemblies::PositioningTask NXOpen::Assemblies::PositioningTask@endlink  from this subset.
                    
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void DeletePositioningTask
            (
                NXOpen::Assemblies::PositioningTask * positioningTask /** positioningtask */ 
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
