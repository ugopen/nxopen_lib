#!/usr/local/bin/perl
#
#   Move a rendered HPGL file to a designated directory
#
#   This script is used in conjunction with a "Render File Then Execute"
#   plot queue defined via the SDI Print Administrator program. Such a queue
#   takes the input file (a CGM file), renders it in the format defined for
#   the queue, and then executes a user supplied script. The script is
#   executed in a temporary directory which contains the original CGM file,
#   the rendered file (which has a temporary name), and various SDI 
#   log files. The script is supplied the name of the rendered (output) file.
#
#   This script moves the output file to a designated directory and renames it 
#   to the input file name with an extension of .hpp instead of .cgm.
#
#   The destination directory is supplied via an environment variable:
#
#   PLOT_HPGL_OUTPUT_DIR
#
#   If this environment variable is not defined or does not point to a writable
#   directory, the script logs an error message and exits without doing anything
#   to the output file.
#
#   The log output, which contains an information message when the script
#   executes successfully, can be directed to a particular file via another
#   environment variable:
#
#   PLOT_HPGL_LOG_FILE
#
#   which should contain a fully specified file name. Log messages will be 
#   appended to this file, which is created if it doesn't exist.
#
#   If the variable is not defined or there is a problem opening the log
#   file, a "default" log file named move_hpgl.log in the HOME directory
#   is used.
#
#   The script determines the name to use for the output file by looking for
#   a file with a .cgm extension in the current directory. The first such file
#   it locates is the name it will use. This works fine when the script is 
#   invoked via SDI as these conditions hold. If no .cgm file is found, 
#   the destination name is "unknown_name.hpp".
#
#   On Windows this script may not be executed by SDI directly as it must be
#   a .bat or .cmd file. So the queue on Windows should be defined to execute
#   a .bat script which in turns invokes this script via:
#
#   perl %UGII_BASE_DIR%\ugopen\move_hpgl.pl %*
#
#   On unix, the queue may be invoke this script directly, e.g.,
#
#   /some_directory/ugopen/move_hpgl.pl
#
sub log_line
{
    my  $line = shift @_;
    printf LOG "%s\n", $line;
}

sub map_cgm_name_to_hpgl
{
    my  $name = "unknown_name.hpp";
    my  $status, $file;

    $status = opendir JOBDIR, ".";
    if  ( ! defined $status )
    {
        return $name;
    }

    while ( $file = readdir JOBDIR )
    {
        if  ( $file =~ /(.+)\.cgm$/ )
        {
            $name = $1 . ".hpp";
            last;
        }
    }
    close JOBDIR;
    return $name;
}

use English;
use File::Spec;

my  $logfile, $output_dir, $output_file;
my  $now, $command, $curdir;

$logfile = $ENV{"PLOT_HPGL_LOG_FILE"};
if  ( !defined $logfile )
{
    $logfile = File::Spec->catfile( $ENV{"HOME"}, "move_hpgl.log" );
}

open LOG, ">> $logfile"
or die "Unable to open $logfile: $!";

$now = localtime();
$output_dir = $ENV{"PLOT_HPGL_OUTPUT_DIR"};
if  ( !defined $output_dir )
{
    log_line $now . 
             ": Environment variable PLOT_HPGL_OUTPUT_DIR must be defined";
    close LOG;
    exit;
}
if  ( ! -d $output_dir || ! -w $output_dir )
{
    log_line $now . 
             ": Output directory $output_dir does not exist or is not writable";
    close LOG;
    exit;
}

$output_file = File::Spec->catfile( $output_dir, map_cgm_name_to_hpgl() );
chomp( $curdir = `pwd` );

log_line "$now: Moving $ARGV[0] from $curdir to $output_file";

$command = ( $OSNAME =~ /MSWin/ ) ? "move " : "mv ";
$command .= "$ARGV[0] $output_file";
system( $command );

close LOG;
