# Define if you want to build the sane backend (default)
%define sane_backend		0
%{?_with_sane:			%global sane_backend 1}
%{?_without_sane:		%global sane_backend 0}

%define hpip_major		0
%define hpip_libname		%mklibname hpip %{hpip_major}

%define sane_hpaio_major	1
%define sane_hpaio_libname	%mklibname sane-hpaio %{sane_hpaio_major}

# Suppress automatically generated Requires for devel packages
%define _requires_exceptions devel\(.*\)

%define subrel 2

Summary: HP Linux Imaging and Printing Project
Name:	hplip
Version:	3.11.7
Release:	9
License:	GPLv2+ and MIT
Group: 	System Environment/Daemons
Source:	%{name}-%{version}.tar.gz

# taken from http://patch-tracker.debian.org/package/hplip/3.11.7-1
Patch1: 01_rss.dpatch
Patch2: 10_shebang_fixes.dpatch
Patch3: 14_charsign_fixes.dpatch
Patch4: 85_rebuild_python_ui.dpatch
Patch5: 87_move_documentation.dpatch
Patch6: hp_photosmart_pro_b9100_support.dpatch
Patch7: pjl-duplex-binding.dpatch
Patch8: kde4-kdesudo-support.dpatch
Patch9: hp-check-groups.dpatch
Patch10: hp-check_debian.dpatch
Patch11: hp-setup-prompt-for-custom-PPD.dpatch
Patch12: hplip-systray-longer-timeout-for-system-tray-start.dpatch
Patch13: kbsd.dpatch
Patch14: udev-rules-use-attrs-not-sysfs-and-hp-mkuri-call-fix.dpatch
Patch15: hp-mkuri-take-into-account-already-installed-plugin-also-for-exit-value.dpatch
Patch16: ubuntu-hp-mkuri-notification-text.dpatch
Patch17: simple-scan-as-default.dpatch
Patch18: make-commafy-correctly-work-with-python-2.dpatch
Patch19: remove-duplicate-entry-for-cp1700-in-drv-files.dpatch
Patch20: black-stripes-on-pcl5c-printouts.dpatch
Patch21: try_libhpmud.so.0.dpatch
Patch22: add-lidil-two-cartridge-modes.dpatch
Patch23: add_missing_newline_for_error_log.dpatch
Patch24: CVE-2010-4267.dpatch
Patch25: large-sizes-borderless-on-photosmart-pro-b-series.dpatch
Patch26: more-user-friendly-choice-names-for-installed-cartridges.dpatch
Patch27: hplip-syslog-fix-debug-messages-to-error.dpatch
Patch28: cups-1.5.0-compatibility.dpatch
Patch29: mdns-py-network-printer-search-key-error.dpatch
Patch30: mdns-py-typo.dpatch
Patch31: hpfax-bug-function-used-before-importing-log.dpatch
Patch32: hp-systray-make-menu-title-visible-in-sni-qt-indicator.dpatch
Patch33: hp-systray-make-menu-appear-in-sni-qt-indicator-with-kde.dpatch
Patch34: hpcups-top-margins-not-respected.dpatch

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

#BuildRequires:	python-sip >= 4.1.1
#BuildRequires:	net-snmp-devel
BuildRequires:	python
#hplip should use libusb-compat-devel not libusb-devel
BuildRequires:	pkgconfig(libusb)
#BuildRequires:	imagemagick
BuildRequires:	autoconf
BuildRequires:	cups-devel
BuildRequires:	libjpeg-devel
#BuildRequires:	python-devel
#BuildRequires:	desktop-file-utils
#BuildRequires:	libdbus-devel
#BuildRequires:	udev-devel
#BuildRequires:	polkit
#BuildRequires:	gphoto2-devel
#BuildRequires:  libv4l-devel
Requires:	cups
# For dynamic ppd generation.
#Requires:	cupsddk-drivers >= 1.2.3-2mdv
#Requires:	foomatic-filters
#Requires:	hplip-model-data
#Requires:	hplip-hpijs
#Requires:	hplip-hpijs-ppds
#Requires:	python-sip >= 4.1.1
# Needed for communicating with ethernet-connected printers
#Requires:	net-snmp-mibs
# Needed to generate fax cover pages
#Requires:	python-reportlab
# Needed since 2.8.4 for IPC
#Requires:	python-dbus
#Requires:	polkit-agent
#Requires:	usermode-consoleonly
#Requires:	python-gobject
# Required by hp-scan for command line scanning
#Requires:	python-imaging
#Requires:	sane-backends-hpaio
# Needed to avoid misleading errors about network connectivity (RH bug #705843)
#Requires:	wget
# Some HP ppds are in foomatic-db and foomatic-db-hpijs (mdv bug #47415)

# foomatic-db-hpijs drivers are provided by hp and by this package now
# NOTE: remove the foomatic-db-hpijs deps sometime in 2010-10-?? ?
Provides:	foomatic-db-hpijs = %{version}-%{release}
Obsoletes:	foomatic-db-hpijs


%description
This is the HP driver package to supply Linux support for most
Hewlett-Packard DeskJet, LaserJet, PSC, OfficeJet, and PhotoSmart
printers and all-in-one peripherals (also known as Multi-Function
Peripherals or MFPs), which can print, scan, copy, fax, and/or access
flash memory cards.

It is work in progress, but printing, scanning, memory card access,
ink/toner/battery/consumable level checking, and inkjet printer
maintenance are supported on most models, when either connected to the
USB or LAN (built-in interfaces or selected HP JetDirect models) on a
Linux workstation with CUPS printing system.

For status and consumable checking and also for inkjet maintenance
there is the graphical tool "hp-toolbox" available (Menu:
"System"/"Monitoring"/"HP Printer Toolbox").

#%package libs
#Summary: Dynamic library for the "hplip" HP printer/all-in-one drivers
#Group: System/Printing

#%description libs
#Library needed for the "hplip" HP printer/all-in-one drivers

%package devel
Summary: Headers and links to compile against the "lib" ("hplip") library
Group: Development/C
#Requires: libs >= %{version}-%{release}
Provides: devel = %{version}-%{release}

%description devel
This package contains all files which one needs to compile programs using
the "lib" library.

#%package model-data
#Summary: Data file listing the HP printer models supported by HPLIP
#Group: System/Printing

#%description model-data
#HPLIP supports most current HP printers and multifunction devices, but
#there are some older models not supported. This package contains the
#list of supported models. Printerdrake installs it automatically to
#determine whether HPLIP has to be installed or not.

#%package doc
#Summary:	Documentation for HPLIP
#Group:		System/Printing

#%description doc
#This package contains documentation for the HPLIP driver.
#This is the HP driver package to supply Linux support for most
#Hewlett-Packard DeskJet, LaserJet, PSC, OfficeJet, and PhotoSmart
#printers and all-in-one peripherals (also known as Multi-Function
#Peripherals or MFPs), which can print, scan, copy, fax, and/or access
#flash memory cards.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
#%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1

# Make all files in the source user-writable
chmod -R u+w .
touch NEWS README AUTHORS ChangeLog
chmod +x debian/autogen.sh
echo "Running autoreconf..."
autoreconf --force --install

%build
#%serverbuild
%configure HPLIP_PPD_PATH=/opt/etc/cups/ppd \
        --config-cache \
        --disable-dependency-tracking \
        --prefix=/usr \
        --mandir=\$${prefix}/share/man \
        --infodir=\$${prefix}/share/info \
        --docdir=\$${prefix}/share/doc/hplip \
        --with-docdir=\$${prefix}/share/doc/hplip \
        --disable-foomatic-drv-install \
        --disable-foomatic-ppd-install \
        --disable-foomatic-rip-hplip-install \
        --with-drvdir=\$${prefix}/share/cups/drv \
        --with-hpppddir=\$${prefix}/share/ppd/hplip/HP \
        --datadir=\$${prefix}/share \
        --libexecdir=\$${prefix}/lib \
        --localstatedir=/var \
        --sysconfdir=/opt/etc \
        --without-icondir \
        --disable-hpijs-only-build \
        --enable-hpcups-only-build \
        --enable-hpcups-install \
        --enable-new-hpcups \
        --disable-network-build \
        --disable-pp-build \
        --disable-scan-build \
        --disable-gui-build \
        --disable-fax-build \
        --disable-dbus-build \
        --disable-cups11-build \
        --disable-udev-acl-rules \
        --enable-cups-drv-install \
        --enable-cups-ppd-install \
        --disable-qt4 \
        --disable-qt3 \
        --disable-policykit

#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make

%install
#rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_sysconfdir}/hp
mkdir -p %{buildroot}/opt/var/run/hplip

# Do not use the macro here, use the standard DESTDIR method as it works
# with HPLIP, in contrary to the non-standard Mandriva method
#make test-destdir DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}

# Install files which the "make install" missed to install
install -m 644 ip/hpip.h %{buildroot}%{_includedir}
install -m 644 ip/xform.h %{buildroot}%{_includedir}

# Move doc in sub-package
#mv %{buildroot}%{_docdir}/%{name}-%{version} %{buildroot}%{_docdir}/%{name}-doc-%{version}

# Remove static libraries of SANE driver
rm -f %{buildroot}%{_libdir}/sane/libsane-hpaio*.so
rm -f %{buildroot}%{_libdir}/sane/libsane-hpaio*.la
rm -f %{buildroot}%{_sysconfdir}/sane.d/dll.conf

# Remove other unneeded files
rm -f %{buildroot}%{py_platsitedir}/*.la

#mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
#desktop-file-install --vendor='' \
#	--dir=%{buildroot}%{_datadir}/applications \
#	--remove-category='Application' \
#	--remove-category='Utility' \
#	--add-category='System' \
#	--add-category='Settings' \
#	--add-category='Printing' \
#        --add-category='Qt' \
#       --add-category='HardwareSettings' \
#      --add-category='X-MandrivaLinux-CrossDesktop' \
#	--remove-key='Version' \
#        %{buildroot}%{_datadir}/applications/hplip.desktop

#cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{_real_vendor}-hp-sendfax.desktop << EOF
#[Desktop Entry]
#Name=HP Sendfax
#Comment=Utility for sending faxes with HP's multi-function devices
#Exec=%{_bindir}/hp-sendfax
#Icon=%{_datadir}/%{name}/data/images/32x32/fax_machine.png
#Terminal=false
#Type=Application
#Categories=TelephonyTools;Qt;Printing;Utility;X-MandrivaLinux-CrossDesktop;
#EOF
#' #Fix vim's stupid syntax

# The systray applet doesn't work properly (displays icon as a
# window), so don't ship the launcher yet.
rm -f %{buildroot}%{_sysconfdir}/xdg/autostart/hplip-systray.desktop


# switched to udev, no need for hal information
rm -rf  %{buildroot}%{_datadir}/hal/fdi 

rm -f   %{buildroot}%{_libdir}/*.la \
        %{buildroot}%{python_sitearch}/*.la \
        %{buildroot}%{_libdir}/sane/*.la

# Regenerate hpcups PPDs on upgrade if necessary (bug #579355).
#install -p -m755 %{SOURCE1} %{buildroot}%{_bindir}/hpcups-update-ppds

# Fedora pstotiff
#rm -f %{buildroot}%{_sysconfdir}/cups/pstotiff.types
#rm -f %{buildroot}%{_datadir}/cups/mime/pstotiff.types
#rm -f %{buildroot}%{_datadir}/hplip/fax/pstotiff*
#rm -f %{buildroot}%{_prefix}/lib/cups/filter/hpcac

# bork?
install -d %{buildroot}%{_sysconfdir}/cups
#cp -p %{buildroot}%{_datadir}/cups/mime/pstotiff.convs %{buildroot}%{_sysconfdir}/cups/pstotiff.convs

# set up consolehelper
#mkdir -p %{buildroot}%{_sbindir}
#mv %{buildroot}%{_bindir}/hp-setup %{buildroot}%{_sbindir}/hp-setup
#ln -s consolehelper %{buildroot}%{_bindir}/hp-setup

# Make sure pyc files are generated, otherwise we can get
# difficult to debug problems
#pushd %{buildroot}%{_datadir}/%{name}
#python -m compileall .
#popd

%triggerin -- hplip < 2.7.7
chkconfig --del hplip

# Restart CUPS to make the Fax PPD known to it
#if [ -f /etc/init.d/cups ]; then
#	/sbin/service cups condrestart || :
#fi

#%post -n hplip-model-data
#/sbin/udevadm trigger --subsystem-match=usb --attr-match=idVendor=03f0

# Restart CUPS to make the removal of the Fax PPD known to it
#if [ -f /etc/init.d/cups ]; then
#	/sbin/service cups condrestart || :
#fi

%clean
rm -rf %{buildroot}

%files
#%manifest hplip.manifest
%defattr(-,root,root)
#doc COPYING doc/*
#%config(noreplace) %{_sysconfdir}/hp
#%dir /opt/var/run/hplip/
#%{_bindir}/hp-align
#%{_bindir}/hp-clean
#%{_bindir}/hp-colorcal
#%{_bindir}/hp-devicesettings
#%{_bindir}/hp-fab
#%{_bindir}/hp-faxsetup
#%{_bindir}/hp-firmware
#%{_bindir}/hp-info
#%{_bindir}/hp-levels
#%{_bindir}/hp-linefeedcal
#%{_bindir}/hp-makecopies
#%{_bindir}/hp-makeuri
#%{_bindir}/hp-mkuri
#%{_bindir}/hp-pkservice
#%{_bindir}/hp-plugin
#%{_bindir}/hp-pqdiag
#%{_bindir}/hp-printsettings
#%{_bindir}/hp-probe
#%{_bindir}/hp-query
#%{_bindir}/hp-scan
#%{_bindir}/hp-sendfax
#%{_bindir}/hp-setup
#%{_sbindir}/hp-setup
#%{_bindir}/hp-testpage
#%{_bindir}/hp-timedate
#%{_bindir}/hp-unload
#%{_bindir}/hp-wificonfig

#%exclude %{_datadir}/hplip/data/models
# C libraries for Python
#%{_libdir}/python*/*/*.so*
# CUPS backends (0755 permissions, so that CUPS 1.2 runs these backends
# as lp user)
# Note: this must be /usr/lib not %{_libdir}, since that's the
# CUPS serverbin directory.
#%attr(0755,root,root) %{_prefix}/lib/cups/backend/hp*
#%{_prefix}/lib/cups/filter/hplipjs
%{_prefix}/lib/cups/filter/hpcups
#%{_prefix}/lib/cups/filter/hpcupsfax
#%{_prefix}/lib/cups/filter/hpps
#%{_prefix}/lib/cups/filter/pstotiff
#%{_datadir}/cups/mime/pstotiff.convs
#%config(noreplace) %{_sysconfdir}/cups/pstotiff.convs
#%{_datadir}/ppd/HP/HP-Fax*.ppd*
#%{_datadir}/cups/drv/hp/hpcups.drv
# Files
#%dir %{_datadir}/hplip
#%{_datadir}/hplip/align.py*
#%{_datadir}/hplip/clean.py*
#%{_datadir}/hplip/colorcal.py*
#%{_datadir}/hplip/devicesettings.py*
#%{_datadir}/hplip/fab.py*
#%{_datadir}/hplip/fax
#%{_datadir}/hplip/faxsetup.py*
#%{_datadir}/hplip/firmware.py*
#%{_datadir}/hplip/hpdio.py*
#%{_datadir}/hplip/hpssd*
#%{_datadir}/hplip/info.py*
#%{_datadir}/hplip/__init__.py*
#%{_datadir}/hplip/levels.py*
#%{_datadir}/hplip/linefeedcal.py*
#%{_datadir}/hplip/makecopies.py*
#%{_datadir}/hplip/makeuri.py*
#%{_datadir}/hplip/pkservice.py*
#%{_datadir}/hplip/plugin.py*
#%{_datadir}/hplip/pqdiag.py*
#%{_datadir}/hplip/printsettings.py*
#%{_datadir}/hplip/probe.py*
#%{_datadir}/hplip/query.py*
#%{_datadir}/hplip/scan.py*
#%{_datadir}/hplip/sendfax.py*
#%{_datadir}/hplip/setup.py*
#%{_datadir}/hplip/testpage.py*
#%{_datadir}/hplip/timedate.py*
#%{_datadir}/hplip/unload.py*
#%{_datadir}/hplip/wificonfig.py*
# Directories
#%{_datadir}/hplip/base
#%{_datadir}/hplip/copier
#%dir %{_datadir}/hplip/data
#%{_datadir}/hplip/data/ldl
#%{_datadir}/hplip/data/localization
#%{_datadir}/hplip/data/models
#%{_datadir}/hplip/data/pcl
#%{_datadir}/hplip/data/ps
#%{_datadir}/hplip/installer
#%{_datadir}/hplip/pcard
#%{_datadir}/hplip/prnt
#%{_datadir}/hplip/scan
#%{_datadir}/polkit-1/actions/com.hp.hplip.policy
#%{_datadir}/dbus-1/system-services/com.hp.hplip.service
#%{_localstatedir}/lib/hp/hplip.state
#%config(noreplace) %{_sysconfdir}/dbus-1/system.d/com.hp.hplip.conf

#%files doc
#%defattr(-,root,root)
#%doc %{_docdir}/%{name}-doc-%{version}

#%files libs
#%defattr(-,root,root)
#%{_libdir}/libhpip*.so.*
#%{_libdir}/libhpmud.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/hpip.h
%{_includedir}/xform.h
#%{_libdir}/libhpip*.so
#%{_libdir}/libhpmud.so

#%files model-data
#%defattr(-,root,root)
#%{_sysconfdir}/udev/rules.d/*.rules
#%{_datadir}/hplip/data/models

%changelog
