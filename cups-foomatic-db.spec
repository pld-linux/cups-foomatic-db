Summary:	Precompiled foomatic database
Summary(pl):	Prekompilowana baza danych foomatic
Name:		cups-foomatic-db
Version:	20050405
Release:	1
License:	GPL	
Group:		Applications/System
URL:		http://www.linuxprinting.org/foomatic.html
Requires:	cups-filter-foomatic >= 3.0.0
Requires:	cups-foomatic-db-driver
BuildRequires:	foomatic-db = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Precompiled foomatic database - common data.

%description
Prekompilowana baza danych foomatic - dane wspólne.

%package Alps
Summary:	Precompiled foomatic database (Alps)
Summary(pl):	Prekompilowana baza danych foomatic (Alps)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Alps
Alps drivers.

%description Alps -l pl
Sterowniki Alps.

%package Apollo
Summary:	Precompiled foomatic database (Apollo)
Summary(pl):	Prekompilowana baza danych foomatic (Apollo)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Apollo
Apollo drivers.

%description Apollo -l pl
Sterowniki Apollo.

%package Apple
Summary:	Precompiled foomatic database (Apple)
Summary(pl):	Prekompilowana baza danych foomatic (Apple)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Apple
Apple drivers.

%description Apple -l pl
Sterowniki Apple.

%package Brother
Summary:	Precompiled foomatic database (Brother)
Summary(pl):	Prekompilowana baza danych foomatic (Brother)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Brother
Brother drivers.

%description Brother -l pl
Sterowniki Brother.

%package Canon
Summary:	Precompiled foomatic database (Canon)
Summary(pl):	Prekompilowana baza danych foomatic (Canon)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Canon
Canon drivers.

%description Canon -l pl
Sterowniki Canon.

%package Citizen
Summary:	Precompiled foomatic database (Citizen)
Summary(pl):	Prekompilowana baza danych foomatic (Citizen)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Citizen
Citizen drivers.

%description Citizen -l pl
Sterowniki Citizen.

%package Compaq
Summary:	Precompiled foomatic database (Compaq)
Summary(pl):	Prekompilowana baza danych foomatic (Compaq)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Compaq
Compaq drivers.

%description Compaq -l pl
Sterowniki Compaq.

%package DEC
Summary:	Precompiled foomatic database (DEC)
Summary(pl):	Prekompilowana baza danych foomatic (DEC)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description DEC
DEC drivers.

%description DEC -l pl
Sterowniki DEC.

%package Dymo-CoStar
Summary:	Precompiled foomatic database (Dymo-CoStar)
Summary(pl):	Prekompilowana baza danych foomatic (Dymo-CoStar)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Dymo-CoStar
Dymo-CoStar drivers.

%description Dymo-CoStar -l pl
Sterowniki Dymo-CoStar.

%package Epson
Summary:	Precompiled foomatic database (Epson)
Summary(pl):	Prekompilowana baza danych foomatic (Epson)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Epson
Epson drivers.

%description Epson -l pl
Sterowniki Epson.

%package Fujitsu
Summary:	Precompiled foomatic database (Fujitsu)
Summary(pl):	Prekompilowana baza danych foomatic (Fujitsu)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Fujitsu
Fujitsu drivers.

%description Fujitsu -l pl
Sterowniki Fujitsu.

%package Generic
Summary:	Precompiled foomatic database (Generic)
Summary(pl):	Prekompilowana baza danych foomatic (Generic)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Generic
Generic drivers.

%description Generic -l pl
Sterowniki Generic.

%package Gestetner
Summary:	Precompiled foomatic database (Gestetner)
Summary(pl):	Prekompilowana baza danych foomatic (Gestetner)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Gestetner
Gestetner drivers.

%description Gestetner -l pl
Sterowniki Gestetner.

%package HP
Summary:	Precompiled foomatic database (HP)
Summary(pl):	Prekompilowana baza danych foomatic (HP)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description HP
HP drivers.

%description HP -l pl
Sterowniki HP.

%package IBM
Summary:	Precompiled foomatic database (IBM)
Summary(pl):	Prekompilowana baza danych foomatic (IBM)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description IBM
IBM drivers.

%description IBM -l pl
Sterowniki IBM.

%package Infotec
Summary:	Precompiled foomatic database (Infotec)
Summary(pl):	Prekompilowana baza danych foomatic (Infotec)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Infotec
Infotec drivers.

%description Infotec -l pl
Sterowniki Infotec.

%package Kyocera
Summary:	Precompiled foomatic database (Kyocera)
Summary(pl):	Prekompilowana baza danych foomatic (Kyocera)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Kyocera
Kyocera drivers.

%description Kyocera -l pl
Sterowniki Kyocera.

%package Lanier
Summary:	Precompiled foomatic database (Lanier)
Summary(pl):	Prekompilowana baza danych foomatic (Lanier)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Lanier
Lanier drivers.

%description Lanier -l pl
Sterowniki Lanier.

%package Lexmark
Summary:	Precompiled foomatic database (Lexmark)
Summary(pl):	Prekompilowana baza danych foomatic (Lexmark)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Lexmark
Lexmark drivers.

%description Lexmark -l pl
Sterowniki Lexmark.

%package Minolta
Summary:	Precompiled foomatic database (Minolta)
Summary(pl):	Prekompilowana baza danych foomatic (Minolta)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Minolta
Minolta drivers.

%description Minolta -l pl
Sterowniki Minolta.

%package NEC
Summary:	Precompiled foomatic database (NEC)
Summary(pl):	Prekompilowana baza danych foomatic (NEC)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description NEC
NEC drivers.

%description NEC -l pl
Sterowniki NEC.

%package NRG
Summary:	Precompiled foomatic database (NRG)
Summary(pl):	Prekompilowana baza danych foomatic (NRG)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description NRG
NRG drivers.

%description NRG -l pl
Sterowniki NRG.

%package Okidata
Summary:	Precompiled foomatic database (Okidata)
Summary(pl):	Prekompilowana baza danych foomatic (Okidata)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Okidata
Okidata drivers.

%description Okidata -l pl
Sterowniki Okidata.

%package Olivetti
Summary:	Precompiled foomatic database (Olivetti)
Summary(pl):	Prekompilowana baza danych foomatic (Olivetti)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Olivetti
Olivetti drivers.

%description Olivetti -l pl
Sterowniki Olivetti.

%package Panasonic
Summary:	Precompiled foomatic database (Panasonic)
Summary(pl):	Prekompilowana baza danych foomatic (Panasonic)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Panasonic
Panasonic drivers.

%description Panasonic -l pl
Sterowniki Panasonic.

%package Ricoh
Summary:	Precompiled foomatic database (Ricoh)
Summary(pl):	Prekompilowana baza danych foomatic (Ricoh)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Ricoh
Ricoh drivers.

%description Ricoh -l pl
Sterowniki Ricoh.

%package Samsung
Summary:	Precompiled foomatic database (Samsung)
Summary(pl):	Prekompilowana baza danych foomatic (Samsung)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Samsung
Samsung drivers.

%description Samsung -l pl
Sterowniki Samsung.

%package Savin
Summary:	Precompiled foomatic database (Savin)
Summary(pl):	Prekompilowana baza danych foomatic (Savin)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Savin
Savin drivers.

%description Savin -l pl
Sterowniki Savin.

%package Sharp
Summary:	Precompiled foomatic database (Sharp)
Summary(pl):	Prekompilowana baza danych foomatic (Sharp)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Sharp
Sharp drivers.

%description Sharp -l pl
Sterowniki Sharp.

%package Star
Summary:	Precompiled foomatic database (Star)
Summary(pl):	Prekompilowana baza danych foomatic (Star)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Star
Star drivers.

%description Star -l pl
Sterowniki Star.

%package Tektronix
Summary:	Precompiled foomatic database (Tektronix)
Summary(pl):	Prekompilowana baza danych foomatic (Tektronix)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Tektronix
Tektronix drivers.

%description Tektronix -l pl
Sterowniki Tektronix.

%package Xerox
Summary:	Precompiled foomatic database (Xerox)
Summary(pl):	Prekompilowana baza danych foomatic (Xerox)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description Xerox
Xerox drivers.

%description Xerox -l pl
Sterowniki Xerox.

%package other
Summary:	Precompiled foomatic database (other)
Summary(pl):	Prekompilowana baza danych foomatic (inne)
Group:		Applications/System
Provides:	%{name}-driver
Requires:	%{name} = %{version}-%{release}

%description other
Other drivers.

%description other -l pl
Inne sterowniki.

%prep
%setup -q -c -T

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

%files Alps
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Alps-*

%files Apollo
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Apollo-*

%files Apple
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Apple-*

%files Brother
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Brother-*

%files Canon
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Canon-*

%files Citizen
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Citizen-*

%files Compaq
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Compaq-*

%files DEC
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/DEC-*

%files Dymo-CoStar
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Dymo-CoStar-*

%files Epson
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Epson-*

%files Fujitsu
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Fujitsu-*

%files Generic
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Generic-*

%files Gestetner
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Gestetner-*

%files HP
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/HP-*

%files IBM
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/IBM-*

%files Infotec
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Infotec-*

%files Kyocera
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Kyocera-*

%files Lanier
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Lanier-*

%files Lexmark
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Lexmark-*

%files Minolta
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Minolta-*

%files NEC
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/NEC-*

%files NRG
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/NRG-*

%files Okidata
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Okidata-*

%files Olivetti
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Olivetti-*

%files Panasonic
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Panasonic-*

%files Ricoh
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Ricoh-*

%files Samsung
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Samsung-*

%files Savin
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Savin-*

%files Sharp
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Sharp-*

%files Star
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Star-*

%files Tektronix
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Tektronix-*

%files Xerox
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Xerox-*

%files other
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
