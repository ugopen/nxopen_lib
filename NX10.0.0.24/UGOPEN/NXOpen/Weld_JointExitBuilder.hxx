#ifndef NXOpen_WELD_JOINTEXITBUILDER_HXX_INCLUDED
#define NXOpen_WELD_JOINTEXITBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_JointExitBuilder.ja
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
#include <NXOpen/LineWelds.hxx>
#include <NXOpen/Weld_WeldJointBuilder.hxx>
#include <NXOpen/Weld_JointExitBuilder.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class JointExitBuilder;
    }
    namespace Weld
    {
        class WeldJointBuilder;
    }
    namespace Weld
    {
        class _JointExitBuilderBuilder;
        class JointExitBuilderImpl;
        /** Used to set custom edge preparation parameters of a @link NXOpen::Weld::WeldJoint NXOpen::Weld::WeldJoint@endlink  feaure.  <br> To create a new instance of this class, use @link NXOpen::Weld::WeldManager::CreateJointExitBuilder  NXOpen::Weld::WeldManager::CreateJointExitBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        NumberSegments </td> <td> 
         
        2 </td> </tr> 

        <tr><td> 
         
        RootOpening </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SplitAngle </td> <td> 
         
        5.0 </td> </tr> 

        </table>  

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  JointExitBuilder : public NXOpen::Weld::WeldJointBuilder
        {
            /** Settings to indicate the desired position of edge preporation thickness and angle. */
            public: enum Positions
            {
                PositionsUpperChamfer/** the upper chamfer position */,
                PositionsUpper/** the upper position */,
                PositionsMiddle/** the middle position */,
                PositionsLower/** the lower position */,
                PositionsLowerChamfer/** the lower chamfer position */
            };

            /** Settings to indicate the side the positions should be applied to. */
            public: enum BodySide
            {
                BodySideFirst/** the first side. For fillet welds only this needs to be specified. */,
                BodySideSecond/** the other side. This is only used for butt welds. */
            };

             /** The structure for defining fillet weld lengths. */
            public:
            struct  FilletSizes
            {
                public: /** The fillet weld throat thickness */double ThroatThickness;
                public: /** The fillet weld first length.    */double LegLength1;
                public: /** The fillet weld second length.   */double LegLength2;
                public: FilletSizes() :
                    ThroatThickness(),
                    LegLength1(),
                    LegLength2()
                {
                }
                /** Constructor for the FilletSizes struct. */ 
                public: FilletSizes(double throatThicknessInitial /** The fillet weld throat thickness */, 
                        double legLength1Initial /** The fillet weld first length.    */, 
                        double legLength2Initial /** The fillet weld second length.   */) :
                    ThroatThickness(throatThicknessInitial),
                    LegLength1(legLength1Initial),
                    LegLength2(legLength2Initial)
                {
                }
            };

            private: JointExitBuilderImpl * m_jointexitbuilder_impl;
            private: friend class  _JointExitBuilderBuilder;
            protected: JointExitBuilder();
            public: ~JointExitBuilder();
            /**Returns  the desired gap between bodies being welded 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double RootOpening
            (
            );
            /**Sets  the desired gap between bodies being welded 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: void SetRootOpening
            (
                double rootOpening /** rootopening */ 
            );
            /**Returns  the side edge preparation values will be applied to 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::JointExitBuilder::BodySide Side
            (
            );
            /**Sets  the side edge preparation values will be applied to 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: void SetSide
            (
                NXOpen::Weld::JointExitBuilder::BodySide side /** side */ 
            );
            /**Returns  the weld finish method 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::FinishMethod FinishMethod
            (
            );
            /**Sets  the weld finish method 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: void SetFinishMethod
            (
                NXOpen::Annotations::FinishMethod method /** method */ 
            );
            /**Returns  the symbol for welding other side when it is not being prepared 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::Symbol OtherSideSymbol
            (
            );
            /**Sets  the symbol for welding other side when it is not being prepared 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: void SetOtherSideSymbol
            (
                NXOpen::Annotations::Symbol symbol /** symbol */ 
            );
            /** Gets the thickness and angle combination to set for the desired weld position 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void GetEdgePrepValues
            (
                NXOpen::Weld::JointExitBuilder::Positions position /** Position of edge preparation values to set. */,
                double* thickness /** The thickness depth for this position. */,
                double* angle /** The angle of edge preporation for this position. */
            );
            /** This method should be called multiple times.  First set the BodySide then call this method for each Position.
                      For Butt welds this function should be used to set each side. After the primary side is set, change
                      the BodySide and call this method for the secondary side. For Fillet welds, only the primary side needs to be set.
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: void SetEdgePrepValues
            (
                NXOpen::Weld::JointExitBuilder::Positions position /** Position of edge preparation values to set. */,
                double thickness /** The thickness depth for this position. */,
                double angle /** The angle of edge preporation for this position. */
            );
            /** Gets the fillet weld values for the side of the welding joint.  @return  The fillet sizes for the side of the welding joint 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::JointExitBuilder::FilletSizes GetFilletLengths
            (
            );
            /** Sets the fillet weld values for the side of the welding joint. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: void SetFilletLengths
            (
                const NXOpen::Weld::JointExitBuilder::FilletSizes & sizes /** The fillet sizes for the side of the welding joint */
            );
            /** Gets the fillet weld values for the opposite side of the welding joint.  @return  The fillet sizes for the opposite side of the welding joint 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::JointExitBuilder::FilletSizes GetOppositeFilletLengths
            (
            );
            /** Sets the fillet weld values for the opposite side of the welding joint. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: void SetOppositeFilletLengths
            (
                const NXOpen::Weld::JointExitBuilder::FilletSizes & sizes /** The fillet sizes for the opposite side of the welding joint */
            );
            /** Sets the symmetric fillet weld values for a welding joint. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: void SetBothFilletLengths
            (
                const NXOpen::Weld::JointExitBuilder::FilletSizes & sizes /** The symmetric fillet sizes for both sides of the welding joint */
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