#ifndef NXOpen_FEATURES_MORPHMESHCOLLECTION_HXX_INCLUDED
#define NXOpen_FEATURES_MORPHMESHCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_MorphMeshCollection.ja
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
#include <NXOpen/BasePart.hxx>
#include <NXOpen/Features_MorphMeshConstraintBuilder.hxx>
#include <NXOpen/Features_MorphMeshDeleteConstraintBuilder.hxx>
#include <NXOpen/Features_MorphMeshTransformBuilder.hxx>
#include <NXOpen/Features_MorphMeshTwistBendData.hxx>
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
        class MorphMeshCollection;
    }
    namespace Features
    {
        class FeatureCollection;
    }
    namespace Features
    {
        class MorphMesh;
    }
    namespace Features
    {
        class MorphMeshBuilder;
    }
    namespace Features
    {
        class MorphMeshCageBuilder;
    }
    namespace Features
    {
        class MorphMeshConstraintBuilder;
    }
    namespace Features
    {
        class MorphMeshDeleteConstraintBuilder;
    }
    namespace Features
    {
        class MorphMeshSymmetricCageBuilder;
    }
    namespace Features
    {
        class MorphMeshTransformBuilder;
    }
    namespace Features
    {
        class MorphMeshTwistBendData;
    }
    namespace Features
    {
        class MorphMeshCollectionImpl;
        /** Collection of Morph Mesh tools  <br> To obtain an instance of this class, refer to @link NXOpen::Features::FeatureCollection  NXOpen::Features::FeatureCollection @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  MorphMeshCollection
        {
            private: MorphMeshCollectionImpl * m_morphmeshcollection_impl;
            private: NXOpen::Features::FeatureCollection* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit MorphMeshCollection(NXOpen::Features::FeatureCollection *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~MorphMeshCollection();
            /** Creates a @link Features::MorphMeshBuilder Features::MorphMeshBuilder@endlink   @return  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Features::MorphMeshBuilder * CreateMorphMeshBuilder
            (
                NXOpen::Features::MorphMesh * morphMesh /** @link Features::MorphMesh Features::MorphMesh@endlink  to be edited */
            );
            /** Creates a @link Features::MorphMeshCageBuilder Features::MorphMeshCageBuilder@endlink  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Features::MorphMeshCageBuilder * CreateMorphMeshCageBuilder
            (
            );
            /** Creates a @link Features::MorphMeshSymmetricCageBuilder Features::MorphMeshSymmetricCageBuilder@endlink  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Features::MorphMeshSymmetricCageBuilder * CreateMorphMeshSymmetricCageBuilder
            (
            );
            /** Creates a @link Features::MorphMeshTransformBuilder Features::MorphMeshTransformBuilder@endlink . 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Features::MorphMeshTransformBuilder * CreateMorphMeshTransformBuilder
            (
            );
            /** Creates a @link Features::MorphMeshTwistBendData Features::MorphMeshTwistBendData@endlink . 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Features::MorphMeshTwistBendData * CreateMorphMeshTwistBendData
            (
            );
            /** Creates a @link Features::MorphMeshConstraintBuilder Features::MorphMeshConstraintBuilder@endlink . 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Features::MorphMeshConstraintBuilder * CreateMorphMeshConstraintBuilder
            (
            );
            /** Creates a @link Features::MorphMeshDeleteConstraintBuilder Features::MorphMeshDeleteConstraintBuilder@endlink . 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Features::MorphMeshDeleteConstraintBuilder * CreateMorphMeshDeleteConstraintBuilder
            (
            );
            /** Stops the symmetric modeling. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: void StopSymmetricModeling
            (
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
