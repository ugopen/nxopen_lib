#ifndef NXOpen_LINEWELDS_HXX_INCLUDED
#define NXOpen_LINEWELDS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineWelds.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        /** Specifies the weld standard */
        enum WeldStandard
        {
            WeldStandardAnsi/** ANSI standard */,
            WeldStandardDin/** DIN standard */,
            WeldStandardJis/** JIS standard */,
            WeldStandardIso/** ISO standard */,
            WeldStandardEskd/** ESKD standard */,
            WeldStandardGb/** GB standard */,
            WeldStandardLast/** Last enum value. Should not be used. */
        };

        /** Specifies the weld finish method */
        enum FinishMethod
        {
            FinishMethodNone/** Specifies no finishing method */,
            FinishMethodChipping/** Specifies chipping finish */,
            FinishMethodGrinding/** Specifies grinding finish */,
            FinishMethodHammering/** Specifies hammering finish */,
            FinishMethodMachining/** Specifies machining finish */,
            FinishMethodRolling/** Specifies rolling finish */,
            FinishMethodPeening/** Specifies peening finish */,
            FinishMethodLast/** Last enum value. Should not be used. */
        };

        /** Specifies the supplementary weld symbol  */
        enum SupplementarySymbol
        {
            SupplementarySymbolNone/** Specifies no supplementary weld symbol */,
            SupplementarySymbolConvex/** Specifies convex supplementary weld symbol */,
            SupplementarySymbolFlush/** Specifies flush supplementary weld symbol */,
            SupplementarySymbolConcave/** Specifies concave supplementary weld symbol */,
            SupplementarySymbolBlendedToes/** Specifies blended toes supplementary weld symbol */,
            SupplementarySymbolBackingStripPermanent/** Specifies backing strip permanent supplementary weld symbol */,
            SupplementarySymbolBackingStripRemovable/** Specifies backing strip removable supplementary weld symbol */,
            SupplementarySymbolLast/** Last enum value. Should not be used. */
        };

        /** Specifies the weld size letter code (ISO and DIN only) */
        enum SizeLetterCode
        {
            SizeLetterCodeNone/** Specifies no letter code */,
            SizeLetterCodeA/** Specifies size letter code "a" */,
            SizeLetterCodeC/** Specifies size letter code "c" */,
            SizeLetterCodeD/** Specifies size letter code "d" */,
            SizeLetterCodeS/** Specifies size letter code "s" */,
            SizeLetterCodeZ/** Specifies size letter code "z" */,
            SizeLetterCodeP/** Specifies size letter code "P" */,
            SizeLetterCodeLast/** Last enum value. Should not be used. */
        };

        /** Specifies the elementary weld symbol */
        enum Symbol
        {
            SymbolNone/** Speifies no weld symbol */,
            SymbolButtWithRaisedEdges/** Specifies butt weld with raised edges */,
            SymbolSingleFlange/** Specifiies single flange weld symbol (JIS only) */,
            SymbolSquareButt/** Specifies square butt weld symbol */,
            SymbolVButt/** Specifies V butt weld symbol */,
            SymbolVButtBroadRootFace/** Specifies V butt with broad root face weld symbol (ISO and DIN only) */,
            SymbolBevelButt/** Specifies bevel butt weld symbol */,
            SymbolBevelButtBroadRootFace/** Specifies bevel butt with broad root face weld symbol (ISO and DIN only) */,
            SymbolUButt/** Specifies U butt weld symbol */,
            SymbolJButt/** Specifies J buttt weld symbol */,
            SymbolFlareV/** Specifies flare V weld symbol */,
            SymbolFlareBevel/** Specifies flare bevel weld symbol */,
            SymbolFillet/** Specifies fillet weld symbol */,
            SymbolPlugSlot/** Specifies plug/slot weld symbol */,
            SymbolEdge/** Specifies edge weld symbol */,
            SymbolSpot/** Specifies spot weld symbol */,
            SymbolSeam/** Specfies seam weld symbol */,
            SymbolSteepFlankedV/** Specifies steep flanked V butt weld symbol (ISO and DIN only) */,
            SymbolSteepFlankedBevel/** Specifies steeep flanked bevel butt weld symbol ( ISO and DIN only) */,
            SymbolBacking/** Specifies backing weld symbol (only one side of reference line ) */,
            SymbolSurfaceJoint/** Specifies surface joint weld symbol (ISO and DIN only ) */,
            SymbolInclinedJoint/** Specifies inclined joint weld symbol */,
            SymbolFoldJoint/** Specifies fold joint weld symbol
                                                        (ISO and DIN only, only on one side of reference line) */,
            SymbolStud/** Specifies stud weld symbol (Arrow side only ) */,
            SymbolSurfacing/** Specifies surfacing weld symbol (ISO and DIN only) */,
            SymbolIntermittent/** Specifies intermittent weld symbol (ESKD only) */,
            SymbolBackingPlate/** Specifies backing plate weld symbol (GB only) */,
            SymbolLast/** Last enum value. Should not be used. */
        };

        /** Specifies the weld tail for the reference line */
        enum Tail
        {
            TailNone/** Specifies no tail */,
            TailFork/** Specifies fork tail */,
            TailBox/** Specifies box tail */,
            TailLast/** Last enum value. Should not be used. */
        };

        /** Specifies the weld identification line location (ISO and DIN only) */
        enum IdentificationLineLocation
        {
            IdentificationLineLocationNone/** Specifies no identification line */,
            IdentificationLineLocationTop/** Specifies identification line above the 
                                                                       reference line */,
            IdentificationLineLocationBottom/** Specifies identification line below the
                                                                          reference line */,
            IdentificationLineLocationLast/** Last enum value. Should not be used. */
        };

    }
}
#undef EXPORTLIBRARY
#endif
