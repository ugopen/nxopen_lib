#ifndef NXOpen_MECHATRONICS_COLLISIONSENSORBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_COLLISIONSENSORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_CollisionSensorBuilder.ja
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
#include <NXOpen/Mechatronics_CollisionShapeBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class CollisionSensorBuilder;
    }
    namespace Mechatronics
    {
        class CollisionShapeBuilder;
    }
    class NXObject;
    class SelectNXObjectList;
    namespace Mechatronics
    {
        class _CollisionSensorBuilderBuilder;
        class CollisionSensorBuilderImpl;
        /** Represents a @link NXOpen::Mechatronics::CollisionSensor NXOpen::Mechatronics::CollisionSensor@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Mechatronics::CollisionSensorCollection::CreateCollisionSensorBuilder  NXOpen::Mechatronics::CollisionSensorCollection::CreateCollisionSensorBuilder @endlink  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  CollisionSensorBuilder : public NXOpen::Mechatronics::CollisionShapeBuilder
        {
            /** the Trigger Shape Types. */
            public: enum CollisionShapeTypes
            {
                CollisionShapeTypesBox/** Box */,
                CollisionShapeTypesSphere/** Sphere */,
                CollisionShapeTypesLine/** Line */,
                CollisionShapeTypesCylinder/** Cylinder*/
            };

            /** the Trigger Shape Option. */
            public: enum ShapePropertiesOption
            {
                ShapePropertiesOptionAutomatic/** Automatic */,
                ShapePropertiesOptionUserDefined/** UserDefined */
            };

            private: CollisionSensorBuilderImpl * m_collisionsensorbuilder_impl;
            private: friend class  _CollisionSensorBuilderBuilder;
            protected: CollisionSensorBuilder();
            public: ~CollisionSensorBuilder();
            /**Returns  the geometries. This can be a @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink , @link NXOpen::Point NXOpen::Point@endlink 
                    , bodies and curves. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::SelectNXObjectList * Geometry
            (
            );
            /** Sets the geometries. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetGeometry
            (
                const std::vector<NXOpen::NXObject *> & geometries /** Input geometries*/
            );
            /**Returns  the collision shape type. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::CollisionSensorBuilder::CollisionShapeTypes CollisionShape
            (
            );
            /**Sets  the collision shape type. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetCollisionShape
            (
                NXOpen::Mechatronics::CollisionSensorBuilder::CollisionShapeTypes collisionShape /** collisionshape */ 
            );
            /**Returns  the trigger shape option. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::CollisionSensorBuilder::ShapePropertiesOption ShapeProperties
            (
            );
            /**Sets  the trigger shape option. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetShapeProperties
            (
                NXOpen::Mechatronics::CollisionSensorBuilder::ShapePropertiesOption shapeProperties /** shapeproperties */ 
            );
            /**Returns  the category. It should be between 0 and 16. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: int Category
            (
            );
            /**Sets  the category. It should be between 0 and 16. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetCategory
            (
                int category /** category */ 
            );
            /**Returns  the name. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the option of highlight on collision. If the highlight is true, then the sensor will
                    be highlighted when it is collided or triggered during simulation. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: bool HighlightOnCollision
            (
            );
            /**Sets  the option of highlight on collision. If the highlight is true, then the sensor will
                    be highlighted when it is collided or triggered during simulation. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetHighlightOnCollision
            (
                bool highlight /** highlight */ 
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
