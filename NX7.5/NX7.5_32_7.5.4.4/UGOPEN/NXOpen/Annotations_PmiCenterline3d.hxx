#ifndef NXOpen_ANNOTATIONS_PMICENTERLINE3D_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMICENTERLINE3D_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiCenterline3d.ja
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
#include <NXOpen/Annotations_IPmi.hxx>
#include <NXOpen/Annotations_AssociatedObject.hxx>
#include <NXOpen/Annotations_BaseCenterline3d.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiCenterline3d;
    }
    namespace Annotations
    {
        class AssociatedObject;
    }
    namespace Annotations
    {
        class BaseCenterline3d;
    }
    namespace Annotations
    {
        class BusinessModifier;
    }
    namespace Annotations
    {
        class IPmi;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    namespace Annotations
    {
        class _PmiCenterline3dBuilder;
        class PmiCenterline3dImpl;
        /** Represents a Pmi 3D centerline */
        class NXOPENCPPEXPORT  PmiCenterline3d : public Annotations::BaseCenterline3d, public virtual Annotations::IPmi
        {
            private: PmiCenterline3dImpl * m_pmicenterline3d_impl;
            private: friend class  _PmiCenterline3dBuilder;
            protected: PmiCenterline3d();
            public: ~PmiCenterline3d();
            /** Returns the business modifiers  @return  List of business modifiers  <br> License requirements : None */
            public: virtual std::vector<NXOpen::Annotations::BusinessModifier *> GetBusinessModifiers
            (
            );
            /** Sets the business modifiers  <br> License requirements : geometric_tol ("GDT") */
            public: virtual void SetBusinessModifiers
            (
                const std::vector<NXOpen::Annotations::BusinessModifier *> & businessModifiers /** List of new business modifiers */
            );
            /** Returns the associated object  @return  Associated object  <br> License requirements : None */
            public: virtual NXOpen::Annotations::AssociatedObject * GetAssociatedObject
            (
            );
            /** Sets the associated object  <br> License requirements : geometric_tol ("GDT") */
            public: virtual void SetAssociatedObject
            (
                NXOpen::Annotations::AssociatedObject * assocObj /** New associated object */
            );
            /**Returns  the index. It is a unique integer assigned to a PMI object.  <br> License requirements : None */
            public: virtual int Index
            (
            );
            /**Sets  the index. It is a unique integer assigned to a PMI object.  <br> License requirements : geometric_tol ("GDT") */
            public: virtual void SetIndex
            (
                int index /** New integer for PMI object */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif