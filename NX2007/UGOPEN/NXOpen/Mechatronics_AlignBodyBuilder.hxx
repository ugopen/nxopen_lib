#ifndef NXOpen_MECHATRONICS_ALIGNBODYBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_ALIGNBODYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_AlignBodyBuilder.ja
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
#include <NXOpen/Builder.hxx>
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
        class AlignBodyBuilder;
    }
    class Builder;
    class CoordinateSystem;
    class Expression;
    namespace Mechatronics
    {
        class SelectRigidBody;
    }
    class NXObject;
    class Point;
    namespace Mechatronics
    {
        class _AlignBodyBuilderBuilder;
        class AlignBodyBuilderImpl;
        /**  @brief  Represents a @link NXOpen::Mechatronics::AlignBody NXOpen::Mechatronics::AlignBody@endlink  builder.  

          <br> To create a new instance of this class, use @link NXOpen::Mechatronics::AlignBodyCollection::CreateAlignBodyBuilder  NXOpen::Mechatronics::AlignBodyCollection::CreateAlignBodyBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  AlignBodyBuilder : public NXOpen::Builder
        {
            /**  @brief  the Snap role types.  

             */
            public: enum RoleType
            {
                RoleTypeSource/** Source */,
                RoleTypeTarget/** Target */
            };

            private: AlignBodyBuilderImpl * m_alignbodybuilder_impl;
            private: friend class  _AlignBodyBuilderBuilder;
            protected: AlignBodyBuilder();
            public: ~AlignBodyBuilder();
            /**Returns   @brief  the rigid body which snap point attaches on. This should be a @link NXOpen::Mechatronics::RigidBody NXOpen::Mechatronics::RigidBody@endlink   

              
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::SelectRigidBody * AttachBody
            (
            );
            /**  @brief  Sets the attached rigid body.  

             
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetAttachbody
            (
                NXOpen::NXObject * rigid /** rigid */ 
            );
            /**Returns   @brief  the positioning of snap point.  

             
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Point * AttachPoint
            (
            );
            /**Sets   @brief  the positioning of snap point.  

             
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetAttachPoint
            (
                NXOpen::Point * attachPoint /** attachpoint */ 
            );
            /**Returns   @brief  the orientation of snap point.  

             
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::CoordinateSystem * Orientation
            (
            );
            /**Sets   @brief  the orientation of snap point.  

             
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetOrientation
            (
                NXOpen::CoordinateSystem * orientation /** orientation */ 
            );
            /**Returns   @brief  the proximity for distance detection.  

             
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Expression * Proximity
            (
            );
            /**Returns   @brief  the role type  

             
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::AlignBodyBuilder::RoleType SnapRole
            (
            );
            /**Sets   @brief  the role type  

             
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetSnapRole
            (
                NXOpen::Mechatronics::AlignBodyBuilder::RoleType roleType /** roletype */ 
            );
            /**Returns   @brief  the category. It should be an integer bigger or equal to zero.  

             
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: int Category
            (
            );
            /**Sets   @brief  the category. It should be an integer bigger or equal to zero.  

             
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetCategory
            (
                int category /** category */ 
            );
            /**Returns   @brief  the junction name converted from MTB.  

              
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXString JunctionName
            (
            );
            /**Sets   @brief  the junction name converted from MTB.  

              
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetJunctionName
            (
                const NXString & junction /** junction */ 
            );
            /**Sets   @brief  the junction name converted from MTB.  

              
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetJunctionName
            (
                const char * junction /** junction */ 
            );
            /**Returns   @brief  the name.  

              
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXString Name
            (
            );
            /**Sets   @brief  the name.  

              
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets   @brief  the name.  

              
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns   @brief  the enable bond  

              
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: bool EnableBond
            (
            );
            /**Sets   @brief  the enable bond  

              
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetEnableBond
            (
                bool enable /** enable */ 
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