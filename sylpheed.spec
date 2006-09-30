#
# Conditional build:
%bcond_without	compface	# without compface support
%bcond_without	gpg		# without GnuPG support
%bcond_without	gtkspell	# without gtkspell support
%bcond_without	ipv6		# without IPv6 support
%bcond_without	jpilot		# without JPilot support
%bcond_without	ldap		# without LDAP support
%bcond_without	ssl		# without SSL support
#
Summary:	GTK+ based fast e-mail client
Summary(pl):	Szybki klient poczty bazuj�cy na GTK+
Summary(pt_BR):	Um r�pido e leve cliente de email baseado em GTK+
Name:		sylpheed
Version:	2.2.9
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://sylpheed.good-day.net/sylpheed/v2.2/%{name}-%{version}.tar.bz2
# Source0-md5:	45e9e89775613b0afb732fbc11c73d26
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-nolibs.patch
URL:		http://sylpheed.good-day.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{?with_compface:BuildRequires:	compface-devel}
BuildRequires:	gettext-devel
%{?with_gpg:BuildRequires:	gpgme-devel >= 1:0.4.5}
BuildRequires:	gtk+2-devel >= 2:2.4.0
%{?with_gtkspell:BuildRequires:	gtkspell-devel}
BuildRequires:	libtool
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.8b}
%{?with_jpilot:BuildRequires:	pilot-link-devel}
%{?with_jpilot:Requires:	pilot-link}
BuildRequires:	pkgconfig
Requires:	mailcap
Obsoletes:	sylpheed-claws
Obsoletes:	sylpheed-gtk2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is an X based fast e-mail client which has features (or
go for it :-)) like:
- user-friendly and intuitive interface
- integrated NetNews client (partially implemented)
- ability of keyboard-only operation
- Mew/Wanderlust-like key bind
- multipart MIME
- unlimited multiple account handling
- assortment function
- address book
- SSL support

%description -l pl
Szybki klient poczty o mo�liwo�ciach takich jak:
- przyjazny, intuicyjny interfejs u�ytkownika
- zintegrowany klient USENET
- mo�liwo�� pracy wy��cznie przy u�yciu klawiatury
- klawiszologia typu Mew/Wanderlust
- obs�uga wielocz�ciowych MIME
- obs�uga dowolnej ilo�ci kont pocztowych
- funkcje sortowania
- ksi��ka adresowa
- wsparcie szyfrowania SSL

%description -l pt_BR
Este programa � um r�pido cliente de email modo gr�fico o qual possui
recursos como:
- interface gr�fica intuitiva e amig�vel
- cliente integrado de not�cias (parcialmente implementado)
- habilitado para operac�o a partir do teclado
- Mew/Wanderlust-like key bind
- multipart MIME
- controle de m�ltiplas contas de email (sem limite)
- armazenamento de mensagens
- func�o de ordenac�o/classificac�o de mensagens
- cat�logo de enderecos XML-based

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{sr,sr@Latn}.po

%{__perl} -pi -e 's/ sr / sr\@Latn /' configure.in

%build
%{__libtoolize}
%{__aclocal} -I ac
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--%{?with_compface:en}%{!?with_compface:dis}able-compface \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-gpgme \
	--%{?with_gtkspell:en}%{!?with_gtkspell}able-gtkspell \
	--%{?with_ipv6:en}%{!?with_ipv6:dis}able-ipv6 \
	--%{?with_jpilot:en}%{!?with_jpilot:dis}able-jpilot \
	--%{?with_ldap:en}%{!?with_ldap:dis}able-ldap \
	--%{?with_ssl:en}%{!?with_ssl:dis}able-ssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/manual
%{_datadir}/%{name}/manual/en
%lang(ja) %{_datadir}/%{name}/manual/ja
%dir %{_datadir}/%{name}/faq
%{_datadir}/%{name}/faq/en
%lang(de) %{_datadir}/%{name}/faq/de
%lang(es) %{_datadir}/%{name}/faq/es
%lang(fr) %{_datadir}/%{name}/faq/fr
%lang(it) %{_datadir}/%{name}/faq/it
%{_desktopdir}/sylpheed.desktop
%{_pixmapsdir}/sylpheed.png
