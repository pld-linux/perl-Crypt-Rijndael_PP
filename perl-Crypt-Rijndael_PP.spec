#
# Conditional build
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Rijndael_PP
Summary:	Crypt::Rijndael_PP Perl module - Rijndael encryption algorithm in pure Perl
Summary(pl):	Modu³ Perla Crypt::Rijndael_PP - algorytm szyfrowania Rijndael w samym Perlu
Name:		perl-Crypt-Rijndael_PP
Version:	0.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	db8e06273eb49358ea2e7aa87dcdd319
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a pure Perl implementation of the new AES Rijndael.

%description -l pl
Ten modu³ jest czysto perlow± implementacj± szyfru Rijndael - nowego
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
