# Conditional build:
# _with_jconv		- adds much more codesets to choice from

Summary:	GTK+ based fast e-mail client
Summary(pl):	Szybki klient poczty bazuj±cy na GTK+
Summary(pt_BR):	Um rápido e leve cliente de email baseado em GTK+
Name:		sylpheed
Version:	0.7.4
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://sylpheed.good-day.net/sylpheed/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
# Hmm... it looks like in 0.7.4 this patch is not really needed, but I've
# modified 0.7.3 version to apply on 0.7.4. If it's really not needed, kick it
# out
Patch0:		%{name}-tmpdir.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib-devel
BuildRequires:	faces-devel
BuildRequires:	gettext-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gtkhtml-devel >= 0.10.1
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
%setup -q
%patch0 -p1

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
	--enable-impib \
	--enable-gdk-pixbuf \
	--enable-threads \
	--enable-ssl \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

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
%{_datadir}/%{name}/manual/en
%lang(ja) %{_datadir}/%{name}/manual/ja
%{_applnkdir}/Network/Mail/*
%{_pixmapsdir}/sylpheed.png
