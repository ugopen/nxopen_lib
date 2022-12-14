#ifndef NXOpen_SIM_MACHINELIBRARYBUILDER_HXX_INCLUDED
#define NXOpen_SIM_MACHINELIBRARYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_MachineLibraryBuilder.ja
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
#include <NXOpen/SIM_MachineLibraryBuilder.hxx>
#include <NXOpen/libnxopencpp_sim_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace SIM
    {
        class MachineLibraryBuilder;
    }
    class Builder;
    namespace SIM
    {
        class _MachineLibraryBuilderBuilder;
        class MachineLibraryBuilderImpl;
        /** This class is used for the Machine Library Dialog.
                Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
              <br> Use the @link Part Part@endlink  class to create a MachineLibraryBuilder object.  <br> 
         <br>  Created in NX10.0.2.  <br>  
        */
        class NXOPENCPP_SIMEXPORT  MachineLibraryBuilder : public NXOpen::Builder
        {
            private: MachineLibraryBuilderImpl * m_machinelibrarybuilder_impl;
            private: friend class  _MachineLibraryBuilderBuilder;
            protected: MachineLibraryBuilder();
            public: ~MachineLibraryBuilder();
            /** Edit a specific machine of the database. That will write the machine_database.dat. 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void EditMachineLibrary
            (
                const NXString & machineName /** machine name (libref)*/,
                const NXString & attName /** library attribute name*/,
                const NXString & value /** the new value that will be set*/
            );
            /** Edit a specific machine of the database. That will write the machine_database.dat. 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void EditMachineLibrary
            (
                const char * machineName /** machine name (libref)*/,
                const char * attName /** library attribute name*/,
                const char * value /** the new value that will be set*/
            );
            /** Insert a machine entry to the machine_database.dat. The libref is the name of the machine entry,
                        that is copied, the libref appended by a count and the new entry is put in the list as next entry.
                    If the libref is empty, a default entry is add to the bottom of the list.  @return  machine name (libref), of the new machien entry
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: NXString InsertEntryToMachineLibrary
            (
                const NXString & selectedMachineName /** machine name (libref), that will copied*/
            );
            /** Insert a machine entry to the machine_database.dat. The libref is the name of the machine entry,
                        that is copied, the libref appended by a count and the new entry is put in the list as next entry.
                    If the libref is empty, a default entry is add to the bottom of the list.  @return  machine name (libref), of the new machien entry
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            NXString InsertEntryToMachineLibrary
            (
                const char * selectedMachineName /** machine name (libref), that will copied*/
            );
            /** Removes a machine entry from the machine_database.dat. The libref is the name of the machine entry,
                        that will reomved from the Library. 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void RemoveEntryFromMachineLibrary
            (
                const NXString & machineName /** machine name (libref)*/
            );
            /** Removes a machine entry from the machine_database.dat. The libref is the name of the machine entry,
                        that will reomved from the Library. 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void RemoveEntryFromMachineLibrary
            (
                const char * machineName /** machine name (libref)*/
            );
            /** Returns a array of the machine names(librefs) that are in the machine database. 
                        This function allocates the memory for machineNames. The caller is responsible to deallocate the memory. @return  array of all machine names (libref)
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: std::vector<NXString> GetAllMachineNames
            (
            );
            /** Returns a array of the library attributes.
                        This function allocates the memory for attributeNames. The caller is responsible to deallocate the memory. @return  array of all attribute names
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: std::vector<NXString> GetAllAttributeNames
            (
            );
            /** Returns the attribute value of a specific machine.  @return  
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: NXString GetValue
            (
                const NXString & machineName /** machine name (libref)*/,
                const NXString & attName /** library attribute name*/
            );
            /** Returns the attribute value of a specific machine.  @return  
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            NXString GetValue
            (
                const char * machineName /** machine name (libref)*/,
                const char * attName /** library attribute name*/
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
