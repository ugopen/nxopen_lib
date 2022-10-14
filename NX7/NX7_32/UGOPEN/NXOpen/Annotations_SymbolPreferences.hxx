#ifndef NXOpen_ANNOTATIONS_SYMBOLPREFERENCES_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_SYMBOLPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_SymbolPreferences.ja
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
#include <NXOpen/Annotations.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class SymbolPreferences;
    }
    namespace Annotations
    {
        /** Represents symbol preferences */
        class NXOPENCPPEXPORT SymbolPreferences : public TransientObject
        {
            public: explicit SymbolPreferences(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~SymbolPreferences();
            /**Returns  the id symbol size  <br> License requirements : None */
            public: double IdSymbolSize
            (
            );
            /**Sets  the id symbol size  <br> License requirements : None */
            public: void SetIdSymbolSize
            (
                double idSymbolSize /** id symbol size */ 
            );
            /** Returns the id symbol color, font, and width  @return   <br> License requirements : None */
            public: NXOpen::Annotations::LineCfw GetIdSymbolCfw
            (
            );
            /** Sets the id symbol color, font, and width   <br> License requirements : None */
            public: void SetIdSymbolCfw
            (
                const NXOpen::Annotations::LineCfw & idSymbolCfw /** id symbol cfw */ 
            );
            /** Returns the user defined symbol color, font, and width   @return   <br> License requirements : None */
            public: NXOpen::Annotations::LineCfw GetUserDefinedSymbolCfw
            (
            );
            /** Sets the user defined symbol color, font, and width   <br> License requirements : None */
            public: void SetUserDefinedSymbolCfw
            (
                const NXOpen::Annotations::LineCfw & userDefinedSymbolCfw /** user defined symbol cfw */ 
            );
            /** Returns the centerline symbol color, font, and width   @return   <br> License requirements : None */
            public: NXOpen::Annotations::LineCfw GetCenterlineSymbolCfw
            (
            );
            /** Sets the centerline symbol color, font, and width   <br> License requirements : None */
            public: void SetCenterlineSymbolCfw
            (
                const NXOpen::Annotations::LineCfw & centerlineSymbolCfw /** centerline symbol cfw */ 
            );
            /** Returns the intersection symbol color, font, and width   @return   <br> License requirements : None */
            public: NXOpen::Annotations::LineCfw GetIntersectionSymbolCfw
            (
            );
            /** Sets the intersection symbol color, font, and width   <br> License requirements : None */
            public: void SetIntersectionSymbolCfw
            (
                const NXOpen::Annotations::LineCfw & intersectionSymbolCfw /** intersection symbol cfw */ 
            );
            /** Returns the target symbol color, font, and width   @return   <br> License requirements : None */
            public: NXOpen::Annotations::LineCfw GetTargetSymbolCfw
            (
            );
            /** Sets the target symbol color, font, and width   <br> License requirements : None */
            public: void SetTargetSymbolCfw
            (
                const NXOpen::Annotations::LineCfw & targetSymbolCfw /** target symbol cfw */ 
            );
            /** Returns the gdt symbol color, font, and width   @return   <br> License requirements : None */
            public: NXOpen::Annotations::LineCfw GetGdtSymbolCfw
            (
            );
            /** Sets the gdt symbol color, font, and width   <br> License requirements : None */
            public: void SetGdtSymbolCfw
            (
                const NXOpen::Annotations::LineCfw & gdtSymbolCfw /** gdt symbol cfw */ 
            );
            /** Returns the weld symbol color, font, and width   @return   <br> License requirements : None */
            public: NXOpen::Annotations::LineCfw GetWeldSymbolCfw
            (
            );
            /** Sets the weld symbol color, font, and width   <br> License requirements : None */
            public: void SetWeldSymbolCfw
            (
                const NXOpen::Annotations::LineCfw & weldSymbolCfw /** weld symbol cfw */ 
            );
            /** Returns the weld line gap   @return   <br> License requirements : None */
            public: double GetWeldLineGap
            (
            );
            /** Sets the weld symbol line gap  <br> License requirements : None */
            public: void SetWeldLineGap
            (
                double lineGap /** linegap */ 
            );
            /** Returns the weld space factor  @return   <br> License requirements : None */
            public: double GetWeldSpaceFactor
            (
            );
            /** Sets the weld symbol space factor  <br> License requirements : None */
            public: void SetWeldSpaceFactor
            (
                double spaceFactor /** spacefactor */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif