/*
==============================================================================
 
        Copyright (c) 2017 Siemens Product Lifecycle Management Software Inc.
                         Unpublished - All rights reserved

==============================================================================

 Description
    This file contains helper functions for handling Matrix calculations


==============================================================================*/
using NXOpen;
using System;

namespace CAMSetupImport
{
    public static class MatrixHelper
    {
        public static Matrix3x3 Multiply(this Matrix3x3 m1, Matrix3x3 m2)
        {
            Matrix3x3 result = new Matrix3x3();
            result.Xx = m1.Xx * m2.Xx + m1.Yx * m2.Xy + m1.Zx * m2.Xz;
            result.Xy = m1.Xy * m2.Xx + m1.Yy * m2.Xy + m1.Zy * m2.Xz;
            result.Xz = m1.Xz * m2.Xx + m1.Yz * m2.Xy + m1.Zz * m2.Xz;
            result.Yx = m1.Xx * m2.Yx + m1.Yx * m2.Yy + m1.Zx * m2.Yz;
            result.Yy = m1.Xy * m2.Yx + m1.Yy * m2.Yy + m1.Zy * m2.Yz;
            result.Yz = m1.Xz * m2.Yx + m1.Yz * m2.Yy + m1.Zz * m2.Yz;
            result.Zx = m1.Xx * m2.Zx + m1.Yx * m2.Zy + m1.Zx * m2.Zz;
            result.Zy = m1.Xy * m2.Zx + m1.Yy * m2.Zy + m1.Zy * m2.Zz;
            result.Zz = m1.Xz * m2.Zx + m1.Yz * m2.Zy + m1.Zz * m2.Zz;
            return result;
        }

        public static Vector3d Multiply(this Matrix3x3 m, Vector3d v)
        {
            Vector3d result = new Vector3d();
            result.X = m.Xx * v.X + m.Yx * v.Y + m.Zx * v.Z;
            result.Y = m.Xy * v.X + m.Yy * v.Y + m.Zy * v.Z;
            result.Z = m.Xz * v.X + m.Yz * v.Y + m.Zz * v.Z;
            return result;
        }

        public static Matrix3x3 ConvertToMatrix(double alpha, double beta, double gamma)
        {
            Matrix3x3 matrix = new Matrix3x3();
            var cosA = Math.Cos(alpha);
            var cosB = Math.Cos(beta);
            var cosC = Math.Cos(gamma);
            var sinA = Math.Sin(alpha);
            var sinB = Math.Sin(beta);
            var sinC = Math.Sin(gamma);

            matrix.Xx = cosA * cosC - sinA * cosB * sinC;
            matrix.Xy = -cosA * sinC - sinA * cosB * cosC;
            matrix.Xz = sinA * sinB;
            matrix.Yx = sinA * cosC + cosA * cosB * sinC;
            matrix.Yy = -sinA * sinC + cosA * cosB * cosC;
            matrix.Yz = -cosA * sinB;
            matrix.Zx = sinB * sinC;
            matrix.Zy = sinB * cosC;
            matrix.Zz = cosB;
            return matrix;
        }
    }
}

