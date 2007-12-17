%define module	CGI-XMLApplication
%define version 1.1.3
%define release %mkrel 3

Summary:	%{module} module for perl
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	MPL
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PH/PHISH/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/~phish/%{module}/
BuildRequires:	perl-devel perl-XML-LibXML perl-XML-LibXSLT
BuildRequires:  perl-CGI
BuildArch:	noarch

%description
%{module} module for perl
CGI::XMLApplication is a CGI application class, that intends to enable
perl artists to implement CGIs that make use of XML/XSLT
functionality, without taking too much care about specialized
errorchecking or even care too much about XML itself. It provides the
power of the XML::LibXML/ XML::LibXSLT module package for
content deliverment.

%prep
%setup -q -n %{module}-%{version}

%{__chmod} 644 Changes MANIFEST README

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make
%make test

%clean 
%{__rm} -rf $RPM_BUILD_ROOT

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes MANIFEST README examples/*
%{_mandir}/*/*
%{perl_vendorlib}/CGI/*


