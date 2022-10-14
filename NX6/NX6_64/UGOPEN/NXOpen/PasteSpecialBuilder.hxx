#ifndef NXOpen_PASTESPECIALBUILDER_HXX_INCLUDED
#define NXOpen_PASTESPECIALBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PasteSpecialBuilder.ja
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
#include <NXOpen/PasteSpecialBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class PasteSpecialBuilder;
    class Builder;
    class CoordinateSystem;
    class _PasteSpecialBuilderBuilder;
    /**
    Represents a @link PasteSpecialBuilder PasteSpecialBuilder@endlink 
     <br> To create a new instance of this class, use @link ClipboardOperationsManager::CreatePasteSpecialBuilder ClipboardOperationsManager::CreatePasteSpecialBuilder@endlink  <br> 
    Default values:
    DestinationOpt: Csys
    LayerOpt: Work
    */
    class NXOPENCPPEXPORT PasteSpecialBuilder : public Builder
    {
        /** This enum represents the paste ppecial destination coordinate system options */
        public: enum DestinationOption
        {
            DestinationOptionWcs/** wcs */ ,
            DestinationOptionCsys/** csys */ 
        };

        /** This enum represents the paste special layer options */
        public: enum LayerOption
        {
            LayerOptionWork/** work */ ,
            LayerOptionOriginal/** original */ ,
            LayerOptionSpecified/** specified */ 
        };

        private: friend class  _PasteSpecialBuilderBuilder;
        protected: PasteSpecialBuilder();
        /**Returns  the destination coordinate system option  <br> License requirements : None */
        public: NXOpen::PasteSpecialBuilder::DestinationOption DestinationOpt
        (
        );
        /**Sets  the destination coordinate system option  <br> License requirements : None */
        public: void SetDestinationOpt
        (
            NXOpen::PasteSpecialBuilder::DestinationOption destinationOpt /** destinationopt */ 
        );
        /**Returns  the destination coordinate system  <br> License requirements : None */
        public: NXOpen::CoordinateSystem * Csys
        (
        );
        /**Sets  the destination coordinate system  <br> License requirements : None */
        public: void SetCsys
        (
            NXOpen::CoordinateSystem * csys /** csys */ 
        );
        /**Returns  the layer option  <br> License requirements : None */
        public: NXOpen::PasteSpecialBuilder::LayerOption LayerOpt
        (
        );
        /**Sets  the layer option  <br> License requirements : None */
        public: void SetLayerOpt
        (
            NXOpen::PasteSpecialBuilder::LayerOption layerOpt /** layeropt */ 
        );
        /**Returns  the layer number  <br> License requirements : None */
        public: int LayerNumber
        (
        );
        /**Sets  the layer number  <br> License requirements : None */
        public: void SetLayerNumber
        (
            int layerNumber /** layernumber */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif