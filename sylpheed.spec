Summary:	A GTK+ based, lightweight, and fast e-mail client
Summary(pl):	Ma³y i szybki program pocztowy wykorzystuj±cy GTK+
Name:		sylpheed
Version:	0.4.64
Release:	1
License:	GPL
Group:          X11/Applications
Group(de):      X11/Applikationen
Group(pl):      X11/Aplikacje
Source:		http://sylpheed.good-day.net/sylpheed/%{name}-%{version}.tar.bz2
Patch:		%{name}-DESTDIR.patch
BuildRequires:	glib-devel >= 1.2.6
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gdk-pixbuf-devel >= 0.8.0
URL:		http://sylpheed.good-day.net/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sylpheed is an e-mail client (and news reader) based on GTK+, running
on X Window System, and aiming for
 - Quick response
 - Graceful, and sophisticated interface
 - Easy configuration, intuitive operation
 - Abundant features The appearance and interface are similar to some
   popular e-mail clients for Windows, such as Outlook Express, Becky!,
   and Datula. The interface is also designed to emulate the mailers on
   Emacsen, and almost all commands are accessible with the keyboard.

The messages are managed by MH format, and you'll be able to use it
together with another mailer based on MH format (like Mew). You can
also utilize fetchmail or/and procmail, and external programs on
receiving (like inc or imget).

%description -l pl
Sylpheed to klient poczty oraz czytnik news pracuj±cy pod X Window. Posiada
wygodny interfejs, ma spore mo¿liwo¶ci i jest ³atwy w konfiguracji.
Obs³uguje POP3, IMAP, filtrowanie poczty i wiele innych.

%prep
%setup -q
%patch -p1

%build
CFLAGS="%{rpmcflags}"
%configure \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf ChangeLog* README* TODO*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog* README* TODO*
%attr(755,root,root) %{_bindir}/sylpheed
%{_datadir}/locale/*/LC_MESSAGES/sylpheed.mo
%{_datadir}/sylpheed/manual/*/*
