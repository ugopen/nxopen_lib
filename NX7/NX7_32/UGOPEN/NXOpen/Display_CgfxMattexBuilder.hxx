#ifndef NXOpen_DISPLAY_CGFXMATTEXBUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_CGFXMATTEXBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_CgfxMattexBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Display_CgfxMattexBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Display
    {
        class CgfxMattexBuilder;
    }
    class Builder;
    class NXObject;
    namespace Display
    {
        class _CgfxMattexBuilderBuilder;
        /** Represents a @link Display::CgfxMattex  Display::CgfxMattex @endlink  builder  <br>  <br> */
        class NXOPENCPPEXPORT CgfxMattexBuilder : public Builder
        {
            /** The technique is an index to a technique name in a list found in the CgFX file.  There is is unknown until the CgFX file is loaded. */
            public: enum Technique
            {
                TechniqueBase/**  place holder for variable technique list */
            };

            /** The texture space type indicates the type of texture space to use for CgFX shader */
            public: enum TextureSpace
            {
                TextureSpaceDefaultUv/** scale 1, 0 offset uv texture space */,
                TextureSpaceEdited/** the one edited using the material texture dialog*/
            };

            private: friend class  _CgfxMattexBuilderBuilder;
            protected: CgfxMattexBuilder();
            /**Returns  the material name  <br> License requirements : None */
            public: NXString MaterialName
            (
            );
            /**Sets  the material name  <br> License requirements : None */
            public: void SetMaterialName
            (
                const NXString & materialName /** materialname */ 
            );
            /**Returns  the display techniques  <br> License requirements : None */
            public: NXOpen::Display::CgfxMattexBuilder::Technique TechniqueType
            (
            );
            /**Sets  the display techniques  <br> License requirements : None */
            public: void SetTechniqueType
            (
                NXOpen::Display::CgfxMattexBuilder::Technique technique /** technique */ 
            );
            /**  Returns the attribute values @return   <br> License requirements : None */
            public: std::vector<NXOpen::NXObject *> GetAttributeValues
            (
            );
            /** Sets the attribute values <br> License requirements : None */
            public: void SetAttributeValues
            (
                const std::vector<NXOpen::NXObject *> & attributeValues /** attribute values */
            );
            /**Returns  the texture space type <br> License requirements : None */
            public: NXOpen::Display::CgfxMattexBuilder::TextureSpace TextureSpaceType
            (
            );
            /**Sets  the texture space type <br> License requirements : None */
            public: void SetTextureSpaceType
            (
                NXOpen::Display::CgfxMattexBuilder::TextureSpace textureSpaceType /** texture space type */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
