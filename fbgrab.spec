Summary:	fbgrab - takes screenshots using the framebuffer device
Summary(pl.UTF-8):	Narzędzie zrzucające zawartość ekranu do pliku poprzez framebuffer
Name:		fbgrab
Version:	1.5
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Graphics
Source0:	https://github.com/GunnarMonell/fbgrab/archive/refs/tags/%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	a75cf6909acb099ef22ef90772fe30f7
URL:		https://github.com/GunnarMonell/fbgrab
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
Obsoletes:	fbshot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fbgrab reads the framebuffer device (/dev/fb*) or a dump thereof and
saves a PNG image file. You can use it for making screenshots of
virtually any application, from traditional text applications to your
X Window System desktop, as well as framebuffer applications.

%description -l pl.UTF-8
fbgrab czyta urządzenie framebuffera (/dev/fb*) lub zrzut z niego i
zapisuje zawartość do pliku graficznego PNG. Programu można używać do
robienia zrzutów ekranu z każdej aplikacji, od tradycyjnych aplikacji
tekstowych do ekranu X Window System, a także aplikacji
framebufferowych.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.md COPYING
%attr(755,root,root) %{_bindir}/fbgrab
%{_mandir}/man1/fbgrab.1*
