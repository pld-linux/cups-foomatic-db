Summary:	precompiled foomatic database
Name:		cups-foomatic-db-common
Version:	20050405
Release:	0.1
License:	GPL	
Group:		Applications/System
URL:		http://www.linuxprinting.org/foomatic.html
BuildRequires:	foomatic-db
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
common 

%package -n cups-foomatic-db-HP
Summary:        precompiled foomatic database (HP)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-HP
HP drivers

%package -n cups-foomatic-db-Alps
Summary:        precompiled foomatic database (Alps)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Alps
Alps drivers

%package -n cups-foomatic-db-Apollo
Summary:        precompiled foomatic database (Apollo)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Apollo
Apollo drivers

%package -n cups-foomatic-db-Apple
Summary:        precompiled foomatic database (Apple)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Apple
Apple drivers

%package -n cups-foomatic-db-Generic
Summary:        precompiled foomatic database (Generic)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Generic
Generic drivers

%package -n cups-foomatic-db-Panasonic
Summary:        precompiled foomatic database (Panasonic)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Panasonic
Panasonic drivers

%package -n cups-foomatic-db-Infotec
Summary:        precompiled foomatic database (Infotec)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Infotec
Infotec drivers

%package -n cups-foomatic-db-NRG
Summary:        precompiled foomatic database (NRG)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-NRG
NRG drivers

%package -n cups-foomatic-db-IBM
Summary:        precompiled foomatic database (IBM)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-IBM
IBM drivers

%package -n cups-foomatic-db-Fujitsu
Summary:        precompiled foomatic database (Fujitsu)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Fujitsu
Fujitsu drivers

%package -n cups-foomatic-db-Minolta
Summary:        precompiled foomatic database (Minolta)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Minolta
Minolta drivers

%package -n cups-foomatic-db-Epson
Summary:        precompiled foomatic database (Epson)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Epson
Epson drivers

%package -n cups-foomatic-db-Citizen
Summary:        precompiled foomatic database (Citizen)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Citizen
Citizen drivers

%package -n cups-foomatic-db-Olivetti
Summary:        precompiled foomatic database (Olivetti)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Olivetti
Olivetti drivers

%package -n cups-foomatic-db-Compaq
Summary:        precompiled foomatic database (Compaq)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Compaq
Compaq drivers

%package -n cups-foomatic-db-Canon
Summary:        precompiled foomatic database (Canon)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Canon
Canon drivers

%package -n cups-foomatic-db-DEC
Summary:        precompiled foomatic database (DEC)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-DEC
DEC drivers

%package -n cups-foomatic-db-Dymo-CoStar
Summary:        precompiled foomatic database (Dymo-CoStar)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Dymo-CoStar
Dymo-CoStar drivers

%package -n cups-foomatic-db-Lexmark
Summary:        precompiled foomatic database (Lexmark)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Lexmark
Lexmark drivers

%package -n cups-foomatic-db-Kyocera
Summary:        precompiled foomatic database (Kyocera)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Kyocera
Kyocera drivers

%package -n cups-foomatic-db-Brother
Summary:        precompiled foomatic database (Brother)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Brother
Brother drivers

%package -n cups-foomatic-db-Samsung
Summary:        precompiled foomatic database (Samsung)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Samsung
Samsung drivers

%package -n cups-foomatic-db-Okidata
Summary:        precompiled foomatic database (Okidata)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Okidata
Okidata drivers

%package -n cups-foomatic-db-Gestetner
Summary:        precompiled foomatic database (Gestetner)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Gestetner
Gestetner drivers

%package -n cups-foomatic-db-Tektronix
Summary:        precompiled foomatic database (Tektronix)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Tektronix
Tektronix drivers

%package -n cups-foomatic-db-Star
Summary:        precompiled foomatic database (Star)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Star
Star drivers

%package -n cups-foomatic-db-Savin
Summary:        precompiled foomatic database (Savin)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Savin
Savin drivers

%package -n cups-foomatic-db-Sharp
Summary:        precompiled foomatic database (Sharp)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Sharp
Sharp drivers

%package -n cups-foomatic-db-Lanier
Summary:        precompiled foomatic database (Lanier)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Lanier
Lanier drivers

%package -n cups-foomatic-db-Ricoh
Summary:        precompiled foomatic database (Ricoh)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Ricoh
Ricoh drivers

%package -n cups-foomatic-db-NEC
Summary:        precompiled foomatic database (NEC)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-NEC
NEC drivers

%package -n cups-foomatic-db-Xerox
Summary:        precompiled foomatic database (Xerox)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-Xerox
Xerox drivers

%package -n cups-foomatic-db-other
Summary:        precompiled foomatic database (other)
Group:		Applications/System
Requires:       cups-foomatic-db-common = %{version}

%description -n cups-foomatic-db-other
other drivers

%build
foomatic-compiledb -t ppd -d . -j 1
%{_gzipbin} ppd/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/cups/model/foomatic
cp -f ppd/*.gz $RPM_BUILD_ROOT%{_datadir}/cups/model/foomatic/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/cups/model/foomatic/

%files -n cups-foomatic-db-HP
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/HP-*

%files -n cups-foomatic-db-Alps
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Alps-*

%files -n cups-foomatic-db-Apollo
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Apollo-*

%files -n cups-foomatic-db-Apple
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Apple-*

%files -n cups-foomatic-db-Generic
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Generic-*

%files -n cups-foomatic-db-Panasonic
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Panasonic-*

%files -n cups-foomatic-db-Infotec
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Infotec-*

%files -n cups-foomatic-db-NRG
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/NRG-*

%files -n cups-foomatic-db-IBM
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/IBM-*

%files -n cups-foomatic-db-Fujitsu
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Fujitsu-*

%files -n cups-foomatic-db-Minolta
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Minolta-*

%files -n cups-foomatic-db-Epson
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Epson-*

%files -n cups-foomatic-db-Canon
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Canon-*

%files -n cups-foomatic-db-Compaq
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Compaq-*

%files -n cups-foomatic-db-DEC
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/DEC-*

%files -n cups-foomatic-db-Olivetti
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Olivetti-*

%files -n cups-foomatic-db-Citizen
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Citizen-*

%files -n cups-foomatic-db-Dymo-CoStar
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Dymo-CoStar-*

%files -n cups-foomatic-db-Kyocera
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Kyocera-*

%files -n cups-foomatic-db-Lexmark
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Lexmark-*

%files -n cups-foomatic-db-Brother
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Brother-*

%files -n cups-foomatic-db-Samsung
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Samsung-*

%files -n cups-foomatic-db-Savin
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Savin-*

%files -n cups-foomatic-db-Sharp
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Sharp-*

%files -n cups-foomatic-db-Lanier
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Lanier-*

%files -n cups-foomatic-db-Ricoh
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Ricoh-*

%files -n cups-foomatic-db-NEC
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/NEC-*

%files -n cups-foomatic-db-Okidata
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Okidata-*

%files -n cups-foomatic-db-Gestetner
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Gestetner-*

%files -n cups-foomatic-db-Tektronix
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Tektronix-*

%files -n cups-foomatic-db-Star
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Star-*

%files -n cups-foomatic-db-Xerox
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Xerox-*

%files -n cups-foomatic-db-other
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Dell-*
%{_datadir}/cups/model/foomatic/Tally-*
%{_datadir}/cups/model/foomatic/Anitech-*
%{_datadir}/cups/model/foomatic/Avery-*
%{_datadir}/cups/model/foomatic/Dell-*
%{_datadir}/cups/model/foomatic/QMS-*
%{_datadir}/cups/model/foomatic/Oce-*
%{_datadir}/cups/model/foomatic/Pentax-*
%{_datadir}/cups/model/foomatic/Raven-*
%{_datadir}/cups/model/foomatic/Kodak-*
%{_datadir}/cups/model/foomatic/CItoh-*
%{_datadir}/cups/model/foomatic/Heidelberg-*
%{_datadir}/cups/model/foomatic/Hitachi-*
%{_datadir}/cups/model/foomatic/Imagen-*
%{_datadir}/cups/model/foomatic/Mitsubishi-*
%{_datadir}/cups/model/foomatic/Seiko-*
%{_datadir}/cups/model/foomatic/PCPI-*
