#
# Conditional build:
%bcond_without jconv		# without jconv support
%bcond_without gpg		# without gpg support
%bcond_without ssl		# without ssl support
%bcond_without ipv6		# without ipv6 support
%bcond_without ldap		# without ldap support
%bcond_without faces		# without compfaces support
#
%define		rname	sylpheed
%define		snap	20031018
#
Summary:	GTK+2 based fast e-mail client
Summary(pl):	Szybki klient poczty bazuj±cy na GTK+2
Summary(pt_BR):	Um rápido e leve cliente de email baseado em GTK+2
Name:		sylpheed-gtk2
Version:	0.9.7
Release:	0.%{snap}.1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	5efb2025a2ca92a05b1f19ffbc98a4fd
Patch0:		%{rname}-desktop.patch
Patch1:		http://www.thewildbeast.co.uk/sylpheed/0.8.0/%{rname}_save_all.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libtool
# experimental sorting of bconds
%{?with_faces:BuildRequires:	faces-devel}
%{?with_gpg:BuildRequires:	gpgme-devel >= 0.3.10}
%{?with_jconv:BuildRequires:	libjconv-devel}
%{?with_ldap:BuildRequires:	openldap-devel}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7c}
%{?with_faces:Requires:	faces}
Requires:	mailcap
URL:		http://sylpheed-gtk2.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	gpgme-devel >= 4.0
Obsoletes:	sylpheed
Obsoletes:	sylpheed-claws

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
Szybki klient poczty o mo¿liwo¶ciach takich jak
- o przyjazny, intuicyjny interfejs u¿ytkownika
- zintegrowany klient USENET
- mo¿liwo¶æ pracy wy³±cznie przy u¿yciu klawiatury
- klawiszologia typu Mew/Wanderlust
- obs³uga wieloczê¶ciowych MIME
- obs³uga dowolnej ilo¶ci kont pocztowych
- funkcje sortowania o ksi±¿ka adresowa
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
%setup -qn %{name}-%{version}-%{snap}
%patch0 -p1
%patch1 -p0

%build
glib-gettextize --copy --force
%{__libtoolize}
intltoolize --copy --force
%{__aclocal} -I ac
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--%{?with_jconv:en}%{!?with_jconv:dis}able-jconv \
	--enable-gdk-pixbuf \
	--enable-threads \
	%{?with_faces:--disable-compfaces} \
	%{?with_gpg:--enable-gpgme} \
	%{?with_ipv6:--enable-ipv6} \
	%{?with_ldap:--enable-ldap} \
	%{?with_ssl:--enable-ssl}

%{__make}

cd po; /bin/sh poconv.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{rname}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install %{rname}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{rname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{rname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{rname}/faq/en
%{_datadir}/%{rname}/manual/en
%dir %{_datadir}/%{rname}
%dir %{_datadir}/%{rname}/faq
%dir %{_datadir}/%{rname}/manual
%lang(de) %{_datadir}/%{rname}/faq/de
%lang(es) %{_datadir}/%{rname}/faq/es
%lang(fr) %{_datadir}/%{rname}/faq/fr
%lang(it) %{_datadir}/%{rname}/faq/it
%lang(ja) %{_datadir}/%{rname}/manual/ja
%{_desktopdir}/sylpheed.desktop
%{_pixmapsdir}/sylpheed.png
