%define name	iasl
%define pkgname	acpica-unix
%define version 20061109
%define release %mkrel 1

Summary:	Intel ASL compiler/decompiler
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{pkgname}-%{version}.tar.bz2
Patch0:		acpica-unix-20061109-deps.patch
License:	ACPICA
Group:		Development/Kernel
Url:		http://www.intel.com/technology/iapc/acpi/downloads.htm
ExclusiveArch:	%{ix86} x86_64
BuildRequires:	flex, bison

%description
iASL compiles ASL (ACPI Source Language) into AML (ACPI Machine
Language). This AML is suitable for inclusion as a DSDT in sytem
firmware. It also can disassemble AML, for debugging purposes.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .deps

%build
%make -C compiler

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m755 compiler/iasl $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/iasl


