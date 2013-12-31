# TODO: update hpijs -> nonfree
Summary:	Precompiled foomatic database
Summary(pl.UTF-8):	Prekompilowana baza danych foomatic
Name:		cups-foomatic-db
Version:	20110615
Release:	2
License:	GPL
Group:		Applications/System
URL:		http://www.linuxprinting.org/foomatic.html
BuildRequires:	foomatic-db = %{version}
BuildRequires:	foomatic-db-hpijs = 2:20081228
#BuildRequires:	foomatic-db-hpijs = 2:%{version}
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
Other drivers: Anitech, Avery, CItoh, Dell, Genicom, Heidelberg,
Hitachi, Imagen, Imagistics, Kodak, Mitsubishi, Oce, PCPI, Pentax,
QMS, Raven, Seiko, SiPix, Sony, Tally, Texas Instruments, Xante.

%description other -l pl.UTF-8
Inne sterowniki: Anitech, Avery, CItoh, Dell, Genicom, Heidelberg,
Hitachi, Imagen, Imagistics, Kodak, Mitsubishi, Oce, PCPI, Pentax,
QMS, Raven, Seiko, SiPix, Sony, Tally, Texas Instruments, Xante.

%prep
%setup -q -c -T

%build
foomatic-compiledb -t ppd -d ppd -j 1
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
%{_datadir}/cups/model/foomatic/Alps-*.ppd.gz

%files Apollo
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Apollo-*.ppd.gz

%files Apple
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Apple-*.ppd.gz

%files Brother
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Brother-*.ppd.gz

%files Canon
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Canon-*.ppd.gz

%files Citizen
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Citizen-*.ppd.gz

%files Compaq
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Compaq-*.ppd.gz

%files DEC
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/DEC-*.ppd.gz

%files Dymo-CoStar
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Dymo-CoStar-*.ppd.gz

%files Epson
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Epson-*.ppd.gz

%files Fujitsu
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Fujitsu-*.ppd.gz

%files Generic
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Generic-*.ppd.gz

%files HP
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/HP-*.ppd.gz

%files IBM
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/IBM-*.ppd.gz

%files Infotec
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Infotec-*.ppd.gz

%files Kyocera
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Kyocera-*.ppd.gz

%files Lexmark
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Lexmark-*.ppd.gz

%files Minolta
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Minolta*.ppd.gz

%files NEC
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/NEC-*.ppd.gz

%files Oki
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Oki-*.ppd.gz

%files Olivetti
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Olivetti-*.ppd.gz

%files Panasonic
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Panasonic-*.ppd.gz

%files Ricoh
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Ricoh-*.ppd.gz

%files Samsung
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Samsung-*.ppd.gz

%files Sharp
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Sharp-*.ppd.gz

%files Star
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Star-*.ppd.gz

%files Tektronix
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Tektronix-*.ppd.gz

%files Toshiba
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Toshiba-*.ppd.gz

%files Xerox
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Xerox-*.ppd.gz

%files other
%defattr(644,root,root,755)
%{_datadir}/cups/model/foomatic/Anitech-*.ppd.gz
%{_datadir}/cups/model/foomatic/Avery-*.ppd.gz
%{_datadir}/cups/model/foomatic/CItoh-*.ppd.gz
%{_datadir}/cups/model/foomatic/Dell-*.ppd.gz
%{_datadir}/cups/model/foomatic/Genicom-*.ppd.gz
%{_datadir}/cups/model/foomatic/Heidelberg-*.ppd.gz
%{_datadir}/cups/model/foomatic/Hitachi-*.ppd.gz
%{_datadir}/cups/model/foomatic/Imagen-*.ppd.gz
%{_datadir}/cups/model/foomatic/Imagistics-*.ppd.gz
%{_datadir}/cups/model/foomatic/Kodak-*.ppd.gz
%{_datadir}/cups/model/foomatic/Mitsubishi-*.ppd.gz
%{_datadir}/cups/model/foomatic/Oce-*.ppd.gz
%{_datadir}/cups/model/foomatic/PCPI-*.ppd.gz
%{_datadir}/cups/model/foomatic/Pentax-*.ppd.gz
%{_datadir}/cups/model/foomatic/QMS-*.ppd.gz
%{_datadir}/cups/model/foomatic/Raven-*.ppd.gz
%{_datadir}/cups/model/foomatic/Seiko-*.ppd.gz
%{_datadir}/cups/model/foomatic/SiPix-*.ppd.gz
%{_datadir}/cups/model/foomatic/Sony-*.ppd.gz
%{_datadir}/cups/model/foomatic/Tally-*.ppd.gz
%{_datadir}/cups/model/foomatic/Texas_Instruments-*.ppd.gz
%{_datadir}/cups/model/foomatic/Xante-*.ppd.gz
