Summary:	GTK+ based fast e-mail client
Summary(pl):	Szybki klient poczty bazuj±cy na GTK+
Name:		sylpheed
Version:	0.4.66
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://sylpheed.good-day.net/sylpheed/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	glib-devel
BuildRequires:	gettext-devel
BuildRequires:	imlib-devel
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
Mew/Wanderlust o obs³uga wieloczê¶ciowych MIME o obs³uga nieskoñczonej
ilo¶ci kont pocztowych o funkcje sortowania o ksi±¿ka adresowa

%prep
%setup -q

%build
libtoolize --copy --force
gettextize --copy --force 
aclocal -I ac
autoconf
automake -a -c
%configure \
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
