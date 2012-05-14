%define pkgname	acpica-unix

Summary:	Intel ASL compiler/decompiler
Name:		iasl
Version:	20120420
Release:	1
Source0:	%{pkgname}-%{version}.tar.gz
Patch0:		acpica-20120420-Werror.patch
License:	ACPICA
Group:		Development/Kernel
Url:		http://www.acpica.org/downloads/unix_source_code.php
ExclusiveArch:	%{ix86} x86_64 %arm
BuildRequires:	flex, bison

%description
IASL compiles ASL (ACPI Source Language) into AML (ACPI Machine
Language). This AML is suitable for inclusion as a DSDT in sytem
firmware. It also can disassemble AML, for debugging purposes.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .werror~

%build
make -C source/compiler CC="%__cc $RPM_OPT_FLAGS"
cd source/tools
for i in *; do
	[ -d "$i" ] || continue
	[ "$i" = "examples" ] && continue # No Makefile here
	cd $i
	sed -i -e 's,-o $(PROG),-o $(PROG) -lpthread,g' Makefile
	make CC="%__cc $RPM_OPT_FLAGS"
	cd ..
done

# Some time soon, the project will likely switch over to using
# the versions in generate/unix:
#make -C generate/unix CC="%__cc $RPM_OPT_FLAGS"

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 source/compiler/iasl %{buildroot}%{_bindir}/
cd source/tools
for i in *; do
	[ -d "$i" ] || continue
	[ "$i" = "examples" ] && continue # No Makefile here
	cd $i
	install -m755 $i %buildroot%_bindir/
	cd ..
done

# Some time soon, the project will likely switch over to using
# the versions in generate/unix:
#make -C generate/unix install CC="%__cc $RPM_OPT_FLAGS" INSTALLDIR="%buildroot%_bindir"

%files
%defattr(-,root,root)
%_bindir/acpi*
%_bindir/iasl
