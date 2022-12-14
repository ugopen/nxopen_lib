#ifndef NXOpen_PDM_CAECLONEMANAGER_HXX_INCLUDED
#define NXOpen_PDM_CAECLONEMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_CaeCloneManager.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/PDM_CaeCloneManager.hxx>
#include <NXOpen/PDM_PartFromPartBuilder.hxx>
#include <NXOpen/libnxopencpp_pdm_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PDM
    {
        class CaeCloneManager;
    }
    namespace PDM
    {
        class PartFromPartBuilder;
    }
    namespace PDM
    {
        class CaeCloneManagerImpl;
        /**  @brief  This class is used for executing CAE Clone on a Simulation File or a FeModel File.
             

           <br> Use @link NXOpen::PDM::PartManager NXOpen::PDM::PartManager@endlink  to get the instance of this class.  <br> 
         <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead. <br>  

         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::PDM::PartOperationCopyBuilder instead.")  CaeCloneManager : public NXOpen::TransientObject
        {
            /** Option for creation of part builder for CAE Clone */
            public: enum CloneOption
            {
                CloneOptionNone/** none */  = -1,
                CloneOptionSim/** sim */ ,
                CloneOptionFem/** fem */ ,
                CloneOptionIdeal/** ideal */ ,
                CloneOptionMaster/** master */ 
            };

            private: CaeCloneManagerImpl * m_caeclonemanager_impl;
            /// \cond NX_NO_DOC 
            public: explicit CaeCloneManager(void *ptr);
            /// \endcond 
            /** Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector. 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead. <br>  

             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::PDM::PartOperationCopyBuilder instead.") virtual ~CaeCloneManager();
            /** Get Part Builders for Clone Operation of a CAE Simulation or a CAE Model part.  
                    Get  builder class @link NXOpen::PDM::PartFromPartBuilder NXOpen::PDM::PartFromPartBuilder@endlink  using this function.
                     @return  the part builder 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead. <br>  

             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::PDM::PartOperationCopyBuilder instead.") NXOpen::PDM::PartFromPartBuilder * GetPartBuilderForClone
            (
                NXOpen::PDM::CaeCloneManager::CloneOption option /** option */ 
            );
            /**
                    Sets the option for include master on the Clone Manager class 
                    
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead. <br>  

             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::PDM::PartOperationCopyBuilder instead.") void SetIncludeMaster
            (
                bool value /** value */ 
            );
            /**
                    Gets the container in Teamcenter where the cloned part is saved
                     @return  
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead. <br>  

             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::PDM::PartOperationCopyBuilder instead.") NXString GetContainer
            (
                NXOpen::PDM::CaeCloneManager::CloneOption option /** option */ 
            );
            /**
                    Sets the container in Teamcenter where the cloned part is saved
                    
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead. <br>  

             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::PDM::PartOperationCopyBuilder instead.") void SetContainer
            (
                NXOpen::PDM::CaeCloneManager::CloneOption option /** option */ ,
                const NXString & container /** container */ 
            );
            /**
                    Sets the container in Teamcenter where the cloned part is saved
                    
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead. <br>  

             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetContainer
            (
                NXOpen::PDM::CaeCloneManager::CloneOption option /** option */ ,
                const char * container /** container */ 
            );
            /** Commits the Clone Operation for the Clone Manager class @link NXOpen::PDM::CaeCloneManager NXOpen::PDM::CaeCloneManager@endlink .
                    Deletes all the Part Builders associated with the Clone Manager
                    
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead. <br>  

             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::PDM::PartOperationCopyBuilder instead.") void CommitClone
            (
            );
        }; //lint !e1712 default constructor not defined for class  

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
