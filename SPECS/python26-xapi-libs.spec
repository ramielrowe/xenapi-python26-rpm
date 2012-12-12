%global		_python26packages	%{_prefix}/lib/python2.6/site-packages

Name:		python26-xapi-libs	
Version:	0.1
Release:	1
Summary:	XenServer API Libs for Python26
License: 	Apache License, Version 2.0
BuildArch: 	noarch
Source0:	XenAPI.py
Source1:	XenAPIPlugin.py
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:	python26, python26-libs

%description
XenServer API and Plugin Libs for Python26

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_python26packages}
cp %{SOURCE0} %{buildroot}/%{_python26packages}/.
cp %{SOURCE1} %{buildroot}/%{_python26packages}/.

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_python26packages}/XenAPI.py
%{_python26packages}/XenAPIPlugin.py

%changelog
* Wed Dec 12 2012 Andrew Melton <andrew.melton@rackspace.com> 0.1-1
- Initial Build
