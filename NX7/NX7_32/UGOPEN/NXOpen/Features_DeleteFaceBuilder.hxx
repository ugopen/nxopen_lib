#ifndef NXOpen_FEATURES_DELETEFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_DELETEFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DeleteFaceBuilder.ja
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
#include <NXOpen/Features_DeleteFaceBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class DeleteFaceBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    namespace Features
    {
        class _DeleteFaceBuilderBuilder;
        /**
            Represents a builder for a delete face feature, don't use it until nx502.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateDeleteFaceBuilder Features::FeatureCollection::CreateDeleteFaceBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        MaxHoleDiameter.Value </td> <td> 
         
        5.0 (millimeters part), 0.2 (inches part) </td> </tr> 

        <tr><td> 
         
        UseHoleDiameter </td> <td> 
         
        True </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT DeleteFaceBuilder : public Features::FeatureBuilder
        {
            /** Enumeration of select type, don't use it until nx502 */
            public: enum SelectTypes
            {
                SelectTypesFace/** This stands for delete face type. */,
                SelectTypesHole/** This stands for delete hole type. */
            };

            private: friend class  _DeleteFaceBuilderBuilder;
            protected: DeleteFaceBuilder();
            /**Returns  the delete face type, don't use it until nx502  <br> License requirements : None */
            public: NXOpen::Features::DeleteFaceBuilder::SelectTypes Type
            (
            );
            /**Sets  the delete face type, don't use it until nx502  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetType
            (
                NXOpen::Features::DeleteFaceBuilder::SelectTypes selectType /** the delete face type */
            );
            /**Returns  the face collector holding the faces to delete, don't use it until nx502  <br> License requirements : None */
            public: NXOpen::ScCollector * FaceCollector
            (
            );
            /**Returns  the flag of using hole diameter to filter hole or not, only for delete hole type and the max hole diameter should be
                        set if it is true, don't use it until nx502  <br> License requirements : None */
            public: bool UseHoleDiameter
            (
            );
            /**Sets  the flag of using hole diameter to filter hole or not, only for delete hole type and the max hole diameter should be
                        set if it is true, don't use it until nx502  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetUseHoleDiameter
            (
                bool useHoleDiameter /** the flag of use hole diameter */
            );
            /**Returns  the maximal diameter of deleted holes, only for delete hole type and only working when use_hole_diameter is true,
                        don't use it until nx502  <br> License requirements : None */
            public: NXOpen::Expression * MaxHoleDiameter
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
