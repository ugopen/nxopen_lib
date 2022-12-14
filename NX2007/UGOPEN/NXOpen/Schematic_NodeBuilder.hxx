#ifndef NXOpen_SCHEMATIC_NODEBUILDER_HXX_INCLUDED
#define NXOpen_SCHEMATIC_NODEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Schematic_NodeBuilder.ja
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
#include <NXOpen/Diagramming_Node.hxx>
#include <NXOpen/Schematic_BaseObjectBuilder.hxx>
#include <NXOpen/Schematic_Connection.hxx>
#include <NXOpen/Schematic_DataType.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_schematic_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Schematic
    {
        class NodeBuilder;
    }
    namespace Diagramming
    {
        class Node;
    }
    namespace Schematic
    {
        class BaseObjectBuilder;
    }
    namespace Schematic
    {
        class Connection;
    }
    namespace Schematic
    {
        class _NodeBuilderBuilder;
        class NodeBuilderImpl;

        /// \cond NX_NO_DOC 
        /**  @brief  Represents a NodeBuilder.  

           <br> To create a new instance of this class, use @link NXOpen::Schematic::SchematicManager::CreateNodeBuilder  NXOpen::Schematic::SchematicManager::CreateNodeBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Rotate </term> <description> 
         
        Zero </description> </item> 

        <item><term> 
         
        SymbolSourceType </term> <description> 
         
        ReuseLibrary </description> </item> 

        </list> 

         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_SCHEMATICEXPORT  NodeBuilder : public NXOpen::Schematic::BaseObjectBuilder
        {
            private: NodeBuilderImpl * m_nodebuilder_impl;
            private: friend class  _NodeBuilderBuilder;
            protected: NodeBuilder();
            public: ~NodeBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the symbol source type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Schematic::SymbolSourceOption SymbolSourceType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the symbol source type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSymbolSourceType
            (
                NXOpen::Schematic::SymbolSourceOption symbolSourceType /** symbolsourcetype */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the symbol ID of this node. It is only applicable when @link NXOpen::Schematic::NodeBuilder::SymbolSourceType NXOpen::Schematic::NodeBuilder::SymbolSourceType@endlink  is @link NXOpen::Schematic::SymbolSourceOptionReuseLibrary NXOpen::Schematic::SymbolSourceOptionReuseLibrary@endlink .
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString SymbolId
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the symbol ID of this node. It is only applicable when @link NXOpen::Schematic::NodeBuilder::SymbolSourceType NXOpen::Schematic::NodeBuilder::SymbolSourceType@endlink  is @link NXOpen::Schematic::SymbolSourceOptionReuseLibrary NXOpen::Schematic::SymbolSourceOptionReuseLibrary@endlink .
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSymbolId
            (
                const NXString & symbolId /** symbolid */ 
            );
            /**Sets  the symbol ID of this node. It is only applicable when @link NXOpen::Schematic::NodeBuilder::SymbolSourceType NXOpen::Schematic::NodeBuilder::SymbolSourceType@endlink  is @link NXOpen::Schematic::SymbolSourceOptionReuseLibrary NXOpen::Schematic::SymbolSourceOptionReuseLibrary@endlink .
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            void SetSymbolId
            (
                const char * symbolId /** symbolid */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the symbol from foundation window. It is only applicable when @link Schematic::NodeBuilder::SymbolSourceType Schematic::NodeBuilder::SymbolSourceType@endlink  is @link Schematic::SymbolSourceOptionExistingSymbol Schematic::SymbolSourceOptionExistingSymbol@endlink .
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::Node * ExistingSymbol
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the symbol from foundation window. It is only applicable when @link Schematic::NodeBuilder::SymbolSourceType Schematic::NodeBuilder::SymbolSourceType@endlink  is @link Schematic::SymbolSourceOptionExistingSymbol Schematic::SymbolSourceOptionExistingSymbol@endlink .
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetExistingSymbol
            (
                NXOpen::Diagramming::Node * existingSymbol /** existingsymbol */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Gets the symbol location.  @return  the symbol location. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point2d GetLocation
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Sets the symbol location. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLocation
            (
                const NXOpen::Point2d & location /** the symbol location. */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the option to lock the aspect ratio. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool LockAspectRatio
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the option to lock the aspect ratio. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLockAspectRatio
            (
                bool lockAspectRatio /** lockaspectratio */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the scale value. It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is true.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double Scale
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the scale value. It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is true.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetScale
            (
                double scale /** scale */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the x scale value. It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is false.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double ScaleX
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the x scale value. It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is false.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetScaleX
            (
                double scaleX /** scalex */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the y scale value. It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is false.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double ScaleY
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the y scale value. It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is false.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetScaleY
            (
                double scaleY /** scaley */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the symbol rotation angle. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Schematic::RotateAngleOption Rotate
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the symbol rotation angle. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRotate
            (
                NXOpen::Schematic::RotateAngleOption rotate /** rotate */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the option to flip the symbol horizontally. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool FlipHorizontal
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the option to flip the symbol horizontally. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFlipHorizontal
            (
                bool flipHorizontal /** fliphorizontal */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the option to flip the symbol vertically. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool FlipVertical
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the option to flip the symbol vertically. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFlipVertical
            (
                bool flipVertical /** flipvertical */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get the node object of the equipment builder. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::Node * GetNode
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Detaches the equipment from all attached connections. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void DetachAllConnections
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Sets connection location for the inline symbol. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetInlineSymbolLocation
            (
                NXOpen::Schematic::Connection * connection /** connection */ ,
                int segementId /** segementid */ ,
                double percent /** percent */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Gets connection location for the inline symbol. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void GetInlineSymbolLocation
            (
                NXOpen::Schematic::Connection ** connection /** connection */ ,
                int* segementId /** segementid */ ,
                double* percent /** percent */ 
            );

            /// \endcond 
        };

        /// \endcond 
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
