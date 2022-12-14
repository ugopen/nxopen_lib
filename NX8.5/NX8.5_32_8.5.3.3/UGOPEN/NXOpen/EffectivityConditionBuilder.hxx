#ifndef NXOpen_EFFECTIVITYCONDITIONBUILDER_HXX_INCLUDED
#define NXOpen_EFFECTIVITYCONDITIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     EffectivityConditionBuilder.ja
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
#include <NXOpen/BasicEffectivityBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/EffectivityConditionBuilder.hxx>
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
    class EffectivityConditionBuilder;
    class BasicEffectivityBuilder;
    class Builder;
    class _EffectivityConditionBuilderBuilder;
    class EffectivityConditionBuilderImpl;
    /** Represent a utility class to assign or edit discrete and range effectivity unit values in the
        context of a @link CollaborativeDesign CollaborativeDesign@endlink .
        Also provides method to apply all units or no units effectivity.
     <br> To create a new instance of this class, use @link BasePart::CreateEffectivityConditionBuilder  BasePart::CreateEffectivityConditionBuilder @endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    EffectivityType </td> <td> 
     
    Unit </td> </tr> 

    </table>  

     <br>  Created in NX8.5.0.  <br>  
    */
    class NXOPENCPPEXPORT  EffectivityConditionBuilder : public Builder
    {
        /** Specifies the effectivity type option */
        public: enum EffectivityConditionType
        {
            EffectivityConditionTypeUnit/** Discrete unit value */,
            EffectivityConditionTypeUnitRange/** Range unit values */
        };

        /** Specifies option for range effectivity value's toUnit. 
                This enumeration is valid only for the effectivity type @link EffectivityConditionBuilder::EffectivityConditionTypeUnitRange EffectivityConditionBuilder::EffectivityConditionTypeUnitRange@endlink 
             */
        public: enum ToUnitType
        {
            ToUnitTypeStockOut/** Sets stock out unit as toUnit effectivity range */,
            ToUnitTypeOpenEnd/** Sets open end unit as toUnit for effectivity range */
        };

        private: EffectivityConditionBuilderImpl * m_effectivityconditionbuilder_impl;
        private: friend class  _EffectivityConditionBuilderBuilder;
        protected: EffectivityConditionBuilder();
        public: ~EffectivityConditionBuilder();
        /**Returns  the effectivity type 
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::EffectivityConditionBuilder::EffectivityConditionType EffectivityType
        (
        );
        /**Sets  the effectivity type 
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: void SetEffectivityType
        (
            NXOpen::EffectivityConditionBuilder::EffectivityConditionType selectTypeEffectivity /** selecttypeeffectivity */ 
        );
        /** Adds specified discrete or range effectivity values to the builder. 
                If the input is a single discrete unit value then pass fromUnit and toUnit as same.
            
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: void AddUnitEffectivity
        (
            int fromUnit /** fromunit */ ,
            int toUnit /** tounit */ 
        );
        /** Adds specified range effectivity value to the builder. 
                This method can be used to set Stock out or Open End as effectivity range's to unit by passing 
                @link EffectivityConditionBuilder::ToUnitTypeStockOut EffectivityConditionBuilder::ToUnitTypeStockOut@endlink  or @link EffectivityConditionBuilder::ToUnitTypeOpenEnd EffectivityConditionBuilder::ToUnitTypeOpenEnd@endlink  respectively.
                This method is valid only for effectivity type @link EffectivityConditionBuilder::EffectivityConditionTypeUnitRange EffectivityConditionBuilder::EffectivityConditionTypeUnitRange@endlink .
            
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: void AddUnitEffectivity
        (
            int fromUnit /** fromunit */ ,
            NXOpen::EffectivityConditionBuilder::ToUnitType toUnitType /** tounittype */ 
        );
        /** Removes specified existing range effectivity values from the builder. 
                To remove single discrete unit value, pass fromUnit and toUnit as same.
            
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: void RemoveUnitEffectivity
        (
            int fromUnit /** fromunit */ ,
            int toUnit /** tounit */ 
        );
        /** Removes specified existing range unit effectivity which has toUnit value either @link EffectivityConditionBuilder::ToUnitTypeStockOut EffectivityConditionBuilder::ToUnitTypeStockOut@endlink  
                or @link EffectivityConditionBuilder::ToUnitTypeOpenEnd EffectivityConditionBuilder::ToUnitTypeOpenEnd@endlink  repectively. 
            
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: void RemoveUnitEffectivity
        (
            int fromUnit /** fromunit */ ,
            NXOpen::EffectivityConditionBuilder::ToUnitType toUnitType /** tounittype */ 
        );
        /** Registers the @link BasicEffectivityBuilder BasicEffectivityBuilder@endlink  to make sure its effectivity formula 
                string is always updated and in sync with the effectivity formula string of this class.
                This method should be called before the commit method is invoked.
            
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: void RegisterBasicEffectivityBuilder
        (
            NXOpen::BasicEffectivityBuilder * beBuilder /** bebuilder */ 
        );
        /**Returns  the string representation of effectivity 
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: NXString EffectivityFormula
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
