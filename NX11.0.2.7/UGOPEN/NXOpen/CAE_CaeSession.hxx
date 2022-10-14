#ifndef NXOpen_CAE_CAESESSION_HXX_INCLUDED
#define NXOpen_CAE_CAESESSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CaeSession.ja
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
#include <NXOpen/CAE_CaeDataContainer.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class CaeSession;
    }
    class Session;
    namespace CAE
    {
        class AssociationUtilities;
    }
    namespace CAE
    {
        class CaeDataContainer;
    }
    namespace CAE
    {
        class CaePart;
    }
    class MaterialUtilities;
    namespace CAE
    {
        class CaeSessionImpl;
        /**  @brief  This class provides access to all session related CAE functionality  

           <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CaeSession
        {
            private: CaeSessionImpl * m_caesession_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CaeSession(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CaeSession();
            /** Returns a @link  NXOpen::CAE::CaeDataContainer   NXOpen::CAE::CaeDataContainer @endlink  to be used for
                        specifying input parameters operations like Simulation Import and Export.
                      @return  the Cae Data Container 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::CaeDataContainer * GetDataContainer
            (
            );
            /** Creates a @link  NXOpen::CAE::SimPart   NXOpen::CAE::SimPart @endlink  and a @link  NXOpen::CAE::FemPart   NXOpen::CAE::FemPart @endlink  from
                        solver specific data.  Import is driven by that properties defined in the input 
                        @link  NXOpen::CAE::CaeDataContainer   NXOpen::CAE::CaeDataContainer @endlink  propertyList.  The exact properties can vary from
                        solver to solver.

                     @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::CaePart * ImportSimulation
            (
                const NXString & solverName /** the solver name to indicate what type of data is being imported */,
                NXOpen::CAE::CaeDataContainer * propertyList /** the import parameters see @link GetDataContainer  GetDataContainer @endlink .
                 */
            );
            /** Creates a @link  NXOpen::CAE::SimPart   NXOpen::CAE::SimPart @endlink  and a @link  NXOpen::CAE::FemPart   NXOpen::CAE::FemPart @endlink  from
                        solver specific data.  Import is driven by that properties defined in the input 
                        @link  NXOpen::CAE::CaeDataContainer   NXOpen::CAE::CaeDataContainer @endlink  propertyList.  The exact properties can vary from
                        solver to solver.

                     @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::CaePart * ImportSimulation
            (
                const char * solverName /** the solver name to indicate what type of data is being imported */,
                NXOpen::CAE::CaeDataContainer * propertyList /** the import parameters see @link GetDataContainer  GetDataContainer @endlink .
                 */
            );


            /** Returns the @link NXOpen::MaterialUtilities NXOpen::MaterialUtilities@endlink  instance belonging to this session 
             <br>  Created in NX10.0.0.  <br>  
            */
            public: NXOpen::MaterialUtilities *MaterialUtils();
            /** Returns the @link NXOpen::CAE::AssociationUtilities NXOpen::CAE::AssociationUtilities@endlink  instance belonging to this session 
             <br>  Created in NX11.0.0.  <br>  
            */
            public: NXOpen::CAE::AssociationUtilities *AssociationUtils();
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