%define name	iasl
%define pkgname	acpica-unix
%define version 20090422
%define release %mkrel 4

Summary:	Intel ASL compiler/decompiler
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{pkgname}-%{version}.tar.gz
License:	ACPICA
Group:		Development/Kernel
Url:		http://www.acpica.org/downloads/unix_source_code.php
ExclusiveArch:	%{ix86} x86_64 %arm
BuildRequires:	flex, bison
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
IASL compiles ASL (ACPI Source Language) into AML (ACPI Machine
Language). This AML is suitable for inclusion as a DSDT in sytem
firmware. It also can disassemble AML, for debugging purposes.

%prep
%setup -q -n %{pkgname}-%{version}

%build
make -C compiler

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m755 compiler/iasl %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/iasl
