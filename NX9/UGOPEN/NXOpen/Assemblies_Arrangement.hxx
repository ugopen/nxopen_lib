#ifndef NXOpen_ASSEMBLIES_ARRANGEMENT_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_ARRANGEMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_Arrangement.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_assemblies_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Assemblies
    {
        class Arrangement;
    }
    namespace Assemblies
    {
        class ComponentAssembly;
    }
    class NXObject;
    namespace Assemblies
    {
        class _ArrangementBuilder;
        class ArrangementImpl;
        /** 
            Manages the suppression of @link Component Component@endlink s within a
            @link ComponentAssembly ComponentAssembly@endlink . Currently, an Arrangement simply acts as a
            context within which a Component can be suppressed or unsuppressed. Future releases
            will add new functionality to Arrangements.
             <br> 
            To create an Arrangement, use the @link ArrangementCollection ArrangementCollection@endlink  class. <br> 
         
         <br>  Created in NX3.0.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  Arrangement : public NXObject
        {
            private: ArrangementImpl * m_arrangement_impl;
            private: friend class  _ArrangementBuilder;
            protected: Arrangement();
            public: ~Arrangement();
            /**Returns  the @link ComponentAssembly ComponentAssembly@endlink  which owns this arrangement 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::ComponentAssembly * Owner
            (
            );
            /** Delete the given @link Arrangement Arrangement@endlink . If the forget_positioning flag is set to
                TRUE then components will not maintain their positions, otherwise variable component positioning
                will be created to maintain the components current positions.  If the part containing the 
                @link Arrangement Arrangement@endlink  is not already fully loaded this method will cause it to be. 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void Delete
            (
                bool forgetPositioning /** If TRUE then components will not maintain their position.*/
            );
            /**Returns 
                    the flag indicating whether this @link Arrangement Arrangement@endlink  is ignoring constraints. 
                
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: bool IgnoringConstraints
            (
            );
            /**Sets 
                    the flag indicating whether this @link Arrangement Arrangement@endlink  is ignoring constraints. 
                
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetIgnoringConstraints
            (
                bool isIgnoreConstraints /** Whether this @link Arrangement Arrangement@endlink  is ignoring all constraints.*/
            );
            /**
                    Get whether this @link Arrangement Arrangement@endlink  is currently used in the session. 
                    If it is, it will be kept up to date.
                 @return  Whether this @link Arrangement Arrangement@endlink  is currently used in the session.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: bool GetMaintainsConstraints
            (
            );
            /**
                    Get whether this @link Arrangement Arrangement@endlink  has postponed its solve.
                    The solving of constraints is postponed in an @link Arrangement Arrangement@endlink  that is not currently used in the session.
                    The constraints will solve when the component positions in the @link Arrangement Arrangement@endlink  are needed.
                 @return  Whether this @link Arrangement Arrangement@endlink  has postponed solving its constraints.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: bool GetHasPostponedConstraints
            (
            );
            /**
                    Forces a postponed @link Arrangement Arrangement@endlink , that is not currently used in the session,
                    to solve its constraints. This could lead to updating the model if required. 
                
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SolvePostponedConstraints
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
