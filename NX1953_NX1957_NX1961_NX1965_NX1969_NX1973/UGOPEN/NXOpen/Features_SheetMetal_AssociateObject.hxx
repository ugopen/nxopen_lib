#ifndef NXOpen_FEATURES_SHEETMETAL_ASSOCIATEOBJECT_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_ASSOCIATEOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_AssociateObject.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class AssociateObject;
        }
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class _AssociateObjectBuilder;
            class AssociateObjectImpl;
            /** Represents an AssociateObject feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::SheetMetal::AssociateObjectBuilder  NXOpen::Features::SheetMetal::AssociateObjectBuilder @endlink  <br> 
             <br>  Created in NX1872.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  AssociateObject : public NXOpen::Features::Feature
            {
                private: AssociateObjectImpl * m_associateobject_impl;
                private: friend class  _AssociateObjectBuilder;
                protected: AssociateObject();
                public: ~AssociateObject();
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
