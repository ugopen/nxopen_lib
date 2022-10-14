#ifndef NXOpen_GEOMETRICUTILITIES_BOOLEANOPERATION_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_BOOLEANOPERATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_BooleanOperation.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class BooleanOperation;
    }
    class Body;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class _BooleanOperationBuilder;
        class BooleanOperationImpl;
        /** Represents a boolean operation .  
            
         <br>  Created in NX3.0.1.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  BooleanOperation : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Boolean operation type. */
            public: enum BooleanType
            {
                BooleanTypeCreate/** Create */,
                BooleanTypeUnite/** Unite */,
                BooleanTypeSubtract/** Subtract */,
                BooleanTypeIntersect/** Intersect */,
                BooleanTypeSew/** Sew */
            };

            private: BooleanOperationImpl * m_booleanoperation_impl;
            private: friend class  _BooleanOperationBuilder;
            protected: BooleanOperation();
            public: ~BooleanOperation();
            /**  Get the Boolean operation type and target body
                    
             <br>  @deprecated Deprecated in NX4.0.0.  Use @link GeometricUtilities::BooleanOperation::Type GeometricUtilities::BooleanOperation::Type@endlink  and @link GeometricUtilities::BooleanOperation::GetTargetBodies GeometricUtilities::BooleanOperation::GetTargetBodies@endlink  instead. <br>  

             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX4.0.0.  Use GeometricUtilities::BooleanOperation::Type and GeometricUtilities::BooleanOperation::GetTargetBodies instead.") void GetBooleanOperationAndBody
            (
                NXOpen::GeometricUtilities::BooleanOperation::BooleanType* type /** boolean type */,
                NXOpen::Body ** targetBody /** target body */
            );
            /**  Set the Boolean operation type and target body
                    
             <br>  @deprecated Deprecated in NX4.0.0.  Use @link GeometricUtilities::BooleanOperation::SetType GeometricUtilities::BooleanOperation::SetType@endlink  and @link GeometricUtilities::BooleanOperation::SetTargetBodies GeometricUtilities::BooleanOperation::SetTargetBodies@endlink  instead. <br>  

             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: NX_DEPRECATED("Deprecated in NX4.0.0.  Use GeometricUtilities::BooleanOperation::SetType and GeometricUtilities::BooleanOperation::SetTargetBodies instead.") void SetBooleanOperationAndBody
            (
                NXOpen::GeometricUtilities::BooleanOperation::BooleanType type /** boolean type */,
                NXOpen::Body * targetBody /** target body */
            );
            /**Returns   the boolean operation type
                    
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BooleanOperation::BooleanType Type
            (
            );
            /**Sets   the boolean operation type
                    
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetType
            (
                NXOpen::GeometricUtilities::BooleanOperation::BooleanType type /** boolean type */
            );
            /**  Get the target bodies 
                     @return  target bodies of boolean 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Body *> GetTargetBodies
            (
            );
            /**  Set the target bodies 
                    
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetTargetBodies
            (
                const std::vector<NXOpen::Body *> & targetBodies /**  target bodies of boolean */
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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