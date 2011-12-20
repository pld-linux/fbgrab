Summary:	fbgrab - takes screenshots using the framebuffer device
Summary(pl.UTF-8):	Narzędzie zrzucające zawartość ekranu do pliku poprzez framebuffer
Name:		fbgrab
Version:	1.0
Release:	3
Epoch:		1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://hem.bredband.net/gmogmo/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	7af4d8774684182ed690d5da82d6d234
Patch0:		%{name}-bigendian.patch
URL:		http://hem.bredband.net/gmogmo/fbgrab/
BuildRequires:	libpng-devel
Obsoletes:	fbshot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fbgrab reads the framebuffer device (/dev/fb*) or a dump thereof and
saves a PNG image file. You can use it for making screenshots of
virtually any application, from traditional text applications to your
X Window System desktop, as well as framebuffer applications.

%description -l pl.UTF-8
fbgrab czyta urządzenie framebuffera (/dev/fb*) lub zrzut z niego i
zapisuje zawartość do pliku graficznego PNG. Programu można używać
do robienia zrzutów ekranu z każdej aplikacji, od tradycyjnych
aplikacji tekstowych do ekranu X Window System, a także aplikacji
framebufferowych.

%prep
%setup -q
%patch0 -p1

%build
%{__cc} %{rpmcflags} %{rpmldflags} -Wall -o fbgrab fbgrab.c -lpng

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install fbgrab $RPM_BUILD_ROOT%{_bindir}
install fbgrab.1.man $RPM_BUILD_ROOT%{_mandir}/man1/fbgrab.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
