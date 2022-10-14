#ifndef NXOpen_FEATURES_BLOCK_HXX_INCLUDED
#define NXOpen_FEATURES_BLOCK_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Block.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class Block;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _BlockBuilder;
        class BlockImpl;
        /** Represents a block feature. */
        class NXOPENCPPEXPORT  Block : public Features::BodyFeature
        {
            private: BlockImpl * m_block_impl;
            private: friend class  _BlockBuilder;
            protected: Block();
            public: ~Block();
        };
    }
}
#undef EXPORTLIBRARY
#endif