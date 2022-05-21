#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	parsedatetime
Summary:	Parse human-readable date/time strings in Python
Name:		python-%{module}
Version:	2.6
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://github.com/bear/%{module}/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	4d9af6a4427c383910bbc34a5d44f151
URL:		https://github.com/bear/parsedatetime
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.713
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pyicu
BuildRequires:	python-test
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pyicu
BuildRequires:	python3-test
%endif
%endif
%if %{with doc}
BuildRequires:	epydoc
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
parsedatetime is a Python module that can parse human-readable
date/time strings.

%package doc
Summary:	Documentation for the parsedatetime Python module
Group:		Documentation

%description doc
This package contains the generated HTML documentation for the
parsedatetime python module

%package -n python3-%{module}
Summary:	Parse human-readable date/time strings in Python
Group:		Libraries/Python

%description -n python3-%{module}
parsedatetime is a Python module that can parse human-readable
date/time strings.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
epydoc --html --config epydoc.conf
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%doc AUTHORS.txt CHANGES.txt README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE.txt
%doc AUTHORS.txt CHANGES.txt README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}*.egg-info
%endif

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc docs/ examples/
%endif
