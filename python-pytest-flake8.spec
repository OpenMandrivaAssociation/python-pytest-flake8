%global pypi_name pytest-flake8

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        1
Summary:        A pytest plugin to check FLAKE8 requirements
Group:          Development/Python
License:        MIT
URL:            https://github.com/tholo/pytest-flake8
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-flake8/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(flake8) >= 3.5
BuildRequires:  python%{pyver}dist(pytest) >= 3.5
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(setuptools-scm)

%description
A pytest plugin for efficiently checking PEP8 compliance

%prep
%autosetup -n pytest_flake8-1.3.0
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
#{python3_sitelib}/__pycache__/*
%{python_sitelib}/pytest_flake8.py
#%%{python3_sitelib}/%{pypi_name}
%{python_sitelib}/pytest_flake8-%{version}.dist-info
%{python_sitelib}/__pycache__/pytest_flake8*.pyc
