#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	Libm
Summary:	Math::Libm - Perl extension for the C math library, libm
Summary(pl.UTF-8):	Math::Libm - rozszerzenie Perla dla biblioteki matematycznej C - libm
Name:		perl-Math-Libm
Version:	1.00
Release:	17
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	26a4ce8fe507d04c7d40b9eadac428ae
URL:		http://search.cpan.org/dist/Math-Libm/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a translation of the C <math.h> file.

%description -l pl.UTF-8
Ten moduł jest tłumaczeniem pliku nagłówkowego C <math.h>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Math/Libm.pm
%dir %{perl_vendorarch}/auto/Math/Libm
%{perl_vendorarch}/auto/Math/Libm/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Libm/Libm.so
%{_mandir}/man3/*
