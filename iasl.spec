%define pkgname	acpica-unix
%define debug_package          %{nil}

Summary:	Intel ASL compiler/decompiler
Name:		iasl
Version:	20140828
Release:	7
License:	ACPICA
Group:		Development/Kernel
Url:		http://www.acpica.org/downloads/unix_source_code.php
Source0:	%{pkgname}-%{version}.tar.gz

ExclusiveArch:	%{ix86} x86_64 %arm
BuildRequires:	bison
BuildRequires:	flex

%description
IASL compiles ASL (ACPI Source Language) into AML (ACPI Machine
Language). This AML is suitable for inclusion as a DSDT in sytem
firmware. It also can disassemble AML, for debugging purposes.

%prep
%setup -qn %{pkgname}-%{version}

%build
make iasl

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 generate/unix/bin*/iasl %{buildroot}%{_bindir}/

%files
%{_bindir}/iasl

