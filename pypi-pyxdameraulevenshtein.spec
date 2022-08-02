#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyxdameraulevenshtein
Version  : 1.7.1
Release  : 9
URL      : https://files.pythonhosted.org/packages/4c/37/fefa8524e61f513a26e2aa7224c5bbed0e4ff1b1bd713e69d5866550d170/pyxDamerauLevenshtein-1.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/4c/37/fefa8524e61f513a26e2aa7224c5bbed0e4ff1b1bd713e69d5866550d170/pyxDamerauLevenshtein-1.7.1.tar.gz
Summary  : pyxDamerauLevenshtein implements the Damerau-Levenshtein (DL) edit distance algorithm for Python in Cython for high performance.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pyxdameraulevenshtein-filemap = %{version}-%{release}
Requires: pypi-pyxdameraulevenshtein-lib = %{version}-%{release}
Requires: pypi-pyxdameraulevenshtein-python = %{version}-%{release}
Requires: pypi-pyxdameraulevenshtein-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
# pyxDamerauLevenshtein
[![Build Status](https://app.travis-ci.com/lanl/pyxDamerauLevenshtein.svg?branch=master)](https://app.travis-ci.com/lanl/pyxDamerauLevenshtein)

%package filemap
Summary: filemap components for the pypi-pyxdameraulevenshtein package.
Group: Default

%description filemap
filemap components for the pypi-pyxdameraulevenshtein package.


%package lib
Summary: lib components for the pypi-pyxdameraulevenshtein package.
Group: Libraries
Requires: pypi-pyxdameraulevenshtein-filemap = %{version}-%{release}

%description lib
lib components for the pypi-pyxdameraulevenshtein package.


%package python
Summary: python components for the pypi-pyxdameraulevenshtein package.
Group: Default
Requires: pypi-pyxdameraulevenshtein-python3 = %{version}-%{release}

%description python
python components for the pypi-pyxdameraulevenshtein package.


%package python3
Summary: python3 components for the pypi-pyxdameraulevenshtein package.
Group: Default
Requires: pypi-pyxdameraulevenshtein-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(pyxdameraulevenshtein)

%description python3
python3 components for the pypi-pyxdameraulevenshtein package.


%prep
%setup -q -n pyxDamerauLevenshtein-1.7.1
cd %{_builddir}/pyxDamerauLevenshtein-1.7.1
pushd ..
cp -a pyxDamerauLevenshtein-1.7.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659452604
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-pyxdameraulevenshtein

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
