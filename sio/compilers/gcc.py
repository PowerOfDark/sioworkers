from __future__ import absolute_import
from sio.compilers.system_gcc import CStyleCompiler


class CCompiler(CStyleCompiler):
    lang = 'c'

    @classmethod
    def gcc_4_8_2_c99(cls):
        obj = cls('gcc.4_8_2')
        obj.options = ['-std=gnu99', '-static', '-O2', '-s', '-lm']
        return obj


class CPPCompiler(CStyleCompiler):
    lang = 'cpp'

    @classmethod
    def gcc_4_8_2_cpp11(cls):
        obj = cls('gcc.4_8_2')
        obj.compiler = 'g++'
        obj.options = ['-std=c++11', '-static', '-O2', '-s', '-lm']
        return obj
    
    @classmethod
    def gcc_8_3_0_cpp17(cls, arch='i386'):
        obj = cls('gcc.8_3_0-%s' % arch)
        obj.compiler = 'g++'
        obj.options = ['-std=c++17', '-static', '-O2', '-s', '-lm']
        return obj


def run_gcc4_8_2_c99(environ):
    return CCompiler.gcc_4_8_2_c99().compile(environ)


def run_gcc_default(environ):
    return CCompiler.gcc_4_8_2_c99().compile(environ)


def run_gplusplus4_8_2_cpp11(environ):
    return CPPCompiler.gcc_4_8_2_cpp11().compile(environ)


def run_gplusplus8_3_0_cpp17_i386(environ):
    return CPPCompiler.gcc_8_3_0_cpp17('i386').compile(environ)

def run_gplusplus8_3_0_cpp17_amd64(environ):
    return CPPCompiler.gcc_8_3_0_cpp17('amd64').compile(environ)


def run_gplusplus_default(environ):
    return run_gplusplus8_3_0_cpp17_i386(environ)


run_c_default = run_gcc_default
run_c_gcc4_8_2_c99 = run_gcc4_8_2_c99
run_cpp_default = run_gplusplus_default
run_cpp_gcc4_8_2_cpp11 = run_gplusplus4_8_2_cpp11
run_cpp_gcc8_3_0_cpp17 = run_cpp_gcc8_3_0_cpp17_i386 = run_gplusplus8_3_0_cpp17_i386
run_cpp_gcc8_3_0_cpp17_amd64 = run_gplusplus8_3_0_cpp17_amd64
