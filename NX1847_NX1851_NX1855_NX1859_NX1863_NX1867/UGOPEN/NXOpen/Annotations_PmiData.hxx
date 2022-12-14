#ifndef NXOpen_ANNOTATIONS_PMIDATA_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiData.ja
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
#include <NXOpen/Annotations_AssociatedObject.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class PmiData;
    }
    namespace Annotations
    {
        class AssociatedObject;
    }
    namespace Annotations
    {
        class BusinessModifier;
    }
    namespace Annotations
    {
    }
    namespace Annotations
    {
        class PmiDataImpl;
        /** Represents PMI(Product and Manufacturing Information) data 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiData : public NXOpen::TransientObject
        {
            private: PmiDataImpl * m_pmidata_impl;
            /// \cond NX_NO_DOC 
            public: explicit PmiData(void *ptr);
            /// \endcond 
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~PmiData();
            /** Returns the business modifiers  @return  List of business modifiers 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Annotations::BusinessModifier *> GetBusinessModifiers
            (
            );
            /** Sets the business modifiers 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBusinessModifiers
            (
                const std::vector<NXOpen::Annotations::BusinessModifier *> & businessModifiers /** List of new business modifiers */
            );
            /** Returns the associated object  @return  Associated objects 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::AssociatedObject * GetAssociatedObject
            (
            );
            /** Sets the associated object 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAssociatedObject
            (
                NXOpen::Annotations::AssociatedObject * assocObj /** List of new associated objects */
            );
            /** Returns the index 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int GetIndex
            (
            );
            /** Sets the index 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetIndex
            (
                int index /** index */ 
            );
            /** Returns the numbers of associated objects list 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: int GetNumAssociatedObjectsSets
            (
            );
            /** Sets the number of associated objects list 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetNumAssociatedObjectsSets
            (
                int numAssocObjectsSets /** numassocobjectssets */ 
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
