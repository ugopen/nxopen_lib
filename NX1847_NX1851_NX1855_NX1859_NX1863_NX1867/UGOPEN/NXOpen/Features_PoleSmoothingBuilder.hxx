#ifndef NXOpen_FEATURES_POLESMOOTHINGBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_POLESMOOTHINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_PoleSmoothingBuilder.ja
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
#include <NXOpen/GeometricUtilities_Continuity.hxx>
#include <NXOpen/GeometricUtilities_ControlPoleManagerData.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class PoleSmoothingBuilder;
    }
    class Direction;
    class Face;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class Continuity;
    }
    namespace GeometricUtilities
    {
        class ControlPoleManagerData;
    }
    class SelectFace;
    namespace Features
    {
        class _PoleSmoothingBuilderBuilder;
        class PoleSmoothingBuilderImpl;
        /**
            Represents a @link NXOpen::Features::PoleSmoothing NXOpen::Features::PoleSmoothing@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreatePoleSmoothingBuilder  NXOpen::Features::FeatureCollection::CreatePoleSmoothingBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ApplyConstraintsToAll </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ModificationPercentage </td> <td> 
         
        100 </td> </tr> 

        <tr><td> 
         
        MoveOnlySelectedPoles </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SmoothingFactor </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        UseSpecificDirection </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  PoleSmoothingBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: PoleSmoothingBuilderImpl * m_polesmoothingbuilder_impl;
            private: friend class  _PoleSmoothingBuilderBuilder;
            protected: PoleSmoothingBuilder();
            public: ~PoleSmoothingBuilder();
            /**Returns  the target face 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::SelectFace * TargetFace
            (
            );
            /**Returns  the indicator to move only selected poles 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: bool MoveOnlySelectedPoles
            (
            );
            /**Sets  the indicator to move only selected poles 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetMoveOnlySelectedPoles
            (
                bool moveOnlySelectedPoles /** moveonlyselectedpoles */ 
            );
            /**Returns  the selected poles, this is used only when @link MoveOnlySelectedPoles MoveOnlySelectedPoles @endlink and @link SetMoveOnlySelectedPoles SetMoveOnlySelectedPoles @endlink  is true 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricUtilities::ControlPoleManagerData * Poles
            (
            );
            /**Returns  the specific moving direction 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: bool UseSpecificDirection
            (
            );
            /**Sets  the specific moving direction 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetUseSpecificDirection
            (
                bool useSpecificDirection /** usespecificdirection */ 
            );
            /**Returns   the movement direction vector, this is used only when @link UseSpecificDirection UseSpecificDirection @endlink and @link SetUseSpecificDirection SetUseSpecificDirection @endlink  is true. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::Direction * MovementVector
            (
            );
            /**Sets   the movement direction vector, this is used only when @link UseSpecificDirection UseSpecificDirection @endlink and @link SetUseSpecificDirection SetUseSpecificDirection @endlink  is true. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetMovementVector
            (
                NXOpen::Direction * movementVector /** movementvector */ 
            );
            /**Returns  the indicator to apply the same constraint to all 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: bool ApplyConstraintsToAll
            (
            );
            /**Sets  the indicator to apply the same constraint to all 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetApplyConstraintsToAll
            (
                bool applyConstraintsToAll /** applyconstraintstoall */ 
            );
            /**Returns  the u minimum continuity constraint 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricUtilities::Continuity * UMinConstraint
            (
            );
            /**Returns  the u maximum continuity constraint 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricUtilities::Continuity * UMaxConstraint
            (
            );
            /**Returns  the v minimum continuity constraint 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricUtilities::Continuity * VMinConstraint
            (
            );
            /**Returns  the v maximum continuity constraint 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricUtilities::Continuity * VMaxConstraint
            (
            );
            /**Returns  the smoothing factor, the min and max values for this are (1 to 100) 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: int SmoothingFactor
            (
            );
            /**Sets  the smoothing factor, the min and max values for this are (1 to 100) 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetSmoothingFactor
            (
                int smoothingFactor /** smoothingfactor */ 
            );
            /**Returns  the modification percentage 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: int ModificationPercentage
            (
            );
            /**Sets  the modification percentage 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetModificationPercentage
            (
                int modificationPercentage /** modificationpercentage */ 
            );
            /**Returns  the number of poles selected 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: int NumberPolesSelected
            (
            );
            /**Sets  the number of poles selected 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetNumberPolesSelected
            (
                int numbePolesSelected /** numbepolesselected */ 
            );
            /**Returns the index of selected poles 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void GetSelectedPolesIndex
            (
                std::vector<int> & selectedPolesIndex /** selected poles index */ 
            );
            /**Sets the index of selected poles 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetSelectedPolesIndex
            (
                const std::vector<int> & selectedPolesIndex /** selected poles index */ 
            );
            /** Returns the indicator for creating a new copy 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: bool GetCreateNewCopy
            (
            );
            /** Sets the indicator for creating a new copy 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetCreateNewCopy
            (
                bool createNewCopy /** createnewcopy */ 
            );
            /** Removes parameters of a owning feature of a face to be smoothed 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void RemoveFeatureParameters
            (
                NXOpen::Face * face /** Face to be used for feature parameter removal */
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
