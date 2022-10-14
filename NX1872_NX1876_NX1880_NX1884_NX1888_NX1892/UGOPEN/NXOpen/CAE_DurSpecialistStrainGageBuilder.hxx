#ifndef NXOpen_CAE_DURSPECIALISTSTRAINGAGEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTSTRAINGAGEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistStrainGageBuilder.ja
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
#include <NXOpen/CAE_DurSpecialistStrainGage.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class DurSpecialistStrainGageBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectFEElemFaceList;
    }
    namespace CAE
    {
        class SelectFENodeList;
    }
    class Expression;
    class SmartObject;
    namespace CAE
    {
        class _DurSpecialistStrainGageBuilderBuilder;
        class DurSpecialistStrainGageBuilderImpl;
        /** Represents a @link NXOpen::CAE::DurSpecialistStrainGageBuilder NXOpen::CAE::DurSpecialistStrainGageBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::CAE::DurSpecialistStrainGageCollection::CreateStrainGageBuilder  NXOpen::CAE::DurSpecialistStrainGageCollection::CreateStrainGageBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        GageType </td> <td> 
         
        UniAxial </td> </tr> 

        <tr><td> 
         
        Placement </td> <td> 
         
        Node </td> </tr> 

        <tr><td> 
         
        Plane </td> <td> 
         
        FacePlane </td> </tr> 

        <tr><td> 
         
        ShellElementFace </td> <td> 
         
        Top </td> </tr> 

        </table>  

         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistStrainGageBuilder : public NXOpen::Builder
        {
            private: DurSpecialistStrainGageBuilderImpl * m_durspecialiststraingagebuilder_impl;
            private: friend class  _DurSpecialistStrainGageBuilderBuilder;
            protected: DurSpecialistStrainGageBuilder();
            public: ~DurSpecialistStrainGageBuilder();
            /**Returns  the type of strain gage
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurspStrainGageType GageType
            (
            );
            /**Sets  the type of strain gage
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetGageType
            (
                NXOpen::CAE::DurspStrainGageType gageType /** gagetype */ 
            );
            /**Returns  the placement type of strain gage
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurspStrainGagePlacementType Placement
            (
            );
            /**Sets  the placement type of strain gage
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetPlacement
            (
                NXOpen::CAE::DurspStrainGagePlacementType gagePlacement /** gageplacement */ 
            );
            /**Returns  the shell element face location type of strain gage 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurspStrainGageShellElementFaceType ShellElementFace
            (
            );
            /**Sets  the shell element face location type of strain gage 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetShellElementFace
            (
                NXOpen::CAE::DurspStrainGageShellElementFaceType shellElementFace /** shell element face */ 
            );
            /**Returns  the destination nodes, 
                        Only available when the strain gage's placement type is DURSP_STRAIN_GAGE_placement_type_node  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectFENodeList * SelectedNode
            (
            );
            /**Returns   the selected element face.
                        Only available when the strain gage's placement type is DURSP_STRAIN_GAGE_placement_type_element_face_center  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectFEElemFaceList * SelectedElementFaces
            (
            );
            /**Returns  the orientation plane type of strain gage
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurspStrainGageOrientationPlane Plane
            (
            );
            /**Sets  the orientation plane type of strain gage
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetPlane
            (
                NXOpen::CAE::DurspStrainGageOrientationPlane plane /** plane */ 
            );
            /**Returns  the orientation direction, Only available when the strain gage's orientation plane type is CSYS 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SmartObject * Csys
            (
            );
            /**Sets  the orientation direction, Only available when the strain gage's orientation plane type is CSYS 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetCsys
            (
                NXOpen::SmartObject * orientationCoordSystem /** orientationcoordsystem */ 
            );
            /**Returns  the rotation angle, Only available when the strain gage's orientation plane type is CSYS 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RotationAngle
            (
            );
            /**Sets  the rotation angle, Only available when the strain gage's orientation plane type is CSYS 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetRotationAngle
            (
                NXOpen::Expression * rotationAngleTag /** rotationangletag */ 
            );
            /**Returns  the name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the description. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Description
            (
            );
            /**Sets  the description. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetDescription
            (
                const NXString & description /** description */ 
            );
            /**Sets  the description. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetDescription
            (
                const char * description /** description */ 
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