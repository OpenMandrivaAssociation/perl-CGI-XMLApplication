%define upstream_name	 CGI-XMLApplication
%define upstream_version 1.1.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 8

Summary:	%{upstream_name} module for perl
License:	MPL
Group:		Development/Perl
Url:		http://search.cpan.org/~phish/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PH/PHISH/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(CGI)
BuildRequires:	perl(XML::LibXML)
BuildRequires:  perl(XML::LibXSLT)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} module for perl
CGI::XMLApplication is a CGI application class, that intends to enable
perl artists to implement CGIs that make use of XML/XSLT
functionality, without taking too much care about specialized
errorchecking or even care too much about XML itself. It provides the
power of the XML::LibXML/ XML::LibXSLT module package for
content deliverment.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%{__chmod} 644 Changes MANIFEST README

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
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
