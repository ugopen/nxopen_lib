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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class LoadOptions;
    class PartCollection;
    /** Contains accessor methods for all the part load options.  <br> To obtain an instance of this class, refer to @link PartCollection PartCollection@endlink  <br> */
    class NXOPENCPPEXPORT LoadOptions
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

        private: NXOpen::PartCollection* m_owner;
        public: explicit LoadOptions(NXOpen::PartCollection *owner): m_owner(owner)
        {
        }
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
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
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link ComponentLoadMethod() ComponentLoadMethod@endlink instead.
        @deprecated
        */
        public: NXOpen::LoadOptions::LoadMethod GetComponentLoadMethod
        (
        ) { return this->ComponentLoadMethod(); }
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
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link ComponentsToLoad() ComponentsToLoad@endlink instead.
        @deprecated
        */
        public: NXOpen::LoadOptions::LoadComponents GetComponentsToLoad
        (
        ) { return this->ComponentsToLoad(); }
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
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link UsePartialLoading() UsePartialLoading@endlink instead.
        @deprecated
        */
        public: bool GetUsePartialLoading
        (
        ) { return this->UsePartialLoading(); }
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
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link GenerateMissingPartFamilyMembers() GenerateMissingPartFamilyMembers@endlink instead.
        @deprecated
        */
        public: bool GetGenerateMissingPartFamilyMembers
        (
        ) { return this->GenerateMissingPartFamilyMembers(); }
        /** Sets the interpart data option which, when turned on, loads parts that
            are mated or contain interpart expressions, as well as those with WAVE data.
            This method also lets you specify how unloaded parents should be loaded
            when interpart data loading is turned on.  <br> License requirements : None */
        public: void SetInterpartData
        (
            bool interpart_option /** whether or not to allow interpart loading */,
            NXOpen::LoadOptions::Parent parent_option /** how to load unloaded parents */
        );
        /** Returns the interpart data option and the parent option  <br> License requirements : None */
        public: void GetInterpartData
        (
            bool* interpart_option /** interpart option */ ,
            NXOpen::LoadOptions::Parent* parent_option /** parent option */ 
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
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link AbortOnFailure() AbortOnFailure@endlink instead.
        @deprecated
        */
        public: bool GetAbortOnFailure
        (
        ) { return this->AbortOnFailure(); }
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
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link AllowSubstitution() AllowSubstitution@endlink instead.
        @deprecated
        */
        public: bool GetAllowSubstitution
        (
        ) { return this->AllowSubstitution(); }
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
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link LoadLatest() LoadLatest@endlink instead.
        @deprecated
        */
        public: bool GetLoadLatest
        (
        ) { return this->LoadLatest(); }
        /** Set which search directories are to appear in the list.  <br> License requirements : None */
        public: void SetSearchDirectories
        (
            std::vector<NXString> & search_directories /** True indicates that sub-directories should be searched as well   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const std::vector<bool> & search_sub_dirs /** search sub dirs */ 
        );
        /** Returns which search directories are to appear in the list.  <br> License requirements : None */
        public: void GetSearchDirectories
        (
            std::vector<NXString> & search_directories /** True indicates that sub-directories will be searched as well*/,
            std::vector<bool> & search_sub_dirs /** search sub dirs */ 
        );
        /** Sets the list of reference sets to be looked
            for, in order, when an assembly is loaded. The default reference set list
            will always contain the three canned default reference sets: "As Saved",
            "Entire Part", and "Empty". These cannot be removed, but their order
            can be changed.  <br> License requirements : None */
        public: void SetDefaultReferenceSets
        (
            std::vector<NXString> & reference_sets /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
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
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link ReferenceSetOverride() ReferenceSetOverride@endlink instead.
        @deprecated
        */
        public: bool GetReferenceSetOverride
        (
        ) { return this->ReferenceSetOverride(); }
        /**  Saves the current load options settings in a system file  <br> License requirements : None */
        public: void Save
        (
            const NXString & options_file /** Name of file to save to. If this is Nothing, 
                        then the default load options file name will be used.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Changes the load options settings to what they are in the specified file  <br> License requirements : None */
        public: void Restore
        (
            const NXString & options_file /** Name of file to restore from. If this is
                        Nothing, then the default load options file name will be used.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif
