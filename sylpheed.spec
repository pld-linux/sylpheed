#
# Conditional build:
%bcond_without	faces		# without compfaces support
%bcond_without	gpg		# without GnuPG support
%bcond_without	ipv6		# without IPv6 support
%bcond_without	jpilot		# without JPilot support
%bcond_without	ldap		# without LDAP support
%bcond_without	ssl		# without SSL support
#
Summary:	GTK+ based fast e-mail client
Summary(pl):	Szybki klient poczty bazuj±cy na GTK+
Summary(pt_BR):	Um rápido e leve cliente de email baseado em GTK+
Name:		sylpheed
Version:	2.0.4
Release:	2
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://sylpheed.good-day.net/sylpheed/v2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	c9f1c4cf2b3933ebbb58519ba3b77887
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-nolibs.patch
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{?with_faces:BuildRequires:	faces-devel}
BuildRequires:	gettext-devel
%{?with_gpg:BuildRequires:	gpgme-devel >= 1:0.4.5}
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libtool
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
%{?with_jpilot:BuildRequires:	pilot-link-devel}
%{?with_jpilot:Requires:	pilot-link}
BuildRequires:	pkgconfig
Requires:	mailcap
URL:		http://sylpheed.good-day.net/
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
Szybki klient poczty o mo¿liwo¶ciach takich jak:
- przyjazny, intuicyjny interfejs u¿ytkownika
- zintegrowany klient USENET
- mo¿liwo¶æ pracy wy³±cznie przy u¿yciu klawiatury
- klawiszologia typu Mew/Wanderlust
- obs³uga wieloczê¶ciowych MIME
- obs³uga dowolnej ilo¶ci kont pocztowych
- funkcje sortowania
- ksi±¿ka adresowa
- wsparcie szyfrowania SSL

%description -l pt_BR
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

mv -f po/{sr,sr@Latn}.po
mv -f po/{zh_TW.Big5,zh_TW}.po

%{__perl} -pi -e 's/ sr / sr\@Latn /;s/zh_TW\.Big5/zh_TW/' configure.in

%build
%{__libtoolize}
%{__aclocal} -I ac
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_faces:--disable-compface} \
	%{?with_gpg:--enable-gpgme} \
	%{!?with_ipv6:--disable-ipv6} \
	%{?with_jpilot:--enable-jpilot} \
	%{?with_ldap:--enable-ldap} \
	%{?with_ssl:--enable-ssl}

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
