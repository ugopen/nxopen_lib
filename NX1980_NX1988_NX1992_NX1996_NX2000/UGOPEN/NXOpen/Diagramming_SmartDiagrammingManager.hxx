#ifndef NXOpen_DIAGRAMMING_SMARTDIAGRAMMINGMANAGER_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_SMARTDIAGRAMMINGMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_SmartDiagrammingManager.ja
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
#include <NXOpen/Diagramming_ReferenceGeometry.hxx>
#include <NXOpen/Diagramming_ReferenceGeometryBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_diagramming_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Diagramming
    {
        class SmartDiagrammingManager;
    }
    class Part;
    namespace Diagramming
    {
        class ReferenceGeometry;
    }
    namespace Diagramming
    {
        class ReferenceGeometryBuilder;
    }
    namespace Diagramming
    {
        class SmartDiagrammingManagerImpl;
        /** A manager to deal with all objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  SmartDiagrammingManager
        {
            private: SmartDiagrammingManagerImpl * m_smartdiagrammingmanager_impl;
            private: NXOpen::Part* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit SmartDiagrammingManager(NXOpen::Part *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~SmartDiagrammingManager();
            /** Creates a @link NXOpen::Diagramming::ReferenceGeometryBuilder NXOpen::Diagramming::ReferenceGeometryBuilder@endlink . 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::ReferenceGeometryBuilder * CreateReferenceGeometryBuilder
            (
                NXOpen::Diagramming::ReferenceGeometry * referenceGeometry /** @link NXOpen::Diagramming::ReferenceGeometry NXOpen::Diagramming::ReferenceGeometry@endlink  to be edited, if NULL then create a new one */
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