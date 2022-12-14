#ifndef NXOpen_DIAGRAMMING_LEADERLINEBUILDER_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_LEADERLINEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_LeaderLineBuilder.ja
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
#include <NXOpen/Diagramming_DataType.hxx>
#include <NXOpen/Diagramming_SheetElement.hxx>
#include <NXOpen/Diagramming_SheetElementBuilder.hxx>
#include <NXOpen/ugmath.hxx>
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
        class LeaderLineBuilder;
    }
    namespace Diagramming
    {
        class SheetElement;
    }
    namespace Diagramming
    {
        class SheetElementBuilder;
    }
    namespace Diagramming
    {
        class _LeaderLineBuilderBuilder;
        class LeaderLineBuilderImpl;
        /**
            Represents a LeaderLineBuilder.
             <br> To create a new instance of this class, use @link NXOpen::Diagramming::LeaderLineCollection::CreateLeaderLineBuilder  NXOpen::Diagramming::LeaderLineCollection::CreateLeaderLineBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  LeaderLineBuilder : public NXOpen::Diagramming::SheetElementBuilder
        {
            /** Represents the option @link NXOpen::Diagramming::LeaderLineBuilder::VerticalAlignment NXOpen::Diagramming::LeaderLineBuilder::VerticalAlignment@endlink 
                       for a @link NXOpen::Diagramming::LeaderLineBuilder NXOpen::Diagramming::LeaderLineBuilder@endlink .
                    
             <br>  Created in NX10.0.0.  <br>  
            */
            public: enum VerticalAlignmentOption
            {
                VerticalAlignmentOptionTop/** Setting the vertical alignment top*/,
                VerticalAlignmentOptionMiddle/** Setting the vertical alignment middle*/,
                VerticalAlignmentOptionBottom/** Setting the vertical alignment bottom*/
            };

            private: LeaderLineBuilderImpl * m_leaderlinebuilder_impl;
            private: friend class  _LeaderLineBuilderBuilder;
            protected: LeaderLineBuilder();
            public: ~LeaderLineBuilder();
            /**Returns  the stub length of this leader line. The negative value is not expected.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double StubLength
            (
            );
            /**Sets  the stub length of this leader line. The negative value is not expected.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStubLength
            (
                double stubLength /** stublength */ 
            );
            /**Returns  the stub sides of this leader line.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::DiagrammingStubsides StubSides
            (
            );
            /**Sets  the stub sides of this leader line.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStubSides
            (
                NXOpen::Diagramming::DiagrammingStubsides stubSides /** stubsides */ 
            );
            /**Returns  the vertical alignment option. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::LeaderLineBuilder::VerticalAlignmentOption VerticalAlignment
            (
            );
            /**Sets  the vertical alignment option. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetVerticalAlignment
            (
                NXOpen::Diagramming::LeaderLineBuilder::VerticalAlignmentOption alignmentOption /** alignmentoption */ 
            );
            /**Returns  the arrow type of the end arrow 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::DiagrammingArrowtype ArrowType
            (
            );
            /**Sets  the arrow type of the end arrow 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetArrowType
            (
                NXOpen::Diagramming::DiagrammingArrowtype arrowTypeOption /** arrowtypeoption */ 
            );
            /** Get bending points for polyline to render the leader line. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void GetBendPoints
            (
                std::vector<NXOpen::Point2d> & points /** points */ 
            );
            /** Set bending points for polyline to render the leader line. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBendPoints
            (
                const std::vector<NXOpen::Point2d> & points /** points */ 
            );
            /** Sets the terminator of the leader. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTerminator
            (
                NXOpen::Diagramming::SheetElement * terminator /** terminator */ ,
                int segmentId /** segmentid */ ,
                double percentX /** percentx */ ,
                double inputX /** inputx */ ,
                double percentY /** percenty */ ,
                double inputY /** inputy */ 
            );
            /** Gets the terminator of the leader. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void GetTerminator
            (
                NXOpen::Diagramming::SheetElement ** terminator /** terminator */ ,
                int* segmentId /** segmentid */ ,
                double* percentX /** percentx */ ,
                double* inputX /** inputx */ ,
                double* percentY /** percenty */ ,
                double* inputY /** inputy */ 
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
