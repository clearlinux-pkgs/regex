#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : regex
Version  : 2020.10.15
Release  : 5
URL      : https://files.pythonhosted.org/packages/c9/16/4ea16f4510afd7ce4b77d8ee7ca97717408b3cf99e0a4b3cdd0a47ef6466/regex-2020.10.15.tar.gz
Source0  : https://files.pythonhosted.org/packages/c9/16/4ea16f4510afd7ce4b77d8ee7ca97717408b3cf99e0a4b3cdd0a47ef6466/regex-2020.10.15.tar.gz
Summary  : Alternative regular expression module, to replace re.
Group    : Development/Tools
License  : Apache-2.0
Requires: regex-python = %{version}-%{release}
Requires: regex-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
------------
        
        This regex implementation is backwards-compatible with the standard 're' module, but offers additional functionality.
        
        Note
        ----
        
        The re module's behaviour with zero-width matches changed in Python 3.7, and this module will follow that behaviour when compiled for Python 3.7.
        
        Old vs new behaviour
        --------------------

%package python
Summary: python components for the regex package.
Group: Default
Requires: regex-python3 = %{version}-%{release}

%description python
python components for the regex package.


%package python3
Summary: python3 components for the regex package.
Group: Default
Requires: python3-core
Provides: pypi(regex)

%description python3
python3 components for the regex package.


%prep
%setup -q -n regex-2020.10.15
cd %{_builddir}/regex-2020.10.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602777140
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
