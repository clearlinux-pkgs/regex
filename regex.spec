#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : regex
Version  : 2020.11.13
Release  : 13
URL      : https://files.pythonhosted.org/packages/2e/e4/3447fed9ab29944333f48730ecff4dca92f0868c5b188d6ab2b2078e32c2/regex-2020.11.13.tar.gz
Source0  : https://files.pythonhosted.org/packages/2e/e4/3447fed9ab29944333f48730ecff4dca92f0868c5b188d6ab2b2078e32c2/regex-2020.11.13.tar.gz
Summary  : Alternative regular expression module, to replace re.
Group    : Development/Tools
License  : Apache-2.0
Requires: regex-license = %{version}-%{release}
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

%package license
Summary: license components for the regex package.
Group: Default

%description license
license components for the regex package.


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
%setup -q -n regex-2020.11.13
cd %{_builddir}/regex-2020.11.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605284604
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
mkdir -p %{buildroot}/usr/share/package-licenses/regex
cp %{_builddir}/regex-2020.11.13/LICENSE.txt %{buildroot}/usr/share/package-licenses/regex/692d7ee2ea91449bb8354092cedb2fd1f5a7a2e0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/regex/692d7ee2ea91449bb8354092cedb2fd1f5a7a2e0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
