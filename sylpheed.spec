# Conditional build:
# _wiht_jconv		- adds much more codesets to choice from

Summary:	GTK+ based fast e-mail client
Summary(pl):	Szybki klient poczty bazuj�cy na GTK+
Summary(pt_BR):	Um r�pido e leve cliente de email baseado em GTK+
Name:		sylpheed
Version:	0.7.8
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://sylpheed.good-day.net/sylpheed/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-ac_fixes.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib-devel
BuildRequires:	faces-devel
BuildRequires:	gettext-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gtkhtml-devel >= 0.10.1
BuildRequires:	gpgme-devel
%{?_with_jconv:BuildRequires:	libjconv-devel}
BuildRequires:	libtool
BuildRequires:	openssl-devel
Requires:	faces
URL:		http://sylpheed.good-day.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	sylpheed-claws

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
aclocal
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?_with_jconv:--disable-jconv} \
	--enable-impib \
	--enable-gdk-pixbuf \
	--enable-threads \
	--enable-ssl \
	--enable-ipv6 \
	--enable-gpgme

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

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
%{_applnkdir}/Network/Mail/*
%{_pixmapsdir}/sylpheed.png
