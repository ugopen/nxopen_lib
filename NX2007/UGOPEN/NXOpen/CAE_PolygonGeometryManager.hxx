#ifndef NXOpen_CAE_POLYGONGEOMETRYMANAGER_HXX_INCLUDED
#define NXOpen_CAE_POLYGONGEOMETRYMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PolygonGeometryManager.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class PolygonGeometryManager;
    }
    namespace CAE
    {
        class FemPart;
    }
    class Body;
    namespace CAE
    {
        class CAEBody;
    }
    namespace CAE
    {
        class GeometryRecipeCollection;
    }
    class Expression;
    namespace CAE
    {
        class PolygonGeometryManagerImpl;
        /**  @brief  Provides methods for managing set @link NXOpen::CAE::PolygonGeometryManager NXOpen::CAE::PolygonGeometryManager@endlink  

           <br> Use the @link NXOpen::CAE::GeometryRecipeCollection NXOpen::CAE::GeometryRecipeCollection@endlink  class to create a recipe.  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PolygonGeometryManager
        {
            /** Entity type */
            public: enum PolygonBodyResolutionType
            {
                PolygonBodyResolutionTypeStandard/** standard */ ,
                PolygonBodyResolutionTypeMedium/** medium */ ,
                PolygonBodyResolutionTypeHigh/** high */ ,
                PolygonBodyResolutionTypeCustom/** custom */ 
            };

            private: PolygonGeometryManagerImpl * m_polygongeometrymanager_impl;
            private: NXOpen::CAE::FemPart* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit PolygonGeometryManager(NXOpen::CAE::FemPart *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~PolygonGeometryManager();
            /** Sets the tesselation on polygon bodies that were created from CAD bodies. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPolygonBodyResolutionOnFemBodies
            (
                NXOpen::CAE::PolygonGeometryManager::PolygonBodyResolutionType resType /** Tesselation on all polygon bodies */
            );
            /** Gets the tesselation on polygon bodies that were created from CAD bodies.  @return  Tesselation on all polygon bodies 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::PolygonGeometryManager::PolygonBodyResolutionType GetPolygonBodyResolutionOnFemBodies
            (
            );
            /** Set Resolution for polygon body with recreate body only 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<NXOpen::CAE::CAEBody *> SetPolygonBodyResolutionWithRecreate
            (
                NXOpen::CAE::PolygonGeometryManager::PolygonBodyResolutionType resolutionType /** resolution type */ ,
                const std::vector<NXOpen::CAE::CAEBody *> & inPolygonBodies /** in polygon bodies */ 
            );
            /** Set Resolution for polygon body with recreate body and update only 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<NXOpen::CAE::CAEBody *> SetPolygonBodyResolutionWithRecreateAndUpdate
            (
                NXOpen::CAE::PolygonGeometryManager::PolygonBodyResolutionType resolutionType /** resolution type */ ,
                const std::vector<NXOpen::CAE::CAEBody *> & inPolygonBodies /** in polygon bodies */ 
            );
            /** Sets the distance for custom resolution tesellation on polygon bodies that were created from CAD bodies.
                        This value will be considered only when polygon body resolution is set to custom 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPolygonBodyResolutionCustomDistanceOnFemBodies
            (
                NXOpen::Expression * customDistance /**Distance for Custom Resolution Option */
            );
            /** Gets the the distance for custom resolution tesselation on polygon bodies that were created from CAD bodies. 
                        This value will be considered only when polygon body resolution is set to custom @return  Distance for Custom Resolution Option on all polygon bodies
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Expression * GetPolygonBodyResolutionCustomDistanceOnFemBodies
            (
            );
            /** Sets the anlge for custom resolution tesellation on polygon bodies that were created from CAD bodies. 
                        This value will be considered only when polygon body resolution is set to custom
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPolygonBodyResolutionCustomAngleOnFemBodies
            (
                NXOpen::Expression * customAngle /** Angle for Custom Resolution Option on all polygon bodies*/
            );
            /** Gets the the angle for custom resolution tesselation on polygon bodies that were created from CAD bodies.
                        This value will be considered only when polygon body resolution is set to custom  @return  Angle for Custom Resolution Option on all polygon bodies 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Expression * GetPolygonBodyResolutionCustomAngleOnFemBodies
            (
            );
            /** Set Distance for Custom Resolution on a polygon bodies 
                         This value will be considered only when polygon body resolution is set to custom 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPolygonBodyResolutionCustomDistance
            (
                NXOpen::Expression * customDistance /** custom distance */ ,
                const std::vector<NXOpen::CAE::CAEBody *> & inPolygonBodies /** in polygon bodies */ 
            );
            /** Gets the distance for custom resolution on a polygon bodies.
                        This value will be null if polygon body resolution is not custom @return  customDistance will be nullptr if polygon body resolution is not null 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Expression * GetPolygonBodyResolutionCustomDistance
            (
                NXOpen::CAE::CAEBody * polygonBody /** polygon body */ 
            );
            /** Set Angle for Custom Resolution on a polygon body. 
                         This value will be considered only when polygon body resolution is set to custom 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPolygonBodyResolutionCustomAngle
            (
                NXOpen::Expression * customAngle /** custom angle */ ,
                const std::vector<NXOpen::CAE::CAEBody *> & inPolygonBodies /** in polygon bodies */ 
            );
            /** Gets the the angle for custom resolution on a polygon body @return  customAngle will be nullptr if polygon body resolution is not null 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Expression * GetPolygonBodyResolutionCustomAngle
            (
                NXOpen::CAE::CAEBody * polygonBody /** polygon body */ 
            );
            /** The creation of custom resolution automatic distance on a fem bodies
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Expression * AutomaticCustomDistance
            (
                const std::vector<NXOpen::Body *> & inSolidBodies /** in solid bodies */ 
            );
            /** The creation of custom resolution automatic distance
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Expression * AutomaticCustomDistanceFromPolygonBodies
            (
                const std::vector<NXOpen::CAE::CAEBody *> & inSolidBodies /** in solid bodies */ 
            );
            /** Find the polygon body that is built from the given cad solid body
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::CAEBody * FindPolygonBodyFromSolidBody
            (
                NXOpen::Body * body /** body */ 
            );


            /** Returns the geometry recipes belonging to the FEM. 
             <br>  Created in NX10.0.0.  <br>  
            */
            public: NXOpen::CAE::GeometryRecipeCollection *CaeGeometryRecipes();
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