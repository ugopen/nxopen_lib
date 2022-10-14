#ifndef NXOpen_CAE_CONNECTIONS_LMIECENTERDEFINITION_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_LMIECENTERDEFINITION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_LMIECenterDefinition.ja
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
#include <NXOpen/CAE_Connections_LMIENode.hxx>
#include <NXOpen/CAE_Connections_LMIEPoint.hxx>
#include <NXOpen/CAE_Connections_LMIESelectionRecipe.hxx>
#include <NXOpen/CAE_Connections_LMIEError.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace Connections
        {
            class LMIECenterDefinition;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class LMIEError;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class LMIENode;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class LMIEPoint;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class LMIESelectionRecipe;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class _LMIECenterDefinitionBuilder;
            class LMIECenterDefinitionImpl;
            /**  Lumped Mass Center Definition. Use this interface to set/get properties and parameters of the Lumped Mass Center Definition.   <br> No creator  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  LMIECenterDefinition : public NXOpen::CAE::Connections::LMIEError
            {
                private: LMIECenterDefinitionImpl * m_lmiecenterdefinition_impl;
                private: friend class  _LMIECenterDefinitionBuilder;
                protected: LMIECenterDefinition();
                public: ~LMIECenterDefinition();
                /**Returns  the flag indicating to use Legs's Center of Gravity 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: bool UseCenterOfLegNodes
                (
                );
                /**Sets  the flag indicating to use Legs's Center of Gravity 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetUseCenterOfLegNodes
                (
                    bool use /** use */ 
                );
                /**Returns  the node 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIENode * Node
                (
                );
                /**Sets  the node 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetNode
                (
                    NXOpen::CAE::Connections::LMIENode * node /** Center Node */
                );
                /** Create a standalone node  @return  Center Node 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIENode * CreateNode
                (
                );
                /**Returns  the point 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIEPoint * Point
                (
                );
                /**Sets  the point 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetPoint
                (
                    NXOpen::CAE::Connections::LMIEPoint * point /** Center Point */
                );
                /** Create a standalone point  @return  Center Point 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIEPoint * CreatePoint
                (
                );
                /**Returns  the selection recipe 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIESelectionRecipe * SelectionRecipe
                (
                );
                /**Sets  the selection recipe 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetSelectionRecipe
                (
                    NXOpen::CAE::Connections::LMIESelectionRecipe * recipe /** Center Selection Recipe */
                );
                /** Create a standalone selection recipe  @return  Center Selection Recipe 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIESelectionRecipe * CreateSelectionRecipe
                (
                );
            };
        }
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