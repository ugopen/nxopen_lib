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
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

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
                    Represents a @link NXOpen::Features::SheetMetal::EditCornerBuilder NXOpen::Features::SheetMetal::EditCornerBuilder@endlink 
                     <br> To create a new instance of this class, use @link NXOpen::Features::SheetMetal::SheetmetalManager::CreateEditCornerBuilder  NXOpen::Features::SheetMetal::SheetmetalManager::CreateEditCornerBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            BendClosureType </term> <description> 
             
            Open </description> </item> 

            <item><term> 
             
            CornerReliefType </term> <description> 
             
            None </description> </item> 

            <item><term> 
             
            Diameter.Value </term> <description> 
             
            2.5 (millimeters part), 0.1 (inches part) </description> </item> 

            <item><term> 
             
            OverlapRatio.Value </term> <description> 
             
            1 </description> </item> 

            <item><term> 
             
            PlateClosureType </term> <description> 
             
            Closed </description> </item> 

            <item><term> 
             
            PlateGap.Value </term> <description> 
             
            0 (millimeters part), 0 (inches part) </description> </item> 

            </list> 

             <br>  Created in NX7.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  EditCornerBuilder : public NXOpen::Features::FeatureBuilder
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
                /**Returns  the bend type 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::EditCornerBuilder::BendClosureTypeOptions BendClosureType
                (
                );
                /**Sets  the bend type 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetBendClosureType
                (
                    NXOpen::Features::SheetMetal::EditCornerBuilder::BendClosureTypeOptions bends /** bends */ 
                );
                /**Returns  the plate type 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::EditCornerBuilder::PlateClosureTypeOptions PlateClosureType
                (
                );
                /**Sets  the plate type 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetPlateClosureType
                (
                    NXOpen::Features::SheetMetal::EditCornerBuilder::PlateClosureTypeOptions plates /** plates */ 
                );
                /**Returns  whether the overlap is reversed or not 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: bool ReverseOverlap
                (
                );
                /**Sets  whether the overlap is reversed or not 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetReverseOverlap
                (
                    bool reverseOverlap /** reverseoverlap */ 
                );
                /**Returns  the gap value between plates
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * PlateGap
                (
                );
                /**Returns  the overlap ratio between plates 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OverlapRatio
                (
                );
                /**Returns  the corner relief type 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::EditCornerBuilder::CornerReliefTypeOptions CornerReliefType
                (
                );
                /**Sets  the corner relief type 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetCornerReliefType
                (
                    NXOpen::Features::SheetMetal::EditCornerBuilder::CornerReliefTypeOptions cornerRelief /** cornerrelief */ 
                );
                /**Returns  the diameter for a circular cutout 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Diameter
                (
                );
                /** Add a face pair.
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void AddFacePair
                (
                    NXOpen::Face * firstFace /**  A bend face from a bend */,
                    NXOpen::Face * secondFace /**  A bend face from an adjacent bend */
                );
                /** Return the face pair. 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void GetFacePair
                (
                    int index /** Index of the desired face pair */,
                    NXOpen::Face ** firstFace /** First face of the face pair */,
                    NXOpen::Face ** secondFace /** Second face of the face pair */
                );
                /** Returns the number of face pairs already identified for the three bend corner feature.
                             @return  The number of face pairs currently identified 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: int GetNumberOfFacePairs
                (
                );
                /** Removes a face pair (that represents a unique corner) from the list of face pairs already added.
                            
                 <br>  Created in NX7.5.0.  <br>  
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
