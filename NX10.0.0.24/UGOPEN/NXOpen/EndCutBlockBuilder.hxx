#ifndef NXOpen_ENDCUTBLOCKBUILDER_HXX_INCLUDED
#define NXOpen_ENDCUTBLOCKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     EndCutBlockBuilder.ja
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
#include <NXOpen/EndCutBlockBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/SketchExpressionModifierBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class EndCutBlockBuilder;
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class SketchExpressionModifierBuilder;
    class _EndCutBlockBuilderBuilder;
    class EndCutBlockBuilderImpl;
    /** Represents a End Cut Block Builder. 
     <br>  Created in NX5.3.0.  <br>  
    */
    class NXOPENCPPEXPORT  EndCutBlockBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
    {
        /** Taper Type */
        public: enum TaperTypeOption
        {
            TaperTypeOptionTrim/** trim */ ,
            TaperTypeOptionExtend/** extend */ ,
            TaperTypeOptionTrimAndExtend/** trim and extend */ 
        };

        private: EndCutBlockBuilderImpl * m_endcutblockbuilder_impl;
        private: friend class  _EndCutBlockBuilderBuilder;
        protected: EndCutBlockBuilder();
        public: ~EndCutBlockBuilder();
        /**Returns  the end cut block 
         <br>  Created in NX5.0.3.  <br>  
         <br> License requirements : None */
        public: NXOpen::SketchExpressionModifierBuilder * SketchBlock
        (
        );
        /**Returns  the taperType 
         <br>  Created in NX5.0.3.  <br>  
         <br> License requirements : None */
        public: NXOpen::EndCutBlockBuilder::TaperTypeOption TaperType
        (
        );
        /**Sets  the taperType 
         <br>  Created in NX5.0.3.  <br>  
         <br> License requirements : nx_ship_concept ("Ship Concept") */
        public: void SetTaperType
        (
            NXOpen::EndCutBlockBuilder::TaperTypeOption taperType /** tapertype */ 
        );
        /**Returns  the angle 
         <br>  Created in NX5.0.3.  <br>  
         <br> License requirements : None */
        public: NXOpen::Expression * Angle
        (
        );
        /**Returns  the offset 
         <br>  Created in NX5.0.3.  <br>  
         <br> License requirements : None */
        public: NXOpen::Expression * Offset
        (
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
