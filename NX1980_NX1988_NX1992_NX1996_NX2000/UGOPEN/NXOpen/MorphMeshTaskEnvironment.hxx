#ifndef NXOpen_MORPHMESHTASKENVIRONMENT_HXX_INCLUDED
#define NXOpen_MORPHMESHTASKENVIRONMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MorphMeshTaskEnvironment.ja
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

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class MorphMeshTaskEnvironment;
    class Session;
    namespace Features
    {
        class MorphMesh;
    }
    class MorphMeshTaskEnvironmentImpl;
    /**
        Represents the Morph Mesh task environment associated with a session.
     <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
     <br>  Created in NX1872.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  MorphMeshTaskEnvironment
    {
        private: MorphMeshTaskEnvironmentImpl * m_morphmeshtaskenvironment_impl;
        private: NXOpen::Session* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit MorphMeshTaskEnvironment(NXOpen::Session *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~MorphMeshTaskEnvironment();
        /** Starts Morph Mesh task environment. This method should
                be called before starting to use Morph Mesh feature tools.
                This method should not be called if already in a Morph Mesh task environment.
            
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
        public: void Enter
        (
        );
        /** Ends Morph Mesh task environment.
            
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
        public: void Exit
        (
        );
        /**Returns  the active Morph Mesh body feature. 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Features::MorphMesh * ActiveMorphMeshFeature
        (
        );
        /** Sets the feature to be edited. 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
        public: void SetFeatureToEdit
        (
            NXOpen::Features::MorphMesh * feature /** feature */ 
        );
        /** Marks the task to be cancelled such that during @link MorphMeshTaskEnvironment::Exit MorphMeshTaskEnvironment::Exit@endlink 
                task is undone and all the changes are discarded.
            
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
        public: void SetCancelled
        (
        );
    }; //lint !e1712 default constructor not defined for class  

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