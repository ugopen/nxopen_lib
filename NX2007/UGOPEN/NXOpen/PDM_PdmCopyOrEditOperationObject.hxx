#ifndef NXOpen_PDM_PDMCOPYOREDITOPERATIONOBJECT_HXX_INCLUDED
#define NXOpen_PDM_PDMCOPYOREDITOPERATIONOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_PdmCopyOrEditOperationObject.ja
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
        class PdmCopyOrEditOperationObject;
    }
    class NXObject;
    namespace PDM
    {
        class LogicalObject;
    }
    namespace PDM
    {
        class _PdmCopyOrEditOperationObjectBuilder;
        class PdmCopyOrEditOperationObjectImpl;
        /**
                Represents the class for object participating in the Copy operation.
             <br> Instances of this class can only be accessed through @link NXOpen::PDM::PdmCopyOrEditOperationBuilder NXOpen::PDM::PdmCopyOrEditOperationBuilder@endlink  builder.  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  PdmCopyOrEditOperationObject : public NXOpen::NXObject
        {
            private: PdmCopyOrEditOperationObjectImpl * m_pdmcopyoreditoperationobject_impl;
            private: friend class  _PdmCopyOrEditOperationObjectBuilder;
            protected: PdmCopyOrEditOperationObject();
            public: ~PdmCopyOrEditOperationObject();
            /** Gets the primary logical object represented by this operation object 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::LogicalObject * GetCurrentPrimaryLogicalObject
            (
            );
            /** Gets the nonmaster logical objects associated with the copy operation object. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void GetSecondaryLogicalObjects
            (
                std::vector<NXOpen::PDM::LogicalObject *> & secondaryLogicalObjects /** secondarylogicalobjects */ 
            );
            /** Gets the initial name of this object.  @return  the filename of added for copy 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetInitialName
            (
            );
            /** Gets the final name of this object.  @return  the final name assigned to the part being cloned 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetFinalName
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
