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
            Manages the suppression of @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink s within a
            @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink . Currently, an Arrangement simply acts as a
            context within which a Component can be suppressed, unsuppressed, or positioned. 
             <br> 
            To create an @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink , use the @link NXOpen::Assemblies::ArrangementCollection NXOpen::Assemblies::ArrangementCollection@endlink  class.
             <br> 
             <br> 
            An isolated @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  is an @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  that is capable of supporting 
            isolated positions and isolated position overrides. 
             <br> 
             <br>  
            A standard @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  is an @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  that does not support isolated 
            position or isolated position overrides. All @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink s created in NX 8.5 or earlier are standard @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink s.
             <br> 
         
         <br>  Created in NX3.0.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  Arrangement : public NXOpen::NXObject
        {
            private: ArrangementImpl * m_arrangement_impl;
            private: friend class  _ArrangementBuilder;
            protected: Arrangement();
            public: ~Arrangement();
            /**Returns  the @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink  which owns this arrangement 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::ComponentAssembly * Owner
            (
            );
            /** Delete the given @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink . If the forget_positioning flag is set to
                TRUE then components will not maintain their positions, otherwise variable component positioning
                will be created to maintain the components current positions.  If the part containing the 
                @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  is not already fully loaded this method will cause it to be. 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void Delete
            (
                bool forgetPositioning /** If TRUE then components will not maintain their position.*/
            );
            /**Returns 
                    the flag indicating whether this @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  is ignoring constraints. 
                
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: bool IgnoringConstraints
            (
            );
            /**Sets 
                    the flag indicating whether this @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  is ignoring constraints. 
                
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetIgnoringConstraints
            (
                bool isIgnoreConstraints /** Whether this @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  is ignoring all constraints.*/
            );
            /**
                    Get whether this @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  is currently used in the session. 
                    If it is, it will be kept up to date.
                 @return  Whether this @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  is currently used in the session.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: bool GetMaintainsConstraints
            (
            );
            /**
                    Get whether this @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  has postponed its solve.
                    The solving of constraints is postponed in an @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  that is not currently used in the session.
                    The constraints will solve when the component positions in the @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  are needed.
                 @return  Whether this @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  has postponed solving its constraints.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: bool GetHasPostponedConstraints
            (
            );
            /**
                    Forces a postponed @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink , that is not currently used in the session,
                    to solve its constraints. This could lead to updating the model if required. 
                
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SolvePostponedConstraints
            (
            );
            /**
                    Get whether this @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  is isolated. 

                    An isolated @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  is an @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  that is capable of supporting 
                    isolated positions and isolated position overrides. 
                 @return  Whether this @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  is isolated.
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: bool IsIsolated
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
