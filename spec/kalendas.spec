Name:           kalendas
Version:        1.3.1
Release:        3%{?dist}
Summary:        Calculations of Calendar and Julian Date
Summary(es):    Cálculos de Calendario y Fecha Juliana
Summary(pt_BR): Cálculos do Calendário e Data Juliana

License:        GPLv3+
URL:            http://mikemolina.github.io/kalendas-home
Source:         https://launchpad.net/kalendas/trunk/%{version}/+download/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  texinfo >= 4.13a
BuildRequires:  gettext >= 0.17
BuildRequires:  perl-libintl >= 1.20
BuildRequires:  pkgconfig(bash-completion)
Requires(post): info
Requires(preun): info
Requires:       perl-libintl >= 1.20
BuildArch:      noarch

%description
kalendas is a Perl Script to make calendar calculations. The
computations are developed on three systems of dating: the Julian
calendar, the Gregorian calendar and the system of numbering of
Julian day/date.

%description -l es
kalendas es un Perl Script para realizar cálculos de calendario.
Los cómputos están desarrollados sobre tres sistemas de datación:
el calendario Juliano, el calendario Gregoriano y el sistema de
numeración de día/fecha Juliana.

%description -l pt_BR
kalendas é um Perl Script para realizar cálculos de calendário.
Os cômputos estão desenvolvidos sobre três sistemas de datação:
o calendário Juliano, o calendário Gregoriano e o sistema de
numeração de dia/data Juliana.

%prep
%setup -q

# Conversion de codificacion latin1 a utf8, preservando tiempo original
for file in DEPENDENCIES; do
   iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
   touch -r $file $file.new && \
   mv $file.new $file
done

%build
%configure
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
%find_lang %{name} --with-man

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
   /sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
fi

%files -f %{name}.lang
%license COPYING LICENCIA
%doc README.md LEAME.md NEWS ChangeLog AUTHORS DEPENDENCIES
%{_bindir}/kalendas
%{_mandir}/man1/kalendas.1.*
%{_infodir}/kalendas.info.gz
%{_datadir}/bash-completion/completions/kalendas

%check
make check

%changelog
* Sat Mar 2 2019 Miguel Molina <mmolina.unphysics@gmail.com> - 1.3.1-3
- Spec file corrections, Red Hat Bugzilla bug 1325477.

* Thu Dec 13 2018 Miguel Molina <mmolina.unphysics@gmail.com> - 1.3.1-2
- Add build dependency referred to compiler C.

* Mon Dec 10 2018 Miguel Molina <mmolina.unphysics@gmail.com> - 1.3.1-1
- Package updated to version 1.3.1.
- Maintenance corrections for package distribution.

* Tue Dec 29 2015 Miguel Molina <mmolina.unphysics@gmail.com> - 1.3.0-1
- Package updated to version 1.3.0.
- URL updated.
- Add tests performance.

* Wed Jul 15 2015 Miguel Molina <mmolina.unphysics@gmail.com> - 1.2.0-1
- Package updated to version 1.2.0.
- URL updated.
- Add dependency with bash-completion via pkg-config.

* Tue Dec 30 2014 Miguel Molina <mmolina.unphysics@gmail.com> - 1.1.0-1
- Package updated to version 1.1.0.
- Packaging for fedora 22.

* Sat Oct 11 2014 Miguel Molina <mmolina.unphysics@gmail.com> - 1.0.2-1
- Package updated to version 1.0.2.
- New direction web for distros based in RPM.
- Spanish, portuguese translations in spec file fields.

* Sun Sep 28 2014 Miguel Molina <mmolina.unphysics@gmail.com> - 1.0.1-1
- Initial packaging.
- Adjusted the package according to packaging guidelines.
