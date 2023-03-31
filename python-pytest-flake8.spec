# Created by pyp2rpm-3.3.5
%global pypi_name pytest-flake8

Name:           python-%{pypi_name}
Version:        1.0.7
Release:        3
Summary:        A pytest plugin to check FLAKE8 requirements
Group:          Development/Python
License:        BSD License
URL:            https://github.com/tholo/pytest-flake8
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8) >= 3.5
BuildRequires:  python3dist(pytest) >= 3.5
BuildRequires:  python3dist(setuptools)

%description
A pytest plugin for efficiently checking PEP8 compliance

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
#{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_flake8.py
#%%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/pytest_flake8-%{version}-py%{python3_version}.egg-info

