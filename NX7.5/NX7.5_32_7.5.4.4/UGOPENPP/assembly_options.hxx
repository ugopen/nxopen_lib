/*
================================================================================

          Copyright (c) 1999-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Search Directory and Assembly Options C++ class definitions

================================================================================

*/

#ifndef ASSEMBLY_OPTIONS_INCLUDED
#define ASSEMBLY_OPTIONS_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_constants.hxx>
#include <ug_string.hxx>
#include <ug_vector.hxx>

#include <uf_assem.h>
#include <libopenpp_exports.hxx>

// This helper class defines a directory to be used to search for
// assembly components, and a status that determines if the 
// subdirectories of that directory are to be searched also.
class OPENPPEXPORT SearchDirectory
{

    public:
    
        // Construct a SearchDirectory object.  This default constructor
        // is necessary because std::vector requires it.
        SearchDirectory ( );

        // Construct a SearchDirectory object from its components.
        SearchDirectory
        (
            const std::string &directory_path,        // <I>
                                                      // The path of the directory
                                                      // to search.
            bool               subdirectory_status = true  // <I>
                                                      // The subdirectory status of
                                                      // the search directory.  If true,
                                                      // the subdirectories are searched.
                                                      // If false, the subdirectories are
                                                      // not searched.
        );

        // Destroy a SearchDirectory object.
        ~SearchDirectory ( );

        // Return the directory path of the invoking SearchDirectory object.
        const std::string getDirectoryPath ( ) const;

        // Edit the directory path of the invoking SearchDirectory object.
        void setDirectoryPath
        (
            const std::string  &directory_path     // <I>     
                                                   // The new path of the directory
                                                   // to search.
        );

        // Return true if the subdirectories of the invoking
        // SearchDirectory object are to be searched.  Return false otherwise.
        bool getSubDirectoryStatus ( ) const;

        // Edit the subdirectory search status of the invoking
        // SearchDirectory object.
        void setSubDirectoryStatus
        (
            bool             subdirectory_status
                                                // <I>
                                                // The new subdirectory status of
                                                // the search directory.  If true,
                                                // the subdirectories are searched.
                                                // If false, the subdirectories are
                                                // not searched.
        );

        // Determine the equality of two SearchDirectory objects.
        // The two objects are considered equal if the directory path of the
        // invoking object is identical to the directory path of the argument
        // object, AND the subdirectory status of the invoking object is equal
        // to the subdirectory status of the argument object.
        bool operator==
        ( 
            const SearchDirectory  &right   // <I>
                                            // The SearchDirectory object to
                                            // test for equality against
                                            // the invoking object.
        ) const;

    private:

        // The directory path of the search directory.
        std::string         m_directory_path;

        // The search status of the subdirectories of the search directory.
        // If true, the subdirectories are also searched.  If false, the
        // subdirectories are not searched.
        bool                m_subdirectory_status;

};

// This class models the assembly options that are currently in effect, and 
// allows the application the means to access those options and change them.
class OPENPPEXPORT AssemblyOptions  
{

    public:

        // Available load options that determine where the parts of an assembly 
        // can be found.
        enum LoadOption
        {
            LoadOptionDirectory = UF_ASSEM_load_from_directory, //
                                                // Part files are looked in the
                                                // current directory.
            LoadOptionSearch    = UF_ASSEM_load_from_search_dirs, //
                                                // Part files are looked in the
                                                // currently defined search
                                                // directories.
            LoadOptionSaved     = UF_ASSEM_load_as_saved //
                                                // The part files are looked for in
                                                // the directory that they were in
                                                // when the assembly was last saved.
        };

        // Available parts list options that determine the display of added components
        // in the parts list output.
        enum PartsListOption
        {
            PartsListOptionNoNew  = UF_ASSEM_do_not_add_components, //
                                                // New components are not added to the
                                                // parts list output.
            PartsListOptionNew    = UF_ASSEM_add_single_level, //
                                                // New components are added to the
                                                // parts list output, but not the 
                                                // components of the new component.
            PartsListOptionAllNew = UF_ASSEM_add_all_levels //
                                                // New components are added to the parts
                                                // list output, and the components of the 
                                                // new component are also added.
        };

        // Available component options that determine how the component part files are 
        // to be loaded with an assembly part.
        enum ComponentOption
        {
            ComponentOptionNone       = UF_ASSEM_dont_load_components, //
                                                // The load assembly operation loads only
                                                // the assembly part.
            ComponentOptionAll        = UF_ASSEM_do_load_components, //
                                                // The load assembly operation attempts 
                                                // to load all components.
            ComponentOptionLastSave   = UF_ASSEM_use_last_component_set, //
                                                // The load assembly operation attempts 
                                               // to load the same set of components as
                                                // when the assembly was last saved.
            ComponentOptionLastFilter = UF_ASSEM_use_last_filter //
                                                // The load assembly operation attempts to
                                                // load components by running the same
                                                // filter as was run the last time the
                                                // assembly was loaded.
        };

        // Available parent part options that determine how parent parts with linked
        // data are loaded when the load-WAVE-data status is set.
        enum WaveParentOption
        {
            WaveParentOptionNone   = UF_ASSEM_none, //
                                                // Partially loaded parts with parent
                                                // geometry will be fully loaded, but not
                                                // the unloaded parts.
            WaveParentOptionSingle = UF_ASSEM_immediate, //
                                                // Parts that satisfy a single level of
                                                // WAVE parent references will be fully
                                                // loaded, as well as any partilly loaded
                                                // parts with parent geometry.
            WaveParentOptionAll    = UF_ASSEM_all //
                                                // All parts with parent geometry, linked
                                                // to geometry in the parts that were
                                                // specified for loading, will be fully
                                                // loaded.
        };

        // Construct an AssemblyOptions object.
        AssemblyOptions ( );

        // Destroy an AssemblyOptions object.
        virtual ~AssemblyOptions ( );

        // Return the load option of the invoking AssemblyOptions object.
        LoadOption getLoadOption ( ) const;
    
        // Edit the load option of the invoking AssemblyOptions object.
        void setLoadOption 
        (
            const LoadOption load_option        // <I>
                                                // The new load option that determines where
                                                // assembly parts can be found.
        );
    
        // Return the parts list option of the invoking AssemblyOptions object.
        PartsListOption getPartsListOption ( ) const;
    
        // Edit the parts list option of the invoking AssemblyOptions object.
        void setPartsListOption
        (
            const PartsListOption parts_list_option
                                                // <I>
                                                // The new parts list option that determines
                                                // the display of new components in the
                                                // parts list output.
        );

        // When opening an assembly and loading its components, any component that has been 
        // modified since its parent assembly was last saved is automatically updated. 
        // A report can be generated that summarizes the component updates.
        // This method checks if the update report setting of the invoking AssemblyOptions
        // object is turned on. Returns true if it is on, false otherwise.
        bool isUpdateReportOn ( ) const;
    
        // When opening an assembly and loading its components, any component that has been 
        // modified since its parent assembly was last saved is automatically updated. 
        // A report can be generated that summarizes the component updates.
        // Edit the update report setting of the invoking AssemblyOptions object to 
        // determine if the report is generated.
        void outputUpdateReport
        (
            bool output_report                  // <I>
                                                // If true, the update report is
                                                // automatically displayed when an assembly
                                                // is loaded. Otherwise, the report is not
                                                // displayed.
        );

        // Return true if the work part is highlighted with respect to the other component
        // parts of the assembly. Return false otherwise.
        bool isWorkPartEmphasized ( ) const;

        // Edit the highlight-work-part status of the invoking AssemblyOptions object to
        // determine if the work part is highlighted.
        void emphasizeWorkPart
        ( 
            bool emphasize_work_part            // <I>
                                                // If true, the work part is highlighted
                                                // with respect to the other component parts
                                                // of the assembly.  If false, the work
                                                // part is not highlighted.
        );

        // Return the color that the other component parts of the assembly are displayed in 
        // if the work part is highlighted.
        UgColor getColor ( ) const;

        // Edit the color that the other component parts of the assembly are displayed in
        // if the work part is highlighted.
        void setColor 
        (
            const UgColor color                 // <I>  
                                                // The new color to display the other
                                                // components of the assembly in if the
                                                // work part is highlighted.
        );

        // Return true if an assembly load operation will abort when a component part file
        // can not be found.  Return false if the assembly load operation will not abort
        // but just not load the missing component part files.
        bool isAbortOnFailure ( ) const;

        // Edit the abort-on-failure status of the invoking AssemblyOptions object to
        // determine if the load operation should fail when a component part file can not
        // be found.
        void abortOnFailure
        (
            bool abort_on_failure               // <I>
                                                // If true, an assembly load operation will
                                                // abort when a component part file can not
                                                // be found.  If false, the assembly load
                                                // operation will not abort but just not
                                                // load the missing component part files.
        );

        // Return true if the work part is unchanged after changing the displayed part.
        // Return false if the work part is set to the displayed part after changing the
        // displayed part.
        bool isWorkPartMaintained ( ) const;

        // Edit the maintain-work-part status of the invoking AssemblyOptions object to 
        // determine if the work part should change after changing the displayed part.
        void maintainWorkPart
        (
            bool maintain_work_part             // <I>
                                                // If true, the work part is unchanged after
                                                // changing the displayed part.  If false,
                                                // the work part is set to the displayed part
                                                // after changing the displayed part.
        );

        // Return true if a search is made for the latest component according to the 
        // version rules. Return false if a search is made for the exact match.
        bool isLoadLatestOn ( ) const;
    
        // Edit the load-latest status of the invoking AssemblyOptions object to determine
        // if a search should be made for the latest component according to the version rules.
        void loadLatest 
        (
            bool load_latest                    // <I>
                                                // If true, search is made of all part names
                                                // that match the "core" portion of the part
                                                // name and the latest component based on the
                                                // specified rule is used.  If false, the
                                                // assembly is loaded with the same component
                                                // versions it was last saved with.
        );

        // Return the component option of the invoking AssemblyOptions object.
        ComponentOption getComponentOption ( ) const;

        //Edit the component option of the invoking AssemblyOptions object
        void setComponentOption
        (
            const ComponentOption component_option
                                                // <I>
                                                // The new component option that determines
                                                // how the component part files are to be 
                                                // loaded with assembly part.
        );


        // Return true if the components of an assembly are partially loaded when the 
        // assembly is opened.  Return false if the  components of an assembly are fully
        // loaded when the assembly is opened.
        bool isPartialLoadingOn ( ) const;

        // Edit the partial-loading status of the invoking AssemblyOptions object to determine
        // if the components of an assembly are partially or fully loaded when the assembly
        // is opened.
        void loadPartially
        (
            bool load_partially                 // <I>
                                                // If true, the components of an assembly
                                                // are partially loaded when the assembly
                                                // is opened.  If false, the components of
                                                // an assembly are fully loaded when the
                                                // assembly is opened.
        );

        // Return true if substitute parts are allowed to be used for the components of 
        // an assembly. Return false if substitute parts are not allowed.
        bool isAllowSubstitutionOn ( ) const;

        // Edit the load-substitution status of the invoking AssemblyOptions object to 
        // determine if the components of an assembly can be substituted.
        void allowSubstitution
        (
            bool allow_substitution             // <I>
                                                // If true, a completely different part can
                                                // be loaded as a component if it has the
                                                // correct name.  If false, no substitutions
                                                // can be made.
        );

        // Return true if default reference sets will be applied to components all the way
        // down the assembly tree. Return false if the default reference sets will not be 
        // applied to the components of a sub-assembly.
        bool isAllLevelsOn ( ) const;


        // Edit the all-levels status of the invoking AssemblyOptions object to determine 
        // if the default reference sets are applied to components all the way down the 
        // assembly tree.
        void applyAllLevels
        (
            bool apply_all_levels               // <I>
                                                // If true, a sub-assembly is loaded with a
                                                // user defined reference set or entire part
                                                // will cause the same default reference
                                                // sets to be applied to all of the components
                                                // included in the sub-assembly reference
                                                // set.  If false, the components will use
                                                // the reference set that the sub-assembly
                                                // reference set referred to when it was
                                                // last saved.
        );

        // Return true if WAVE geometry is loaded regardless of the partial-loading status.
        // Return false if WAVE geometry is not loaded if the partial-loading status is on.
        bool isLoadWaveDataOn ( ) const;

        // Edit the load-WAVE-data status of the invoking AssemblyOptions object to determine
        // if the components of an assembly will have their WAVE geometry loaded regardless
        // of the partial-loading status.
        void loadWaveData 
        (
            bool load_wave_data                 // <I>
                                                // If true, components containing linked WAVE
                                                // geometry will be loaded fully regardless
                                                // of the partial-loading status.  If false,
                                                // components containing linked WAVE geometry
                                                // will be loaded as specified by the
                                                // partial-loading status.
        );

        // Return the WAVE parent option of the invoking AssemblyOptions object.
        WaveParentOption getWaveParentOption ( ) const;
    
        // Edit the WAVE parent option of the invoking AssemblyOptions object.
        void setWaveParentOption
        (
            const WaveParentOption wave_option  //  <I>
                                                // The new WAVE parent option that determines
                                                // how linked parent parts are loaded.
        );

        // Return a std::vector object that contains the names of the default reference sets.
        // Returns a zero length std::vector if there are no default reference sets. The names
        // of the reference sets are returned in the order in which they are applied.
        const std::vector < std::string > getDefaultReferenceSets ( );

        // Edit the default reference sets in the order that they are supplied. The default 
        // reference sets must have "As Saved", "Entire Part", and "Empty" in the std::vector. If
        // any of these are not specified in the std::vector, they are added to the end of the 
        // list of default reference sets in that order.
        void setDefaultReferenceSets
        (
            const std::vector < std::string > &defaults
                                                // <I>
                                                // The ordered std::vector of reference set 
                                                // names indicating the default reference
                                                // sets.
        );

        // Return a std::vector object that contains the names of all of the current search 
        // directories. Return a zero-length std::vector if there are no search directories.
        const std::vector < SearchDirectory > getSearchDirectories ( );

        // Edit the list of search directories.
        void setSearchDirectories
        (
            const std::vector < SearchDirectory > &dir_names
                                                // <I>
                                                // New list of search directories.
        );

    private :

        // Initialize the member variable of the invoking AssemblyOptions obect
        void initialize ( );

        // Save the member variable of the invoking AssemblyOptions object.
        void save ( ) const;   
        
        // Attribute to define the assembly options that are currently in effect.
        UF_ASSEM_options_t  m_assembly_options;
 
};

#undef EXPORTLIBRARY

#endif // ASSEMBLY_OPTIONS_INCLUDED
