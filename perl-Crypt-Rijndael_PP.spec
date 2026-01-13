#
# Conditional build
%bcond_without	tests	# Do not perform "make test"

%define		pdir	Crypt
%define		pnam	Rijndael_PP
Summary:	Crypt::Rijndael_PP Perl module - Rijndael encryption algorithm in pure Perl
Summary(pl.UTF-8):	Moduł Perla Crypt::Rijndael_PP - algorytm szyfrowania Rijndael w samym Perlu
Name:		perl-Crypt-Rijndael_PP
Version:	0.05
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3b3715e6af129feeb2ce06ec0ebd1592
URL:		http://search.cpan.org/dist/Crypt-Rijndael_PP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a pure Perl implementation of the new AES Rijndael.

%description -l pl.UTF-8
Ten moduł jest czysto perlową implementacją szyfru Rijndael - nowego
standardu zaawansowanego szyfrowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Crypt/Rijndael_PP.pm
%{_mandir}/man3/*
