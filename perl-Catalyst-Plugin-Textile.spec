%define upstream_name    Catalyst-Plugin-Textile
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Textile for Catalyst
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Text::Textile)
BuildRequires:	perl(Class::Data::Inheritable)
BuildArch:	noarch

%description
Persistent Textile processor for Catalyst.

METHODS
    $c->textile;
        Returns a ready to use the Text::Textile manpage object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

