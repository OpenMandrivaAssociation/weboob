
%define name weboob
%define version 0.7
%define release %mkrel 2

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
Requires: python-qt4-phonon python-yaml python-dateutill
Suggests: python-html2text

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
%{_bindir}/webcontentedit
%{_bindir}/qwebcontentedit
%{_datadir}/icons/hicolor/64x64/apps/*.png
%{_datadir}/applications/*.desktop
%{_datadir}/man/man1/*

%changelog
