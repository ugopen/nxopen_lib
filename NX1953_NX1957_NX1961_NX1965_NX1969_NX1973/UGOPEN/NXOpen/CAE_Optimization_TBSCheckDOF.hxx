#ifndef NXOpen_CAE_OPTIMIZATION_TBSCHECKDOF_HXX_INCLUDED
#define NXOpen_CAE_OPTIMIZATION_TBSCHECKDOF_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Optimization_TBSCheckDOF.ja
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
        namespace Optimization
        {
            class TBSCheckDOF;
        }
    }
    class CoordinateSystem;
    class NXObject;
    namespace CAE
    {
        namespace Optimization
        {
            class _TBSCheckDOFBuilder;
            class TBSCheckDOFImpl;
            /** Represents the restriction of dispacement in the coordinate direction of the referenced coordinate system   
             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  TBSCheckDOF : public NXOpen::NXObject
            {
                /** Represents the status of displacement restriction */
                public: enum CheckDofOption
                {
                    CheckDofOptionFix/** Displacement is constrainted  */,
                    CheckDofOptionFree/** Displacement is allowed  */
                };

                 /** the displacement restriction settings on three axial directions of referenced coordinate system  */
                public:
                struct DofSettings
                {
                    public: /** Represents displacement in the X axial direction */NXOpen::CAE::Optimization::TBSCheckDOF::CheckDofOption Dof1;
                    public: /** Represents displacement in the Y axial direction */NXOpen::CAE::Optimization::TBSCheckDOF::CheckDofOption Dof2;
                    public: /** Represents displacement in the Z axial direction */NXOpen::CAE::Optimization::TBSCheckDOF::CheckDofOption Dof3;
                    public: DofSettings() :
                        Dof1((NXOpen::CAE::Optimization::TBSCheckDOF::CheckDofOption)0),
                        Dof2((NXOpen::CAE::Optimization::TBSCheckDOF::CheckDofOption)0),
                        Dof3((NXOpen::CAE::Optimization::TBSCheckDOF::CheckDofOption)0)
                    {
                    }
                    /** Constructor for the DofSettings struct. */ 
                    public: DofSettings(NXOpen::CAE::Optimization::TBSCheckDOF::CheckDofOption dof1Initial /** Represents displacement in the X axial direction */, 
                            NXOpen::CAE::Optimization::TBSCheckDOF::CheckDofOption dof2Initial /** Represents displacement in the Y axial direction */, 
                            NXOpen::CAE::Optimization::TBSCheckDOF::CheckDofOption dof3Initial /** Represents displacement in the Z axial direction */) :
                        Dof1(dof1Initial),
                        Dof2(dof2Initial),
                        Dof3(dof3Initial)
                    {
                    }
                };

                private: TBSCheckDOFImpl * m_tbscheckdof_impl;
                private: friend class  _TBSCheckDOFBuilder;
                protected: TBSCheckDOF();
                public: ~TBSCheckDOF();
                /**Returns  the displacement restriction settings on referenced coordinate system 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Optimization::TBSCheckDOF::DofSettings Dofs
                (
                );
                /**Sets  the displacement restriction settings on referenced coordinate system 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : cae_opt_toposhape ("NX Shape Optimization") */
                public: void SetDofs
                (
                    const NXOpen::CAE::Optimization::TBSCheckDOF::DofSettings & dofs /** dofs */ 
                );
                /**Returns  the referenced coordinate system for displacement restriction  
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CoordinateSystem * ReferencedCoordinateSystem
                (
                );
                /**Sets  the referenced coordinate system for displacement restriction  
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : cae_opt_toposhape ("NX Shape Optimization") */
                public: void SetReferencedCoordinateSystem
                (
                    NXOpen::CoordinateSystem * csys /** csys */ 
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
