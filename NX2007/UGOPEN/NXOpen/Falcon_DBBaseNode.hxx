#ifndef NXOpen_FALCON_DBBASENODE_HXX_INCLUDED
#define NXOpen_FALCON_DBBASENODE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Falcon_DBBaseNode.ja
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
#include <NXOpen/libnxopencpp_falcon_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Falcon
    {
        class DBBaseNode;
    }
    class NXObject;
    namespace Falcon
    {
        class _DBBaseNodeBuilder;
        class DBBaseNodeImpl;

        /// \cond NX_NO_DOC 
        /** Represents DB Base non-displayable node  <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_FALCONEXPORT  DBBaseNode : public NXOpen::NXObject
        {
            private: DBBaseNodeImpl * m_dbbasenode_impl;
            private: friend class  _DBBaseNodeBuilder;
            protected: DBBaseNode();
            public: ~DBBaseNode();
        };

        /// \endcond 
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