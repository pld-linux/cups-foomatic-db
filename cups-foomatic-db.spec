Summary:	Precompiled foomatic database
Summary(pl):	Prekompilowana baza danych foomatic
Name:		cups-foomatic-db
Version:	20050405
Release:	0.1
License:	GPL	
Group:		Applications/System
URL:		http://www.linuxprinting.org/foomatic.html
Requires:	cups-filter-foomatic >= 3.0.0
Requires:	cups-foomatic-db-driver
BuildRequires:	foomatic-db = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Precompiled foomatic database - common data.

%description
Prekompilowana baza danych foomatic - dane wspólne.

%package -n cups-foomatic-db-Alps
Summary:	Precompiled foomatic database (Alps)
Summary(pl):	Prekompilowana baza danych foomatic (Alps)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Alps
Alps drivers.

%description -n cups-foomatic-db-Alps -l pl
Sterowniki Alps.

%package -n cups-foomatic-db-Apollo
Summary:	Precompiled foomatic database (Apollo)
Summary(pl):	Prekompilowana baza danych foomatic (Apollo)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Apollo
Apollo drivers.

%description -n cups-foomatic-db-Apollo -l pl
Sterowniki Apollo.

%package -n cups-foomatic-db-Apple
Summary:	Precompiled foomatic database (Apple)
Summary(pl):	Prekompilowana baza danych foomatic (Apple)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Apple
Apple drivers.

%description -n cups-foomatic-db-Apple -l pl
Sterowniki Apple.

%package -n cups-foomatic-db-Brother
Summary:	Precompiled foomatic database (Brother)
Summary(pl):	Prekompilowana baza danych foomatic (Brother)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Brother
Brother drivers.

%description -n cups-foomatic-db-Brother -l pl
Sterowniki Brother.

%package -n cups-foomatic-db-Canon
Summary:	Precompiled foomatic database (Canon)
Summary(pl):	Prekompilowana baza danych foomatic (Canon)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Canon
Canon drivers.

%description -n cups-foomatic-db-Canon -l pl
Sterowniki Canon.

%package -n cups-foomatic-db-Citizen
Summary:	Precompiled foomatic database (Citizen)
Summary(pl):	Prekompilowana baza danych foomatic (Citizen)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Citizen
Citizen drivers.

%description -n cups-foomatic-db-Citizen -l pl
Sterowniki Citizen.

%package -n cups-foomatic-db-Compaq
Summary:	Precompiled foomatic database (Compaq)
Summary(pl):	Prekompilowana baza danych foomatic (Compaq)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Compaq
Compaq drivers.

%description -n cups-foomatic-db-Compaq -l pl
Sterowniki Compaq.

%package -n cups-foomatic-db-DEC
Summary:	Precompiled foomatic database (DEC)
Summary(pl):	Prekompilowana baza danych foomatic (DEC)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-DEC
DEC drivers.

%description -n cups-foomatic-db-DEC -l pl
Sterowniki DEC.

%package -n cups-foomatic-db-Dymo-CoStar
Summary:	Precompiled foomatic database (Dymo-CoStar)
Summary(pl):	Prekompilowana baza danych foomatic (Dymo-CoStar)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Dymo-CoStar
Dymo-CoStar drivers.

%description -n cups-foomatic-db-Dymo-CoStar -l pl
Sterowniki Dymo-CoStar.

%package -n cups-foomatic-db-Epson
Summary:	Precompiled foomatic database (Epson)
Summary(pl):	Prekompilowana baza danych foomatic (Epson)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Epson
Epson drivers.

%description -n cups-foomatic-db-Epson -l pl
Sterowniki Epson.

%package -n cups-foomatic-db-Fujitsu
Summary:	Precompiled foomatic database (Fujitsu)
Summary(pl):	Prekompilowana baza danych foomatic (Fujitsu)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Fujitsu
Fujitsu drivers.

%description -n cups-foomatic-db-Fujitsu -l pl
Sterowniki Fujitsu.

%package -n cups-foomatic-db-Generic
Summary:	Precompiled foomatic database (Generic)
Summary(pl):	Prekompilowana baza danych foomatic (Generic)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Generic
Generic drivers.

%description -n cups-foomatic-db-Generic -l pl
Sterowniki Generic.

%package -n cups-foomatic-db-Gestetner
Summary:	Precompiled foomatic database (Gestetner)
Summary(pl):	Prekompilowana baza danych foomatic (Gestetner)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Gestetner
Gestetner drivers.

%description -n cups-foomatic-db-Gestetner -l pl
Sterowniki Gestetner.

%package -n cups-foomatic-db-HP
Summary:	Precompiled foomatic database (HP)
Summary(pl):	Prekompilowana baza danych foomatic (HP)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-HP
HP drivers.

%description -n cups-foomatic-db-HP -l pl
Sterowniki HP.

%package -n cups-foomatic-db-IBM
Summary:	Precompiled foomatic database (IBM)
Summary(pl):	Prekompilowana baza danych foomatic (IBM)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-IBM
IBM drivers.

%description -n cups-foomatic-db-IBM -l pl
Sterowniki IBM.

%package -n cups-foomatic-db-Infotec
Summary:	Precompiled foomatic database (Infotec)
Summary(pl):	Prekompilowana baza danych foomatic (Infotec)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Infotec
Infotec drivers.

%description -n cups-foomatic-db-Infotec -l pl
Sterowniki Infotec.

%package -n cups-foomatic-db-Kyocera
Summary:	Precompiled foomatic database (Kyocera)
Summary(pl):	Prekompilowana baza danych foomatic (Kyocera)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Kyocera
Kyocera drivers.

%description -n cups-foomatic-db-Kyocera -l pl
Sterowniki Kyocera.

%package -n cups-foomatic-db-Lanier
Summary:	Precompiled foomatic database (Lanier)
Summary(pl):	Prekompilowana baza danych foomatic (Lanier)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Lanier
Lanier drivers.

%description -n cups-foomatic-db-Lanier -l pl
Sterowniki Lanier.

%package -n cups-foomatic-db-Lexmark
Summary:	Precompiled foomatic database (Lexmark)
Summary(pl):	Prekompilowana baza danych foomatic (Lexmark)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Lexmark
Lexmark drivers.

%description -n cups-foomatic-db-Lexmark -l pl
Sterowniki Lexmark.

%package -n cups-foomatic-db-Minolta
Summary:	Precompiled foomatic database (Minolta)
Summary(pl):	Prekompilowana baza danych foomatic (Minolta)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Minolta
Minolta drivers.

%description -n cups-foomatic-db-Minolta -l pl
Sterowniki Minolta.

%package -n cups-foomatic-db-NEC
Summary:	Precompiled foomatic database (NEC)
Summary(pl):	Prekompilowana baza danych foomatic (NEC)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-NEC
NEC drivers.

%description -n cups-foomatic-db-NEC -l pl
Sterowniki NEC.

%package -n cups-foomatic-db-NRG
Summary:	Precompiled foomatic database (NRG)
Summary(pl):	Prekompilowana baza danych foomatic (NRG)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-NRG
NRG drivers.

%description -n cups-foomatic-db-NRG -l pl
Sterowniki NRG.

%package -n cups-foomatic-db-Okidata
Summary:	Precompiled foomatic database (Okidata)
Summary(pl):	Prekompilowana baza danych foomatic (Okidata)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Okidata
Okidata drivers.

%description -n cups-foomatic-db-Okidata -l pl
Sterowniki Okidata.

%package -n cups-foomatic-db-Olivetti
Summary:	Precompiled foomatic database (Olivetti)
Summary(pl):	Prekompilowana baza danych foomatic (Olivetti)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Olivetti
Olivetti drivers.

%description -n cups-foomatic-db-Olivetti -l pl
Sterowniki Olivetti.

%package -n cups-foomatic-db-Panasonic
Summary:	Precompiled foomatic database (Panasonic)
Summary(pl):	Prekompilowana baza danych foomatic (Panasonic)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Panasonic
Panasonic drivers.

%description -n cups-foomatic-db-Panasonic -l pl
Sterowniki Panasonic.

%package -n cups-foomatic-db-Ricoh
Summary:	Precompiled foomatic database (Ricoh)
Summary(pl):	Prekompilowana baza danych foomatic (Ricoh)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Ricoh
Ricoh drivers.

%description -n cups-foomatic-db-Ricoh -l pl
Sterowniki Ricoh.

%package -n cups-foomatic-db-Samsung
Summary:	Precompiled foomatic database (Samsung)
Summary(pl):	Prekompilowana baza danych foomatic (Samsung)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Samsung
Samsung drivers.

%description -n cups-foomatic-db-Samsung -l pl
Sterowniki Samsung.

%package -n cups-foomatic-db-Savin
Summary:	Precompiled foomatic database (Savin)
Summary(pl):	Prekompilowana baza danych foomatic (Savin)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Savin
Savin drivers.

%description -n cups-foomatic-db-Savin -l pl
Sterowniki Savin.

%package -n cups-foomatic-db-Sharp
Summary:	Precompiled foomatic database (Sharp)
Summary(pl):	Prekompilowana baza danych foomatic (Sharp)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Sharp
Sharp drivers.

%description -n cups-foomatic-db-Sharp -l pl
Sterowniki Sharp.

%package -n cups-foomatic-db-Star
Summary:	Precompiled foomatic database (Star)
Summary(pl):	Prekompilowana baza danych foomatic (Star)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Star
Star drivers.

%description -n cups-foomatic-db-Star -l pl
Sterowniki Star.

%package -n cups-foomatic-db-Tektronix
Summary:	Precompiled foomatic database (Tektronix)
Summary(pl):	Prekompilowana baza danych foomatic (Tektronix)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Tektronix
Tektronix drivers.

%description -n cups-foomatic-db-Tektronix -l pl
Sterowniki Tektronix.

%package -n cups-foomatic-db-Xerox
Summary:	Precompiled foomatic database (Xerox)
Summary(pl):	Prekompilowana baza danych foomatic (Xerox)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-Xerox
Xerox drivers.

%description -n cups-foomatic-db-Xerox -l pl
Sterowniki Xerox.

%package -n cups-foomatic-db-other
Summary:	Precompiled foomatic database (other)
Summary(pl):	Prekompilowana baza danych foomatic (inne)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description -n cups-foomatic-db-other
Other drivers.

%description -n cups-foomatic-db-other -l pl
Inne sterowniki.

%build
foomatic-compiledb -t ppd -d . -j 1
gzip ppd/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/cups/model/foomatic
cp -f ppd/*.gz $RPM_BUILD_ROOT%{_datadir}/cups/model/foomatic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/cups/model/foomatic

%files -n cups-foomatic-db-Alps
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Alps-*

%files -n cups-foomatic-db-Apollo
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Apollo-*

%files -n cups-foomatic-db-Apple
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Apple-*

%files -n cups-foomatic-db-Brother
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Brother-*

%files -n cups-foomatic-db-Canon
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Canon-*

%files -n cups-foomatic-db-Citizen
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Citizen-*

%files -n cups-foomatic-db-Compaq
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Compaq-*

%files -n cups-foomatic-db-DEC
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/DEC-*

%files -n cups-foomatic-db-Dymo-CoStar
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Dymo-CoStar-*

%files -n cups-foomatic-db-Epson
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Epson-*

%files -n cups-foomatic-db-Fujitsu
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Fujitsu-*

%files -n cups-foomatic-db-Generic
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Generic-*

%files -n cups-foomatic-db-Gestetner
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Gestetner-*

%files -n cups-foomatic-db-HP
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/HP-*

%files -n cups-foomatic-db-IBM
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/IBM-*

%files -n cups-foomatic-db-Infotec
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Infotec-*

%files -n cups-foomatic-db-Kyocera
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Kyocera-*

%files -n cups-foomatic-db-Lanier
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Lanier-*

%files -n cups-foomatic-db-Lexmark
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Lexmark-*

%files -n cups-foomatic-db-Minolta
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Minolta-*

%files -n cups-foomatic-db-NEC
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/NEC-*

%files -n cups-foomatic-db-NRG
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/NRG-*

%files -n cups-foomatic-db-Okidata
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Okidata-*

%files -n cups-foomatic-db-Olivetti
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Olivetti-*

%files -n cups-foomatic-db-Panasonic
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Panasonic-*

%files -n cups-foomatic-db-Ricoh
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Ricoh-*

%files -n cups-foomatic-db-Samsung
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Samsung-*

%files -n cups-foomatic-db-Savin
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Savin-*

%files -n cups-foomatic-db-Sharp
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Sharp-*

%files -n cups-foomatic-db-Star
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Star-*

%files -n cups-foomatic-db-Tektronix
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Tektronix-*

%files -n cups-foomatic-db-Xerox
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Xerox-*

%files -n cups-foomatic-db-other
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Anitech-*
%{_datadir}/cups/model/foomatic/Avery-*
%{_datadir}/cups/model/foomatic/CItoh-*
%{_datadir}/cups/model/foomatic/Dell-*
%{_datadir}/cups/model/foomatic/Heidelberg-*
%{_datadir}/cups/model/foomatic/Hitachi-*
%{_datadir}/cups/model/foomatic/Imagen-*
%{_datadir}/cups/model/foomatic/Kodak-*
%{_datadir}/cups/model/foomatic/Mitsubishi-*
%{_datadir}/cups/model/foomatic/Oce-*
%{_datadir}/cups/model/foomatic/PCPI-*
%{_datadir}/cups/model/foomatic/Pentax-*
%{_datadir}/cups/model/foomatic/QMS-*
%{_datadir}/cups/model/foomatic/Raven-*
%{_datadir}/cups/model/foomatic/Seiko-*
%{_datadir}/cups/model/foomatic/Tally-*
