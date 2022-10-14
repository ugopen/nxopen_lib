#ifndef NXOpen_CAE_STRESSLINEARIZATION_HXX_INCLUDED
#define NXOpen_CAE_STRESSLINEARIZATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_StressLinearization.ja
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
#include <NXOpen/CAE_StressLinearizationResult.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class StressLinearization;
    }
    namespace CAE
    {
        class QueryCurve;
    }
    namespace CAE
    {
        class StressLinearizationResult;
    }
    class Expression;
    class NXObject;
    namespace CAE
    {
        class _StressLinearizationBuilder;
        class StressLinearizationImpl;
        /** Represents a @link NXOpen::CAE::StressLinearization NXOpen::CAE::StressLinearization@endlink .  <br> To create or edit an instance of this class, use @link NXOpen::CAE::StressLinearizationBuilder  NXOpen::CAE::StressLinearizationBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  StressLinearization : public NXOpen::NXObject
        {
             /** Stress Linearization input and output entity
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::CAE::StressLinearizationResult::StressState NXOpen::CAE::StressLinearizationResult::StressState@endlink  instead. <br>  
            */
            public:
            struct NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::CAE::StressLinearizationResult::StressState instead.") StressState
            {
                public: /** Global Coordinates */NXOpen::Point3d Location;
                public: /** Local X Coordinate along SCL */double XLocal;
                public: /** xx */ double XX;
                public: /** yy */ double YY;
                public: /** zz */ double ZZ;
                public: /** xy */ double XY;
                public: /** yz */ double YZ;
                public: /** zx */ double ZX;
                public: /** sigma 11 */ double Sigma11;
                public: /** sigma 22 */ double Sigma22;
                public: /** sigma 33 */ double Sigma33;
                public: /** maxshear */ double MaxShear;
                public: /** intensity */ double Intensity;
                public: /** vonmises */ double VonMises;
                public: StressState() :
                    Location(),
                    XLocal(),
                    XX(),
                    YY(),
                    ZZ(),
                    XY(),
                    YZ(),
                    ZX(),
                    Sigma11(),
                    Sigma22(),
                    Sigma33(),
                    MaxShear(),
                    Intensity(),
                    VonMises()
                {
                }
                /** Constructor for the StressState struct. */ 
                public: StressState(const NXOpen::Point3d &locationInitial /** Global Coordinates */, 
                        double xLocalInitial /** Local X Coordinate along SCL */, 
                        double xXInitial /** xx */ , 
                        double yYInitial /** yy */ , 
                        double zZInitial /** zz */ , 
                        double xYInitial /** xy */ , 
                        double yZInitial /** yz */ , 
                        double zXInitial /** zx */ , 
                        double sigma11Initial /** sigma 11 */ , 
                        double sigma22Initial /** sigma 22 */ , 
                        double sigma33Initial /** sigma 33 */ , 
                        double maxShearInitial /** maxshear */ , 
                        double intensityInitial /** intensity */ , 
                        double vonMisesInitial /** vonmises */ ) :
                    Location(locationInitial),
                    XLocal(xLocalInitial),
                    XX(xXInitial),
                    YY(yYInitial),
                    ZZ(zZInitial),
                    XY(xYInitial),
                    YZ(yZInitial),
                    ZX(zXInitial),
                    Sigma11(sigma11Initial),
                    Sigma22(sigma22Initial),
                    Sigma33(sigma33Initial),
                    MaxShear(maxShearInitial),
                    Intensity(intensityInitial),
                    VonMises(vonMisesInitial)
                {
                }
            };


            /// \cond NX_NO_DOC 
             /** Selected tensors to compute for bending*/
            public:
            struct BendingTensors
            {
                public: /** xx */ bool XX;
                public: /** yy */ bool YY;
                public: /** zz */ bool ZZ;
                public: /** xy */ bool XY;
                public: /** yz */ bool YZ;
                public: /** zx */ bool ZX;
                public: BendingTensors() :
                    XX(),
                    YY(),
                    ZZ(),
                    XY(),
                    YZ(),
                    ZX()
                {
                }
                /** Constructor for the BendingTensors struct. */ 
                public: BendingTensors(bool xXInitial /** xx */ , 
                        bool yYInitial /** yy */ , 
                        bool zZInitial /** zz */ , 
                        bool xYInitial /** xy */ , 
                        bool yZInitial /** yz */ , 
                        bool zXInitial /** zx */ ) :
                    XX(xXInitial),
                    YY(yYInitial),
                    ZZ(zZInitial),
                    XY(xYInitial),
                    YZ(yZInitial),
                    ZX(zXInitial)
                {
                }
            };


            /// \endcond 
             /** Selected tensor components to compute for bending*/
            public:
            struct BendingTensorComponents
            {
                public: /** xx */ bool XX;
                public: /** yy */ bool YY;
                public: /** zz */ bool ZZ;
                public: /** xy */ bool XY;
                public: /** yz */ bool YZ;
                public: /** zx */ bool ZX;
                public: BendingTensorComponents() :
                    XX(),
                    YY(),
                    ZZ(),
                    XY(),
                    YZ(),
                    ZX()
                {
                }
                /** Constructor for the BendingTensorComponents struct. */ 
                public: BendingTensorComponents(bool xXInitial /** xx */ , 
                        bool yYInitial /** yy */ , 
                        bool zZInitial /** zz */ , 
                        bool xYInitial /** xy */ , 
                        bool yZInitial /** yz */ , 
                        bool zXInitial /** zx */ ) :
                    XX(xXInitial),
                    YY(yYInitial),
                    ZZ(zZInitial),
                    XY(xYInitial),
                    YZ(yZInitial),
                    ZX(zXInitial)
                {
                }
            };

            /** Result selection */
            public: enum ResultSelection
            {
                ResultSelectionFirst/** first */ ,
                ResultSelectionLast/** last */ ,
                ResultSelectionIndex/** index */ ,
                ResultSelectionAll/** all */ ,
                ResultSelectionFirstToIndex/** first to index */ ,
                ResultSelectionIndexToLast/** index to last */ ,
                ResultSelectionByName/** by name */ 
            };

            /** Result type */
            public: enum ResultType
            {
                ResultTypeStressElemental/** stress elemental */ ,
                ResultTypeStressElementNodal/** stress element nodal */ 
            };

            /** Structure type */
            public: enum StructureTypes
            {
                StructureTypesNonaxisymmetric/** nonaxisymmetric */ ,
                StructureTypesAxisymmetric/** axisymmetric */ 
            };

            /** SCL ends support */
            public: enum SclEndsSupports
            {
                SclEndsSupportsUnknown/** unknown */  = -1,
                SclEndsSupportsPoints/** points */ ,
                SclEndsSupportsNodes/** nodes */ 
            };

             /** Stress Linearization input and constant entity */
            public:
            struct Parameters
            {
                public: /** Start point A; can be applied in both 3d and 2d */NXOpen::Point3d A;
                public: /** End point B; can be applied in both 3d and 2d */NXOpen::Point3d B;
                public: /** Axis of symmetry */NXOpen::Vector3d AxisSymmetry;
                public: /** Radial axis */NXOpen::Vector3d AxisRadial;
                public: /** Local coordinate system; can be applied in both 3d and 2d */NXOpen::Matrix3x3 LocalCsys;
                public: /** Distance between start point and axis of symmetry */double RA;
                public: /** Distance between end point and axis of symmetry */double RB;
                public: /** Distance between middle point and axis of symmetry */double RC;
                public: /** Thickness of SCL; can be applied in both 3d and 2d */double T;
                public: /** Cosine phi */double CosPhi;
                public: /** Distance from mid-surface to neutral axis */double Xf;
                public: /** Distance from mid-surface to neutral axis, on hoop direction */double Xh;
                public: /** Interval length calculated by Thickness / Num of intervals */double D;
                public: Parameters() :
                    A(),
                    B(),
                    AxisSymmetry(),
                    AxisRadial(),
                    LocalCsys(),
                    RA(),
                    RB(),
                    RC(),
                    T(),
                    CosPhi(),
                    Xf(),
                    Xh(),
                    D()
                {
                }
                /** Constructor for the Parameters struct. */ 
                public: Parameters(const NXOpen::Point3d &aInitial /** Start point A; can be applied in both 3d and 2d */, 
                        const NXOpen::Point3d &bInitial /** End point B; can be applied in both 3d and 2d */, 
                        const NXOpen::Vector3d &axisSymmetryInitial /** Axis of symmetry */, 
                        const NXOpen::Vector3d &axisRadialInitial /** Radial axis */, 
                        const NXOpen::Matrix3x3 &localCsysInitial /** Local coordinate system; can be applied in both 3d and 2d */, 
                        double rAInitial /** Distance between start point and axis of symmetry */, 
                        double rBInitial /** Distance between end point and axis of symmetry */, 
                        double rCInitial /** Distance between middle point and axis of symmetry */, 
                        double tInitial /** Thickness of SCL; can be applied in both 3d and 2d */, 
                        double cosPhiInitial /** Cosine phi */, 
                        double xfInitial /** Distance from mid-surface to neutral axis */, 
                        double xhInitial /** Distance from mid-surface to neutral axis, on hoop direction */, 
                        double dInitial /** Interval length calculated by Thickness / Num of intervals */) :
                    A(aInitial),
                    B(bInitial),
                    AxisSymmetry(axisSymmetryInitial),
                    AxisRadial(axisRadialInitial),
                    LocalCsys(localCsysInitial),
                    RA(rAInitial),
                    RB(rBInitial),
                    RC(rCInitial),
                    T(tInitial),
                    CosPhi(cosPhiInitial),
                    Xf(xfInitial),
                    Xh(xhInitial),
                    D(dInitial)
                {
                }
            };

            private: StressLinearizationImpl * m_stresslinearization_impl;
            private: friend class  _StressLinearizationBuilder;
            protected: StressLinearization();
            public: ~StressLinearization();
            /**Returns  the name of the Stress Linearization 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString Name
            (
            );
            /**Returns  the description of the Stress Linearization 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString Description
            (
            );
            /**Returns  the query curve 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::QueryCurve * Scl
            (
            );
            /**Returns  the query curve ends type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::StressLinearization::SclEndsSupports SclEnds
            (
            );
            /**Returns  the name of load case 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString LoadCaseName
            (
            );
            /**Returns  the iteration selection 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::StressLinearization::ResultSelection IterationSelection
            (
            );
            /**Returns  the iteration index.
                        Warning: Returned iteration index starts at 1.
                    
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::CAE::StressLinearization::IterationRange NXOpen::CAE::StressLinearization::IterationRange@endlink  <br>  

             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::CAE::StressLinearization::IterationRange") int Iteration
            (
            );
            /**Returns  the iteration range as specified in the UI.
                        Warning: All iteration indices starts at 1.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString IterationRange
            (
            );
            /** Get the result type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::StressLinearization::ResultType GetResultType
            (
            );
            /**Returns  the number of intervals 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int NumIntervals
            (
            );
            /**Returns  the bending tensor components 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::StressLinearization::BendingTensorComponents BendingComponents
            (
            );
            /**Returns  the structure type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::StressLinearization::StructureTypes StructureType
            (
            );
            /**Returns  the radius of curvature 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::Expression * Rho
            (
            );
            /**Returns  the radius of curvature is infinite? 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool RhoInfinite
            (
            );
            /** Computes stress linearization of the points on a SCL
                        and returns all the stresses and invariants.
                        All the values are expressed in Part Base Unit
                        (@link NXOpen::UnitCollection::GetBase NXOpen::UnitCollection::GetBase@endlink ).
                        This method only works for single iteration Stress Linearization.
                      
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::CAE::StressLinearization::ComputeAll NXOpen::CAE::StressLinearization::ComputeAll@endlink  to take all iterations into account. <br>  

             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::CAE::StressLinearization::ComputeAll to take all iterations into account.") void Compute
            (
                NXOpen::CAE::StressLinearization::Parameters* parameters /** parameters */ ,
                std::vector<NXOpen::CAE::StressLinearization::StressState> & membranes /** membranes */ ,
                std::vector<NXOpen::CAE::StressLinearization::StressState> & bendings /** bendings */ ,
                std::vector<NXOpen::CAE::StressLinearization::StressState> & membranePlusBending /** membraneplusbending */ ,
                std::vector<NXOpen::CAE::StressLinearization::StressState> & peaks /** peaks */ ,
                std::vector<NXOpen::CAE::StressLinearization::StressState> & totals /** totals */ 
            );
            /** Computes stress linearization of the points on a SCL
                        and returns all the stresses and invariants.
                        All the values are expressed in Part Base Unit
                        (@link NXOpen::UnitCollection::GetBase NXOpen::UnitCollection::GetBase@endlink ).
                      
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void ComputeAll
            (
                NXOpen::CAE::StressLinearization::Parameters* parameters /** parameters */ ,
                std::vector<NXOpen::CAE::StressLinearizationResult *> & results /** results */ 
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