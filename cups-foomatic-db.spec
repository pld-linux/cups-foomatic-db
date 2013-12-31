Summary:	Precompiled foomatic database
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic
Name:		cups-foomatic-db
Version:	20110615
Release:	1
License:	GPL
Group:		Applications/System
URL:		http://www.linuxprinting.org/foomatic.html
BuildRequires:	foomatic-db = %{version}
BuildRequires:	foomatic-db-hpijs = 2:%{version}
Requires:	cups-filters >= 1.0.43
Requires:	cups-foomatic-db-driver
Obsoletes:	cups-foomatic-db-Gestetner
Obsoletes:	cups-foomatic-db-Lanier
Obsoletes:	cups-foomatic-db-NRG
Obsoletes:	cups-foomatic-db-Savin
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Precompiled foomatic database - common data.

%description -l pl.UTF-8
Prekompilowana baza danych foomatic - dane wspólne.

%package Alps
Summary:	Precompiled foomatic database (Alps)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Alps)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Alps
Alps drivers.

%description Alps -l pl.UTF-8
Sterowniki Alps.

%package Apollo
Summary:	Precompiled foomatic database (Apollo)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Apollo)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Apollo
Apollo drivers.

%description Apollo -l pl.UTF-8
Sterowniki Apollo.

%package Apple
Summary:	Precompiled foomatic database (Apple)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Apple)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Apple
Apple drivers.

%description Apple -l pl.UTF-8
Sterowniki Apple.

%package Brother
Summary:	Precompiled foomatic database (Brother)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Brother)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Brother
Brother drivers.

%description Brother -l pl.UTF-8
Sterowniki Brother.

%package Canon
Summary:	Precompiled foomatic database (Canon)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Canon)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Canon
Canon drivers.

%description Canon -l pl.UTF-8
Sterowniki Canon.

%package Citizen
Summary:	Precompiled foomatic database (Citizen)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Citizen)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Citizen
Citizen drivers.

%description Citizen -l pl.UTF-8
Sterowniki Citizen.

%package Compaq
Summary:	Precompiled foomatic database (Compaq)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Compaq)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Compaq
Compaq drivers.

%description Compaq -l pl.UTF-8
Sterowniki Compaq.

%package DEC
Summary:	Precompiled foomatic database (DEC)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (DEC)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description DEC
DEC drivers.

%description DEC -l pl.UTF-8
Sterowniki DEC.

%package Dymo-CoStar
Summary:	Precompiled foomatic database (Dymo-CoStar)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Dymo-CoStar)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Dymo-CoStar
Dymo-CoStar drivers.

%description Dymo-CoStar -l pl.UTF-8
Sterowniki Dymo-CoStar.

%package Epson
Summary:	Precompiled foomatic database (Epson)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Epson)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Epson
Epson drivers.

%description Epson -l pl.UTF-8
Sterowniki Epson.

%package Fujitsu
Summary:	Precompiled foomatic database (Fujitsu)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Fujitsu)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Fujitsu
Fujitsu drivers.

%description Fujitsu -l pl.UTF-8
Sterowniki Fujitsu.

%package Generic
Summary:	Precompiled foomatic database (Generic)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Generic)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Generic
Generic drivers.

%description Generic -l pl.UTF-8
Sterowniki Generic.

%package HP
Summary:	Precompiled foomatic database (HP)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (HP)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description HP
HP drivers.

%description HP -l pl.UTF-8
Sterowniki HP.

%package IBM
Summary:	Precompiled foomatic database (IBM)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (IBM)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description IBM
IBM drivers.

%description IBM -l pl.UTF-8
Sterowniki IBM.

%package Infotec
Summary:	Precompiled foomatic database (Infotec)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Infotec)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Infotec
Infotec drivers.

%description Infotec -l pl.UTF-8
Sterowniki Infotec.

%package Kyocera
Summary:	Precompiled foomatic database (Kyocera)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Kyocera)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Kyocera
Kyocera drivers.

%description Kyocera -l pl.UTF-8
Sterowniki Kyocera.

%package Lexmark
Summary:	Precompiled foomatic database (Lexmark)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Lexmark)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Lexmark
Lexmark drivers.

%description Lexmark -l pl.UTF-8
Sterowniki Lexmark.

%package Minolta
Summary:	Precompiled foomatic database (Minolta)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Minolta)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	min12xxw
Provides:	%{name}-driver

%description Minolta
Minolta drivers.

%description Minolta -l pl.UTF-8
Sterowniki Minolta.

%package NEC
Summary:	Precompiled foomatic database (NEC)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (NEC)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description NEC
NEC drivers.

%description NEC -l pl.UTF-8
Sterowniki NEC.

%package Oki
Summary:	Precompiled foomatic database (Oki)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Oki)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver
Obsoletes:	cups-foomatic-db-Okidata

%description Oki
Oki drivers.

%description Oki -l pl.UTF-8
Sterowniki Oki.

%package Olivetti
Summary:	Precompiled foomatic database (Olivetti)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Olivetti)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Olivetti
Olivetti drivers.

%description Olivetti -l pl.UTF-8
Sterowniki Olivetti.

%package Panasonic
Summary:	Precompiled foomatic database (Panasonic)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Panasonic)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Panasonic
Panasonic drivers.

%description Panasonic -l pl.UTF-8
Sterowniki Panasonic.

%package Ricoh
Summary:	Precompiled foomatic database (Ricoh)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Ricoh)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Ricoh
Ricoh drivers.

%description Ricoh -l pl.UTF-8
Sterowniki Ricoh.

%package Samsung
Summary:	Precompiled foomatic database (Samsung)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Samsung)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Samsung
Samsung drivers.

%description Samsung -l pl.UTF-8
Sterowniki Samsung.

%package Sharp
Summary:	Precompiled foomatic database (Sharp)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Sharp)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Sharp
Sharp drivers.

%description Sharp -l pl.UTF-8
Sterowniki Sharp.

%package Star
Summary:	Precompiled foomatic database (Star)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Star)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Star
Star drivers.

%description Star -l pl.UTF-8
Sterowniki Star.

%package Tektronix
Summary:	Precompiled foomatic database (Tektronix)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Tektronix)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Tektronix
Tektronix drivers.

%description Tektronix -l pl.UTF-8
Sterowniki Tektronix.

%package Toshiba
Summary:	Precompiled foomatic database (Toshiba)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Toshiba)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Toshiba
Toshiba drivers.

%description Toshiba -l pl.UTF-8
Sterowniki Toshiba.

%package Xerox
Summary:	Precompiled foomatic database (Xerox)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (Xerox)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description Xerox
Xerox drivers.

%description Xerox -l pl.UTF-8
Sterowniki Xerox.

%package other
Summary:	Precompiled foomatic database (other)
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic (inne)
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-driver

%description other
Other drivers.

%description other -l pl.UTF-8
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

%files Lexmark
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Lexmark-*

%files Minolta
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Minolta*

%files NEC
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/NEC-*

%files Oki
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Oki-*

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

%files Sharp
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Sharp-*

%files Star
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Star-*

%files Tektronix
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Tektronix-*

%files Toshiba
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Toshiba-*

%files Xerox
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Xerox-*

%files other
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Anitech-*
%{_datadir}/cups/model/foomatic/Avery-*
%{_datadir}/cups/model/foomatic/CItoh-*
%{_datadir}/cups/model/foomatic/Dell-*
%{_datadir}/cups/model/foomatic/Genicom-*
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
%{_datadir}/cups/model/foomatic/SiPix-*
%{_datadir}/cups/model/foomatic/Sony-*
%{_datadir}/cups/model/foomatic/Tally-*
%{_datadir}/cups/model/foomatic/Xante-*
