%define upstream_name	 CGI-XMLApplication
%define upstream_version 1.1.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	10

Summary:	%{upstream_name} module for perl
License:	MPL
Group:		Development/Perl
Url:		http://search.cpan.org/~phish/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PH/PHISH/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(CGI)
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::LibXSLT)

BuildRequires:	perl-devel
BuildArch:	noarch

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

chmod 644 Changes MANIFEST README

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes MANIFEST README examples/*
%{_mandir}/*/*
%{perl_vendorlib}/CGI/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.1.3-8mdv2011.0
+ Revision: 680702
- mass rebuild

* Fri Feb 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.1.3-7mdv2011.0
+ Revision: 504808
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1.3-6mdv2010.0
+ Revision: 430321
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.1.3-5mdv2009.0
+ Revision: 255835
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1.3-3mdv2008.1
+ Revision: 136678
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.3-3mdv2008.0
+ Revision: 86065
- rebuild


* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.1.3-2mdk
- buildrequires fix

* Tue May 11 2004 Michael Scherer <misc@mandrake.org> 1.1.3-1mdk
- New release 1.1.3
- rpmbuildupdate aware
- add make test

* Thu Aug 28 2003 François Pons <fpons@mandrakesoft.com> 1.1.2-1mdk
- 1.1.2.

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 1.1.1-4mdk
- macroize
- %%makeinstall-std
- remove automatically found requires

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.1-3mdk
- rebuild for new auto{prov,req}

* Wed Jul 10 2002 Pixel <pixel@mandrakesoft.com> 1.1.1-2mdk
- rebuild for perl 5.8.0

* Mon Apr 15 2002 Philippe Libat <philippe@mandrakesoft.com> 1.1.1-1mdk
- initial RPM

