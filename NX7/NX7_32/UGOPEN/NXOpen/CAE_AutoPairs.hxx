#ifndef NXOpen_CAE_AUTOPAIRS_HXX_INCLUDED
#define NXOpen_CAE_AUTOPAIRS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AutoPairs.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class AutoPairs;
    }
    namespace CAE
    {
        class CAEBody;
    }
    namespace CAE
    {
        class CAEFace;
    }
    namespace CAE
    {
        class PropertyTable;
    }
    class NXObject;
    namespace CAE
    {
        class _AutoPairsBuilder;
        /**  @brief  Represents an autopairs obj  

           <br> This is a sub object <br> */
        class NXOPENCPPEXPORT AutoPairs : public NXObject
        {
            private: friend class  _AutoPairsBuilder;
            protected: AutoPairs();
            /** Set the list of @link CAE::CAEFace CAE::CAEFace@endlink    <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetFaces
            (
                const std::vector<NXOpen::CAE::CAEFace *> & faces /** Selected faces */
            );
            /** Get the list @link CAE::CAEFace CAE::CAEFace@endlink    <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void GetFaces
            (
                std::vector<NXOpen::CAE::CAEFace *> & faces /** Selected faces */
            );
            /** Set the list of @link CAE::CAEBody CAE::CAEBody@endlink     <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetBodies
            (
                const std::vector<NXOpen::CAE::CAEBody *> & faces /** Bodies  */
            );
            /** Get the list of @link CAE::CAEBody CAE::CAEBody@endlink    <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void GetBodies
            (
                std::vector<NXOpen::CAE::CAEBody *> & bodies /** Bodies */
            );
            /** Create face pairs whose distance is less than the distance tolerance stored
                        in the recipe. These faces are instances of @link CAE::CAEFace CAE::CAEFace@endlink   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void CreateFacePairs
            (
                std::vector<NXOpen::CAE::CAEFace *> & side1Faces /** side 1 faces */,
                std::vector<NXOpen::CAE::CAEFace *> & side2Faces /** side 2 faces */
            );
            /**Returns  the property table associated with the auto pairs object. 
                        The property table contains the parametes needed for the generation
                        of the face pairs. One of these parameters is the distance tolerance.   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::PropertyTable * PropertyTable
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
