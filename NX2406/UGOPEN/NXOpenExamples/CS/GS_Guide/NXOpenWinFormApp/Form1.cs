/*=================================================================================================
                      Copyright (c) 2022 Siemens PLM 

                    Unpublished - All rights reserved
                    

==================================================================================================*/
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using NXOpen;

namespace NXOpenWinform
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public void button1_Click(object sender, EventArgs e)
        {
            Guide.InfoWriteLine("Creating a sphere");
            Guide.CreateSphere(0.0, 0.0, 0.0, 10.0);
        }
    }
}
