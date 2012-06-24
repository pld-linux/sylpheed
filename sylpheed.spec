#
# Conditional build:
# _without_jconv	- without jconv support
# _without_gpg		- without gpg support
# _without_ssl		- without ssl support
# _without_ipv6		- without ipv6 support
# _without_ldap		- without ldap support
Summary:	GTK+ based fast e-mail client
Summary(pl):	Szybki klient poczty bazuj�cy na GTK+
Summary(pt_BR):	Um r�pido e leve cliente de email baseado em GTK+
Name:		sylpheed
Version:	0.9.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://sylpheed.good-day.net/sylpheed/%{name}-%{version}.tar.bz2
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-desktop.patch
Patch2:		http://www.thewildbeast.co.uk/sylpheed/0.8.0/%{name}_save_all.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	faces-devel
BuildRequires:	gettext-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gtk+-devel >= 1.2.6
%{!?_without_gpg:BuildRequires:	gpgme-devel >= 0.3.10}
%{!?_without_jconv:BuildRequires:	libjconv-devel}
BuildRequires:	libtool
%{!?_without_ssl:BuildRequires:	openssl-devel >= 0.9.6j}
%{!?_without_ldap:BuildRequires:        openldap-devel}
Requires:	faces
Requires:	mailcap
URL:		http://sylpheed.good-day.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	gpgme-devel >= 4.0
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
Szybki klient poczty o mo�liwo�ciach takich jak
- o przyjazny, intuicyjny interfejs u�ytkownika
- zintegrowany klient USENET
- mo�liwo�� pracy wy��cznie przy u�yciu klawiatury
- klawiszologia typu Mew/Wanderlust
- obs�uga wielocz�ciowych MIME
- obs�uga dowolnej ilo�ci kont pocztowych
- funkcje sortowania o ksi��ka adresowa
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
%patch2 -p0

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--%{!?_without_jconv:en}%{?_without_jconv:dis}able-jconv \
	--enable-gdk-pixbuf \
	--enable-threads \
	%{!?_without_ssl: --enable-ssl} \
	%{!?_without_ldap: --enable-ldap} \
	%{!?_without_ipv6: --enable-ipv6} \
	%{!?_without_gpg: --enable-gpgme}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

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
