#ifndef NXOpen_MOTION_MOTIONSIMULATION_HXX_INCLUDED
#define NXOpen_MOTION_MOTIONSIMULATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_MotionSimulation.ja
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
#include <NXOpen/Motion_AddSubmechanismBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class MotionSimulation;
    }
    class Session;
    namespace Motion
    {
        class AddSubmechanismBuilder;
    }
    namespace Motion
    {
        class MotionSolution;
    }
    class NXObject;
    class Part;
    namespace Motion
    {
        class MotionSimulationImpl;
        /** Represents Motion.Simulation  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  MotionSimulation
        {
            /** Format to export the geometry of Adams */
            public: enum JaMotionMotionExportAdamsGeometryFormat
            {
                JaMotionMotionExportAdamsGeometryFormatNone/** NONE format to export the geometry of Adams */ = -1,
                JaMotionMotionExportAdamsGeometryFormatStl/** STL format to export the geometry of Adams */,
                JaMotionMotionExportAdamsGeometryFormatParasolid/** PARASOLID format to export the geometry of Adams */
            };

            private: MotionSimulationImpl * m_motionsimulation_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit MotionSimulation(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~MotionSimulation();
            /** Calculate the gruebler count of given motion part  @return  gruebler count 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int CalculateGrueblerCount
            (
                NXOpen::NXObject * motionPart /** motion part object */
            );
            /** Export Recurdyn sdk data, need an active solution in simulation 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void ExportRecurdynSdk
            (
                const NXString & fullFileName /** full name with directory and extension*/
            );
            /** Export Recurdyn sdk data, need an active solution in simulation 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void ExportRecurdynSdk
            (
                const char * fullFileName /** full name with directory and extension*/
            );
            /** Creates a new @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink  in this motion simulation assembly as master part 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void AddMaster
            (
                NXOpen::Part * motionPart /** the motion part to add master part into it*/,
                NXOpen::NXObject * masterPart /** the master part to be added, it can be a part occurrence tag or part tag */
            );
            /** Removes existing master part in this motion simulation assembly 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void RemoveMaster
            (
                NXOpen::Part * motionPart /** the motion part to remove master part from it */,
                bool deleteMotionObjects /** the tag whether to keep or delete motion objects referencing master part */
            );
            /** Gets the loaded master part in this motion simulation assembly.  @return  the loaded master part 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Part * GetMasterCadPart
            (
                NXOpen::Part * motionPart /** the motion part to remove master part from it */
            );
            /** Sets the custom name of the Submechanism object.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void RenameSubmechanism
            (
                NXOpen::NXObject * submechanism /** submechanism */ ,
                const NXString & name /** name */ 
            );
            /** Sets the custom name of the Submechanism object.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void RenameSubmechanism
            (
                NXOpen::NXObject * submechanism /** submechanism */ ,
                const char * name /** name */ 
            );
            /** Copies the deactivated states of motion objects occurrences belonging to a given 
                        submechanism from a given solution to the motion assembly. The motion objects deactivated from the
                        given solution will become "Deactivated for All" in the motion assembly. 
                        If submechanism tag is NULL then will copy the deactivated states from the selected solution to the active one.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void ReadDeactivatedStates
            (
                NXOpen::NXObject * sumbmechanism /** submechanism child of current root part */,
                NXOpen::Motion::MotionSolution * solution /** the solution, from the submechanism part, from which the deactivated states are read */
            );
            /**   Returns  @link  NXOpen::Motion::AddSubmechanismBuilder   NXOpen::Motion::AddSubmechanismBuilder @endlink  object   @return  @link  NXOpen::Motion::AddSubmechanismBuilder   NXOpen::Motion::AddSubmechanismBuilder @endlink  object 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::AddSubmechanismBuilder * CreateAddSubmechanismBuilder
            (
                NXOpen::NXObject * part /** the part object */
            );
            /** Deactivates a motion object for all solutions 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void AddSuppressedObjectForAllSolutions
            (
                NXOpen::Part * motionPart /** motionpart */ ,
                NXOpen::NXObject * obj /** obj */ 
            );
            /** Activates a motion object for all solutions 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void RemoveSuppressedObjectForAllSolutions
            (
                NXOpen::Part * motionPart /** motionpart */ ,
                NXOpen::NXObject * obj /** obj */ 
            );
            /** Convert Text Based Elements 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void ConvertTextBasedElements
            (
                NXOpen::Part * motionPart /** motionpart */ 
            );
            /** Adams Stl parameters 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetAdamsStlParams
            (
                double minFacetEdgeLen /** minfacetedgelen */ ,
                double maxFacetEdgeLen /** maxfacetedgelen */ ,
                double facetToSurfaceTolerance /** facettosurfacetolerance */ 
            );
            /** Write geometry file for Adams solver, the active solver should be Recurdyn 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void WriteAdamsGeometryFile
            (
                const NXString & fullFileName /** full name with directory and extension*/,
                NXOpen::Motion::MotionSimulation::JaMotionMotionExportAdamsGeometryFormat geoFormat /** geoformat */ 
            );
            /** Write geometry file for Adams solver, the active solver should be Recurdyn 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void WriteAdamsGeometryFile
            (
                const char * fullFileName /** full name with directory and extension*/,
                NXOpen::Motion::MotionSimulation::JaMotionMotionExportAdamsGeometryFormat geoFormat /** geoformat */ 
            );
            /** Write Adams anl file 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void WriteAdamsAnlFile
            (
                const NXString & fullFileName /** full name with directory and extension*/
            );
            /** Write Adams anl file 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void WriteAdamsAnlFile
            (
                const char * fullFileName /** full name with directory and extension*/
            );
            /** Write adams adm file for Recurdyn solver, the active solver should be Recurdyn
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void WriteRdsdkAdmFile
            (
                const NXString & fullFileName /** full name with directory and extension*/
            );
            /** Write adams adm file for Recurdyn solver, the active solver should be Recurdyn
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void WriteRdsdkAdmFile
            (
                const char * fullFileName /** full name with directory and extension*/
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
