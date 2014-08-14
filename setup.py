# -----------------------------------------------------------------------
# Copyright (c) 2012 Tableau Software, Incorporated
#                    and its licensors. All rights reserved.
# Protected by U.S. Patent 7,089,266; Patents Pending.
#
# Portions of the code
# Copyright (c) 2002 The Board of Trustees of the Leland Stanford
#                    Junior University. All rights reserved.
# -----------------------------------------------------------------------
# setup.py
# -----------------------------------------------------------------------
# WARNING: Computer generated file.  Do not hand modify.
from distutils import log
from distutils.core import setup
from distutils.command.build_py import build_py
from distutils.command.install_lib import install_lib
import os
import sys

# Skip the version check when building the source dist; we can
# patch things up later.
if len(sys.argv) < 2 or sys.argv[1] != 'sdist':
    if sys.version_info < (2, 6):
        print 'Python >= 2.6 required'
        exit(1)

class build_with_libs(build_py):
    def build_package_data(self):
        """Copy package_data files into the build directory, preserving executable bits and symlinks"""
        for package, src_dir, build_dir, filenames in self.data_files:
            for filename in filenames:
                src_file = os.path.join(src_dir, filename)
                dst_file = os.path.join(build_dir, filename)
                self.mkpath(os.path.dirname(dst_file))
                if os.path.islink(src_file):
                    link_dst = os.path.basename(os.path.realpath(src_file))
                    log.info('symbolically linking %s -> %s', dst_file, link_dst)
                    if os.path.exists(dst_file):
                        os.unlink(dst_file)
                    os.symlink(link_dst, dst_file)
                else:
                    self.copy_file(src_file, dst_file)

class install_lib_with_links(install_lib):
    def install(self):
        if os.path.isdir(self.build_dir):
            out = self.copy_tree(self.build_dir, self.install_dir, preserve_symlinks=1)
        else:
            # Let our parent deal with this error
            out = super.install(self)
        return out

    def copy_tree(self, src, dst, preserve_mode=1, preserve_times=1,
                  preserve_symlinks=0, update=0, verbose=1, dry_run=0):
        """Same as dir_util.copy_tree, but clobber existing symlinks."""
        from distutils.file_util import copy_file
        from distutils.dir_util import mkpath

        if not dry_run and not os.path.isdir(src):
            raise DistutilsFileError, \
                  "cannot copy tree '%s': not a directory" % src
        try:
            names = os.listdir(src)
        except os.error, (errno, errstr):
            if dry_run:
                names = []
            else:
                raise DistutilsFileError, \
                      "error listing files in '%s': %s" % (src, errstr)

        if not dry_run:
            mkpath(dst, verbose=verbose)

        outputs = []

        for n in names:
            src_name = os.path.join(src, n)
            dst_name = os.path.join(dst, n)

            if preserve_symlinks and os.path.islink(src_name):
                link_dest = os.readlink(src_name)
                if verbose >= 1:
                    log.info("linking %s -> %s", dst_name, link_dest)
                if not dry_run:
                    if os.path.islink(dst_name):
                        os.unlink(dst_name)
                    os.symlink(link_dest, dst_name)
                outputs.append(dst_name)

            elif os.path.isdir(src_name):
                outputs.extend(
                    self.copy_tree(src_name, dst_name, preserve_mode,
                              preserve_times, preserve_symlinks, update,
                              verbose=verbose, dry_run=dry_run))
            else:
                copy_file(src_name, dst_name, preserve_mode,
                          preserve_times, update, verbose=verbose,
                          dry_run=dry_run)
                outputs.append(dst_name)

        return outputs


setup(
    name='DataExtract',
    cmdclass={'build_py' : build_with_libs, 'install_lib' : install_lib_with_links},
    version='8200.14.0720.2105',
    packages=['dataextract'],
    package_data={'dataextract' : ['bin/*', 'lib/*so*']},
    description="Create extracts for Tableau's Fast Data Engine",
    license='LICENSE.txt'
)
