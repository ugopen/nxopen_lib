#ifndef NXOpen_FEATURES_WRAPGEOMETRYBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_WRAPGEOMETRYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_WrapGeometryBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_WrapGeometryBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class WrapGeometryBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class PlaneList;
    class SelectDisplayableObjectList;
    namespace Features
    {
        class _WrapGeometryBuilderBuilder;
        /**
            Represents a @link Features::WrapGeometry Features::WrapGeometry@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateWrapGeometryBuilder Features::FeatureCollection::CreateWrapGeometryBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AddOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        Associative </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CloseGaps </td> <td> 
         
        Sharp </td> </tr> 

        <tr><td> 
         
        DistTol </td> <td> 
         
        2.54 </td> </tr> 

        <tr><td> 
         
        IsInterpart </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SplitOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT WrapGeometryBuilder : public Features::FeatureBuilder
        {
            /** Represents the close gap type */
            public: enum CloseGapType
            {
                CloseGapTypeSharp/** sharp */ ,
                CloseGapTypeBeveled/** beveled */ ,
                CloseGapTypeNoOffset/** no offset */ 
            };

            private: friend class  _WrapGeometryBuilderBuilder;
            protected: WrapGeometryBuilder();
            /**Returns  the geometry to be wrapped (solid, sheet, curve, point)  <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * Geometry
            (
            );
            /**Returns  the Planes to split the geometry, tightens the wrap along this plane  <br> License requirements : None */
            public: NXOpen::PlaneList * PlanesList
            (
            );
            /**Returns   the  Remove parms switch  <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets   the  Remove parms switch  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the  Method used to close the gaps after offset of the wrap  <br> License requirements : None */
            public: NXOpen::Features::WrapGeometryBuilder::CloseGapType CloseGaps
            (
            );
            /**Sets  the  Method used to close the gaps after offset of the wrap  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCloseGaps
            (
                NXOpen::Features::WrapGeometryBuilder::CloseGapType closeGaps /** closegaps */ 
            );
            /**Returns  the  Additional offset. Will expand the wrap.  <br> License requirements : None */
            public: NXOpen::Expression * AddOffset
            (
            );
            /**Returns   the Offset applied to both sides of the splitting planes.  <br> License requirements : None */
            public: NXOpen::Expression * SplitOffset
            (
            );
            /**Returns  the Distance tolerance used to facet the solids. Also used for default offset calculation.  <br> License requirements : None */
            public: double DistTol
            (
            );
            /**Sets  the Distance tolerance used to facet the solids. Also used for default offset calculation.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDistTol
            (
                double distTol /** disttol */ 
            );
            /**Returns  the Setting that determines if this feature have interpart references  <br> License requirements : None */
            public: bool IsInterpart
            (
            );
            /**Sets  the Setting that determines if this feature have interpart references  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetInterpart
            (
                bool isInterpart /** isinterpart */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
