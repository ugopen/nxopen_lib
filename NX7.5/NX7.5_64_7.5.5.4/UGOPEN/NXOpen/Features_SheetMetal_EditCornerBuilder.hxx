#ifndef NXOpen_FEATURES_SHEETMETAL_EDITCORNERBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_EDITCORNERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_EditCornerBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_SheetMetal_EditCornerBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class EditCornerBuilder;
        }
    }
    class Expression;
    class Face;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class _EditCornerBuilderBuilder;
            class EditCornerBuilderImpl;
            /**
                    Represents a @link Features::SheetMetal::EditCornerBuilder Features::SheetMetal::EditCornerBuilder@endlink 
                     <br> To create a new instance of this class, use @link Features::SheetMetal::SheetmetalManager::CreateEditCornerBuilder Features::SheetMetal::SheetmetalManager::CreateEditCornerBuilder@endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            BendClosureType </td> <td> 
             
            Open </td> </tr> 

            <tr><td> 
             
            CornerReliefType </td> <td> 
             
            None </td> </tr> 

            <tr><td> 
             
            Diameter.Value </td> <td> 
             
            2.5 (millimeters part), 0.1 (inches part) </td> </tr> 

            <tr><td> 
             
            OverlapRatio.Value </td> <td> 
             
            1 </td> </tr> 

            <tr><td> 
             
            PlateClosureType </td> <td> 
             
            Closed </td> </tr> 

            <tr><td> 
             
            PlateGap.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            </table>  
            */
            class NXOPENCPPEXPORT  EditCornerBuilder : public Features::FeatureBuilder
            {
                /** This enum specifies the type of bend closure required at the corner. */
                public: enum BendClosureTypeOptions
                {
                    BendClosureTypeOptionsOpen/** open */ ,
                    BendClosureTypeOptionsClosed/** closed */ 
                };

                /** This enum specifies the type of plate closure required at the corner. */
                public: enum PlateClosureTypeOptions
                {
                    PlateClosureTypeOptionsClosed/** closed */ ,
                    PlateClosureTypeOptionsOverlapped/** overlapped */ 
                };

                /** This enum specifies the type of relief required at the corner.*/
                public: enum CornerReliefTypeOptions
                {
                    CornerReliefTypeOptionsNone/** none */ ,
                    CornerReliefTypeOptionsCircularCutout/** circular cutout */ 
                };

                private: EditCornerBuilderImpl * m_editcornerbuilder_impl;
                private: friend class  _EditCornerBuilderBuilder;
                protected: EditCornerBuilder();
                public: ~EditCornerBuilder();
                /**Returns  the bend type  <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::EditCornerBuilder::BendClosureTypeOptions BendClosureType
                (
                );
                /**Sets  the bend type  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetBendClosureType
                (
                    NXOpen::Features::SheetMetal::EditCornerBuilder::BendClosureTypeOptions bends /** bends */ 
                );
                /**Returns  the plate type  <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::EditCornerBuilder::PlateClosureTypeOptions PlateClosureType
                (
                );
                /**Sets  the plate type  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetPlateClosureType
                (
                    NXOpen::Features::SheetMetal::EditCornerBuilder::PlateClosureTypeOptions plates /** plates */ 
                );
                /**Returns  whether the overlap is reversed or not  <br> License requirements : None */
                public: bool ReverseOverlap
                (
                );
                /**Sets  whether the overlap is reversed or not  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetReverseOverlap
                (
                    bool reverseOverlap /** reverseoverlap */ 
                );
                /**Returns  the gap value between plates <br> License requirements : None */
                public: NXOpen::Expression * PlateGap
                (
                );
                /**Returns  the overlap ratio between plates  <br> License requirements : None */
                public: NXOpen::Expression * OverlapRatio
                (
                );
                /**Returns  the corner relief type  <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::EditCornerBuilder::CornerReliefTypeOptions CornerReliefType
                (
                );
                /**Sets  the corner relief type  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetCornerReliefType
                (
                    NXOpen::Features::SheetMetal::EditCornerBuilder::CornerReliefTypeOptions cornerRelief /** cornerrelief */ 
                );
                /**Returns  the diameter for a circular cutout  <br> License requirements : None */
                public: NXOpen::Expression * Diameter
                (
                );
                /** Add a face pair. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void AddFacePair
                (
                    NXOpen::Face * firstFace /**  A bend face from a bend */,
                    NXOpen::Face * secondFace /**  A bend face from an adjacent bend */
                );
                /** Return the face pair.  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void GetFacePair
                (
                    int index /** Index of the desired face pair */,
                    NXOpen::Face ** firstFace /** First face of the face pair */,
                    NXOpen::Face ** secondFace /** Second face of the face pair */
                );
                /** Returns the number of face pairs already identified for the three bend corner feature.
                             @return  The number of face pairs currently identified  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: int GetNumberOfFacePairs
                (
                );
                /** Removes a face pair (that represents a unique corner) from the list of face pairs already added.
                             <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void RemoveFacePair
                (
                    NXOpen::Face * firstFace /** A face from an already selected face pair */,
                    NXOpen::Face * secondFace /** The other face from the face pair */
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
