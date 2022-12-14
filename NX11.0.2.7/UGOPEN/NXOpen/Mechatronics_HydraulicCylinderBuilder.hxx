#ifndef NXOpen_MECHATRONICS_HYDRAULICCYLINDERBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_HYDRAULICCYLINDERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_HydraulicCylinderBuilder.ja
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
#include <NXOpen/Mechatronics_HydraulicCylinderBuilder.hxx>
#include <NXOpen/Mechatronics_PhysicsConstraintBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class HydraulicCylinderBuilder;
    }
    class Expression;
    namespace Mechatronics
    {
        class PhysicsConstraintBuilder;
    }
    namespace Mechatronics
    {
        class SelectPhysicsJoint;
    }
    namespace Mechatronics
    {
        class _HydraulicCylinderBuilderBuilder;
        class HydraulicCylinderBuilderImpl;
        /**  @brief  Represents a @link NXOpen::Mechatronics::HydraulicCylinder NXOpen::Mechatronics::HydraulicCylinder@endlink  builder.  

           <br> To create a new instance of this class, use @link NXOpen::Mechatronics::HydraulicCylinderCollection::CreateHydraulicCylinderBuilder  NXOpen::Mechatronics::HydraulicCylinderCollection::CreateHydraulicCylinderBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  HydraulicCylinderBuilder : public NXOpen::Mechatronics::PhysicsConstraintBuilder
        {
            /**  @brief  the Rod types.  

              */
            public: enum OutputRodType
            {
                OutputRodTypeSingle/** single rod */,
                OutputRodTypeDouble/** double rod */
            };

            private: HydraulicCylinderBuilderImpl * m_hydrauliccylinderbuilder_impl;
            private: friend class  _HydraulicCylinderBuilderBuilder;
            protected: HydraulicCylinderBuilder();
            public: ~HydraulicCylinderBuilder();
            /**Returns   @brief  the Axis Joint. This can be a @link PhysicsJoint PhysicsJoint@endlink . 

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::SelectPhysicsJoint * AxisJoint
            (
            );
            /**Returns   @brief  the initial pressure of chamber A.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Expression * PressureA
            (
            );
            /**Returns   @brief  the initial pressure of chamber B.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Expression * PressureB
            (
            );
            /**Returns   @brief  the overall stroke length of the cylinder.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Expression * StrokeLength
            (
            );
            /**Returns   @brief  the diameter of the piston.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Expression * PistonDiameter
            (
            );
            /**Returns   @brief  the diameter of the piston rod.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Expression * PistonRodDiameter
            (
            );
            /**Returns   @brief  the rod type.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::HydraulicCylinderBuilder::OutputRodType RodType
            (
            );
            /**Sets   @brief  the rod type.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetRodType
            (
                NXOpen::Mechatronics::HydraulicCylinderBuilder::OutputRodType rodType /** rodtype */ 
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
