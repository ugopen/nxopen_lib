#ifndef NXOpen_BODY_HXX_INCLUDED
#define NXOpen_BODY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Body.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/IBody.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/IOrientation.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Body;
    class BasePart;
    class DisplayableObject;
    class Edge;
    class Face;
    namespace Features
    {
        class Feature;
    }
    class IBody;
    class INXObject;
    class IOrientation;
    class NXObject;
    class _BodyBuilder;
    /** 
    Represents a Body
    */
    class NXOPENCPPEXPORT Body : public DisplayableObject, public virtual IOrientation, public virtual IBody
    {
        private: friend class  _BodyBuilder;
        protected: Body();
        /** Returns the features used to construct the body  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: std::vector<NXOpen::Features::Feature *> GetFeatures
        (
        );
        /** Returns the faces in the body  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: std::vector<NXOpen::Face *> GetFaces
        (
        );
        /** Returns the edges in the body  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: std::vector<NXOpen::Edge *> GetEdges
        (
        );
        /**Returns  the solid density of the body  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: double Density
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Density() Density@endlink instead.
        @deprecated
        */
        public: double GetDensity
        (
        ) { return this->Density(); }
        /**Sets  the solid density of the body  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetDensity
        (
            double density /** */
        );
        /**Returns  true if the body is a sheet body  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: bool IsSheetBody
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link IsSheetBody() IsSheetBody@endlink instead.
        @deprecated
        */
        public: bool GetIsSheetBody
        (
        ) { return this->IsSheetBody(); }
        /**Returns  true if the body is a solid body  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: bool IsSolidBody
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link IsSolidBody() IsSolidBody@endlink instead.
        @deprecated
        */
        public: bool GetIsSolidBody
        (
        ) { return this->IsSolidBody(); }
    };
}
#undef EXPORTLIBRARY
#endif
