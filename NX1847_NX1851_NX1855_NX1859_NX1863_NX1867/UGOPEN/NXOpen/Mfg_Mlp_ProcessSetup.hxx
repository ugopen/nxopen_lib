#ifndef NXOpen_MFG_MLP_PROCESSSETUP_HXX_INCLUDED
#define NXOpen_MFG_MLP_PROCESSSETUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mfg_Mlp_ProcessSetup.ja
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
#include <NXOpen/Mfg_Mlp_IProcess.hxx>
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
            class ProcessSetup;
        }
    }
    class DisplayableObject;
    class INXObject;
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
            class Line;
        }
    }
    namespace Mfg
    {
        namespace Mlp
        {
            class Operation;
        }
    }
    namespace Mfg
    {
        namespace Mlp
        {
            class ProcessPlan;
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
            class Workpiece;
        }
    }
    namespace Mfg
    {
        namespace Mlp
        {
            class _ProcessSetupBuilder;
            class ProcessSetupImpl;
            /** Represents a Machining Line Planner process setup  <br> To obtain an instance of this class use GetSetup of Operation, Workpiece or ToolSet or GetSetups on ProcessPlan or Line.  <br> 
             <br>  Created in NX11.0.1.  <br>  
            */
            class MFGMLPOPENCPPEXPORT  ProcessSetup : public NXOpen::DisplayableObject, public virtual NXOpen::Mfg::Mlp::IProcess
            {
                private: ProcessSetupImpl * m_processsetup_impl;
                private: friend class  _ProcessSetupBuilder;
                protected: ProcessSetup();
                public: ~ProcessSetup();
                /** Get the Process plan of this setup 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::Mlp::ProcessPlan * GetProcessPlan
                (
                );
                /** Is this setup the Not Allocated setup 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: bool IsNotAllocated
                (
                );
                /** Get the Line of this setup 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::Mlp::Line * GetLine
                (
                );
                /** Get the Workpieces being manufactured in this setup 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::Mfg::Mlp::Workpiece *> GetWorkpieces
                (
                );
                /** Get the Operations in this Setup in the order in which they are machined 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::Mfg::Mlp::Operation *> GetOperations
                (
                );
                /** Get the Tool Set 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::Mlp::ToolSet * GetToolSet
                (
                );
                /** Finds the @link  Mfg::Mlp::Operation   Mfg::Mlp::Operation @endlink , @link  Mfg::Mlp::Workpiece   Mfg::Mlp::Workpiece @endlink , 
                            @link  Mfg::Mlp::ToolSet   Mfg::Mlp::ToolSet @endlink  or @link  Mfg::Mlp::MachineTool   Mfg::Mlp::MachineTool @endlink 
                            with the given identifier as recorded in a journal. 
                            An object may not return the same value as its JournalIdentifier in different versions of 
                            the software. However newer versions of the software should find the same object when 
                            FindObject is passed older versions of its journal identifier. In general, this method 
                            should not be used in handwritten code and exists to support record and playback of journals.

                            An exception will be thrown if no object can be found with the given journal identifier.  @return  Object found, or null if no such object exists.
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::INXObject * FindObject
                (
                    const NXString & journalIdentifier /** Name of the operation, workpiece, machinetool or toolset to be found */
                );
                /** Finds the @link  Mfg::Mlp::Operation   Mfg::Mlp::Operation @endlink , @link  Mfg::Mlp::Workpiece   Mfg::Mlp::Workpiece @endlink , 
                            @link  Mfg::Mlp::ToolSet   Mfg::Mlp::ToolSet @endlink  or @link  Mfg::Mlp::MachineTool   Mfg::Mlp::MachineTool @endlink 
                            with the given identifier as recorded in a journal. 
                            An object may not return the same value as its JournalIdentifier in different versions of 
                            the software. However newer versions of the software should find the same object when 
                            FindObject is passed older versions of its journal identifier. In general, this method 
                            should not be used in handwritten code and exists to support record and playback of journals.

                            An exception will be thrown if no object can be found with the given journal identifier.  @return  Object found, or null if no such object exists.
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                NXOpen::INXObject * FindObject
                (
                    const char * journalIdentifier /** Name of the operation, workpiece, machinetool or toolset to be found */
                );
                /** Get the Resource used by this process 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Mfg::Mlp::IResource * GetResource
                (
                );
                /** Get the Predecessors of this process (note that these are the immediate predecessors, this function does not recurse) 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: virtual std::vector<NXOpen::Mfg::Mlp::IProcess *> GetPredecessors
                (
                );
                /** Get the Successors of this process (note that these are the immediate successors, this function does not recurse) 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: virtual std::vector<NXOpen::Mfg::Mlp::IProcess *> GetSuccessors
                (
                );
                /** Get the Constraint Predecessors of this process (note that these are the immediate predecessors, this function does not recurse) 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: virtual std::vector<NXOpen::Mfg::Mlp::IProcess *> GetConstraintPredecessors
                (
                );
                /** Get the Constraint Successors of this process (note that these are the immediate successors, this function does not recurse) 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: virtual std::vector<NXOpen::Mfg::Mlp::IProcess *> GetConstraintSuccessors
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
