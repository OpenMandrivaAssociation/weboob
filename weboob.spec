
%define name weboob
%define version 0.3
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:	Weboob (Web Out Of Browsers) provides several applications to interact with a lot of websites
Group:		Networking/Other
License:	GPLv3
URL:		http://weboob.org/
Source0: 	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch

BuildRequires:	python-setuptools python-qt4-devel

%description
Why using Weboob?
* You get information faster;
* You can script around weboob to automate tasks;
* It extends websites features;
* It helps blind people use crappy websites.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --prefix %{_prefix} --skip-build --root %{buildroot}
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS README
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-*.egg-info
%{_bindir}/*oo*
%{_bindir}/*sex
%{_bindir}/web*
%{_datadir}/man/man1/*.lzma
%{_datadir}/icons/hicolor/64x64/apps/*.png
%{_datadir}/applications/*.desktop

%changelog
