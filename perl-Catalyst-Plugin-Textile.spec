%define upstream_name    Catalyst-Plugin-Textile
Name:		perl-%{upstream_name}
Version:	0.01
Release:	8

Summary:	Textile for Catalyst
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Catalyst-Plugin-Textile
Source0:	https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Textile-%{version}.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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

