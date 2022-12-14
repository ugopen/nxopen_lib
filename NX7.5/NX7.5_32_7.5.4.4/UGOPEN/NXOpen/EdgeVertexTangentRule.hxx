#ifndef NXOpen_EDGEVERTEXTANGENTRULE_HXX_INCLUDED
#define NXOpen_EDGEVERTEXTANGENTRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     EdgeVertexTangentRule.ja
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
#include <NXOpen/SelectionIntentRule.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class EdgeVertexTangentRule;
    class Edge;
    class SelectionIntentRule;
    class EdgeVertexTangentRuleImpl;
    /** Represents an edge vertex tangent rule */
    class NXOPENCPPEXPORT  EdgeVertexTangentRule : public SelectionIntentRule
    {
        private: EdgeVertexTangentRuleImpl * m_edgevertextangentrule_impl;
        public: explicit EdgeVertexTangentRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : None */
        public: virtual ~EdgeVertexTangentRule();
        /** Gets the data of the edge vertex tangent rule. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            NXOpen::Edge ** startEdge /** Start edge of edge tangent rule*/,
            bool* isFromStart /** True: the tangent starts from the start
                                                     point of the start edge if end edge is provided*/,
            double* angleTolerance /** Angle tolerance for tangent edges */,
            bool* hasSameConvexity /** True: will only find tangent edges that 
                                                         has the same convexity*/
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif
