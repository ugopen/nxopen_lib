#ifndef NXOpen_PID_OFFSHEETCONNECTORBUILDER_HXX_INCLUDED
#define NXOpen_PID_OFFSHEETCONNECTORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PID_OffSheetConnectorBuilder.ja
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
#include <NXOpen/Diagramming_TextStyleBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/PDM_ConnectionElementRevision.hxx>
#include <NXOpen/PDM_CrossSheetReference.hxx>
#include <NXOpen/PDM_SheetRevision.hxx>
#include <NXOpen/PID_DataType.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libpidopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PID
    {
        class OffSheetConnectorBuilder;
    }
    class Builder;
    namespace Diagramming
    {
        class Node;
    }
    namespace Diagramming
    {
        class TextStyleBuilder;
    }
    namespace PID
    {
        class OffSheetConnector;
    }
    namespace PID
    {
        class Pipe;
    }
    namespace PID
    {
        class Sheet;
    }
    namespace PID
    {
        class _OffSheetConnectorBuilderBuilder;
        class OffSheetConnectorBuilderImpl;
        /**  @brief 
            Builder used to model a piece of Off Sheet Connector.  

         
             <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateOffSheetConnectorBuilder  NXOpen::PID::PidManager::CreateOffSheetConnectorBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        RotateOption </td> <td> 
         
        Zero </td> </tr> 

        </table>  

         <br>  Created in NX11.0.1.  <br>  
        */
        class PIDOPENCPPEXPORT  OffSheetConnectorBuilder : public NXOpen::Builder
        {
            /**  @brief  the style of OSC elements.  

              */
            public: enum StyleOption
            {
                StyleOptionSmallFilledArrowOut/** small filled arrow out */ ,
                StyleOptionSmallFilledArrowIn/** small filled arrow in */ ,
                StyleOptionBox/** box */ ,
                StyleOptionChevronOut/** chevron out */ ,
                StyleOptionChevronIn/** chevron in */ 
            };

            private: OffSheetConnectorBuilderImpl * m_offsheetconnectorbuilder_impl;
            private: friend class  _OffSheetConnectorBuilderBuilder;
            protected: OffSheetConnectorBuilder();
            public: ~OffSheetConnectorBuilder();
            /**Returns  the style of OSC 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::PID::OffSheetConnectorBuilder::StyleOption Style
            (
            );
            /**Sets  the style of OSC 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetStyle
            (
                NXOpen::PID::OffSheetConnectorBuilder::StyleOption style /** style */ 
            );
            /**Returns  the symbol rotation angle. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::PID::RotateAngleOption RotateOption
            (
            );
            /**Sets  the symbol rotation angle. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetRotateOption
            (
                NXOpen::PID::RotateAngleOption rotate /** rotate */ 
            );
            /**Returns  the option to flip the symbol horizontally. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: bool Horizontal
            (
            );
            /**Returns  the option to flip the symbol vertically. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: bool Vertical
            (
            );
            /** To rotate a off sheet connector
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void Rotate
            (
            );
            /** To flip a off sheet connector horizonally
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void FlipHorizontally
            (
            );
            /** To flip a off sheet connector vertically
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void FlipVertically
            (
            );
            /** Gets the symbol location.  @return  the symbol location. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::Point2d GetLocation
            (
            );
            /** Sets the symbol location. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetLocation
            (
                const NXOpen::Point2d & location /** the osc location. */
            );
            /**Returns  the current element ID of this OSC. It works only in edit mode, it's optional and the first element ID stored in the OSC will be used as default.
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXString ElementId
            (
            );
            /**Sets  the current element ID of this OSC. It works only in edit mode, it's optional and the first element ID stored in the OSC will be used as default.
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetElementId
            (
                const NXString & elementId /** elementid */ 
            );
            /**Sets  the current element ID of this OSC. It works only in edit mode, it's optional and the first element ID stored in the OSC will be used as default.
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            void SetElementId
            (
                const char * elementId /** elementid */ 
            );
            /**Returns  the owning sheet of this sheet element. Its setting method works only in creation mode. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::PID::Sheet * OwningSheet
            (
            );
            /**Sets  the owning sheet of this sheet element. Its setting method works only in creation mode. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetOwningSheet
            (
                NXOpen::PID::Sheet * owningSheet /** owningsheet */ 
            );
            /** To set the connection connecting to the OSC sheet element.
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetConnection
            (
                NXOpen::PID::ConnectionEndType type /** type */ ,
                NXOpen::PID::Pipe * connection /** connection */ ,
                const NXString & connectionId /** connectionid */ 
            );
            /** To set the connection connecting to the OSC sheet element.
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            void SetConnection
            (
                NXOpen::PID::ConnectionEndType type /** type */ ,
                NXOpen::PID::Pipe * connection /** connection */ ,
                const char * connectionId /** connectionid */ 
            );
            /** To get the connection connecting to the OSC sheet element.
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void GetConnection
            (
                NXOpen::PID::ConnectionEndType* type /** type */ ,
                NXOpen::PID::Pipe ** connection /** connection */ ,
                NXString* connectionId /** connectionid */ 
            );
            /**Returns  the text style of the OSC. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::Diagramming::TextStyleBuilder * TextStyleBuilder
            (
            );
            /** Links to the destination OSC. If the input OffSheetConnector is NULL, it means break the existing link.  
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void LinkOSC
            (
                NXOpen::PID::OffSheetConnector * desObject /** desobject */ 
            );
            /** Get the node object of the off sheet connector builder. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::Diagramming::Node * GetNode
            (
            );
        };
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