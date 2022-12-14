#ifndef NXOpen_CAE_CAELABEL_HXX_INCLUDED
#define NXOpen_CAE_CAELABEL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CaeLabel.ja
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
#include <NXOpen/Annotations_NoteBase.hxx>
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
        class CaeLabel;
    }
    namespace Annotations
    {
        class NoteBase;
    }
    class TaggedObject;
    namespace CAE
    {
        class _CaeLabelBuilder;
        class CaeLabelImpl;
        /** Represents an object that manages annotation for CAE  <br> To obtain an instance of this object use on of the creator in @link NXOpen::CAE::NoteCollection NXOpen::CAE::NoteCollection@endlink .  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CaeLabel : public NXOpen::Annotations::NoteBase
        {
            private: CaeLabelImpl * m_caelabel_impl;
            private: friend class  _CaeLabelBuilder;
            protected: CaeLabel();
            public: ~CaeLabel();
            /** Set Associated Objects into the CAE Notes 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetAssociatedObjects
            (
                const std::vector<NXOpen::TaggedObject *> & objectArray /**Array of assocated objects */
            );
            /** Get Associated Objects from the CAE Notes  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::TaggedObject *> GetAssociatedObjects
            (
            );
            /** Remove Associated Objects from the CAE Labels 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void RemoveAssociatedObjects
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
