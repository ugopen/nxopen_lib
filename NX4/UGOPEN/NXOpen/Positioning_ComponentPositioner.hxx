#ifndef NXOpen_POSITIONING_COMPONENTPOSITIONER_HXX_INCLUDED
#define NXOpen_POSITIONING_COMPONENTPOSITIONER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Positioning_ComponentPositioner.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Positioning_Positioner.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Positioning
    {
        class ComponentPositioner;
    }
    namespace Assemblies
    {
        class Arrangement;
    }
    namespace Positioning
    {
        class Positioner;
    }
    namespace Positioning
    {
        class _ComponentPositionerBuilder;
        /**
          An instance of this class can be used to create @link Constraint Constraint@endlink s and
          associated objects.
         <br> Not directly created by user. <br> */
        class NXOPENCPPEXPORT ComponentPositioner : public Positioning::Positioner
        {
            private: friend class  _ComponentPositionerBuilder;
            protected: ComponentPositioner();
            /**Returns  
                    the @link Assemblies::Arrangement Assemblies::Arrangement@endlink  in which the 
                    primary @link Positioning::Network Positioning::Network@endlink  will solve.
                 <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: NXOpen::Assemblies::Arrangement * PrimaryArrangement
            (
            );
            /**Sets  
                    the @link Assemblies::Arrangement Assemblies::Arrangement@endlink  in which the 
                    primary @link Positioning::Network Positioning::Network@endlink  will solve.
                 <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetPrimaryArrangement
            (
                NXOpen::Assemblies::Arrangement * arrangement /** The primary @link Assemblies::Arrangement Assemblies::Arrangement@endlink . */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
