#ifndef NXOpen_LOADOPTIONS_HXX_INCLUDED
#define NXOpen_LOADOPTIONS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LoadOptions.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class LoadOptions;
    class PartCollection;
    class LoadOptionsImpl;
    /** Contains accessor methods for all the part load options.  <br> To obtain an instance of this class, refer to @link PartCollection PartCollection@endlink  <br> */
    class NXOPENCPPEXPORT  LoadOptions
    {
        /** Options for specifying how to load component parts */
        public: enum LoadMethod
        {
            LoadMethodAsSaved/** use same directory in which they were saved */,
            LoadMethodFromDirectory/** use same directory as the parent assembly */,
            LoadMethodSearchDirectories/** use a list of search directories  */
        };

        /** Options for specifying what component parts to load during part open */
        public: enum LoadComponents
        {
            LoadComponentsAll/** load all components */,
            LoadComponentsNone/** load none of the components */,
            LoadComponentsLastSet/** use same set of components as when the assembly was last saved */,
            LoadComponentsLastFilter/** use same filter used to last load the assembly */,
            LoadComponentsSpecifyFilter/** display list of pre-defined component groups to select from */
        };

        /** Options to allow you to specify how unloaded parents should be loaded
            when interpart data loading is turned on */
        public: enum Parent
        {
            ParentPartial/** Do not load any unloaded parents,
                                                            but fully load partially loaded parts with parent geometry. */,
            ParentImmediate/** Fully load parts that satisfy one level of parent
                                                              references as well as any partially loaded parts
                                                              with parent geometry. */,
            ParentAll/** Recursively fully load all parts with parent geometry linked
                                                       to geometry in the parts selected for loading */
        };

        /** The options to specify what components to load and visualize when matched by the bookmark restore */
        public: enum BookmarkComponents
        {
            BookmarkComponentsNoChange/** Don't change what gets loaded and visualized, (not exposed in UI) */,
            BookmarkComponentsLoadVisible/** Load and show only what was shown on the bookmark's save.
                                                                          Don't load invisible components. */,
            BookmarkComponentsLoadLoaded/** Load and show only what was loaded on the bookmark's save
                                                                          Load invisible components and keep them invisible. */,
            BookmarkComponentsLoadLoadedAndNonDisplayed/** Load and show only what was loaded on the bookmark's save, including non-display parts.
                                                                          Load invisible components and keep them invisible. All non-display parts are invisible. */
        };

        /** the options that specify if reference set data from the bookmark should be restored
                and load should be optimized by loading topology from the selected reference sets only */
        public: enum BookmarkRefsets
        {
            BookmarkRefsetsImportData/** Import refset data */,
            BookmarkRefsetsImportAndOptimizeLoad/** Import refset data and use it to optimize load */,
            BookmarkRefsetsDontImport/** Do nothing with the bookmark refset data */
        };

        private: LoadOptionsImpl * m_loadoptions_impl;
        private: NXOpen::PartCollection* m_owner;
        /** Constructor */
        public: explicit LoadOptions(NXOpen::PartCollection *owner);
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~LoadOptions();
        /**Sets  the option indicating what method to use to determine where to
            find component parts to load  <br> License requirements : None */
        public: void SetComponentLoadMethod
        (
            NXOpen::LoadOptions::LoadMethod option /** option */ 
        );
        /**Returns  the option indicating what method to use to determine where to
            find component parts to load  <br> License requirements : None */
        public: NXOpen::LoadOptions::LoadMethod ComponentLoadMethod
        (
        );
        /**Sets  the option indicating what component parts to load during part open.
           
            Note that this property cannot be set to
            @link LoadOptions::LoadComponentsLastFilter LoadOptions::LoadComponentsLastFilter@endlink  or
            @link LoadOptions::LoadComponentsSpecifyFilter LoadOptions::LoadComponentsSpecifyFilter@endlink  without an
            adv_assemblies license. A license exception will be thrown if an attempt is
            made to set this property to one of these two values without this license.  <br> License requirements : None */
        public: void SetComponentsToLoad
        (
            NXOpen::LoadOptions::LoadComponents option /** option */ 
        );
        /**Returns  the option indicating what component parts to load during part open.
           
            Note that this property cannot be set to
            @link LoadOptions::LoadComponentsLastFilter LoadOptions::LoadComponentsLastFilter@endlink  or
            @link LoadOptions::LoadComponentsSpecifyFilter LoadOptions::LoadComponentsSpecifyFilter@endlink  without an
            adv_assemblies license. A license exception will be thrown if an attempt is
            made to set this property to one of these two values without this license.  <br> License requirements : None */
        public: NXOpen::LoadOptions::LoadComponents ComponentsToLoad
        (
        );
        /**Sets  the option that controls the partial loading of components. A value of
            False means that when an assembly is opened its components are fully loaded with it  <br> License requirements : None */
        public: void SetUsePartialLoading
        (
            bool option /** option */ 
        );
        /**Returns  the option that controls the partial loading of components. A value of
            False means that when an assembly is opened its components are fully loaded with it  <br> License requirements : None */
        public: bool UsePartialLoading
        (
        );
        /**Sets  the option that controls if components are displayed with a lightweight 
            or exact representation. A value of True indicates that the lightweight 
            representation is used for the components after the assembly is loaded  <br> License requirements : None */
        public: void SetUseLightweightRepresentations
        (
            bool option /** option */ 
        );
        /**Returns  the option that controls if components are displayed with a lightweight 
            or exact representation. A value of True indicates that the lightweight 
            representation is used for the components after the assembly is loaded  <br> License requirements : None */
        public: bool UseLightweightRepresentations
        (
        );
        /**Sets  the option that controls whether to automatically regenerate missing part
            family members when it loads the parent assembly  <br> License requirements : None */
        public: void SetGenerateMissingPartFamilyMembers
        (
            bool option /** option */ 
        );
        /**Returns  the option that controls whether to automatically regenerate missing part
            family members when it loads the parent assembly  <br> License requirements : None */
        public: bool GenerateMissingPartFamilyMembers
        (
        );
        /** Sets the interpart data option which, when turned on, loads parts that
            are mated or contain interpart expressions, as well as those with WAVE data.
            This method also lets you specify how unloaded parents should be loaded
            when interpart data loading is turned on.  <br> License requirements : None */
        public: void SetInterpartData
        (
            bool interpartOption /** whether or not to allow interpart loading */,
            NXOpen::LoadOptions::Parent parentOption /** how to load unloaded parents */
        );
        /** Returns the interpart data option and the parent option  <br> License requirements : None */
        public: void GetInterpartData
        (
            bool* interpartOption /** interpart option */ ,
            NXOpen::LoadOptions::Parent* parentOption /** parent option */ 
        );
        /**  <br> License requirements : None */
        public: void SetBookmarkComponentsToLoad
        (
            bool restoreAnt /** whether or not to restore the state of assembly navigator */,
            bool restoreFullyLoadedStatus /** whether or not to restore a part's full "loadness" state */,
            NXOpen::LoadOptions::BookmarkComponents componentsLoadOption /** what components to load */
        );
        /** Returns the options for component parts to load and visualize during the bookmark import  <br> License requirements : None */
        public: void GetBookmarkComponentsToLoad
        (
            bool* restoreAnt /** whether to restore ANT's state */,
            NXOpen::LoadOptions::BookmarkComponents* componentsLoadOption /** what components to load */
        );
        /**Sets  the options that specify import and loading of components' reference set  <br> License requirements : None */
        public: void SetBookmarkRefsetLoadBehavior
        (
            NXOpen::LoadOptions::BookmarkRefsets refsetLoadOption /** what to do with refset data */
        );
        /**Returns  the options that specify import and loading of components' reference set  <br> License requirements : None */
        public: NXOpen::LoadOptions::BookmarkRefsets BookmarkRefsetLoadBehavior
        (
        );
        /**Sets  the option that specifies what action the system should take if
            it can't find a component part file  <br> License requirements : None */
        public: void SetAbortOnFailure
        (
            bool option /** option */ 
        );
        /**Returns  the option that specifies what action the system should take if
            it can't find a component part file  <br> License requirements : None */
        public: bool AbortOnFailure
        (
        );
        /**Sets  the allow substition option. If the component found by the
            assembly has the wrong internal identifier (but the correct name),
            this option enables the assembly to be loaded with this component
            even though it is a completely different part.  <br> License requirements : None */
        public: void SetAllowSubstitution
        (
            bool option /** option */ 
        );
        /**Returns  the allow substition option. If the component found by the
            assembly has the wrong internal identifier (but the correct name),
            this option enables the assembly to be loaded with this component
            even though it is a completely different part.  <br> License requirements : None */
        public: bool AllowSubstitution
        (
        );
        /**Sets  the option that specifies whether the system searches for
            the latest component according to the version rules, or looks
            for the exact match.  <br> License requirements : None */
        public: void SetLoadLatest
        (
            bool option /** option */ 
        );
        /**Returns  the option that specifies whether the system searches for
            the latest component according to the version rules, or looks
            for the exact match.  <br> License requirements : None */
        public: bool LoadLatest
        (
        );
        /** Set which search directories are to appear in the list.  <br> License requirements : None */
        public: void SetSearchDirectories
        (
            std::vector<NXString> & searchDirectories /** True indicates that sub-directories should be searched as well   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const std::vector<bool> & searchSubDirs /** search sub dirs */ 
        );
        /** Returns which search directories are to appear in the list.  <br> License requirements : None */
        public: void GetSearchDirectories
        (
            std::vector<NXString> & searchDirectories /** True indicates that sub-directories will be searched as well*/,
            std::vector<bool> & searchSubDirs /** search sub dirs */ 
        );
        /** Sets the list of reference sets to be looked
            for, in order, when an assembly is loaded. The default reference set list
            will always contain the three canned default reference sets: "As Saved",
            "Entire Part", and "Empty". These cannot be removed, but their order
            can be changed.  <br> License requirements : None */
        public: void SetDefaultReferenceSets
        (
            std::vector<NXString> & referenceSets /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Returns the list of reference sets to be looked
            for, in order, when an assembly is loaded. The default reference set list
            will always contain the three canned default reference sets: "As Saved",
            "Entire Part", and "Empty".  @return   <br> License requirements : None */
        public: std::vector<NXString> GetDefaultReferenceSets
        (
        );
        /**Sets  the option that specifies if the default reference set list should be
            applied to components all the way down an assembly tree. This option is referred
            to as "Apply to All Levels" in the User Interface.  <br> License requirements : None */
        public: void SetReferenceSetOverride
        (
            bool option /** option */ 
        );
        /**Returns  the option that specifies if the default reference set list should be
            applied to components all the way down an assembly tree. This option is referred
            to as "Apply to All Levels" in the User Interface.  <br> License requirements : None */
        public: bool ReferenceSetOverride
        (
        );
        /**  Saves the current load options settings in a system file  <br> License requirements : None */
        public: void Save
        (
            const NXString & optionsFile /** Name of file to save to. If this is Nothing, 
                        then the default load options file name will be used.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Changes the load options settings to what they are in the specified file  <br> License requirements : None */
        public: void Restore
        (
            const NXString & optionsFile /** Name of file to restore from. If this is
                        Nothing, then the default load options file name will be used.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif