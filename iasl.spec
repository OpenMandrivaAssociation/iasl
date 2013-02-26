%define name	iasl
%define pkgname	acpica-unix
%define version 20130214
%define release 1

Summary:	Intel ASL compiler/decompiler
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{pkgname}-%{version}.tar.gz
License:	ACPICA
Group:		Development/Kernel
Url:		http://www.acpica.org/downloads/unix_source_code.php
ExclusiveArch:	%{ix86} x86_64
BuildRequires:	flex, bison
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
IASL compiles ASL (ACPI Source Language) into AML (ACPI Machine
Language). This AML is suitable for inclusion as a DSDT in sytem
firmware. It also can disassemble AML, for debugging purposes.

%prep
%setup -q -n %{pkgname}-%{version}

%build
make iasl

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m755 generate/unix/bin*/iasl %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/iasl


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 20090422-4mdv2011.0
+ Revision: 665491
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 20090422-3mdv2011.0
+ Revision: 605945
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 20090422-2mdv2010.1
+ Revision: 522891
- rebuilt for 2010.1

* Sun May 17 2009 Isabel Vallejo <isabel@mandriva.org> 20090422-1mdv2010.0
+ Revision: 376696
- New release 20090422
- New release 20090422
- New release 20090422

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 20080213-2mdv2009.0
+ Revision: 221435
- rebuild

* Tue Feb 19 2008 Erwan Velu <erwan@mandriva.org> 20080213-1mdv2008.1
+ Revision: 173046
- New release 20080213

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20061109-1mdv2008.1
+ Revision: 126921
- kill re-definition of %%buildroot on Pixel's request


* Tue Jan 30 2007 Gwenole Beauchesne <gbeauchesne@mandriva.com> 20061109-1mdv2007.0
+ Revision: 115577
- initial packaging

