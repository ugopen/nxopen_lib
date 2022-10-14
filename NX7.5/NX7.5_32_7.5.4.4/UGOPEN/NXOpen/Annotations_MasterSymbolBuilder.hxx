#ifndef NXOpen_ANNOTATIONS_MASTERSYMBOLBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_MASTERSYMBOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_MasterSymbolBuilder.ja
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
#include <NXOpen/Annotations_MasterSymbolBuilder.hxx>
#include <NXOpen/Annotations_MasterSymbolListItemBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Gateway_ImageCaptureBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class MasterSymbolBuilder;
    }
    namespace Annotations
    {
        class Annotation;
    }
    namespace Annotations
    {
        class MasterSymbol;
    }
    namespace Annotations
    {
        class MasterSymbolListItemBuilder;
    }
    class Builder;
    namespace Gateway
    {
        class ImageCaptureBuilder;
    }
    class NXObjectList;
    class Point;
    class SelectNXObjectList;
    namespace Annotations
    {
        class _MasterSymbolBuilderBuilder;
        class MasterSymbolBuilderImpl;
        /** Represents a Builder for MasterSymbol functionality <br> To create a new instance of this class, use @link Annotations::CustomSymbolCollection::CreateMasterSymbolBuilder Annotations::CustomSymbolCollection::CreateMasterSymbolBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ImageCapture.CaptureMethod </td> <td> 
         
        GraphicsArea </td> </tr> 

        <tr><td> 
         
        ImageCapture.Format </td> <td> 
         
        Bmp </td> </tr> 

        <tr><td> 
         
        ImageCapture.Size </td> <td> 
         
        Pixels64 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  MasterSymbolBuilder : public Builder
        {
            /** The Enum for Attachment options */
            public: enum LeaderAttachmentType
            {
                LeaderAttachmentTypeLeft/** Left Attachment */,
                LeaderAttachmentTypeRight/** Right Attachment */
            };

            private: MasterSymbolBuilderImpl * m_mastersymbolbuilder_impl;
            private: friend class  _MasterSymbolBuilderBuilder;
            protected: MasterSymbolBuilder();
            public: ~MasterSymbolBuilder();
            /** Create Master Symbol list item  builder @return   <br> License requirements : None */
            public: NXOpen::Annotations::MasterSymbolListItemBuilder * CreateNewListItem
            (
                NXOpen::Annotations::Annotation * noteTag /** notetag */ ,
                const std::vector<NXString> & notes /** name of the solution */
            );
            /**Returns  the JA method support for accessing and setting Symbol Name value  <br> License requirements : None */
            public: NXString SymbolName
            (
            );
            /**Sets  the JA method support for accessing and setting Symbol Name value  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolName
            (
                const NXString & symbolName /** symbolname */ 
            );
            /**Returns  the symbol image name  <br> License requirements : None */
            public: NXString ImageName
            (
            );
            /**Sets  the symbol image name  <br> License requirements : drafting ("DRAFTING") */
            public: void SetImageName
            (
                const NXString & imageName /** imagename */ 
            );
            /**Returns  the part file name  <br> License requirements : None */
            public: NXString PartFileName
            (
            );
            /**Sets  the part file name  <br> License requirements : drafting ("DRAFTING") */
            public: void SetPartFileName
            (
                const NXString & partFileName /** partfilename */ 
            );
            /**Returns  the item number, valid in team center  <br> License requirements : None */
            public: NXString ItemNumber
            (
            );
            /**Sets  the item number, valid in team center  <br> License requirements : drafting ("DRAFTING") */
            public: void SetItemNumber
            (
                const NXString & itemNumber /** itemnumber */ 
            );
            /**Returns  the revision, valid in team center  <br> License requirements : None */
            public: NXString Revision
            (
            );
            /**Sets  the revision, valid in team center  <br> License requirements : drafting ("DRAFTING") */
            public: void SetRevision
            (
                const NXString & revision /** revision */ 
            );
            /**Returns  the Item Name, valid in team center <br> License requirements : None */
            public: NXString ItemName
            (
            );
            /**Sets  the Item Name, valid in team center <br> License requirements : drafting ("DRAFTING") */
            public: void SetItemName
            (
                const NXString & itemName /** itemname */ 
            );
            /** Item number assign button. This will generate the item number, valid in team center  <br> License requirements : drafting ("DRAFTING") */
            public: void GenerateItemNumber
            (
            );
            /** Revision assign button, This will generate the revision number, valid in team center  <br> License requirements : drafting ("DRAFTING") */
            public: void GenerateRevision
            (
            );
            /**Returns  the select object  <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * Contents
            (
            );
            /**Returns  the anchor point  <br> License requirements : None */
            public: NXOpen::Point * AnchorPoint
            (
            );
            /**Sets  the anchor point  <br> License requirements : drafting ("DRAFTING") */
            public: void SetAnchorPoint
            (
                NXOpen::Point * anchorPoint /** anchorpoint */ 
            );
            /**Returns  the image capture builder  <br> License requirements : None */
            public: NXOpen::Gateway::ImageCaptureBuilder * ImageCapture
            (
            );
            /** Getting Leader attachment point from builder side @return   <br> License requirements : None */
            public: NXOpen::Point * GetLeaderAttachmentPoint
            (
                NXOpen::Annotations::MasterSymbolBuilder::LeaderAttachmentType attachmentType /** Attachment type either of left or right*/
            );
            /** Setting Leader attachment point on builder side <br> License requirements : drafting ("DRAFTING") */
            public: void SetLeaderAttachmentPoint
            (
                NXOpen::Annotations::MasterSymbolBuilder::LeaderAttachmentType attachmentType /** Attachment type either of left or right */,
                NXOpen::Point * leaderAttachmentPoint /** Attachment point */
            );
            /**Returns  the note list  <br> License requirements : None */
            public: NXOpen::NXObjectList * NoteList
            (
            );
            /** Returns the  multiple notes for a given Text Type
                        this property is valid if JA_MASTER_SYMBOL_BUILDER_TextTypes value is either of controlled, partially controlled or arbitory  @return  Multiple notes as Output <br> License requirements : None */
            public: std::vector<NXString> GetMultilineString
            (
            );
            /** Setting Path retrieved from Global method at builder side  <br> License requirements : drafting ("DRAFTING") */
            public: void SetPath
            (
                const NXString & path /** location of symbol */
            );
            /** Sets if it is part symbol  <br> License requirements : drafting ("DRAFTING") */
            public: void SetIsPartSymbol
            (
                bool isPartSymbol /** True If it is part symbol*/
            );
            /** Renames symbol  <br> License requirements : drafting ("DRAFTING") */
            public: void Rename
            (
                NXOpen::Annotations::MasterSymbol * currentSymbolTag /** symbol Tag*/,
                const NXString & newSymbolName /** New symbol name */
            );
            /** Changes symbol image <br> License requirements : drafting ("DRAFTING") */
            public: void EditImage
            (
                NXOpen::Annotations::MasterSymbol * currentSymbolTag /** symbol Tag*/,
                const NXString & newImageName /** New image name */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif