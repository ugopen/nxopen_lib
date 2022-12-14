#ifndef NXOpen_FEATURES_OFFSETSURFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_OFFSETSURFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_OffsetSurfaceBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ugmath.hxx>
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
        class OffsetSurfaceBuilder;
    }
    class Expression;
    class Face;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class FaceSetOffset;
    }
    namespace GeometricUtilities
    {
        class FaceSetOffsetList;
    }
    class ObjectList;
    namespace Features
    {
        class _OffsetSurfaceBuilderBuilder;
        class OffsetSurfaceBuilderImpl;
        /** This class represents a offset surface builder, used for creating or editing an
               offset surface feature. The offset surface feature allows different face sets to
               be offset by different distances. Inputs to this class can be convergent objects.
              <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateOffsetSurfaceBuilder  NXOpen::Features::FeatureCollection::CreateOffsetSurfaceBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        ApproxOption </term> <description> 
         
        False </description> </item> 

        <item><term> 
         
        OutputOption </term> <description> 
         
        OneFeatureForConnectedFaces </description> </item> 

        <item><term> 
         
        PartialOption </term> <description> 
         
        False </description> </item> 

        <item><term> 
         
        StepOption </term> <description> 
         
        True </description> </item> 

        </list> 

         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  OffsetSurfaceBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Represents the type of output option. The faces to be offset can be disconnected 
                   and also from multiple bodies. If either is the case, then multiple features are created.
                   For deciding whether there should be one feature for each topologically connected set of
                   faces or one feature for each face selected the enum below has been provided */
            public: enum OutputOptionType
            {
                OutputOptionTypeOneFeatureForConnectedFaces/** one feature for connected faces */ ,
                OutputOptionTypeOneFeatureForEachFace/** one feature for each face */ ,
                OutputOptionTypeOneFeatureForAllFaces/** one feature for all faces */ 
            };

            /** Represents the type of orientation method. This is applicable only if the output
                   output is @link NXOpen::Features::OffsetSurfaceBuilder::OutputOptionTypeOneFeatureForEachFace NXOpen::Features::OffsetSurfaceBuilder::OutputOptionTypeOneFeatureForEachFace@endlink . 
                   The first enum value implies that the offset direction will be that of the surface normal whereas the
                   second enum value implies that am interior position will be specified and the offset direction
                   will be away from this point */
            public: enum OrientationMethodType
            {
                OrientationMethodTypeUseExistingNormals/** use existing normals */ ,
                OrientationMethodTypeSpecifyInteriorPosition/** specify interior position */ 
            };

            private: OffsetSurfaceBuilderImpl * m_offsetsurfacebuilder_impl;
            private: friend class  _OffsetSurfaceBuilderBuilder;
            protected: OffsetSurfaceBuilder();
            public: ~OffsetSurfaceBuilder();
            /**Returns  the list of face sets. Each element defines a set of faces, and an offset distance applied to those faces.
                 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::FaceSetOffsetList * FaceSets
            (
            );
            /**Sets  the offset surface output option based on the enum @link NXOpen::Features::OffsetSurfaceBuilder::OutputOptionType NXOpen::Features::OffsetSurfaceBuilder::OutputOptionType@endlink 
                 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOutputOption
            (
                NXOpen::Features::OffsetSurfaceBuilder::OutputOptionType outputOption /** Output option */
            );
            /**Returns  the offset surface output option based on the enum @link NXOpen::Features::OffsetSurfaceBuilder::OutputOptionType NXOpen::Features::OffsetSurfaceBuilder::OutputOptionType@endlink 
                 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::OffsetSurfaceBuilder::OutputOptionType OutputOption
            (
            );
            /**Sets  the option to create approximate offset surface if the offset surface has 
                   self-intersections.
                 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetApproxOption
            (
                bool approxOption /** Approximate offset option */
            );
            /**Returns  the option to create approximate offset surface if the offset surface has 
                   self-intersections.
                 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool ApproxOption
            (
            );
            /**Sets  the offset surface allow step boundaries option. If this option is true 
                   then side faces will be created along any smooth edge between a face 
                   which is offset and one which is not.
                 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetStepOption
            (
                bool stepOption /** Allow step boundaries option */
            );
            /**Returns  the offset surface allow step boundaries option. If this option is true 
                   then side faces will be created along any smooth edge between a face 
                   which is offset and one which is not.
                 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool StepOption
            (
            );
            /**Returns  the offset surface tolerance
                
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: double Tolerance
            (
            );
            /**Sets  the offset surface tolerance
                
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTolerance
            (
                double tolerance /** Tolerance */
            );
            /** Sets the orientation method 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOrientationMethod
            (
                NXOpen::Features::OffsetSurfaceBuilder::OrientationMethodType orientationMethod /** Orientation method */
            );
            /** Returns the offset surface orientation method based on the @link NXOpen::Features::OffsetSurfaceBuilder::OutputOptionType NXOpen::Features::OffsetSurfaceBuilder::OutputOptionType@endlink 
                  @return  Orientation method 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::OffsetSurfaceBuilder::OrientationMethodType GetOrientationMethod
            (
            );
            /** Sets the offset surface interior position for specify interior position method. This allows
                 *  the specified faces to be offset away from the interior position.
                 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetInteriorPosition
            (
                const NXOpen::Point3d & point /** Interior position for specify interior position method */
            );
            /** Gets the offset surface interior position for specify interior position method. 
                  @return  Interior position for specify interior position method 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d GetInteriorPosition
            (
            );
            /** Gets the list of face sets
                  @return  Face set list
             <br>  @deprecated Deprecated in NX5.0.0.  Use @link NXOpen::Features::OffsetSurfaceBuilder::FaceSets NXOpen::Features::OffsetSurfaceBuilder::FaceSets@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX5.0.0.  Use NXOpen::Features::OffsetSurfaceBuilder::FaceSets instead.") NXOpen::ObjectList * GetFaceSetList
            (
            );
            /** Gets the face sets. A face set is a combination of a face collector and an offset
                   distance.
                  @return  Face set list
             <br>  @deprecated Deprecated in NX5.0.0.  Use @link NXOpen::Features::OffsetSurfaceBuilder::FaceSets NXOpen::Features::OffsetSurfaceBuilder::FaceSets@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX5.0.0.  Use NXOpen::Features::OffsetSurfaceBuilder::FaceSets instead.") std::vector<NXOpen::GeometricUtilities::FaceSetOffset *> GetFaceSets
            (
            );
            /** Deletes a face set at the specified index from the face set list
                 
             <br>  @deprecated Deprecated in NX5.0.0.  Use @link NXOpen::Features::OffsetSurfaceBuilder::FaceSets NXOpen::Features::OffsetSurfaceBuilder::FaceSets@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NX_DEPRECATED("Deprecated in NX5.0.0.  Use NXOpen::Features::OffsetSurfaceBuilder::FaceSets instead.") void DeleteFaceSet
            (
                int index /** Index of face set to be deleted */
            );
            /** Finds and returns a face set at the specified index from the face set list
                  @return  Face set returned
             <br>  @deprecated Deprecated in NX5.0.0.  Use @link NXOpen::Features::OffsetSurfaceBuilder::FaceSets NXOpen::Features::OffsetSurfaceBuilder::FaceSets@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NX_DEPRECATED("Deprecated in NX5.0.0.  Use NXOpen::Features::OffsetSurfaceBuilder::FaceSets instead.") NXOpen::GeometricUtilities::FaceSetOffset * FindFaceSet
            (
                int index /** Index of face set to be returned */
            );
            /** Adds face sets to the face set list
                 
             <br>  @deprecated Deprecated in NX5.0.0.  Use @link NXOpen::Features::OffsetSurfaceBuilder::FaceSets NXOpen::Features::OffsetSurfaceBuilder::FaceSets@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NX_DEPRECATED("Deprecated in NX5.0.0.  Use NXOpen::Features::OffsetSurfaceBuilder::FaceSets instead.") void AddFaceSets
            (
                const std::vector<NXOpen::GeometricUtilities::FaceSetOffset *> & faceSets /** Face set list*/
            );
            /**Returns  the option to pursue a partial offset result
                
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool PartialOption
            (
            );
            /**Sets  the option to pursue a partial offset result
                
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPartialOption
            (
                bool partialOption /** partialoption */ 
            );
            /**Returns  the maximum excluded objects during partial offset. If the excluded objects reach this number, the partial offset will stop.
                 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int MaximumExcludedObjects
            (
            );
            /**Sets  the maximum excluded objects during partial offset. If the excluded objects reach this number, the partial offset will stop.
                 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetMaximumExcludedObjects
            (
                int maximumExcludedObjects /** Maximum excluded objects */
            );
            /**Returns  the option to remove problem vertices
                
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveProblemVerticesOption
            (
            );
            /**Sets  the option to remove problem vertices
                
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRemoveProblemVerticesOption
            (
                bool removeProblemVerticesOption /** removeproblemverticesoption */ 
            );
            /**Returns  the radius for error vertex excision during partial offset
                
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Radius
            (
            );
            /** Get error faces
                 @return  Error faces
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Face *> GetErrorFaces
            (
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
