/*=================================================================================================
                      Copyright (c) 2022 Siemens PLM 

                    Unpublished - All rights reserved
                    

==================================================================================================*/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using NXOpen;

namespace NXOpenWinform
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        public static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());

            Form1 form = new Form1();
            form.ShowDialog();

        }
    }
}
