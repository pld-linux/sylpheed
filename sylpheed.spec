# Conditional build:
# _with_jconv		- adds much more codesets to choice from
Summary:	GTK+ based fast e-mail client
Summary(pl):	Szybki klient poczty bazuj±cy na GTK+
Name:		sylpheed
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://sylpheed.good-day.net/sylpheed/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-open-url.patch
Patch1:		%{name}-fix-compose-cmdline.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	faces-devel
BuildRequires:	gettext-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gtkhtml-devel >= 0.10.1
%{?_with_jconv:BuildRequires:	libjconv-devel}
BuildRequires:	libtool
Requires:	faces
URL:		http://sylpheed.good-day.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This program is an X based fast e-mail client which has features (or
go for it :-)) like: o user-friendly and intuitive interface o
integrated NetNews client (partially implemented) o ability of
keyboard-only operation o Mew/Wanderlust-like key bind o multipart
MIME o unlimited multiple account handling o assortment function o
address book

%description -l pl
Szybki klient poczty o mo¿liwo¶ciach takich jak: o przyjazny,
intuicyjny interfejs u¿ytkownika o zintegrowany klient USENET o
mo¿liwo¶æ pracy wy³±cznie przy u¿yciu klawiatury o klawiszologia typu
Mew/Wanderlust o obs³uga wieloczê¶ciowych MIME o obs³uga dowolnej
ilo¶ci kont pocztowych o funkcje sortowania o ksi±¿ka adresowa

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force 
aclocal -I ac
autoconf
autoheader
automake --add-missing --foreign --copy
%configure \
	%{!?_with_jconv:--disable-jconv} \
	--enable-threads \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/manual
%lang(ja) %{_datadir}/%{name}/manual/ja
%{_applnkdir}/Network/Mail/*
