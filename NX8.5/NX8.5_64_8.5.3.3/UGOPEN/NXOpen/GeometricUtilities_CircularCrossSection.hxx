#ifndef NXOpen_GEOMETRICUTILITIES_CIRCULARCROSSSECTION_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_CIRCULARCROSSSECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_CircularCrossSection.ja
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
#include <NXOpen/GeometricUtilities_LawBuilder.hxx>
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
        class CircularCrossSection;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class LawBuilder;
    }
    namespace GeometricUtilities
    {
        /** This enum represents the radius options */
        enum RadiusMethod
        {
            RadiusMethodConstant/** Constant */,
            RadiusMethodLaw/** Control by law */,
            RadiusMethodTangency/** Control by tangency */
        };

    }
    namespace GeometricUtilities
    {
        class _CircularCrossSectionBuilder;
        class CircularCrossSectionImpl;
        /** Represents a circular section data for face blend. 
            
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  CircularCrossSection : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: CircularCrossSectionImpl * m_circularcrosssection_impl;
            private: friend class  _CircularCrossSectionBuilder;
            protected: CircularCrossSection();
            public: ~CircularCrossSection();
            /**Returns  the radius for the circular section with face blend
                
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Radius
            (
            );
            /** Sets a radius for the circular section with face blend.
                
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRadius
            (
                const NXString & radius /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets a radius for the circular section with face blend.
                
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetRadius
            (
                const char * radius /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the radius option for the circular section with face blend
                
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::RadiusMethod RadiusOption
            (
            );
            /**Sets  the radius option for the circular section with face blend
                
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRadiusOption
            (
                NXOpen::GeometricUtilities::RadiusMethod method /** method */ 
            );
            /**Returns  the Law builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LawBuilder * LawControl
            (
            );
            /** Sets a constant radius for the law control of the circular section with face blend.
                
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetLawControlConstantRadius
            (
                const NXString & radius /** The value to be set */
            );
            /** Sets a constant radius for the law control of the circular section with face blend.
                
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetLawControlConstantRadius
            (
                const char * radius /** The value to be set */
            );
            /** Sets a start radius for the law control of the circular section with face blend.
                
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetLawControlStartRadius
            (
                const NXString & radius /** The value to be set */
            );
            /** Sets a start radius for the law control of the circular section with face blend.
                
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetLawControlStartRadius
            (
                const char * radius /** The value to be set */
            );
            /** Sets a end radius for the law control of the circular section with face blend.
                
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetLawControlEndRadius
            (
                const NXString & radius /** The value to be set */
            );
            /** Sets a end radius for the law control of the circular section with face blend.
                
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetLawControlEndRadius
            (
                const char * radius /** The value to be set */
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