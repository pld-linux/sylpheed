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
Summary(pl.UTF-8):	Szybki klient poczty bazujący na GTK+
Summary(pt_BR.UTF-8):	Um rápido e leve cliente de email baseado em GTK+
Name:		sylpheed
Version:	2.4.8
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://sylpheed.sraoss.jp/sylpheed/v2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	97fcbaa1e278849408ab1d628d4d1af7
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-nolibs.patch
URL:		http://sylpheed.sraoss.jp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{?with_compface:BuildRequires:	compface-devel}
BuildRequires:	gettext-devel
%{?with_gpg:BuildRequires:	gpgme-devel >= 1:0.4.5}
BuildRequires:	gtk+2-devel >= 2:2.4.0
%{?with_gtkspell:BuildRequires:	gtkspell-devel}
BuildRequires:	libtool
%{?with_ldap:BuildRequires:	openldap-devel >= 2.4.6}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.8b}
%{?with_jpilot:BuildRequires:	pilot-link-devel}
%{?with_jpilot:Requires:	pilot-link}
BuildRequires:	pkgconfig
Requires:	mailcap
Obsoletes:	sylpheed-gtk2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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

%description -l pl.UTF-8
Szybki klient poczty o możliwościach takich jak:
- przyjazny, intuicyjny interfejs użytkownika
- zintegrowany klient USENET
- możliwość pracy wyłącznie przy użyciu klawiatury
- klawiszologia typu Mew/Wanderlust
- obsługa wieloczęściowych MIME
- obsługa dowolnej ilości kont pocztowych
- funkcje sortowania
- książka adresowa
- wsparcie szyfrowania SSL

%description -l pt_BR.UTF-8
Este programa é um rápido cliente de email modo gráfico o qual possui
recursos como:
- interface gráfica intuitiva e amigável
- cliente integrado de notícias (parcialmente implementado)
- habilitado para operacão a partir do teclado
- Mew/Wanderlust-like key bind
- multipart MIME
- controle de múltiplas contas de email (sem limite)
- armazenamento de mensagens
- funcão de ordenacão/classificacão de mensagens
- catálogo de enderecos XML-based

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{sr,sr@latin}.po

%{__perl} -pi -e 's/ sr / sr\@latin /' configure.in

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
