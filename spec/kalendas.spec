Name:           kalendas
Version:        1.0.1
Release:        1%{?dist}
Summary:        Calculations of Calendar and Julian Date
Group:          Applications/Engineering

License:        GPLv3+
URL:            https://github.com/mikemolina/kalendas
Source:         https://launchpad.net/kalendas/trunk/%{version}/+download/%{name}-%{version}.tar.gz

Requires(post): info
Requires(preun): info
BuildRequires:  texinfo >= 4.13a, gettext >= 0.17, perl-libintl >= 1.20
Requires:       perl-libintl >= 1.20
BuildArch:      noarch

%description
kalendas is a Perl script to make calendar calculations. The
computations are developed on three systems of dating: the Julian
calendar, the Gregorian calendar and the system of numbering of
Julian day/date.

%prep
%setup -q

# Conversion de codificacion latin1 a utf8, preservando tiempo original
for file in LEAME LICENCIA DEPENDENCIES; do
   iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
   touch -r $file $file.new && \
   mv $file.new $file
done
sed -i 's/\r$//' LICENCIA

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
%find_lang %{name}
%find_lang %{name} --with-man

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
   /sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
fi

%files -f %{name}.lang
%doc README.md LEAME NEWS ChangeLog AUTHORS COPYING LICENCIA DEPENDENCIES
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Sep 28 2014 Miguel Molina <mmolina.unphysics@gmail.com> - 1.0.1-1
- Initial packaging.
- Adjusted the package according to packaging guidelines.