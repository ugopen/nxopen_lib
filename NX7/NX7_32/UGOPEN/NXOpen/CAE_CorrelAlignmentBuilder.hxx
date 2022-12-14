#ifndef NXOpen_CAE_CORRELALIGNMENTBUILDER_HXX_INCLUDED
#define NXOpen_CAE_CORRELALIGNMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CorrelAlignmentBuilder.ja
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
#include <NXOpen/CAE_CorrelAlignmentBuilder.hxx>
#include <NXOpen/CAE_CorrelBaseBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class CorrelAlignmentBuilder;
    }
    namespace CAE
    {
        class CorrelBaseBuilder;
    }
    namespace CAE
    {
        class SelectFENode;
    }
    class Point;
    namespace CAE
    {
        class _CorrelAlignmentBuilderBuilder;
        /** This builder is used to control the alignment parameters of a @link CAE::CorrelSolution CAE::CorrelSolution@endlink   <br> To create a new instance of this class, use @link CAE::CorrelSolution::CreateAlignmentBuilder CAE::CorrelSolution::CreateAlignmentBuilder@endlink  <br> */
        class NXOPENCPPEXPORT CorrelAlignmentBuilder : public CAE::CorrelBaseBuilder
        {
            /** the way the scaling factor is computed */
            public: enum ScalingChoice
            {
                ScalingChoiceFromSecondAxis/** Computed from the lenght of the second axis */,
                ScalingChoiceSpecify/** User specified scaling factor */
            };

             /** Specifies the data for the selected reference points */
            public:
            struct ReferencePt
            {
                public: /** defined */ bool Defined;
                public: /** x */ double X;
                public: /** y */ double Y;
                public: /** z */ double Z;
                public: ReferencePt() :
                    Defined(),
                    X(),
                    Y(),
                    Z()
                {
                }
                /** Constructor for the ReferencePt struct. */ 
                public: ReferencePt(bool INIT_defined /** defined */ , 
                        double INIT_x /** x */ , 
                        double INIT_y /** y */ , 
                        double INIT_z /** z */ ) :
                    Defined(INIT_defined),
                    X(INIT_x),
                    Y(INIT_y),
                    Z(INIT_z)
                {
                }
            };

            private: friend class  _CorrelAlignmentBuilderBuilder;
            protected: CorrelAlignmentBuilder();
            /**Returns  the reference common origin node -- obsolete version 
             @deprecated Deprecated in NX6.0.2 <br> 
             <br> License requirements : None */
            public: NXOpen::CAE::SelectFENode * RefPt1
            (
            );
            /** Gets the reference common origin point  @return   <br> License requirements : None */
            public: NXOpen::CAE::CorrelAlignmentBuilder::ReferencePt GetReferencePt1
            (
            );
            /** Sets the reference common origin point  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetReferencePt1
            (
                const NXOpen::CAE::CorrelAlignmentBuilder::ReferencePt & referencePt1 /** referencept1 */ 
            );
            /**Returns  the working common origin point  <br> License requirements : None */
            public: NXOpen::Point * WrkPt1
            (
            );
            /**Sets  the working common origin point  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetWrkPt1
            (
                NXOpen::Point * wrkPt1 /** wrkpt1 */ 
            );
            /** Gets the working common origin point position  @return   <br> License requirements : None */
            public: NXOpen::CAE::CorrelAlignmentBuilder::ReferencePt GetWrkNode1
            (
            );
            /** Sets the working common origin point position  @return   <br> License requirements : nx_correl_base ("FE Correlation") */
            public: NXOpen::CAE::CorrelAlignmentBuilder::ReferencePt SetWrkNode1
            (
            );
            /**Returns  the reference first axis node -- obsolete version 
             @deprecated Deprecated in NX6.0.2 <br> 
             <br> License requirements : None */
            public: NXOpen::CAE::SelectFENode * RefPt2
            (
            );
            /** Gets the reference first axis origin point  @return   <br> License requirements : None */
            public: NXOpen::CAE::CorrelAlignmentBuilder::ReferencePt GetReferencePt2
            (
            );
            /** Sets the reference first axis origin point  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetReferencePt2
            (
                const NXOpen::CAE::CorrelAlignmentBuilder::ReferencePt & referencePt2 /** referencept2 */ 
            );
            /**Returns  the working first axis origin point  <br> License requirements : None */
            public: NXOpen::Point * WrkPt2
            (
            );
            /**Sets  the working first axis origin point  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetWrkPt2
            (
                NXOpen::Point * wrkPt2 /** wrkpt2 */ 
            );
            /** Gets the working first axis point position  @return   <br> License requirements : None */
            public: NXOpen::CAE::CorrelAlignmentBuilder::ReferencePt GetWrkNode2
            (
            );
            /** Sets the working first axis point position  @return   <br> License requirements : nx_correl_base ("FE Correlation") */
            public: NXOpen::CAE::CorrelAlignmentBuilder::ReferencePt SetWrkNode2
            (
            );
            /**Returns  the reference second axis node -- obsolete version 
             @deprecated Deprecated in NX6.0.2 <br> 
             <br> License requirements : None */
            public: NXOpen::CAE::SelectFENode * RefPt3
            (
            );
            /** Gets the reference second axis point  @return   <br> License requirements : None */
            public: NXOpen::CAE::CorrelAlignmentBuilder::ReferencePt GetReferencePt3
            (
            );
            /** Sets the reference second axis point  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetReferencePt3
            (
                const NXOpen::CAE::CorrelAlignmentBuilder::ReferencePt & referencePt3 /** referencept3 */ 
            );
            /**Returns  the working second axis point  <br> License requirements : None */
            public: NXOpen::Point * WrkPt3
            (
            );
            /**Sets  the working second axis point  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetWrkPt3
            (
                NXOpen::Point * wrkPt3 /** wrkpt3 */ 
            );
            /** Gets the working second axis point position  @return   <br> License requirements : None */
            public: NXOpen::CAE::CorrelAlignmentBuilder::ReferencePt GetWrkNode3
            (
            );
            /** Sets the working second axis point position  @return   <br> License requirements : nx_correl_base ("FE Correlation") */
            public: NXOpen::CAE::CorrelAlignmentBuilder::ReferencePt SetWrkNode3
            (
            );
            /**Returns  the scaling type  <br> License requirements : None */
            public: NXOpen::CAE::CorrelAlignmentBuilder::ScalingChoice ScalingType
            (
            );
            /**Sets  the scaling type  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetScalingType
            (
                NXOpen::CAE::CorrelAlignmentBuilder::ScalingChoice scalingType /** scalingtype */ 
            );
            /**Returns  the scaling value  <br> License requirements : None */
            public: double ScalingValue
            (
            );
            /**Sets  the scaling value  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetScalingValue
            (
                double scalingValue /** scalingvalue */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
