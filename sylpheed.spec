#
# maybe TODO: jpilot (libpisock)
#
# Conditional build:
%bcond_without	gpg		# without gpg support [disabled by ac_fixes patch?]
%bcond_without	ssl		# without ssl support
%bcond_without	ipv6		# without ipv6 support
%bcond_without	ldap		# without ldap support
%bcond_without	faces		# without compfaces support
#
Summary:	GTK+ based fast e-mail client
Summary(pl):	Szybki klient poczty bazuj�cy na GTK+
Summary(pt_BR):	Um r�pido e leve cliente de email baseado em GTK+
Name:		sylpheed
Version:	0.9.10
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://sylpheed.good-day.net/sylpheed/%{name}-%{version}.tar.bz2
# Source0-md5:	4e2242436de3cf3977a1b25b1ddc4930
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-desktop.patch
Patch2:		http://www.thewildbeast.co.uk/sylpheed/0.8.0/%{name}_save_all.patch
Patch3:		%{name}-nolibs.patch
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{?with_faces:BuildRequires:	faces-devel}
BuildRequires:	gettext-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8
%{?with_gpg:BuildRequires:	gpgme-devel >= 0.3.10}
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	libtool
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7c}
%{?with_ldap:BuildRequires:	openldap-devel}
%{?with_gpg:BuildConflicts:	gpgme-devel >= 0.4.0}
%{?with_faces:Requires:	faces}
Requires:	mailcap
URL:		http://sylpheed.good-day.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
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
%patch3 -p1

mv -f po/{sr,sr@Latn}.po
mv -f po/{zh_TW.Big5,zh_TW}.po

%{__perl} -pi -e 's/ sr / sr\@Latn /;s/zh_TW\.Big5/zh_TW/' configure.in

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I ac
%{__autoconf}
%{__automake}
%configure \
	--enable-gdk-pixbuf \
	--enable-threads \
	%{?with_faces:--disable-compfaces} \
	%{?with_gpg:--enable-gpgme} \
	%{!?with_ipv6:--disable-ipv6} \
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
