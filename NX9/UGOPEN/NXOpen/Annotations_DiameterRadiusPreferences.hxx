#ifndef NXOpen_ANNOTATIONS_DIAMETERRADIUSPREFERENCES_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DIAMETERRADIUSPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DiameterRadiusPreferences.ja
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
#include <NXOpen/Dimensions.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class DiameterRadiusPreferences;
    }
    namespace Annotations
    {
    }
    namespace Annotations
    {
        class DiameterRadiusPreferencesImpl;
        /** Represents diameter and radius preferences 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  DiameterRadiusPreferences : public TransientObject
        {
            private: DiameterRadiusPreferencesImpl * m_diameterradiuspreferences_impl;
            /// \cond NX_NO_DOC 
            public: explicit DiameterRadiusPreferences(void *ptr);
            /// \endcond 
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~DiameterRadiusPreferences();
            /**Returns  the diameter symbol 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DiameterSymbol DiameterSymbol
            (
            );
            /**Sets  the diameter symbol 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDiameterSymbol
            (
                NXOpen::Annotations::DiameterSymbol symbol /** New diameter symbol */
            );
            /**Returns  the symbol text for user defined diameter symbol 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DiameterSymbolText
            (
            );
            /**Sets  the symbol text for user defined diameter symbol 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDiameterSymbolText
            (
                const NXString & symbolText /** New symbol text */
            );
            /**Sets  the symbol text for user defined diameter symbol 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            void SetDiameterSymbolText
            (
                const char * symbolText /** New symbol text */
            );
            /**Returns  the radius symbol 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::RadiusSymbol RadiusSymbol
            (
            );
            /**Sets  the radius symbol 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRadiusSymbol
            (
                NXOpen::Annotations::RadiusSymbol symbol /** New radius symbol */
            );
            /**Returns  the symbol text for user defined radius symbol 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXString RadiusSymbolText
            (
            );
            /**Sets  the symbol text for user defined radius symbol 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRadiusSymbolText
            (
                const NXString & symbolText /** New symbol text */
            );
            /**Sets  the symbol text for user defined radius symbol 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            void SetRadiusSymbolText
            (
                const char * symbolText /** New symbol text */
            );
            /**Returns  the diameter/radius symbol placement relative to the dimension text 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DiameterRadiusSymbolPlacement SymbolPlacement
            (
            );
            /**Sets  the diameter/radius symbol placement relative to the dimension text 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSymbolPlacement
            (
                NXOpen::Annotations::DiameterRadiusSymbolPlacement symbolPlacement /** New symbol placement relative to dimension text */
            );
            /**Returns  the distance between diameter/radius symbol and dimension text 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: double DistanceBetweenSymbolAndDimensionText
            (
            );
            /**Sets  the distance between diameter/radius symbol and dimension text 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDistanceBetweenSymbolAndDimensionText
            (
                double symbolToDimensionTextDistance /** New distance between symbol and dimension text */
            );
            /**Returns  the leader stub relative to diameter/radius dimension text 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::Annotations::DimensionPreferences::TextPosition NXOpen::Annotations::DimensionPreferences::TextPosition@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::Annotations::DimensionPreferences::TextPosition instead.") NXOpen::Annotations::DiameterRadiusLeaderStub LeaderStub
            (
            );
            /**Sets  the leader stub relative to diameter/radius dimension text 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::Annotations::DimensionPreferences::SetTextPosition NXOpen::Annotations::DimensionPreferences::SetTextPosition@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::Annotations::DimensionPreferences::SetTextPosition instead.") void SetLeaderStub
            (
                NXOpen::Annotations::DiameterRadiusLeaderStub leaderStub /** New leader stub relative to dimension text */
            );
            /**Returns  the interior angle for folded radius type dimension 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: double FoldedRadiusAngle
            (
            );
            /**Sets  the interior angle for folded radius type dimension 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFoldedRadiusAngle
            (
                double foldedRadiusAngle /** New folded radius angle */
            );
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