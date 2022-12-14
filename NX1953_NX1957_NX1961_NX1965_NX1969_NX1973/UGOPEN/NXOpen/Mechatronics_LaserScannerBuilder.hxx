#ifndef NXOpen_MECHATRONICS_LASERSCANNERBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_LASERSCANNERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_LaserScannerBuilder.ja
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
#include <NXOpen/Mechatronics_CollisionShapeBuilder.hxx>
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
        class LaserScannerBuilder;
    }
    class Expression;
    namespace Mechatronics
    {
        class CollisionShapeBuilder;
    }
    class SelectNXObject;
    namespace Mechatronics
    {
        class _LaserScannerBuilderBuilder;
        class LaserScannerBuilderImpl;
        /**  @brief  Represents a @link NXOpen::Mechatronics::LaserScanner NXOpen::Mechatronics::LaserScanner@endlink  builder.  

           <br> To create a new instance of this class, use @link NXOpen::Mechatronics::LaserScannerCollection::CreateLaserScannerBuilder  NXOpen::Mechatronics::LaserScannerCollection::CreateLaserScannerBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  LaserScannerBuilder : public NXOpen::Mechatronics::CollisionShapeBuilder
        {
            private: LaserScannerBuilderImpl * m_laserscannerbuilder_impl;
            private: friend class  _LaserScannerBuilderBuilder;
            protected: LaserScannerBuilder();
            public: ~LaserScannerBuilder();
            /**Returns   @brief  the scanner body. This can be a @link NXOpen::Mechatronics::RigidBody NXOpen::Mechatronics::RigidBody@endlink  or @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink 
                    If there is a rigid body, then the scanner will move with the rigid body. 

              
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::SelectNXObject * ScannerBody
            (
            );
            /**Returns   @brief  the protective field range. The measure range of the 2D Laser Scanner. 

              
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Expression * Range
            (
            );
            /**Returns   @brief  the scanning angle. 

              
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Expression * ScanningAngle
            (
            );
            /**Returns   @brief  the angular resolution. 

              
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Expression * AngularResolution
            (
            );
            /**Returns   @brief  the divergence of beam. 

              
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Expression * Angle
            (
            );
            /**Returns   @brief  the scan cycle time. 

              
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Expression * CycleTime
            (
            );
            /**Returns   @brief  the name.  

              
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXString Name
            (
            );
            /**Sets   @brief  the name.  

              
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets   @brief  the name.  

              
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetName
            (
                const char * name /** name */ 
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
