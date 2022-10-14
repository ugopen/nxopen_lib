#ifndef NXOpen_MFG_MLP_TOOLASSEMBLY_HXX_INCLUDED
#define NXOpen_MFG_MLP_TOOLASSEMBLY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mfg_Mlp_ToolAssembly.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/Mfg_Mlp_IResource.hxx>
#include <NXOpen/libmfgmlpopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mfg
    {
        namespace Mlp
        {
            class ToolAssembly;
        }
    }
    class DisplayableObject;
    namespace Mfg
    {
        namespace Mlp
        {
            class IProcess;
        }
    }
    namespace Mfg
    {
        namespace Mlp
        {
            class IResource;
        }
    }
    namespace Mfg
    {
        namespace Mlp
        {
            class ToolSet;
        }
    }
    namespace Mfg
    {
        namespace Mlp
        {
            class _ToolAssemblyBuilder;
            class ToolAssemblyImpl;
            /** Represents a Machining Line Planner tool assembly  <br> To obtain an instance of this class use (not yet implemented!) GetToolAssembly of Operation.  <br> 
             <br>  Created in NX11.0.1.  <br>  
            */
            class MFGMLPOPENCPPEXPORT  ToolAssembly : public NXOpen::DisplayableObject, public virtual NXOpen::Mfg::Mlp::IResource
            {
                private: ToolAssemblyImpl * m_toolassembly_impl;
                private: friend class  _ToolAssemblyBuilder;
                protected: ToolAssembly();
                public: ~ToolAssembly();
                /** Get the Tool Set 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::Mlp::ToolSet * GetToolSet
                (
                );
                /** Get the Processes 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: virtual std::vector<NXOpen::Mfg::Mlp::IProcess *> GetProcesses
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