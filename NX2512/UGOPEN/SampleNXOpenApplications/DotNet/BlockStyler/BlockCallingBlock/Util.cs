/*==================================================================================================

            Copyright (c) 2015 Unigraphics Solutions Inc.
                   Unpublished - All rights reserved

====================================================================================================
File description:

External utility functions for Journalling and Automation support. 

Note: This file is clone of nxopenuf/uf/Util.cs for internal wraptest module, both the files should be in sync.

====================================================================================================
   Date      Name                    Description of Change
09-Sep-2015  Prabhakar Mandlik       Modifications for UFWRAPTEST. 
15-Jul-2016  Prabhakar Mandlik       ARCH11211: Modified code for ITI Support in UFWrapper for .Net.
15-Jul-2016  Debarshi Goswami        ARCH11211: Added functions ConvertStructStringstoUTF8 and ConvertStructStringsFromUTF8 to handle conversion of struct
                                     string fields. Also fixed some existing Util functions to Call JAM api for international string conversion.
17-Jul-2017  Debarshi Goswami        8341395: Added if check to avoid processing Null Strings
13-Jun-2018  Sudhir Pawar            PR#9180546: Added if check to avoid processing Null Strings
20-Apr-2022  Piyush Kakadiya         PR#10129684: Added ArrayToSM functions for marshalling.
$HISTORY$
==================================================================================================*/
using System;
using System.Runtime.InteropServices;
using System.Diagnostics;
using System.Text;
using System.Globalization;
using System.Collections.Generic;
using System.Reflection;
using System.Linq;
using NXOpen;
using NXOpen.Utilities;

namespace NXOpen.UF
{
    [Serializable, AttributeUsage(AttributeTargets.Delegate)]
    public sealed class CallConvCdeclAttribute : Attribute
    {
        public CallConvCdeclAttribute()
        {
        }
    }

    internal class Util
    {
        [DllImport("libjam.dll", CallingConvention = CallingConvention.Cdecl, EntryPoint = "JAM_sm_length")]
        internal static unsafe extern int SM_length(void* ptr);

        [DllImport("libjam.dll", CallingConvention = CallingConvention.Cdecl, EntryPoint = "JAM_sm_free")]
        internal static unsafe extern void SM_free(void* ptr);

        [DllImport("libjam.dll", CallingConvention = CallingConvention.Cdecl, EntryPoint = "JAM_sm_alloc")]
        internal static unsafe extern IntPtr SM_alloc(int nBytes);

        [DllImport("libjam", CallingConvention = CallingConvention.Cdecl, CharSet = CharSet.Ansi)]
        [return: MarshalAs(UnmanagedType.U1)]
        static extern bool JAM_is_in_utf8_mode();
        //  <BJS> 30-June-2004
        //  This gets the encoding for "locale" strings (does assume the thread this will be called in
        //  has the matching info - but this should be the main thread in our case).
        public static Encoding localeEncoding = null;

        public static Encoding GetLocaleEncoding()
        {
            if (localeEncoding == null)
                localeEncoding = JAM_is_in_utf8_mode() ? Encoding.UTF8 : Encoding.GetEncoding(CultureInfo.CurrentCulture.TextInfo.ANSICodePage);
            return localeEncoding;
        }

        /* Converts sbyte* into string i.e. Compatible to C code*/
        internal static unsafe string ArrayFromPointer(int len, sbyte* src)
        {
            String result = JAM.ToStringFromLocale((IntPtr)src, false);

            if (localeEncoding == null)
                localeEncoding = GetLocaleEncoding();

            int utf8_byte_count = localeEncoding.GetByteCount(result);
            if (len > 0 && utf8_byte_count > len)
                throw new Exception(String.Format("Length of string array does not match with length provided."));

            return result;
        }
        internal static unsafe string ArrayFromPointerString(sbyte* src)
        {
            return new String(src);
        }
        internal static unsafe int[] ArrayFromPointer(int len, int* src)
        {
            int[] result = new int[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            return result;
        }

        internal static unsafe uint[] ArrayFromPointer(int len, uint* src)
        {
            uint[] result = new uint[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            return result;
        }

        internal static unsafe float[] ArrayFromPointer(int len, float* src)
        {
            float[] result = new float[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            return result;
        }

        internal static unsafe double[] ArrayFromPointer(int len, double* src)
        {
            double[] result = new double[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            return result;
        }


        internal static unsafe Tag[] ArrayFromPointer(int len, Tag* src)
        {
            Tag[] result = new Tag[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            return result;
        }

        internal static unsafe string[] ArrayFromPointer(int n_char, int n_strings, sbyte* src)
        {
            int i = 0;
            sbyte* temp_src = src;
            string[] result = new String[n_strings];
            for (i = 0; i < n_strings; i++)
            {
                byte[] bytes = new byte[n_char];
                if (n_char > 0)
                    Marshal.Copy((IntPtr)temp_src, bytes, 0, n_char);

                if (localeEncoding == null)
                    localeEncoding = GetLocaleEncoding();

                result[i] = localeEncoding.GetString(bytes);
                temp_src = temp_src + n_char;
            }
            return result;
        }

        internal static unsafe string ArrayFromSM(sbyte* src)
        {
            // Frees input string by default
            String result = JAM.ToStringFromLocale((IntPtr)src);
            return result;
        }

        internal static unsafe string[] ArrayFromSM(int n_strings, sbyte** src)
        {
            int i = 0;
            string[] result = new String[n_strings];
            for (i = 0; i < n_strings; i++)
            {
                result[i] = JAM.ToStringFromLocale((IntPtr)src[i]);
            }
            SM_free(src);
            return result;
        }
        internal static unsafe string[] ArrayFromSM(uint n_strings, sbyte** src)
        {
            int i = 0;
            string[] result = new String[n_strings];
            for (i = 0; i < n_strings; i++)
            {
                result[i] = JAM.ToStringFromLocale((IntPtr)src);
            }
            SM_free(src);
            return result;
        }
        internal static unsafe Tag[][] ArrayFromSM(int[] count_array, Tag** src)
        {
            int ii = 0, jj = 0, kk = 0;
            Tag[][] temp = new Tag[count_array.Length][];
            for (ii = 0; ii < count_array.Length; ii++)
            {
                temp[ii] = new Tag[count_array[ii]];
            }
            for (jj = 0; jj < count_array.Length; jj++)
            {
                for (kk = 0; kk < count_array[jj]; kk++)
                {
                    temp[jj][kk] = src[jj][kk];
                }
            }
            for (ii = 0; ii < count_array.Length; ii++)
            {
                SM_free(src[ii]);
            }
            SM_free(src);
            // free memory
            return temp;
        }
        internal static unsafe int[][] ArrayFromSM(int[] count_array, int** src)
        {
            int ii = 0, jj = 0, kk = 0;
            int[][] temp = new int[count_array.Length][];
            for (ii = 0; ii < count_array.Length; ii++)
            {
                temp[ii] = new int[count_array[ii]];
            }
            for (jj = 0; jj < count_array.Length; jj++)
            {
                for (kk = 0; kk < count_array[jj]; kk++)
                {
                    temp[jj][kk] = src[jj][kk];
                }
            }
            for (ii = 0; ii < count_array.Length; ii++)
            {
                SM_free(src[ii]);
            }
            SM_free(src);
            // free memory
            return temp;
        }
        internal static unsafe uint[][] ArrayFromSM(int[] count_array, uint** src)
        {
            int ii = 0, jj = 0, kk = 0;
            uint[][] temp = new uint[count_array.Length][];
            for (ii = 0; ii < count_array.Length; ii++)
            {
                temp[ii] = new uint[count_array[ii]];
            }
            for (jj = 0; jj < count_array.Length; jj++)
            {
                for (kk = 0; kk < count_array[jj]; kk++)
                {
                    temp[jj][kk] = src[jj][kk];
                }
            }
            for (ii = 0; ii < count_array.Length; ii++)
            {
                SM_free(src[ii]);
            }
            SM_free(src);
            // free memory
            return temp;
        }
        internal static unsafe double[][] ArrayFromSM(int[] count_array, double** src)
        {
            int ii = 0, jj = 0, kk = 0;
            double[][] temp = new double[count_array.Length][];
            for (ii = 0; ii < count_array.Length; ii++)
            {
                temp[ii] = new double[count_array[ii]];
            }
            for (jj = 0; jj < count_array.Length; jj++)
            {
                for (kk = 0; kk < count_array[jj]; kk++)
                {
                    temp[jj][kk] = src[jj][kk];
                }
            }
            for (ii = 0; ii < count_array.Length; ii++)
            {
                SM_free(src[ii]);
            }
            SM_free(src);
            // free memory
            return temp;
        }

        //        internal static unsafe int [] ArrayFromSM(int n, int *src)
        //        {
        //            int [] result = new int[n];
        //            for (int i = 0; i < n; i++)
        //                result[i] = src[i];
        //            SM_free(src);
        //            return result;
        //        }

        internal static unsafe int[] ArrayFromSM(int n, int* src)
        {
            return ArrayFromSM(src);
        }

        internal static unsafe int[] ArrayFromSM(int* src)
        {
            int len = SM_length(src) / 4;
            int[] result = new int[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            SM_free(src);
            return result;
        }
        internal static unsafe IntPtr[] ArrayFromSM(int n, IntPtr* src)
        {
            int len = SM_length(src) / System.IntPtr.Size;
            IntPtr[] result = new IntPtr[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            SM_free(src);
            return result;
        }

        internal static unsafe uint[] ArrayFromSM(uint* src)
        {
            int len = SM_length(src) / 4;
            uint[] result = new uint[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            SM_free(src);
            return result;
        }

        internal static unsafe uint[] ArrayFromSM(byte* src)
        {
            int len = SM_length(src) / 2;
            uint[] result = new uint[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            SM_free(src);
            return result;
        }

        internal static unsafe bool[] ArrayFromSM(bool* src)
        {
            int len = SM_length(src) / 1;
            bool[] result = new bool[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            SM_free(src);
            return result;
        }


        internal static unsafe byte[][] ArrayFromSM(byte** src)
        {
            byte[][] tempArray = new byte[1][];
            tempArray[0] = new byte[1];
            return tempArray;
        }


        //        internal static unsafe Tag [] ArrayFromSM(int n, Tag *src)
        //        {
        //            Tag [] result = new Tag [n];
        //            for (int i = 0; i < n; i++)
        //                result[i] = src[i];
        //            SM_free(src);
        //            return result;
        //        }
        internal static unsafe Tag[] ArrayFromSM(int n, Tag* src)
        {
            return ArrayFromSM(src);
        }

        internal static unsafe Tag[] ArrayFromSM(Tag* src)
        {
            int len = SM_length(src) / 4;
            Tag[] result = new Tag[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            SM_free(src);
            return result;
        }

        //        internal static unsafe double [] ArrayFromSM(int n, double *src)
        //        {
        //            double [] result = new double[n];
        //            for (int i = 0; i < n; i++)
        //                result[i] = src[i];
        //            SM_free(src);
        //            return result;
        //        }
        internal static unsafe double[] ArrayFromSM(int n, double* src)
        {
            return ArrayFromSM(src);
        }

        internal static unsafe byte[] ArrayFromSM(int n, byte* src)
        {
            byte[] result = new byte[n];
            for (int i = 0; i < n; i++)
                result[i] = src[i];
            SM_free(src);
            return result;
        }

        internal static unsafe byte[] ArrayFromSM(int n, sbyte* src)
        {
            byte[] result = new byte[n];
            for (int i = 0; i < n; i++)
                result[i] = (byte)src[i];
            SM_free(src);
            return result;
        }
        internal static unsafe double[] ArrayFromSM(double* src)
        {
            int len = SM_length(src) / 8;
            double[] result = new double[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            SM_free(src);
            return result;
        }

        internal static unsafe float[] ArrayFromSM(float* src)
        {
            int len = SM_length(src) / 4;
            float[] result = new float[len];
            for (int i = 0; i < len; i++)
                result[i] = src[i];
            SM_free(src);
            return result;
        }

        //        internal static unsafe Array ArrayFromSM(Type type, int n, IntPtr ptr)
        //        {
        //            // FIXME: write this
        //            return null;
        //        }

        internal static unsafe double[,] Array2DFromSM(int lenA, int lenB, double* src)
        {
            double[,] result = new double[lenA, lenB];
            int k = 0;
            for (int i = 0; i < lenA; i++)
                for (int j = 0; j < lenB; j++)
                    result[i, j] = src[k++];
            SM_free(src);
            return result;
        }

        internal static unsafe double[,] Array2DFromSM(double* src)
        {
            int len = SM_length(src) / 4;
            double[,] result = new double[len, 4];
            int k = 0;
            for (int i = 0; i < len; i++)
                for (int j = 0; j < 4; j++)
                    result[i, j] = src[k++];
            SM_free(src);
            return result;
        }

        [DllImport("libufun.dll", CallingConvention = CallingConvention.Cdecl, CharSet = CharSet.Ansi, EntryPoint = "UF_MODL_ask_list_count")]
        internal static extern int AskListCount
        (
            IntPtr list,    /* pointer to struct uf_list_s I */
            out int count    /* pointer to int O */
        );

        [DllImport("libufun.dll", CallingConvention = CallingConvention.Cdecl, CharSet = CharSet.Ansi, EntryPoint = "UF_MODL_delete_list")]
        public static extern int DeleteList
        (
            ref IntPtr list    /* pointer to pointer to struct uf_list_s I */
        );

        [DllImport("libufun.dll", CallingConvention = CallingConvention.Cdecl, CharSet = CharSet.Ansi, EntryPoint = "UF_MODL_ask_list_item")]
        internal static extern int AskListItem
        (
            IntPtr list,    /* pointer to struct uf_list_s I */
            int index,    /* int I */
            out Tag @object    /* pointer to tag_t O */
        );

        [DllImport("libufun.dll", CallingConvention = CallingConvention.Cdecl, CharSet = CharSet.Ansi, EntryPoint = "UF_MODL_create_list")]
        internal static extern int CreateList
        (
            out IntPtr list    /* pointer to pointer to struct uf_list_s O */
        );


        [DllImport("libufun.dll", CallingConvention = CallingConvention.Cdecl, CharSet = CharSet.Ansi, EntryPoint = "UF_MODL_put_list_item")]
        internal static extern int PutListItem
        (
            IntPtr list,    /* pointer to struct uf_list_s I */
            Tag obj_id    /* tag_t I */
        );

        internal static Tag[] ArrayFromList(IntPtr ufList)
        {
            int count;
            AskListCount(ufList, out count);
            Tag[] res = new Tag[count];
            for (int i = 0; i < count; i++)
                AskListItem(ufList, i, out res[i]);
            DeleteList(ref ufList);
            return res;
        }

        internal static IntPtr ListFromArray(Tag[] array)
        {
            IntPtr res;
            CreateList(out res);
            for (int i = 0; i < array.Length; i++)
                PutListItem(res, array[i]);
            return res;
        }

        internal static unsafe int* ArrayToPointer(int[] array)
        {
            if (array == null)
                return null;
            int* result = (int*)Marshal.AllocHGlobal(array.Length);
            for (int ii = 0; ii < array.Length; ii++)
            {
                result[ii] = array[ii];
            }
            return result;
        }

        internal static unsafe uint* ArrayToPointer(uint[] array)
        {
            if (array == null)
                return null;
            uint* result = (uint*)Marshal.AllocHGlobal(array.Length);
            for (int ii = 0; ii < array.Length; ii++)
            {
                result[ii] = array[ii];
            }
            return result;

        }

        internal static unsafe double* ArrayToPointer(double[] array)
        {
            if (array == null)
                return null;
            double* result = (double*)Marshal.AllocHGlobal(array.Length);
            for (int ii = 0; ii < array.Length; ii++)
            {
                result[ii] = array[ii];
            }
            return result;

        }

        internal static unsafe Tag* ArrayToPointer(Tag[] array)
        {
            if (array == null)
                return null;
            Tag* result = (Tag*)Marshal.AllocHGlobal(array.Length);
            for (int ii = 0; ii < array.Length; ii++)
            {
                result[ii] = array[ii];
            }
            return result;
        }

        internal static unsafe sbyte* ArrayToPointer(string array)
        {
            if (array == null)
                return null;
            IntPtr result = JAM.ToLocaleString(array);
            return (sbyte*)result;
        }

        /*Converts string to IntPtr. Compatible to CSharp code*/
        internal static unsafe IntPtr ArrayToPointer(string array, int array_length)
        {
            if (array == null)
                return IntPtr.Zero;

            if (localeEncoding == null)
                localeEncoding = GetLocaleEncoding();

            int utf8_byte_count = localeEncoding.GetByteCount(array);
            if (array_length > 0 && utf8_byte_count > array_length)
                throw new Exception(String.Format("Length of string array does not match with length provided."));

            IntPtr result = JAM.ToLocaleString(array);
            return result;

        }

        internal static unsafe void StringToArray(string s, int array_length, sbyte* array)
        {
            if (s == null)
                array[0] = 0;
            else
            {
                //Array length check
                if (localeEncoding == null)
                    localeEncoding = GetLocaleEncoding();

                int utf8_byte_count = localeEncoding.GetByteCount(s);
                if (array_length > 0 && utf8_byte_count > array_length)
                    throw new Exception(String.Format("Length of String array does not match with length provided."));

                IntPtr ptrSrc = JAM.ToLocaleString(s);
                IntPtr ptrDst = (IntPtr)array;

                byte[] data = new byte[array_length];
                Marshal.Copy(ptrSrc, data, 0, array_length);
                Marshal.WriteByte(data, data.Length, (byte)'\0');
                Marshal.Copy(data, 0, ptrDst, data.Length);

            }
        }

        internal static unsafe void FreePointer(Tag* pointer)
        {
            Marshal.FreeHGlobal((IntPtr)pointer);
        }

        internal static unsafe void FreePointer(int* pointer)
        {
            Marshal.FreeHGlobal((IntPtr)pointer);
        }

        internal static unsafe void FreePointer(uint* pointer)
        {
            Marshal.FreeHGlobal((IntPtr)pointer);
        }

        internal static unsafe void FreePointer(double* pointer)
        {
            Marshal.FreeHGlobal((IntPtr)pointer);
        }

        internal static unsafe void FreePointer(sbyte* pointer)
        {
            Marshal.FreeHGlobal((IntPtr)pointer);
        }

        internal static unsafe void FreePointer(sbyte* pointer, bool is_SM)
        {
            SM_free((void*)pointer);
        }
        internal static unsafe sbyte** ArrayToPointer(string[] array)
        {
            if (array == null)
                return null;
            sbyte** result = (sbyte**)SM_alloc(array.Length * sizeof(sbyte*));
            for (int i = 0; i < array.Length; i++)
            {
                if (array[i] == null)
                    result[i] = null;
                else
                {
                    result[i] = (sbyte*)JAM.ToLocaleString(array[i]);
                }
            }
            return result;
        }
        internal static NXException CreateException(int errorCode)
        {
            return NXException.Create(errorCode);
        }

        // <BJS> 23-Aug-2005
        // Following utilities convert from 2d arrays to 1d arrays
        // and back but with the same memory layout. This is to
        // work aroung a bug on x64 when pinvoke seems to not cope
        // with 2d arrays.
        internal static int[] ToSingleArray(int[,] array2d)
        {
            if (array2d == null)
                return null;
            int[] array1d = new int[array2d.Length];
            int n = array2d.GetLength(0);
            int m = array2d.GetLength(1);
            int k = 0;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    array1d[k++] = array2d[i, j];
            return array1d;
        }

        internal static double[] ToSingleArray(double[,] array2d)
        {
            if (array2d == null)
                return null;
            double[] array1d = new double[array2d.Length];
            int n = array2d.GetLength(0);
            int m = array2d.GetLength(1);
            int k = 0;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    array1d[k++] = array2d[i, j];
            return array1d;
        }

        internal static void To2DArray(int[] array1d, int[,] array2d)
        {
            int n = array2d.GetLength(0);
            int m = array2d.GetLength(1);
            int k = 0;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    array2d[i, j] = array1d[k++];
        }

        internal static void To2DArray(double[] array1d, double[,] array2d)
        {
            int n = array2d.GetLength(0);
            int m = array2d.GetLength(1);
            int k = 0;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    array2d[i, j] = array1d[k++];
        }

        internal static IntPtr[] ToStringArrayFromPointers(string[] in_strings)
        {
            IntPtr[] LOCAL_s1 = JAM.ToLocaleStringArray(in_strings);
            return LOCAL_s1;
        }

        //  <agrawals>  14-Aug-2015
        //  We are exposing UF_initialize and inside we have to set Text mode 
        //  Hence wrapping these two functions here so that we can call them inside .Net bindings
        [Serializable]
        internal enum ModeS
        {
            Locale = 0,
            Utf8 = 1,
            AllUtf8 = 2
        }
        [DllImport("libufun.dll", CallingConvention = CallingConvention.Cdecl, CharSet = CharSet.Ansi, EntryPoint = "UF_TEXT_ask_text_mode")]
        internal static extern ModeS _AskTextMode
        (
        );

        internal static ModeS AskTextMode()
        {
            ModeS ret = _AskTextMode();
            return ret;
        }

        [DllImport("libufun.dll", CallingConvention = CallingConvention.Cdecl, CharSet = CharSet.Ansi, EntryPoint = "UF_TEXT_set_text_mode")]
        internal static extern int _SetTextMode
        (
            ModeS mode    /* enum UF_TEXT_mode_s I */
        );
        internal static int SetTextMode
        (
            ModeS mode    /* enum UF_TEXT_mode_s */
        )
        {
            int ret = _SetTextMode(mode);
            return ret;
        }

        // Function for converting .Net managed strings to byte[] (for char[])
        // We are using byte[] here instead of IntPtr or sbyte* because char[] inside
        // a sturct behaves differently and IntPtr and sbyte* can only hold first char correctly
        // Considering UTF-8 will be the default codeset for UF
        internal static unsafe byte[] ToUTF8BytesFromString(string s, int len)
        {
            if (s == null)
                return null;

            else
            {
                if (localeEncoding == null)
                    localeEncoding = GetLocaleEncoding();
                byte[] bytes = localeEncoding.GetBytes(s);
                byte[] retPtr = null;
                if (len == 0)
                    retPtr = new byte[localeEncoding.GetByteCount(s)];
                else
                    retPtr = new byte[len];
                bytes.CopyTo(retPtr, 0);

                return retPtr;
            }
        }

        // Assuming UF default codeset is UTF-8
        private static unsafe int strlen(byte[] str)
        {
            int len = 0;
            while (str[len] != 0)
                len++;
            return len;
        }

        private static byte[] GetActualByteArr(byte[] byte_arr)
        {
            int len = strlen(byte_arr);
            byte[] ret_val = new byte[len];
            Array.Copy(byte_arr, ret_val, len);
            return ret_val;
        }

        internal static unsafe string ToStringFromUTF8Bytes(byte[] bytes)
        {
            if (localeEncoding == null)
                localeEncoding = GetLocaleEncoding();

            byte[] actual = GetActualByteArr(bytes);
            return localeEncoding.GetString(actual);
        }

        internal static unsafe string[] ToStringArrayFromLocale(int count, IntPtr[] strings)
        {
            string[] res = new string[count];
            for (int i = 0; i < count; i++)
            {
                res[i] = JAM.ToStringFromLocale(strings[i]);
            }
            return res;
        }

        internal static unsafe IntPtr ConvertStringArrayToPointer(string[] array)
        {
            if (array == null)
                return IntPtr.Zero;
            sbyte** result = (sbyte**)SM_alloc(array.Length * sizeof(sbyte*));
            for (int i = 0; i < array.Length; i++)
            {
                if (array[i] == null)
                    result[i] = null;
                else
                {
                    IntPtr utf8_string = JAM.ToLocaleString(array[i]);
                    result[i] = (sbyte*)utf8_string;
                }
            }
            return (IntPtr)result;
        }

        internal static unsafe void ConvertNestedStructStringstoUTF8(dynamic inStruct, ref IntPtr outStructPtr, Type outStructType, Dictionary<string, int> array_len_info)
        {
            IntPtr copy_ptr = Marshal.AllocHGlobal(Marshal.SizeOf(inStruct));
            Marshal.StructureToPtr(inStruct, copy_ptr, false);
            dynamic out_struct_obj = Activator.CreateInstance(outStructType);
            out_struct_obj = Marshal.PtrToStructure(copy_ptr, outStructType);
            out_struct_obj = Util.ConvertStructStringstoUTF8(inStruct, out_struct_obj, array_len_info);
            outStructPtr = Marshal.AllocHGlobal(Marshal.SizeOf(out_struct_obj));
            Marshal.StructureToPtr(out_struct_obj, outStructPtr, false);
        }


        internal static unsafe dynamic ConvertNestedStructStringsFromUTF8(IntPtr inStruct, dynamic outStruct, Type inStructType, Dictionary<string, int> array_len_info)
        {
            dynamic in_struct_obj = Activator.CreateInstance(inStructType);
            in_struct_obj = Marshal.PtrToStructure(inStruct, inStructType);
            return Util.ConvertStructStringsFromUTF8(in_struct_obj, outStruct, array_len_info);
        }

        // Function for converting .Net managed string (Unicode) to unmagaed UTF-8 codeset. This function is typically used for inputs
        // inStruct: A managed struct exposed to UF .net users
        // outStruct: An unmanaged struct used to pass values to unmanaged C UF.
        // array_len_info: An Dictionary of Key Value pair of Struct string array member and their length. Only required for char**
        internal static unsafe dynamic ConvertStructStringstoUTF8(dynamic inStruct, dynamic outStruct, Dictionary<string, int> array_len_info)
        {
            Type inStructType = inStruct.GetType();
            Type outStructType = outStruct.GetType();
            dynamic retObject = outStruct;

            FieldInfo[] inStructInfo = inStructType.GetFields(BindingFlags.Instance |
                                                    BindingFlags.NonPublic |
                                                    BindingFlags.Public);
            FieldInfo[] outStructInfo = outStructType.GetFields(BindingFlags.Instance |
                                                    BindingFlags.NonPublic |
                                                    BindingFlags.Public);

            var in_out_struct_info = inStructInfo.Zip(outStructInfo, (in_field, out_field) => new { InField = in_field, OutField = out_field });
            foreach (var field in in_out_struct_info)
            {
                // char*
                // Managed: string
                // Unsafe: sbyte*
                if (field.InField.FieldType == typeof(System.String) && field.OutField.FieldType == typeof(System.SByte*))
                {
                    // Convert the string to UTF-8 codeset
                    //sbyte* str = ConvertStringToPinter(field.InField.GetValue(inStruct));
                    IntPtr str = JAM.ToLocaleString(field.InField.GetValue(inStruct));
                    field.OutField.SetValueDirect(__makeref(retObject), str);
                }

                // char []
                // Managed: string
                // Unsafe: byte[]
                else if (field.InField.FieldType == typeof(System.String) &&
                    (field.OutField.FieldType.IsArray && field.OutField.FieldType.GetElementType() == typeof(System.Byte)))
                {
                    // This field may have a fixed size and we assume size is at least mentioned in unmanaged struct
                    // Retrieve the size of the array from Marshal Attribute. This is the size declared in C function.
                    int array_size = 0;
                    object[] marshal_attrs = field.OutField.GetCustomAttributes(typeof(MarshalAsAttribute), false);
                    if (marshal_attrs != null && marshal_attrs.Length > 0)
                    {
                        MarshalAsAttribute marshal = (MarshalAsAttribute)marshal_attrs[0];
                        if (marshal != null)
                        {
                            array_size = marshal.SizeConst;
                        }
                    }

                    if (localeEncoding == null)
                        localeEncoding = GetLocaleEncoding();

                    string inString = field.InField.GetValue(inStruct);
                    /*<Sudhir Pawar>  13-Jun-2018
                        PR#9180546: Added if check to avoid processing Null Strings
                    */
                    int utf8_byte_count = 0;
                    if (inString != null)
                    {
                        utf8_byte_count = localeEncoding.GetByteCount(inString);
                    }
                    // Throw only when size is given
                    if (array_size > 0 && array_size < utf8_byte_count)
                    {
                        string field_name = inStructType + "." + field.InField.Name;
                        throw new Exception(String.Format("String is too long. Expecting {0} bytes of UTF-8 string in {1}.", array_size, field_name));
                    }

                    // Convert the string to UTF-8 codeset
                    byte[] byteString = ToUTF8BytesFromString(field.InField.GetValue(inStruct), array_size);
                    field.OutField.SetValueDirect(__makeref(retObject), byteString);
                }

                // char *[]
                // Managed: string []
                // Unsafe: IntPtr[]
                else if ((field.InField.FieldType.IsArray && field.InField.FieldType.GetElementType() == typeof(System.String)) &&
                    (field.OutField.FieldType.IsArray && field.OutField.FieldType.GetElementType() == typeof(System.IntPtr)))
                {
                    // This field may have a fixed size and we assume size is at least mentioned in unmanaged struct
                    // Retrieve the size of the array from Marshal Attribute. This is the size declared in C function.
                    int array_size = 0;
                    object[] marshal_attrs = field.OutField.GetCustomAttributes(typeof(MarshalAsAttribute), false);
                    if (marshal_attrs != null && marshal_attrs.Length > 0)
                    {
                        MarshalAsAttribute marshal = (MarshalAsAttribute)marshal_attrs[0];
                        if (marshal != null)
                        {
                            array_size = marshal.SizeConst;
                        }
                    }

                    string[] inString_array = field.InField.GetValue(inStruct);
                    int array_len = inString_array.Length;
                    // Throw only when size is given
                    if (array_size > 0 && array_size < array_len)
                    {
                        string field_name = inStructType + "." + field.InField.Name;
                        throw new Exception(String.Format("The String array has fixed size of {0}. {1} strings found in {2}", array_size, array_len, field_name));
                    }

                    // Convert the string to UTF-8 codeset
                    IntPtr[] string_array = JAM.ToLocaleStringArray(field.InField.GetValue(inStruct));
                    field.OutField.SetValueDirect(__makeref(retObject), string_array);
                }

                // char **
                // Managed: string[]
                // Unsafe: sbyte**
                else if ((field.InField.FieldType.IsArray && field.InField.FieldType.GetElementType() == typeof(System.String)) &&
                    field.OutField.FieldType == typeof(System.SByte**) && field.InField.GetValue(inStruct) != null)
                {
                    if ((array_len_info == null || array_len_info.Count == 0) ||
                        array_len_info.ContainsKey(field.InField.Name) == false)
                    {
                        throw new Exception(String.Format("Length of String array {0} is unknown.", field.InField.Name));
                    }

                    int array_len = array_len_info[field.InField.Name];
                    if (array_len != field.InField.GetValue(inStruct).Length)
                    {
                        throw new Exception(String.Format("Length of String array {0} does not match with length provided.", field.InField.Name));
                    }
                    // Convert the string to UTF-8 codeset
                    IntPtr string_arr = ConvertStringArrayToPointer(field.InField.GetValue(inStruct));
                    field.OutField.SetValueDirect(__makeref(retObject), string_arr);
                }
            }

            return retObject;
        }

        // Function for converting unmanaged UTF-8 codeset to .Net managed string (Unicode). This function is typically used for outputs
        // inStruct: An unmanaged struct holding values returned by unmanaged UF
        // outStruct: An managed struct exposed to .Net program.
        // array_len_info: An Dictionary of Key Value pair of Struct string array member and their length. Only required for char**
        // We don't have to check the length here in this function since we are not passing outStruct to unmanaged code
        internal static unsafe dynamic ConvertStructStringsFromUTF8(dynamic inStruct, dynamic outStruct, Dictionary<string, int> array_len_info)
        {
            Type inStructType = inStruct.GetType();
            Type outStructType = outStruct.GetType();
            dynamic retObject = outStruct;

            FieldInfo[] inStructInfo = inStructType.GetFields(BindingFlags.Instance |
                                                    BindingFlags.NonPublic |
                                                    BindingFlags.Public);
            FieldInfo[] outStructInfo = outStructType.GetFields(BindingFlags.Instance |
                                                    BindingFlags.NonPublic |
                                                    BindingFlags.Public);

            var in_out_struct_info = inStructInfo.Zip(outStructInfo, (in_field, out_field) => new { InField = in_field, OutField = out_field });
            foreach (var field in in_out_struct_info)
            {
                // char*
                // Managed: string
                // Unsafe: sbyte*
                if (field.InField.FieldType == typeof(System.SByte*) && field.OutField.FieldType == typeof(System.String))
                {
                    // Convert the string to UTF-8 codeset
                    Pointer ptr = field.InField.GetValue(inStruct);
                    sbyte* str_value = (sbyte*)Pointer.Unbox(ptr);
                    string managed_str = ArrayFromSM(str_value);
                    field.OutField.SetValueDirect(__makeref(retObject), managed_str);
                }

                // char []
                // Managed: string
                // Unsafe: byte[]
                else if ((field.InField.FieldType.IsArray && field.InField.FieldType.GetElementType() == typeof(System.Byte)) &&
                    field.OutField.FieldType == typeof(System.String))
                {
                    // Convert the string to UTF-8 codeset
                    string str = ToStringFromUTF8Bytes(field.InField.GetValue(inStruct));
                    field.OutField.SetValueDirect(__makeref(retObject), str);
                }

                // char *[]
                // Managed: string []
                // Unsafe: IntPtr[]
                else if ((field.InField.FieldType.IsArray && field.InField.FieldType.GetElementType() == typeof(System.IntPtr)) &&
                    (field.OutField.FieldType.IsArray && field.OutField.FieldType.GetElementType() == typeof(System.String)))
                {
                    int array_size = 0;
                    object[] marshal_attrs = field.InField.GetCustomAttributes(typeof(MarshalAsAttribute), false);
                    if (marshal_attrs != null && marshal_attrs.Length > 0)
                    {
                        MarshalAsAttribute marshal = (MarshalAsAttribute)marshal_attrs[0];
                        if (marshal != null)
                        {
                            array_size = marshal.SizeConst;
                        }
                    }
                    // Convert the string to UTF-8 codeset
                    string[] string_array = ToStringArrayFromLocale(array_size, field.InField.GetValue(inStruct));
                    field.OutField.SetValueDirect(__makeref(retObject), string_array);

                }

                // char **
                // Managed: string[]
                // Unsafe: sbyte**
                else if (field.InField.FieldType == typeof(System.SByte**) &&
                    (field.OutField.FieldType.IsArray && field.OutField.FieldType.GetElementType() == typeof(System.String)) &&
                    field.InField.GetValue(inStruct) != null)
                {
                    if ((array_len_info == null || array_len_info.Count == 0) ||
                        array_len_info.ContainsKey(field.InField.Name) == false)
                    {
                        throw new Exception(String.Format("Length of String array {0} is unknown.", field.InField.Name));
                    }

                    int array_len = array_len_info[field.InField.Name];

                    // Convert the string to UTF-8 codeset
                    Pointer ptr = field.InField.GetValue(inStruct);
                    sbyte** str_arr = (sbyte**)Pointer.Unbox(ptr);
                    string[] string_array = ArrayFromSM(array_len, str_arr);
                    field.OutField.SetValueDirect(__makeref(retObject), string_array);
                }
            }
            return retObject;
        }

        internal static unsafe double* ArrayToSM(double[] arr)
        {
            int len = arr.Length;
            double* ptr = (double*)SM_alloc(len * sizeof(double));
            for (int i = 0; i < len; ++i)
            {
                ptr[i] = arr[i];
            }
            return ptr;
        }

        internal static unsafe int* ArrayToSM(int[] arr)
        {
            int len = arr.Length;
            int* ptr = (int*)SM_alloc(len * sizeof(int));
            for (int i = 0; i < len; ++i)
            {
                ptr[i] = arr[i];
            }
            return ptr;
        }

        internal static unsafe bool* ArrayToSM(bool[] arr)
        {
            int len = arr.Length;
            bool* ptr = (bool*)SM_alloc(len);
            for (int i = 0; i < len; ++i)
            {
                ptr[i] = arr[i];
            }
            return ptr;
        }

        internal static unsafe Tag* ArrayToSM(Tag[] arr)
        {
            int len = arr.Length;
            Tag* ptr = (Tag*)SM_alloc(len * sizeof(Tag));
            for (int i = 0; i < len; ++i)
            {
                ptr[i] = arr[i];
            }
            return ptr;
        }

        internal static unsafe byte* ArrayToSM(byte[] arr)
        {
            int len = arr.Length;
            byte* ptr = (byte*)SM_alloc(len);
            for (int i = 0; i < len; ++i)
            {
                ptr[i] = arr[i];
            }
            return ptr;
        }

        internal static unsafe sbyte* ArrayToSM(sbyte[] arr)
        {
            int len = arr.Length;
            sbyte* ptr = (sbyte*)SM_alloc(len);
            for (int i = 0; i < len; ++i)
            {
                ptr[i] = arr[i];
            }
            return ptr;
        }

        internal static unsafe float* ArrayToSM(float[] arr)
        {
            int len = arr.Length;
            float* ptr = (float*)SM_alloc(len * sizeof(float));
            for (int i = 0; i < len; ++i)
            {
                ptr[i] = arr[i];
            }
            return ptr;
        }

        // This function converts managed 2d Array into SM allocated 2d array.
        internal static unsafe double* ArrayToSM(double[,] arr)
        {
            int lenA = arr.GetLength(0);
            int lenB = arr.GetLength(1);
            double* ptr = (double*)SM_alloc(lenA * lenB * sizeof(double));
            int k = 0;
            for (int i = 0; i < lenA; i++)
                for (int j = 0; j < lenB; j++)
                    ptr[k++] = arr[i, j];
            return ptr;
        }
    }

    internal class UTF8TextMode : IDisposable
    {
        Util.ModeS prevMode = Util.ModeS.Locale;
        public UTF8TextMode()
        {
            prevMode = Util.AskTextMode();

            if (prevMode != Util.ModeS.AllUtf8)
            {
                Util.SetTextMode(Util.ModeS.AllUtf8);
            }
        }

        public void Dispose()
        {
            Util.SetTextMode(prevMode);
        }
    }
}
