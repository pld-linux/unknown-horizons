# TODO
# - do py_postclean
# - noarch subpackage for data
# - use system python-enet then can make whole package noarch
#
# used in the tarball name
%define		ver_hash1	244f49f
# used in the directory name
%define		ver_hash2	bedaf75
Summary:	Unknown Horizons - a 2D realtime strategy simulation
Name:		unknown-horizons
Version:	2012.1a
Release:	2
License:	GPL v2+, distributable (see docs)
Group:		Applications/Games
# https://github.com/unknown-horizons/unknown-horizons/releases
Source0:	%{name}-%{name}-%{version}-0-g%{ver_hash1}.zip
# Source0-md5:	522c5a6c7a583d98a9ecb686b085f7d6
URL:		http://www.unknown-horizons.org/
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python-PyYAML
Requires:	python-fife
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unknown Horizons is a 2D realtime strategy simulation with an emphasis
on economy and city building. Expand your small settlement to a strong
and wealthy colony, collect taxes and supply your inhabitants with
valuable goods. Increase your power with a well balanced economy and
with strategic trade and diplomacy.

%prep
%setup -q -n %{name}-%{name}-%{ver_hash2}

# fix #!%{_bindir}/env python -> #!%{__python}:
%{__sed} -i -e '1s,^#!.*python,#!%{__python},' run_uh.py

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

%py_install

# contains binary code
mv $RPM_BUILD_ROOT%{py_sitescriptdir}/* $RPM_BUILD_ROOT%{py_sitedir}

rm -r $RPM_BUILD_ROOT%{py_sitedir}/horizons/network/{darwin,freebsd,windows}-*

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README doc/{APL,AUTHORS,CC,CHANGELOG,GPL_fontexception,LICENSE,MIT,OFL}
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%dir %{py_sitedir}/horizons
%{py_sitedir}/horizons/ai
%{py_sitedir}/horizons/command
%{py_sitedir}/horizons/engine
%{py_sitedir}/horizons/ext
%{py_sitedir}/horizons/gui
%{py_sitedir}/horizons/i18n
%dir %{py_sitedir}/horizons/network
%dir %{py_sitedir}/horizons/network/linux-*
%attr(755,root,root) %{py_sitedir}/horizons/network/linux-*/enet.so
%{py_sitedir}/horizons/network/linux-*/*.py*
%{py_sitedir}/horizons/network/packets
%{py_sitedir}/horizons/network/*.py*
%{py_sitedir}/horizons/scenario
%{py_sitedir}/horizons/util
%{py_sitedir}/horizons/world
%{py_sitedir}/horizons/*.py*
%{py_sitedir}/*.egg-info
%{_pixmapsdir}/*.xpm
%{_desktopdir}/*.desktop
%{_mandir}/man6/%{name}.6*
