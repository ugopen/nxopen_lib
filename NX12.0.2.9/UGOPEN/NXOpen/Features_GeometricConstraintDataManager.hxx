#ifndef NXOpen_FEATURES_GEOMETRICCONSTRAINTDATAMANAGER_HXX_INCLUDED
#define NXOpen_FEATURES_GEOMETRICCONSTRAINTDATAMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_GeometricConstraintDataManager.ja
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
#include <NXOpen/Features_GeometricConstraintData.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class GeometricConstraintDataManager;
    }
    namespace Features
    {
        class GeometricConstraintData;
    }
    namespace Features
    {
        class _GeometricConstraintDataManagerBuilder;
        class GeometricConstraintDataManagerImpl;
        /** Represents Geometric Constraint Data Manager class.
                This class maintains a list of @link NXOpen::Features::GeometricConstraintData NXOpen::Features::GeometricConstraintData@endlink  objects
                and manages them.
            
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  GeometricConstraintDataManager : public NXOpen::TaggedObject
        {
            private: GeometricConstraintDataManagerImpl * m_geometricconstraintdatamanager_impl;
            private: friend class  _GeometricConstraintDataManagerBuilder;
            protected: GeometricConstraintDataManager();
            public: ~GeometricConstraintDataManager();
            /** Creates a new empty @link NXOpen::Features::GeometricConstraintData NXOpen::Features::GeometricConstraintData@endlink  object  @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::GeometricConstraintData * CreateGeometricConstraintData
            (
            );
            /** Appends @link NXOpen::Features::GeometricConstraintData NXOpen::Features::GeometricConstraintData@endlink  object to the end of the list 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Append
            (
                NXOpen::Features::GeometricConstraintData * constraint /** constraint */ 
            );
            /** Inserts @link NXOpen::Features::GeometricConstraintData NXOpen::Features::GeometricConstraintData@endlink  object in the list
                        before a given position 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Insert
            (
                int insertBeforeIndex /** insert before index */ ,
                NXOpen::Features::GeometricConstraintData * constraint /** constraint */ 
            );
            /** Deletes a given @link NXOpen::Features::GeometricConstraintData NXOpen::Features::GeometricConstraintData@endlink  object from the list 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Delete
            (
                NXOpen::Features::GeometricConstraintData * constraint /** constraint */ 
            );
            /** Deletes @link NXOpen::Features::GeometricConstraintData NXOpen::Features::GeometricConstraintData@endlink  object of a certain index from the list 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Delete
            (
                int constraintIndex /** constraint index */ 
            );
            /** Deletes all @link NXOpen::Features::GeometricConstraintData NXOpen::Features::GeometricConstraintData@endlink  objects from the list 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Clear
            (
            );
            /**Returns  the number of @link NXOpen::Features::GeometricConstraintData NXOpen::Features::GeometricConstraintData@endlink  objects in the list 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int Length
            (
            );
            /** Queries all the @link NXOpen::Features::GeometricConstraintData NXOpen::Features::GeometricConstraintData@endlink  objects  @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Features::GeometricConstraintData *> GetContents
            (
            );
            /** Sets array of @link NXOpen::Features::GeometricConstraintData NXOpen::Features::GeometricConstraintData@endlink  objects in the list. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetContents
            (
                const std::vector<NXOpen::Features::GeometricConstraintData *> & constraints /** constraints */ 
            );
            /** Returns @link NXOpen::Features::GeometricConstraintData NXOpen::Features::GeometricConstraintData@endlink  object at the input index. 
                        May be NULL if not found.  @return  object found at input index 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::GeometricConstraintData * FindItem
            (
                int constraintIndex /** index of object to return */
            );
            /** Finds index of @link NXOpen::Features::GeometricConstraintData NXOpen::Features::GeometricConstraintData@endlink  object in the list  @return  Equals -1 if not found 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int GetIndex
            (
                NXOpen::Features::GeometricConstraintData * constraint /** constraint */ 
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
