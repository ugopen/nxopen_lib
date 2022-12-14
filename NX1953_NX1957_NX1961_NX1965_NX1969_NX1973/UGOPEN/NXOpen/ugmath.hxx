#ifndef NXOpen_UGMATH_HXX_INCLUDED
#define NXOpen_UGMATH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ugmath.ja
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

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
     /** Represents three-dimensional cartesian coordinates for a point 
     <br>  Created in NX3.0.0.  <br>  
    */

    struct Point3d
    {
        public: /** x */ double X;
        public: /** y */ double Y;
        public: /** z */ double Z;
        public: Point3d() :
            X(),
            Y(),
            Z()
        {
        }
        /** Constructor for the Point3d struct. */ 
        public: Point3d(double xInitial /** x */ , 
                double yInitial /** y */ , 
                double zInitial /** z */ ) :
            X(xInitial),
            Y(yInitial),
            Z(zInitial)
        {
        }
    };

     /** Represents a three-dimensional vector 
     <br>  Created in NX3.0.0.  <br>  
    */

    struct Vector3d
    {
        public: /** x */ double X;
        public: /** y */ double Y;
        public: /** z */ double Z;
        public: Vector3d() :
            X(),
            Y(),
            Z()
        {
        }
        /** Constructor for the Vector3d struct. */ 
        public: Vector3d(double xInitial /** x */ , 
                double yInitial /** y */ , 
                double zInitial /** z */ ) :
            X(xInitial),
            Y(yInitial),
            Z(zInitial)
        {
        }
    };

     /** Represents a 3 x 3 matrix 
     <br>  Created in NX3.0.0.  <br>  
    */

    struct Matrix3x3
    {
        public: /** xx */ double Xx;
        public: /** xy */ double Xy;
        public: /** xz */ double Xz;
        public: /** yx */ double Yx;
        public: /** yy */ double Yy;
        public: /** yz */ double Yz;
        public: /** zx */ double Zx;
        public: /** zy */ double Zy;
        public: /** zz */ double Zz;
        public: Matrix3x3() :
            Xx(),
            Xy(),
            Xz(),
            Yx(),
            Yy(),
            Yz(),
            Zx(),
            Zy(),
            Zz()
        {
        }
        /** Constructor for the Matrix3x3 struct. */ 
        public: Matrix3x3(double xxInitial /** xx */ , 
                double xyInitial /** xy */ , 
                double xzInitial /** xz */ , 
                double yxInitial /** yx */ , 
                double yyInitial /** yy */ , 
                double yzInitial /** yz */ , 
                double zxInitial /** zx */ , 
                double zyInitial /** zy */ , 
                double zzInitial /** zz */ ) :
            Xx(xxInitial),
            Xy(xyInitial),
            Xz(xzInitial),
            Yx(yxInitial),
            Yy(yyInitial),
            Yz(yzInitial),
            Zx(zxInitial),
            Zy(zyInitial),
            Zz(zzInitial)
        {
        }
    };

     /** Represents two-dimensional cartesian coordinates for a point 
     <br>  Created in NX6.0.0.  <br>  
    */

    struct Point2d
    {
        public: /** x */ double X;
        public: /** y */ double Y;
        public: Point2d() :
            X(),
            Y()
        {
        }
        /** Constructor for the Point2d struct. */ 
        public: Point2d(double xInitial /** x */ , 
                double yInitial /** y */ ) :
            X(xInitial),
            Y(yInitial)
        {
        }
    };

     /** Represents four-dimensional homogeneous coordinates for a point.
        To convert to three-dimensional cartesian coordinates, 
        divide x, y and z by w.

     <br>  Created in NX8.5.0.  <br>  
    */

    struct Point4d
    {
        public: /** x */ double X;
        public: /** y */ double Y;
        public: /** z */ double Z;
        public: /** weight */double W;
        public: Point4d() :
            X(),
            Y(),
            Z(),
            W()
        {
        }
        /** Constructor for the Point4d struct. */ 
        public: Point4d(double xInitial /** x */ , 
                double yInitial /** y */ , 
                double zInitial /** z */ , 
                double wInitial /** weight */) :
            X(xInitial),
            Y(yInitial),
            Z(zInitial),
            W(wInitial)
        {
        }
    };

     /** Represents a homogenous coordinate system transformation matrix.

     <br>  Created in NX1847.0.0.  <br>  
    */

    struct Matrix4x4
    {
        public: /** rxx */ double Rxx;
        public: /** rxy */ double Rxy;
        public: /** rxz */ double Rxz;
        public: /** x translation*/double Xt;
        public: /** ryx */ double Ryx;
        public: /** ryy */ double Ryy;
        public: /** ryz */ double Ryz;
        public: /** y translation*/double Yt;
        public: /** rzx */ double Rzx;
        public: /** rzy */ double Rzy;
        public: /** rzz */ double Rzz;
        public: /** zt */ double Zt;
        public: /** must be 0*/double Sx;
        public: /** must be 0*/double Sy;
        public: /** must be 0*/double Sz;
        public: /** 1.0/scale.*/double Ss;
        public: Matrix4x4() :
            Rxx(),
            Rxy(),
            Rxz(),
            Xt(),
            Ryx(),
            Ryy(),
            Ryz(),
            Yt(),
            Rzx(),
            Rzy(),
            Rzz(),
            Zt(),
            Sx(),
            Sy(),
            Sz(),
            Ss()
        {
        }
        /** Constructor for the Matrix4x4 struct. */ 
        public: Matrix4x4(double rxxInitial /** rxx */ , 
                double rxyInitial /** rxy */ , 
                double rxzInitial /** rxz */ , 
                double xtInitial /** x translation*/, 
                double ryxInitial /** ryx */ , 
                double ryyInitial /** ryy */ , 
                double ryzInitial /** ryz */ , 
                double ytInitial /** y translation*/, 
                double rzxInitial /** rzx */ , 
                double rzyInitial /** rzy */ , 
                double rzzInitial /** rzz */ , 
                double ztInitial /** zt */ , 
                double sxInitial /** must be 0*/, 
                double syInitial /** must be 0*/, 
                double szInitial /** must be 0*/, 
                double ssInitial /** 1.0/scale.*/) :
            Rxx(rxxInitial),
            Rxy(rxyInitial),
            Rxz(rxzInitial),
            Xt(xtInitial),
            Ryx(ryxInitial),
            Ryy(ryyInitial),
            Ryz(ryzInitial),
            Yt(ytInitial),
            Rzx(rzxInitial),
            Rzy(rzyInitial),
            Rzz(rzzInitial),
            Zt(ztInitial),
            Sx(sxInitial),
            Sy(syInitial),
            Sz(szInitial),
            Ss(ssInitial)
        {
        }
    };

}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#endif
