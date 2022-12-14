#ifndef NXOpen_PREVIEWPROPERTIESBUILDER_HXX_INCLUDED
#define NXOpen_PREVIEWPROPERTIESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PreviewPropertiesBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
    class PreviewPropertiesBuilder;
    class Builder;
    class SelectNXObjectList;
    class _PreviewPropertiesBuilderBuilder;
    class PreviewPropertiesBuilderImpl;
    /**
        Represents a @link NXOpen::PreviewPropertiesBuilder NXOpen::PreviewPropertiesBuilder@endlink  to be used for creating and storing
        previews.  Both part previews and model view previews are supported.  
         <br> To create a new instance of this class, use @link NXOpen::PropertiesManager::CreatePreviewPropertiesBuilder  NXOpen::PropertiesManager::CreatePreviewPropertiesBuilder @endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    ModelViewCreation </td> <td> 
     
    OnPartSave </td> </tr> 

    <tr><td> 
     
    PartCreation </td> <td> 
     
    OnSave </td> </tr> 

    <tr><td> 
     
    StoreModelViewPreview </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    StorePartPreview </td> <td> 
     
    0 </td> </tr> 

    </table>  

     <br>  Created in NX8.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  PreviewPropertiesBuilder : public NXOpen::Builder
    {
        /** Specifies when the part preview will be created */
        public: enum PartCreationOptions
        {
            PartCreationOptionsOnSave/** Part preview will be created when the part is saved */,
            PartCreationOptionsOnDemand/** Interactive only option that allows the part preview to be created by selecting the Create Now button */
        };

        /** Specifies when the model view preview will be created */
        public: enum ModelViewCreationOptions
        {
            ModelViewCreationOptionsOnPartSave/** Model view preview will be created when the part is saved */,
            ModelViewCreationOptionsOnViewSave/** Model view preview will be created when the view is saved */,
            ModelViewCreationOptionsOnDemand/** Interactive only option that allows the model view preview to be created by selected the Create Now button */
        };

        private: PreviewPropertiesBuilderImpl * m_previewpropertiesbuilder_impl;
        private: friend class  _PreviewPropertiesBuilderBuilder;
        protected: PreviewPropertiesBuilder();
        public: ~PreviewPropertiesBuilder();
        /**Returns  the selected object(s) list. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectNXObjectList * SelectedObjects
        (
        );
        /**Returns  the store part preview.  Determines if the part preview will be stored.  If true, the
                    part creation option will decide when the preview will be stored. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: bool StorePartPreview
        (
        );
        /**Sets  the store part preview.  Determines if the part preview will be stored.  If true, the
                    part creation option will decide when the preview will be stored. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void SetStorePartPreview
        (
            bool storePartPreview /** storepartpreview */ 
        );
        /**Returns  the part creation.  This option determines when the part preview will be stored.  It is 
                    only used if the store part preview is turned on. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::PreviewPropertiesBuilder::PartCreationOptions PartCreation
        (
        );
        /**Sets  the part creation.  This option determines when the part preview will be stored.  It is 
                    only used if the store part preview is turned on. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void SetPartCreation
        (
            NXOpen::PreviewPropertiesBuilder::PartCreationOptions partCreation /** partcreation */ 
        );
        /**Returns  the store model view preview.  Determines if the model view preview will be stored.  
                    If true, the model view creation option will decide when the preview will be stored. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: bool StoreModelViewPreview
        (
        );
        /**Sets  the store model view preview.  Determines if the model view preview will be stored.  
                    If true, the model view creation option will decide when the preview will be stored. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void SetStoreModelViewPreview
        (
            bool storeModelViewPreview /** storemodelviewpreview */ 
        );
        /**Returns  the model view creation.  This option determines when the model view preview will be stored.  
                    It is only used if the store model view preview is turned on. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::PreviewPropertiesBuilder::ModelViewCreationOptions ModelViewCreation
        (
        );
        /**Sets  the model view creation.  This option determines when the model view preview will be stored.  
                    It is only used if the store model view preview is turned on. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void SetModelViewCreation
        (
            NXOpen::PreviewPropertiesBuilder::ModelViewCreationOptions modelViewCreation /** modelviewcreation */ 
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
