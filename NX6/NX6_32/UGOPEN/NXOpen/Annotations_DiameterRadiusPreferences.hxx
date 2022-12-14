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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Dimensions.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** Represents diameter and radius preferences */
        class NXOPENCPPEXPORT DiameterRadiusPreferences : public TransientObject
        {
            public: explicit DiameterRadiusPreferences(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~DiameterRadiusPreferences();
            /**Returns  the diameter symbol  <br> License requirements : None */
            public: NXOpen::Annotations::DiameterSymbol DiameterSymbol
            (
            );
            /**Sets  the diameter symbol  <br> License requirements : None */
            public: void SetDiameterSymbol
            (
                NXOpen::Annotations::DiameterSymbol symbol /** New diameter symbol */
            );
            /**Returns  the symbol text for user defined diameter symbol  <br> License requirements : None */
            public: NXString DiameterSymbolText
            (
            );
            /**Sets  the symbol text for user defined diameter symbol  <br> License requirements : None */
            public: void SetDiameterSymbolText
            (
                const NXString & symbolText /** New symbol text */
            );
            /**Returns  the radius symbol  <br> License requirements : None */
            public: NXOpen::Annotations::RadiusSymbol RadiusSymbol
            (
            );
            /**Sets  the radius symbol  <br> License requirements : None */
            public: void SetRadiusSymbol
            (
                NXOpen::Annotations::RadiusSymbol symbol /** New radius symbol */
            );
            /**Returns  the symbol text for user defined radius symbol  <br> License requirements : None */
            public: NXString RadiusSymbolText
            (
            );
            /**Sets  the symbol text for user defined radius symbol  <br> License requirements : None */
            public: void SetRadiusSymbolText
            (
                const NXString & symbolText /** New symbol text */
            );
            /**Returns  the diameter/radius symbol placement relative to the dimension text  <br> License requirements : None */
            public: NXOpen::Annotations::DiameterRadiusSymbolPlacement SymbolPlacement
            (
            );
            /**Sets  the diameter/radius symbol placement relative to the dimension text  <br> License requirements : None */
            public: void SetSymbolPlacement
            (
                NXOpen::Annotations::DiameterRadiusSymbolPlacement symbolPlacement /** New symbol placement relative to dimension text */
            );
            /**Returns  the distance between diameter/radius symbol and dimension text  <br> License requirements : None */
            public: double DistanceBetweenSymbolAndDimensionText
            (
            );
            /**Sets  the distance between diameter/radius symbol and dimension text  <br> License requirements : None */
            public: void SetDistanceBetweenSymbolAndDimensionText
            (
                double symbolToDimensionTextDistance /** New distance between symbol and dimension text */
            );
            /**Returns  the leader stub relative to diameter/radius dimension text  <br> License requirements : None */
            public: NXOpen::Annotations::DiameterRadiusLeaderStub LeaderStub
            (
            );
            /**Sets  the leader stub relative to diameter/radius dimension text  <br> License requirements : None */
            public: void SetLeaderStub
            (
                NXOpen::Annotations::DiameterRadiusLeaderStub leaderStub /** New leader stub relative to dimension text */
            );
            /**Returns  the interior angle for folded radius type dimension  <br> License requirements : None */
            public: double FoldedRadiusAngle
            (
            );
            /**Sets  the interior angle for folded radius type dimension  <br> License requirements : None */
            public: void SetFoldedRadiusAngle
            (
                double foldedRadiusAngle /** New folded radius angle */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
