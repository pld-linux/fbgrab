Summary:	fbgrab - takes screenshots using the framebuffer device
Summary(pl):	Narzêdzie zrzucaj±ce zawarto¶æ ekranu do pliku poprzez framebuffer
Name:		fbgrab
Version:	1.0
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://hem.bredband.net/gmogmo/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	7af4d8774684182ed690d5da82d6d234
URL:		http://hem.bredband.net/gmogmo/fbgrab/
BuildRequires:	libpng-devel
Obsoletes:	fbshot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fbgrab reads the framebuffer device (/dev/fb*) or a dump thereof and
saves a PNG image file. You can use it for making screenshots of
virtually any application, from traditional text applications to your
X Window System desktop, as well as framebuffer applications.

%description -l pl
fbgrab czyta urz±dzenie framebuffera (/dev/fb*) lub zrzut z niego i
zapisuje zawarto¶æ do pliku graficznego PNG. Programu mo¿na u¿ywaæ
do robienia zrzutów ekranu z ka¿dej aplikacji, od tradycyjnych
aplikacji tekstowych do ekranu X Window System, a tak¿e aplikacji
framebufferowych.

%prep
%setup -q

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
