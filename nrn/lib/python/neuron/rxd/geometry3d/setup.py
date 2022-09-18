# run with
# python setup.py build_ext --inplace

import sys
nrn_srcdir = "D:/a/1/s"
#using_pgi=True
using_pgi=False
mingw = 1
#mingw = 0
instdir = "C:/nrn-install"
if nrn_srcdir[0] == '/' or (len(nrn_srcdir) > 2 and nrn_srcdir[1] == ':'):
    pass
else: # not an absolute path
    # TODO: is this right?
    nrn_srcdir = '../../../../../../' + nrn_srcdir

pgi_compiler_flags = "-noswitcherror"

from distutils.core import setup
from distutils.extension import Extension

def have_vc():
    if not mingw:
        return False
    import traceback
    try:
        from distutils import spawn
        x = spawn.find_executable("cl")
        x = True if x is not None and "Microsoft" in x else False
    except:
        traceback.print_exc()
        x = False
    return x

try:
    import numpy
except:
    setup()
else:
    olevel = "2"
    use_vc = have_vc()
    if mingw and sys.version_info[0] == 3:
      use_vc = True
    if use_vc:
        mpicc_bin = 'cl'
        mpicxx_bin = 'cl'
        if olevel == '0' and sys.version_info[0] == 3:
          olevel = 'd'
    else:
        mpicc_bin = "C:/msys64/mingw64/bin/cc.exe"
        mpicxx_bin = "C:/msys64/mingw64/bin/c++.exe"
    print (mpicxx_bin)
    import os
    os.environ["CC"]=mpicc_bin
    os.environ["CXX"]=mpicxx_bin

    define_macros=[]

    extra_compile_args = []
    extra_link_args = []
    if olevel != "":
        extra_compile_args.append('-O' + olevel)
    if using_pgi:
        extra_compile_args.append(pgi_compiler_flags)

    include_dirs = [nrn_srcdir + '/share/lib/python/neuron/rxd/geometry3d', '.', numpy.get_include()]

    srcdir = nrn_srcdir + '/share/lib/python/neuron/rxd/geometry3d/'

    #    name='neuron/rxd/geometry3d',
    setup(
        ext_modules = [
                       Extension("neuron.rxd.geometry3d.graphicsPrimitives",
                                 sources=["graphicsPrimitives.cpp"],
                                 define_macros=define_macros,
                                 extra_compile_args=extra_compile_args,
                                 extra_link_args=extra_link_args,
                                 include_dirs=include_dirs),
                       Extension("neuron.rxd.geometry3d.ctng",
                                 sources=["ctng.cpp"],
                                 define_macros=define_macros,
                                 extra_compile_args=extra_compile_args,
                                 extra_link_args=extra_link_args,
                                 include_dirs=include_dirs),
                       Extension("neuron.rxd.geometry3d.surfaces",
                                 sources=["surfaces.cpp", nrn_srcdir + "/src/nrnpython/rxd_marching_cubes.cpp", nrn_srcdir + "/src/nrnpython/rxd_llgramarea.cpp"],
                                 define_macros=define_macros,
                                 extra_compile_args=extra_compile_args,
                                 extra_link_args=extra_link_args,
                                 include_dirs=include_dirs)],
    )
    #    package_dir = {'': instdir + '/share/lib/python/neuron/rxd/geometry3d'}

