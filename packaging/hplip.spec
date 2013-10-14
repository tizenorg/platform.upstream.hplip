#
# spec file for package hplip
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define _unpackaged_files_terminate_build 0

Name:           hplip
Summary:        HP's Printing, Scanning, and Faxing Software
License:        BSD-3-Clause ; GPL-2.0+ ; MIT
Group:          Hardware/Printing
# HPLIP has reached 1.0 status. With this release a date encoded revision number is used:
# x.y.m : x = major release number, y = year (eg: 6 = 2006), m = month (eg: 6a = second release in June)
# Official releases have a 3 digit number and release candidates have a 4 digit number: x.y.m.rc
Version:        3.12.4
Release:        13
Url:            http://hplipopensource.com
# Source0...Source9 is for sources from HP:
# URL for Source0: http://prdownloads.sourceforge.net/hplip/hplip-3.12.4.tar.gz
# URL to verify Source0: http://prdownloads.sourceforge.net/hplip/hplip-3.12.4.tar.gz.asc
# How to verify Source0 see: http://hplipopensource.com/node/327
# For example: /usr/bin/gpg --keyserver pgp.mit.edu --recv-keys 0xA59047B9
#              /usr/bin/gpg --verify hplip-3.12.4.tar.gz.asc hplip-3.12.4.tar.gz
# must result: Good signature from "HPLIP (HP Linux Imaging and Printing) <hplip@hp.com>"
Source0:        hplip-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-build

# BuildRequires foomatic-filters to avoid /usr/lib/rpm/brp-symlink ERROR:
# link target doesn't exist (neither in build root nor in installed system):
# /usr/lib/cups/filter/foomatic-rip-hplip -> /usr/bin/foomatic-rip
Requires:  cups
BuildRequires:  cups-devel
#BuildRequires:  dbus-1-devel
#BuildRequires:  fdupes
#BuildRequires:  foomatic-filters
#BuildRequires:  hicolor-icon-theme
#BuildRequires:  libdrm-devel
#BuildRequires:  libgphoto2-devel
BuildRequires:  libjpeg-devel
#BuildRequires:  libqt4-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(libusb)
#BuildRequires:  net-snmp-devel
BuildRequires:  pkgconfig
# All printer driver packages should have "BuildRequires: python-cups"
# because python-cups installs special rpm macros that adds Provides tags
# for the printer drivers supported by the package,
# see https://bugzilla.novell.com/show_bug.cgi?id=735865
#BuildRequires:  python-cups
BuildRequires:  python-devel
#BuildRequires:  python-openssl
#BuildRequires:  python-qt4
#BuildRequires:  python-xml
#BuildRequires:  readline-devel
#%if 0%{?suse_version} > 1130
#BuildRequires:  sane-backends-devel
#%else
#BuildRequires:  sane-backends
#%endif
#BuildRequires:  update-desktop-files
# Patch0...Patch9 is for patches from HP:
# Patch10...Patch99 is for Suse patches for the sources from HP:
# Patch10 fixes "... is used uninitialized ..." warnings:
Patch10:        fix-uninitialized-variables.diff
# Patch11 fix_gcc44_glib.diff is obsolete since version 3.9.6b because it is fixed in the source.
# Patch12 hplip-3.9.8-CVE-2010-4267.patch fixes a remote buffer overflow in hpmud/pml.c:
Patch12:        hplip-3.9.8-CVE-2010-4267.patch
# Source100... is for special Suse sources:
# Source100 is the primary source for the suse_update_desktop_file stuff.
# It is found automatically in $RPM_SOURCE_DIR by 'suse_update_desktop_file -i hplip':
Source100:      hplip.desktop
# Source101 hp-toolbox.wrapper was a wrapper for hp-toolbox which is no longer needed
# see https://bugzilla.novell.com/show_bug.cgi?id=755820
# Source102 is a small man page for /usr/bin/hpijs:
Source102:      hpijs.1.gz
# Source103 was the init script for hpssd which is obsolete since version 2.8.4.
# Source104 was a script which outputs a global HAL fdi file which is obsolete
# since openSUSE 11.2 where HAL is no longer used to manage ACLs,
# see https://bugzilla.novell.com/show_bug.cgi?id=542473#c13
# Source105 hplip.SuSEfirewall2 provides support
# to open UDP ports 5353(mdns) and 427(svrloc) for mDNS support
# according to the init-suse-firewall in the tar ball
# (compare also Novell/Suse Bugzilla bnc#498429)
# hplip.SuSEfirewall2 is no longer provided
# see https://bugzilla.novell.com/show_bug.cgi?id=757354#c10
# Source106 is a wrapper for hp-systray which tests via "lpstat"
# whether or not a 'hp:/...' print queue exists and exits otherwise,
# see https://bugzilla.novell.com/show_bug.cgi?id=649280
# hp-systray.wrapper is called via /etc/xdg/autostart/hplip-systray.desktop
# which is changed accordingly in the install section.
Source106:      hp-systray.wrapper
# Patch100... is for special Suse patches:
# Patch101 changes the udev rules files 55-hpmud.rules and 56-hpmud_support.rules:
Patch101:       change-udev-rules.diff
# Patch102 deactivates the "chgrp lp -R /var/log/hp" in Makefile.am
# because during install this results "Operation not permitted"
# this is done in the files section via attr(0774,root,lp)
# where mode 0774 matches to what is set in Makefile.am:
Patch102:       no-chgrp_lp_hplip_Logdir.diff

# Tizen patch
# Tizen do not use dbus communication in hpcups filter
Patch103:		tizen_disable_dbus_hpcups.patch
# Added SIGPIPE, IGN to avoide hpcups crash
Patch104:		tizen_add_sigpipe_ign.patch
Patch105:		tizen_fix_image_align.patch
Patch106:		tizen_fix_debug_log.patch
Patch107:		tizen_add_job_media_progress.patch

#PreReq:         coreutils
#PreReq:         /bin/grep
#PreReq:         /bin/sed
#PreReq:         /usr/bin/find
# Require the exact matching version-release of the hpijs sub-package to make sure
# to have the exact matching version of libhpip and libhpmud installed.
# The exact matching version-release of the sub-package is available on the same
# repository where the main-package is (compare the "Recommends: hplip" entry below).
#Requires:       %{name}-hpijs = %{version}-%{release}
# Same rationale for the sane subpackage.
#Requires:       %{name}-sane = %{version}-%{release}
# Because foomatic-rip-hplip has CVE-2011-2697 (bnc#698451)
# plus a leftover in CVE-2004-0801 (bnc#59233)
# foomatic-rip-hplip is no longer installed and foomatic-rip
# from the foomatic-filters RPM is used instead.
# The RPM requirement for foomatic-filters should actually be
# in the hplip-hpijs sub-package but this would bloat a minimalist system
# (see the comment for the hplip-hpijs sub-package below).
# Therefore the hplip main package which is intended
# to get "all the HPLIP stuff" installed has the RPM requirement:
#Requires:       foomatic-filters
# foomatic-filters does not require Ghostscript because depending on the PPD
# (e.g. some PPDs for PostScript printers in OpenPrintingPPDs-postscript)
# foomatic-rip can also be used without Ghostscript but for the drivers
# HPIJS and HPCUPS Ghostscript is needed.
# The RPM requirement for ghostscript should actually be in the
# hplip-hpijs sub-package but this would bloat a minimalist system
# (see the comment for the hplip-hpijs sub-package below).
# Therefore the hplip main package which is intended
# to get "all the HPLIP stuff" installed has the RPM requirement:
#Requires:       ghostscript
# Require special Python stuff (which pulls in Python base stuff).
# At least since openSUSE 11.1 and SLE11 pyxml is no longer required
# (pyxml was required in particular for openSUSE 10.3 and SLE10,
#  see https://answers.launchpad.net/hplip/+question/25696)
# but meanwhile python-xml alone is sufficient for "import xml.parsers.expat"
# see https://bugzilla.novell.com/show_bug.cgi?id=656779#c3
#Requires:       python-xml
# Since version 3.9.2 by default only Qt4 is used:
#Requires:       python-qt4
# Since version 2.8.4 all interprocess communication uses dbus.
# Therefore python-dbus version 0.80 or greater is required (which pulls in dbus base stuff).
# The dbus stuff in HPLIP requires the Python module gobject
# but there is no automated RPM requirement for python-gobject2,
# see https://answers.launchpad.net/hplip/+question/30741
#Requires:       dbus-1-python >= 0.80
#Requires:       python-gobject2
# Either the hplip17 packages or the hplip packages can be installed,
# see https://bugzilla.novell.com/show_bug.cgi?id=251830#c20
# for the full story why there is this unversioned Obsoletes:
Obsoletes:      hplip17
# Obsolete the hplip3 copy that was introduced for older SLED11-GA HP preloads:
Provides:       hplip3 = 3.9.5
Obsoletes:      hplip3 < 3.9.5
# Skip testing devel dependencies required by libtool .la files by the following comment:
# skip-check-libtool-deps

%description
The Hewlett-Packard Linux Imaging and Printing project (HPLIP) provides
a unified single and multifunction connectivity solution for HP
printers and scanners (in particular, HP all-in-one devices).

HPLIP provides unified connectivity for printing, scanning, sending
faxes, photo card access, and device management and is designed to work
with CUPS.

It includes the Ghostscript printer driver HPIJS for HP printers and a
special "hp" CUPS back-end that provides bidirectional communication
with the device (required for HP printer device management).

It also includes the SANE scanner driver "hpaio" for HP all-in-one
devices. Basic PC send fax functionality is supported on a number of
devices.

The special "hpfax" CUPS back-end is required to send faxes. Direct
uploading (i.e. without print and scan) of received faxes from the
device to the PC is not supported.

The "hp-toolbox" program is provided for device management.

The "hp-sendfax" program must be used to send faxes.

The "hp-setup" program can be used to set up HP all-in-one devices.

The HPLIP project is open source software and uses GPL-compatible
licenses. For more information, see:

http://hplipopensource.com

/usr/share/doc/packages/hplip/index.html

%prep
# Be quiet when unpacking:
%setup -q
# Patch10 fix-uninitialized-variables.diff
# fixes "... is used uninitialized ..." warnings:
%patch10
# Patch12 hplip-3.9.8-CVE-2010-4267.patch
# fixes a remote buffer overflow in hpmud/pml.c:
%patch12
# Patch101 change-udev-rules.diff
# changes the udev rules files 55-hpmud.rules and 56-hpmud_support.rules:
%patch101
# Patch102 deactivates the "chgrp lp -R /var/log/hp" in Makefile.am
# because during install this results "Operation not permitted"
# this is done in the files section via attr(0774,root,lp)
# where mode 0774 matches to what is set in Makefile.am:
%patch102
%patch103
%patch104
%patch105
%patch106
%patch107 -p1

%build
# If AUTOMAKE='automake --foreign' is not set, autoreconf (in fact automake)
# complains about missing files like NEWS, README, AUTHORS, ChangeLog
# in each directory where a Makefile.am exists:
AUTOMAKE='automake --foreign' autoreconf --force --install
# Set our preferred architecture-specific flags for the compiler and linker:
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
# Static "hpijs" PPD files via enable-foomatic-ppd-install
# require foomatic-rip-hplip via their cupsFilter entries
# so that enable-foomatic-rip-hplip-install is also needed.
# Since version 3.9.6 the default printer driver install changed from hpijs to hpcups.
# According to http://hplipopensource.com/hplip-web/release_notes.html
# all drv installs require CUPSDDK 1.2.3 or higher.
# Otherwise a static PPD install must be performed.
# Furthermore dynamic PPDs will be deprecated in the future in CUPS,
# see http://www.cups.org/str.php?L3772
# For hpcups static PPD install one needs:
# --enable-hpcups-install enable hpcups install (default=yes)
# --disable-cups-drv-install enable cups dynamic ppd install (default=yes)
# --enable-cups-ppd-install enable cups static ppd install (default=no)
# For both hpcups and hpijs install with static PPDs one needs additionally:
# --enable-hpijs-install enable hpijs install (default=no)
# --disable-foomatic-drv-install enable foomatic dynamic ppd install (default=no), uses drvdir and hpppddir
# --enable-foomatic-ppd-install enable foomatic static ppd install (default=no), uses hpppddir
# --enable-foomatic-rip-hplip-install enable foomatic-rip-hplip install (default=no), uses cupsfilterdir
# Because foomatic-rip-hplip has CVE-2011-2697 (bnc#698451) plus a leftover in CVE-2004-0801 (bnc#59233)
# which are fixed up to openSUSE 11.4 with patches, after openSUSE 11.4 (i.e. since openSUSE 12.1)
# foomatic-rip-hplip is no longer installed and foomatic-rip from foomatic-filters is used instead so that 
# --disable-foomatic-rip-hplip-install is explicitly set and as a consequence the "cupsFilter" entries
# in the static PPDs are changed in the install section to use foomatic-rip.
./configure --prefix=/usr \
            --libdir=%{_libdir} \
			--prefix=/usr \
    	    --localstatedir=/var \
	        --sysconfdir=/opt/etc \
	        --mandir=\$${prefix}/share/man \
        	--infodir=\$${prefix}/share/info \
    	    --docdir=\$${prefix}/share/doc/hplip \
	        --with-docdir=\$${prefix}/share/doc/hplip \
            --disable-qt3 \
            --disable-qt4 \
            --disable-policykit \
            --disable-doc-build \
            --disable-network-build \
            --disable-pp-build \
            --disable-scan-build \
            --disable-gui-build \
            --disable-fax-build \
            --disable-dbus-build \
            --enable-hpcups-install \
            --disable-cups-drv-install \
            --disable-cups-ppd-install \
            --disable-hpijs-install \
            --disable-foomatic-drv-install \
            --disable-foomatic-ppd-install \
            --disable-foomatic-rip-hplip-install \
            --with-hpppddir=%{_datadir}/cups/model/manufacturer-PPDs/%{name} \
            --with-cupsbackenddir=/usr/lib/cups/backend \
            --with-cupsfilterdir=/usr/lib/cups/filter
#            --with-drvdir=/usr/lib/cups/driver \
#            --with-mimedir=%{_sysconfdir}/cups \
#            --with-docdir=%{_defaultdocdir}/%{name}
make

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/usr/share/license/%{name}

# Remove the installed /etc/sane.d/dll.conf
# because this is provided by the sane-backends package:
#rm %{buildroot}%{_sysconfdir}/sane.d/dll.conf
# Remove the installed HAL fdi file because HAL is no longer used (HAL is deprecated):
#rm %{buildroot}%{_datadir}/hal/fdi/preprobe/10osvendor/20-hplip-devices.fdi
# Remove the outdated "Check and add printer for Suse 10.3 distro" udev rule
# and let the build fail if it does no longer match to notify about the change:
#grep 'for Suse 10.3 distro' %{buildroot}%{_sysconfdir}/udev/rules.d/56-hpmud_add_printer.rules || exit 1
#sed -i -e '/for Suse 10.3 distro/,+1 d' %{buildroot}%{_sysconfdir}/udev/rules.d/56-hpmud_add_printer.rules
# Begin "General tests and adjustments for all PPDs" (see manufacturer-PPDs.spec):
#pushd %{buildroot}%{_datadir}/cups/model/manufacturer-PPDs/%{name}
# Do not pollute the build log file with zillions of meaningless messages:
#set +x
#gunzip *.ppd.gz
# Make some general tests and adjustments for all PPDs:
#echo "Making some general tests and adjustments for all PPDs:"
# Add a line-feed to the end of all PPDs to fix those PPDs where it is missing.
# See Novell/Suse Bugzilla bug #309832: Unix/Linux text files must end with a line-feed.
# Otherwise reading the last line results EOF and then some programs may ignore the last line.
#echo "Adding a line-feed to the end of all PPDs to fix those PPDs where it is missing..."
#for p in *.ppd
#do echo -en '\n' >>$p
#done
# Because foomatic-rip-hplip has CVE-2011-2697 (bnc#698451) plus a leftover in CVE-2004-0801 (bnc#59233)
# foomatic-rip-hplip is no longer installed and foomatic-rip from foomatic-filters is used instead so that 
# the "cupsFilter" entries in the static PPDs must be changed accordingly:
#echo "Replacing insecure foomatic-rip-hplip with foomatic-rip everywhere in in the PPDs..."
#for p in *.ppd
#do sed -i -e 's/foomatic-rip-hplip/foomatic-rip/' $p
#done
# Final test by cupstestppd:
# To save disk space gzip the files (gzipped PPDs can also be used by CUPS).
# Future goal: Only have files which don't FAIL for cupstestppd.
# Ignore FAILs because of errors in UIConstraints and/or NonUIConstraints
# which are detected since cupstestppd in CUPS > 1.2.7 (i.e. in openSUSE 10.3).
# See Novell/Suse Bugzilla bug #309822: When this bug is fixed, cupstestppd would
# no longer result zero exit code.
# In the long run the PPDs should be fixed but as far as we know there have been
# no problems because of such UIConstraints errors so that it should be o.k.
# let those PPDs pass even if they are not strictly compliant.
# Ignore FAILs because of missing cupsFilter programs because
# in the package build environment the usual HPLIP filters
# like "hpcups" and "hpcupsfax" are
# installed at an unusual place (in the BuildRoot directory).
# For now keep all PPDs even if cupstestppd FAILs.
# Reason:
# With each CUPS version upgrade cupstestppd finds more and more errors
# so that more and more PPDs would be no longer included in the RPM
# which have been included before which results a regression.
# As far as we know there have been no problems at all because of
# not strictly compliant PPDs in HPLIP so that it is much better
# to provide all HPLIP PPDs so that the matching printers can be used
# than to be rigorous regarding enforcing compliance to the PPD specification:
#echo "Final testing by cupstestppd..."
#for p in *.ppd
#do grep -E -v '^\*UIConstraints:|^\*NonUIConstraints:|^\*cupsFilter:' $p | cupstestppd - || true
#   gzip $p
#done
#echo "End of general tests and adjustments for all PPDs."
# Switch back to the usual build log messages:
#set -x
# End of "General tests and adjustments for all PPDs":
#popd
# Because foomatic-rip-hplip has CVE-2011-2697 (bnc#698451)
# plus a leftover in CVE-2004-0801 (bnc#59233)
# foomatic-rip-hplip is no longer installed and foomatic-rip
# from the foomatic-filters RPM must be used instead.
# To be backward compatible with PPDs in /etc/cups/ppd/
# for existing print queues a compatibility link
# /usr/lib/cups/filter/foomatic-rip-hplip
# which points to foomatic-rip is installed:
#ln -s ../../../bin/foomatic-rip %{buildroot}/usr/lib/cups/filter/foomatic-rip-hplip
# Begin "Desktop menue entry stuff":
# Install /usr/share/hplip/data/images/64x64/hp_logo.png as desktop icon file
# because it is used in the hplip.desktop.in and hplip-systray.desktop.in sources:
#install -D -m 644 %{buildroot}%{_datadir}/hplip/data/images/32x32/hp_logo.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/HPmenu.png
#install -D -m 644 %{buildroot}%{_datadir}/hplip/data/images/64x64/hp_logo.png %%{buildroot}%{_datadir}/icons/hicolor/64x64/apps/HPmenu.png
#install -D -m 644 %{buildroot}%{_datadir}/hplip/data/images/128x128/hp_logo.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/HPmenu.png
#install -D -m 644 %{buildroot}%{_datadir}/hplip/data/images/256x256/hp_logo.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/HPmenu.png
# Set up and install the desktop menue entry stuff using "Categories=System;Monitor;"
# and remove HP's hplip.desktop and hplip-systray.desktop files before because we use Source100:
# (additionally there is/was a typo in HP's install because of the trailing blank at 'applications ')
#rm %{buildroot}%{_datadir}/applications/hplip*.desktop
#%suse_update_desktop_file -i %{name} System HardwareSettings Printing
# Let suse_update_desktop_file add X-SuSE-translate key to /etc/xdg/autostart/hplip-systray.desktop
# so that we can update its translations with translation-only packages.
#%suse_update_desktop_file %{buildroot}/etc/xdg/autostart/hplip-systray.desktop
# End of "Desktop menue entry stuff".
# Install the man page for /usr/bin/hpijs:
#install -d %{buildroot}%{_mandir}/man1
#install -m 644 %{SOURCE102} %{buildroot}%{_mandir}/man1/
# Begin "Desktop autostart notification tray stuff":
# Install the wrapper for hp-systray:
#install -m 755 %{SOURCE106} %{buildroot}%{_bindir}/hp-systray.wrapper
# Change /etc/xdg/autostart/hplip-systray.desktop to call hp-systray.wrapper:
#sed -i -e '/^Exec=hp-systray$/s/hp-systray/hp-systray.wrapper/;' %{buildroot}/etc/xdg/autostart/hplip-systray.desktop
# End of "Desktop autostart notification tray stuff".
# Find duplicate files:
#%fdupes -s %{buildroot}

%post
#%if 0%{?suse_version} > 1130
#%icon_theme_cache_post
#%else
#gtk-update-icon-cache %{_datadir}/icons/hicolor || true
#%endif
/sbin/ldconfig
#exit 0

#%triggerin -- sane-backends
# As hplip can be used for plain printers it cannot "PreReq sane-backends".
# Therefore if sane-backends is installed it may be installed or updated after hplip.
# In this case trigger to add the SANE backend "hpaio" to /etc/sane.d/dll.conf if it is not there.
# To be safe there is a test that /etc/sane.d/dll.conf is writable.
#if [ -w /etc/sane.d/dll.conf ]
#then if ! grep -q 'hpaio' /etc/sane.d/dll.conf
#     then echo -e '# The hpaio backend is provided by the hplip package:\n#hpaio' >>/etc/sane.d/dll.conf
#     fi
#fi
#exit 0

%preun
# If the package was removed and if it was updated
# remove all byte-compiled Python .pyc (and perhaps .pyo) files
# which are created at run-time by Python in /usr/share/hplip/.
# Use a generic method via "find" so that it works in any case
# without the need to maintain a long list of individual files.
# Even if this may accidentally remove "foreign" .pyc/.pyo files
# which do not originate from matching .py files from this package
# (e.g. third-party stuff in /usr/share/hplip/), there is no damage
# because Python could re-create them or work only with .py files.
#find /usr/share/hplip/ -name '*.py[co]' -delete
#exit 0

%postun
#%if 0%{?suse_version} > 1130
#%icon_theme_cache_postun
#%else
#gtk-update-icon-cache %{_datadir}/icons/hicolor || true
#%endif
/sbin/ldconfig
# If the package was removed (but not if it was updated)
# then remove the hpaio lines in /etc/sane.d/dll.conf.
# Don't remove them when the hplip package was automatically
# replaced by the hplip17 package (via RPM obsoletes) or vice versa.
# Because postun of the old package runs last (after triggerin -- sane-backends)
# it is done via a special "ls" test if any libsane-hpaio.so exists
# (e.g. there could be only 32-bit installed on 64-bit hardware).
# If the "ls" test does not fail, some kind of HPLIP is installed.
# The package sane-backends may not be installed (see triggerin)
# and therefore the test that /etc/sane.d/dll.conf is writable.
# The "exit 0" is necessary, otherwise the postun script
# would exit with non-zero exit-code if the package was not removed.
#if [ "$1" = "0" ]
#then if ! ls /usr/lib*/sane/libsane-hpaio.so* &>/dev/null
#     then [ -w /etc/sane.d/dll.conf ] && sed -i -e '/hpaio/d' /etc/sane.d/dll.conf
#     fi
#fi
#exit 0

#%post hpijs
#/sbin/ldconfig
#exit 0

#%postun hpijs
#/sbin/ldconfig
#exit 0

%files
%manifest hplip.manifest
%defattr(-, root, root)
/usr/share/license/%{name}
#%config %{_sysconfdir}/xdg/autostart/hplip-systray.desktop
#%dir %{_sysconfdir}/udev
#%dir %{_sysconfdir}/udev/rules.d
#%config %{_sysconfdir}/udev/rules.d/55-hpmud.rules
#%config %{_sysconfdir}/udev/rules.d/56-hpmud_add_printer.rules
#%config %{_sysconfdir}/udev/rules.d/56-hpmud_support.rules
#%config %{_sysconfdir}/udev/rules.d/86-hpmud_plugin.rules
#%{_bindir}/hp-align
#%{_bindir}/hp-check
#%{_bindir}/hp-check-plugin
#%{_bindir}/hp-clean
#%{_bindir}/hp-colorcal
#%{_bindir}/hp-config_usb_printer
#%{_bindir}/hp-devicesettings
#%{_bindir}/hp-diagnose_plugin
#%{_bindir}/hp-diagnose_queues
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
#%{_bindir}/hp-print
#%{_bindir}/hp-printsettings
#%{_bindir}/hp-probe
#%{_bindir}/hp-query
#%{_bindir}/hp-scan
#%{_bindir}/hp-sendfax
#%{_bindir}/hp-setup
#%{_bindir}/hp-systray
#%{_bindir}/hp-testpage
#%{_bindir}/hp-timedate
#%{_bindir}/hp-toolbox
#%{_bindir}/hp-uninstall
#%{_bindir}/hp-unload
#%{_bindir}/hp-upgrade
#%{_bindir}/hp-wificonfig
#%{_libdir}/python%{py_ver}/site-packages/cupsext.*
#%{_libdir}/python%{py_ver}/site-packages/hpmudext.*
#%{_libdir}/python%{py_ver}/site-packages/pcardext.*
#%{_libdir}/python%{py_ver}/site-packages/scanext.*
#%dir /usr/lib/cups
#%dir /usr/lib/cups/backend
#/usr/lib/cups/backend/hpfax
%dir /usr/lib/cups/filter
/usr/lib/cups/filter/hpcups
#/usr/lib/cups/filter/hpcupsfax
#%doc %{_defaultdocdir}/%{name}/
#%{_datadir}/icons/hicolor/*/apps/HPmenu.png
#%{_datadir}/applications/%{name}.desktop
#%{_bindir}/hp-systray.wrapper
#%{_datadir}/hplip/
#%exclude %{_datadir}/hplip/data/models/models.dat

#%files hpijs
#%defattr(-, root, root)
#%config %{_sysconfdir}/hp/
#%config %{_sysconfdir}/cups/pstotiff.convs
#%config %{_sysconfdir}/cups/pstotiff.types
#%{_bindir}/hpijs
#%doc %{_mandir}/man1/hpijs.1.gz
#%{_libdir}/libhpip.*
#%{_libdir}/libhpmud.*
#%dir /usr/lib/cups
#%dir /usr/lib/cups/backend
#/usr/lib/cups/backend/hp
#%dir /usr/lib/cups/filter
#/usr/lib/cups/filter/foomatic-rip-hplip
#/usr/lib/cups/filter/hpcac
#/usr/lib/cups/filter/hplipjs
#/usr/lib/cups/filter/hpps
#/usr/lib/cups/filter/pstotiff
#%dir %{_datadir}/cups
#%dir %{_datadir}/cups/model
#%dir %{_datadir}/cups/model/manufacturer-PPDs
#%{_datadir}/cups/model/manufacturer-PPDs/%{name}/
#%{_datadir}/%{name}/data/models/models.dat
#%dir %attr(0774,root,lp) %{_var}/log/hp

#%files sane
#%defattr(-, root, root)
#%dir %{_libdir}/sane
#%{_libdir}/sane/libsane-hpaio.*

%changelog
* Tue Apr 24 2012 jsmeix@suse.de
-  hplip.SuSEfirewall2 is no longer provided
  (see SUSE Bugzilla bnc#757354 comment #10).
* Thu Apr 12 2012 jsmeix@suse.de
- Upgraded to version 3.12.4:
  Uninstall Support: User can uninstall complete HPLIP package
  by running "hp-uninstall" command.
  Upgrade Support: Settings can be configured using
  "hp-systray -> settings -> Update settings" for notification
  of newer version of HPLIP release. User can also upgrade to
  latest version by running "hp-upgrade" command.
  Queue Analyzer: Print/Fax queues can be analyzed by
  running "hp-diagnose-queues" command or by clicking
  on "Diagnose Queues" from toolbox.
  Several more supported printers and all-in-one devices.
  Several bug fixes.
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- Removed hp-toolbox.wrapper because the reason for it
  is no longer valid (see SUSE Bugzilla bnc#755820).
- Added "BuildRequires: python-cups" to get special
  RPM Provides tags for the printers supported by
  this package (see SUSE Bugzilla bnc#735865).
* Wed Feb  8 2012 jsmeix@suse.de
- Upgraded to version 3.12.2:
  Fixed digital signature mismatch issue for plugin download.
  Removed unsupported features (Water Mark overlay, Job Storage,
  PIN 2 Print) from the PS PPDs.
  Several more supported printers and all-in-one devices.
  A few bug fixes.
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
* Thu Jan 12 2012 jsmeix@suse.de
- Upgraded to version 3.11.12:
  Auto-detection and installation of missing plug-ins.
  Designed tool to detect the missing plugin files and intimate
  user about it and giving the path forward to install it.
  SYSFS is replaced by ATTRS in udev rules.
  Uses D-Bus from separate threads without locking.
  Several more supported printers and all-in-one devices.
  Several bug fixes.
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- change-udev-rules.diff changes ATTRS to ATTR (bnc#436085).
- no-chgrp_lp_hplip_Logdir.diff deactivates
  the "chgrp lp -R /var/log/hp" in Makefile.am because
  during install this results "Operation not permitted".
  This is done in the files section via attr(0774,root,lp)
  where mode 0774 matches to what is set in Makefile.am.
* Fri Oct 28 2011 badshah400@gmail.com
- Install icons of various sizes in hicolor icon directory for
  better appearance in gnome-shell (bnc#713902).
- Add hicolor-icon-theme BuildRequires to own the hicolor icon
  directory correctly and install icons in there
- Use appropriate icon theme macros in post scripts
- Modified hplip.desktop to use these hicolor icons
- In hplip.desktop replace the category "Settings" by "System" to
  make it appear under the correct group "System Tools" rather
  than "Others" in desktop menus.
* Sat Oct 15 2011 coolo@suse.com
- add libtool as buildrequire to make the spec file more reliable
* Thu Oct 13 2011 vuntz@opensuse.org
- Split the sane driver in a hplip-sane subpackage, so that it's
  not necessary to install the full hplip tools to use an
  all-in-one HP printer. See bnc#723870.
* Tue Oct  4 2011 jsmeix@suse.de
- Upgraded to version 3.11.10:
  Fixed insecure tmp file handling in hpcupsfax.cpp CVE-2011-2722
  see https://bugs.launchpad.net/hplip/+bug/809904 (bnc#704608).
  New tech classes for HP OfficeJet Pro 8100,
  HP Deskjet 3070 B611 series and HP Photosmart 7510 e-All-in-One.
  Added new subtech class for HP Photosmart 6510 e-All-in-one.
  Modified the error message which was displayed in case
  of missing .asc file for manual plug-in install.
  Several more supported printers and all-in-one devices.
  Several bug fixes.
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
* Fri Aug 12 2011 jsmeix@suse.de
- Upgraded to version 3.11.7:
  A few more supported printers and all-in-one devices.
  Several bug fixes.
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- Because foomatic-rip-hplip has CVE-2011-2697 (bnc#698451)
  plus a leftover in CVE-2004-0801 (bnc#59233)
  foomatic-rip-hplip is no longer installed and foomatic-rip
  from the foomatic-filters RPM is used instead and the
  "cupsFilter" entries in the PPDs are changed accordingly.
  To be backward compatible with PPDs in /etc/cups/ppd/
  for existing print queues a compatibility link
  /usr/lib/cups/filter/foomatic-rip-hplip
  which points to foomatic-rip is installed.
- The DefaultPageSize in the PPDs is no longer set to A4
  if A4 is an available PageSize choice but left "as is"
  because the DefaultPageSize in the PPD templates in
  /usr/share/cups/model/ does not matter because the cupsd
  sets the DefaultPageSize for PPDs in /etc/cups/ppd/
  by default according to the locale that the cupsd runs in or
  according to a DefaultPaperSize entry in /etc/cups/cupsd.conf.
- No longer "Correcting or removing non-working PPDs..."
  because none of those cases which were fixed still exist
  (i.e. all those cases are meanwhile fixed upstream).
* Fri May 13 2011 jsmeix@suse.de
- Upgraded to version 3.11.5:
  Added LEDM ADF Scan support.
  Added LEDM Wireless support.
  Some more supported printers and all-in-one devices.
  It may fix the inverted/wrong color problem in HPCUPS
  (see Novell/openSUSE Bugzilla bnc #692905).
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
* Tue Mar 29 2011 jsmeix@suse.de
- Upgraded to version 3.11.3a:
  Fixed hp-plugin plugin download error (no Suse bug), see
  http://hplipopensource.com/hplip-web/release_notes.html
* Fri Mar 18 2011 jsmeix@suse.de
- Upgraded to version 3.11.3:
  New device class StingrayOJ for HP OfficeJet 100 Mobile L411.
  New filter hpps (HP PS filter for PostScript printers) currently
  only used via hp-officejet_pro_8000_enterprise_a811a-ps.ppd.gz
  Some more supported printers and all-in-one devices.
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
* Tue Feb  1 2011 jsmeix@suse.de
- Updated to version 3.11.1:
  New encapsulation format for LJZJStream class.
  Alignment of cartridges over LEDM (Low End Data Model).
  LEDM dynamic scan resolution.
  New fax protocol (Low End Data Model) support.
  ADF and color scan for some HP LaserJet Pro and MFP devices.
  Some more supported all-in-one devices.
  Many bug fixes (no Suse bugs).
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- Adapted change-udev-rules.diff for version 3.11.1
  because the "DesignJet product (0x03f0xx14)" was added.
* Thu Jan 13 2011 jsmeix@suse.de
-  hplip-3.9.8-CVE-2010-4267.patch fixes a remote buffer overflow
  (CVE-2010-4267 and Novell/Suse Bugzilla bnc#336658).
* Wed Dec 29 2010 gber@opensuse.org
- Use more appropriate categories for hplip.desktop
  'Settings HardwareSettings Printing' instead of 'System Monitor'
* Fri Dec  3 2010 jsmeix@suse.de
- Removed explicite RPM requirement for pyxml. At least since
  openSUSE 11.1 and SLE11 pyxml is no longer required (pyxml was
  required e.g. for openSUSE 10.3 and SLE10, see the entry below
  dated "Wed Apr  2 14:40:57 CEST 2008") but meanwhile python-xml
  alone is sufficient for "import xml.parsers.expat"
  (see Novell/openSUSE Bugzilla bnc#656779 comment #3).
- Added "Obsoletes: hplip-hpcups" because HPLIP does not work
  if the openSUSE packages hplip and hplip-hpijs are installed
  together with a leftover PackMan package hplip-hpcups
  (see Novell/openSUSE Bugzilla bnc#515005 comment #17).
- Do not pollute the build log file with zillions of meaningless
  messages while "General tests and adjustments for all PPDs"
  (compare the OpenPrintingPPDs.spec file).
* Wed Oct 27 2010 jsmeix@suse.de
- Added hp-systray.wrapper which is called
  via /etc/xdg/autostart/hplip-systray.desktop
  to increase desktop startup speed so that the purpose
  of this hp-systray.wrapper is different to the
  entry below dated "Tue Apr  8 14:56:53 CEST 2008".
  hp-systray.wrapper tests via "lpstat" if a 'hp:/...'
  print queue exists and exits otherwise.
  This avoids that hp-systray with all its Python stuff must be
  loaded when the desktop starts up only to let hp-systray do
  its built-in test and exit if there is no HPLIP print queue
  (see Novell/openSUSE Bugzilla bnc#649280).
- Updated to version 3.10.9:
  New Scan protocol (Low End Data Model) support.
  Many more supported all-in-one devices.
  Many bug fixes.
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- Updated to version 3.10.6:
  New protocol support (LEDM) for device status over Network
  and USB.
  Some more supported all-in-one devices.
  Several bug fixes.
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- Updated to version 3.10.5:
  Fixed "libusb couldn't open USB device, Permission denied"
  error message in openSUSE.
  Several more supported all-in-one devices.
  Several bug fixes.
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
* Wed Sep 15 2010 aj@suse.de
- Change BuildRequires for sane-backends devel split.
* Thu Apr  1 2010 jsmeix@suse.de
- Updated to version 3.10.2:
  The hpcups driver is again updated to better align with
  the product specifications for various printer models.
  Several more supported all-in-one devices.
  Several bug fixes (no Suse bugs).
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- Updated to version 3.9.12:
  The hpcups driver is updated to better align with the
  product specifications for various printer models.
  Several more supported printers.
  Several bug fixes (no Suse bugs).
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- Updated to version 3.9.10:
  The hpcups driver has been re-written. It does no longer do
  bi-directional IO. Printer specific settings are no longer
  hard coded, but are controlled by the PPD file.
  Many more supported printers and all-in-one devices.
  Several bug fixes (no Suse bugs).
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- hpcups.drv.in-3.9.8-reorder.patch and
  hpcups-ppds-3.9.8-reorder.tar.bz2 are obsolete
  because it is fixed in the source.
- create_hal_global_fdi_from_hpmud_rules is obsolete
  because HAL is no longer used to manage ACLs
  (see Novell/Suse Bugzilla bnc#542473 comment#13).
- change-udev-rules.diff fixes now also 56-hpmud_support.rules
  (see for example Novell/Suse Bugzilla bnc#577035) and
  it should trigger udev's generic ACL support for SANE
  via 'ENV{libsane_matched}="yes"' in 55-hpmud.rules
  (see Novell/Suse Bugzilla bnc#542473 comment#14).
  Perhaps the latter could be better achieved with the
  configure option --enable-udev-acl-rules (default=no)
  which installs 40-hplip.rules instead of 55-hpmud.rules
  but this was not at all tested up to now and it is
  likely not backward compatible (e.g. for openSUSE 11.2).
* Thu Oct 15 2009 jsmeix@suse.de
- Also moved /usr/share/hplip/data/models/models.dat
  and /etc/hp/hplip.conf to the hplip-hpijs sub-package
  so that the "hp" backend can autodetect printers
  (see Novell/Suse Bugzilla bnc#546856 comment#10).
* Thu Oct 15 2009 jsmeix@suse.de
- In the hplip-hpijs sub-package made weak package dependencies
  even weaker to avoid bloating of minimal installations. Now
  the hplip-hpijs sub-package only "Enhances: ghostscript_any"
  and "Suggests: hplip" (see Novell/Suse Bugzilla bnc#546893).
- Enlarged hplip-hpijs to be useful for a CUPS print queue.
  Moved the following files from the hplip main package
  to the hplip-hpijs sub-package: cups/backend/hp,
  cups/filter/foomatic-rip-hplip, cups/filter/hpcac,
  cups/filter/hpcups, cups/filter/hplipjs,
  and all PPD files (see Novell/Suse Bugzilla bnc#546856).
* Wed Sep 16 2009 jsmeix@suse.de
- hpcups.drv.in-3.9.8-reorder.patch addresses two issues
  in the 3.9.8 hpcups.drv.in file from which dynamic PPDs
  are generated.
  It re-orders common paper sizes so that normal, fullbleed
  and duplex papers sizes are grouped together in the PPD.
  It changes the LJColor device class from RGBW to RGB
  color space. The K band was not being printed by hpcups.
- The hpcups-ppds-3.9.8-reorder.tar.bz2 source file contains
  the matching static PPDs which are fixed according to what
  hpcups.drv.in-3.9.8-reorder.patch fixes for dynamic PPDs.
* Thu Aug  6 2009 jsmeix@suse.de
- The hplip.SuSEfirewall2 source file provides support
  to open UDP ports 5353(mdns) and 427(svrloc) for mDNS support
  according to the init-suse-firewall in the tar ball
  (see Novell/Suse Bugzilla bnc#528819).
- Updated to version 3.9.8:
  Added mDNS/Bonjour support.
  Enabled mDNS as the default network search mechanism.
  Added front-end support for mDNS/Bonjour in setup.
  Added hpmud support for mDNS.
  The tar ball provides a init-suse-firewall init script
  for mDNS support which is not included in the RPM.
  Fixed wificonfig associate issue when called from hp-setup.
  Added 40-hplip.rules to the tar ball for distros with
  udev ACL support. Use configure option --enable-udev-acl-rules
  to install 40-hplip.rules instead of 55-hpmud.rules.
  Fixed Normal Grayscale on DJ8xx and DJ8x5 for HPCUPS.
  Added -lsane link option for libsane-hpaio in Makefile.
  Many more supported printers and all-in-one devices.
  Many bug fixes (no Suse bugs).
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
* Wed Jul  1 2009 jsmeix@suse.de
- Fixed hp-toolbox.wrapper by adding "..." quotation when
  calling 'test -x "$( type -p whatever )"' because
  when 'type -p whatever' fails calling 'test -x' without
  an explicite empty argument would result true
  (see Novell/Suse Bugzilla bnc#503322 comment#6).
- fix_gcc44_glib.diff is obsolete since version 3.9.6b
  because it is fixed in the source.
- Updated to version 3.9.6b:
  The new native CUPS driver (HPCUPS) is now the default
  printer driver. HPCUPS provides new paper sizes for borderless
  and duplex so that there are now HPCUPS PPDs with exact
  printable regions for normal, borderless and duplex paper sizes
  which should fix https://bugs.launchpad.net/hplip/+bug/173857
  For now HPIJS (and its matching foomatic-rip-hplip PPDs)
  are still included (HPIJS can co-exist with HPCUPS).
  A new utility 'hp-wificonfig' can pre-configure wifi-capable
  printers on a wireless network. Once pre-configured, a queue
  for the printer can be set up as usual using hp-setup.
  Renamed hp-devicesetup to hp-devicesettings.
  Added CUPS filter hpcupsfax and new hpcups fax PPDs.
  Bumped libhpmud.so.0.0.4 to libhpmud.so.0.0.5.
  Integrated --enable-lite-build (default=no) into configure.in
  which can be used to get a minimal print/scan only build with
  limited Plugin support (Novell/Suse provides the "full" build).
  Many more supported printers and all-in-one devices.
  Many bug fixes (no Suse bugs).
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
* Tue Jun  2 2009 jsmeix@suse.de
- fix_gcc44_glib.diff fixes GCC/glibc issues, here in particular
  "invalid conversion from 'const char*' to 'char*'" errors.
  The upstream bug report is
  https://bugs.launchpad.net/hplip/+bug/382720
* Tue May  5 2009 jsmeix@suse.de
- force-qt4-for-hp-systray-desktop.diff is obsolete because
  configure uses --enable-qt4 by default now which obsoletes
  also "Recommends: python-qt" (only python-qt4 is required).
- Updated to version 3.9.4b:
  A few bug fixes (no Suse bugs).
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- Updated to version 3.9.4:
  Added PolicyKit support. Command line tools like hp-setup,
  hp-plugin, etc. are now run as regular user.
  Added GPG digital signature support to the HPLIP plug-in
  to validate that the plug-in is not corrupted and authentic.
  Added native CUPS driver support (hpcups) currently for
  testing only and added static PPDs for hpcups.
  Some more supported printers and all-in-one devices
  (in particular a few Designjet PostScript printers).
  Many bug fixes (no Suse bugs).
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- Updated to version 3.9.2:
  Qt4 now default UI.
  Support policy change. End of support date is added to
  all HPLIP supported devices, for details see
  http://hplipopensource.com/node/314
  New file /var/lib/hp/hplip.state for runtime variable data.
  Removed any variable data from /etc/hp/hplip.conf.
  Some more supported printers and all-in-one devices.
  Major bug fixing on Qt4 solution (no Suse bugs).
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- Updated to version 2.8.12:
  From this release forward, all PPD files - even for devices
  that require a binary plug-in - will reside in the tarball
  (the "plugin PPDs" are moved into hpijs.drv).
  Preview (alpha) release of the Qt4 version of HPLIP.
  Replaced "MODE 0666" udev device permissions with
  "console permissions via HAL".
  No new supported devices.
  Several bug fixes (no Suse bugs).
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- Updated to version 2.8.10:
  Bumped libhpmud version for new plugin attribute.
  Many more supported printers and all-in-one devices.
  Several bug fixes (no Suse bugs).
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
- Updated to version 2.8.9:
  Added Qt4 configure option but Qt3 is the default.
  Many bug fixes (no Suse bugs).
  Several more supported printers, in particular
  some Compact Photo (QuickConnect) printers.
  For details see
  http://hplipopensource.com/hplip-web/release_notes.html
* Wed Dec  3 2008 lnussel@suse.de
- use "usb" instead of "usb_device" (bnc#438867)
* Wed Dec  3 2008 jsmeix@suse.de
- Moved /etc/hal/fdi/policy/10osvendor/70-hpmud.fdi
  to /usr/share/hal/fdi/information/20thirdparty/70-hpmud.fdi
  (see Novell/Suse Bugzilla bnc#438867).
* Tue Nov 18 2008 jsmeix@suse.de
- Let suse_update_desktop_file add X-SuSE-translate key
  to /etc/xdg/autostart/hplip-systray.desktop so that we can
  update its translations with translation-only packages
  (see Novell/Suse Bugzilla bnc#445738).
* Tue Oct 21 2008 jsmeix@suse.de
- Changed change-udev-rules.diff to jump to the end
  if SUBSYSTEM!="usb" and replaced SYSFS by ATTR
  (see Novell/Suse Bugzilla bnc#436085).
* Tue Sep 16 2008 jsmeix@suse.de
- Added "Recommends: hplip" to hplip-hpijs because when only
  hplip-hpijs is there, it should tell the dependency resolver
  that for usual functionality, hplip should be installed
  too (if possible).
* Thu Sep 11 2008 jsmeix@suse.de
- force-qt4-for-hp-systray-desktop.diff forces Gnome and KDE
  to execute hp-systray as "hp-systray --qt4" via
  /etc/xdg/autostart/hplip-systray.desktop so that
  hp-systray docks to the notification tray of the desktops.
  Because of this the python-qt4 RPM is now required
  (see Novell/Suse Bugzilla bnc#377575).
  This additional requirement should be no problem because
  in an upcoming release HPLIP is converted over to Qt4, see
  https://bugs.launchpad.net/hplip/+bug/231978/comments/7
  and then the "Recommends: python-qt" can be dropped
  (see the entry below) but currently only hp-systray
  can be used with Qt4.
* Wed Sep 10 2008 jsmeix@suse.de
- Do no longer have a hard RPM requirement for python-qt
  (now there is only "Recommends: python-qt") to be able
  to provide hplip even on a distribution without python-qt.
  Without python-qt all GUI stuff would fail but
  several /usr/bin/hp-* tools have a command line
  option to run in non-graphical mode so that the basic driver
  functionality still works even without python-qt.
- Have versioned "Obsoletes" for hpijs-standalone to meet our
  policies even if the real intention is that any installed
  version of hpijs-standalone is replaced and explain the
  unversioned "Obsoletes" for hplip17 and hplip17-hpijs
  (see Novell/Suse Bugzilla bnc#251830).
* Tue Sep  9 2008 jsmeix@suse.de
- The configure option disable-foomatic-xml-install
  does no longer exist.
- Updated to version 2.8.7:
  Some bug fixes (no Suse bugs).
  Some more supported printers.
  For details see release_notes.html
- Updated to version 2.8.6b:
  Replaced the doc directory with an abbreviated web document
  (there is no longer hpijs.html and device_classes.html).
  Redesigned the proprietary plugin support. There is now only
  one plugin that is valid for each HPLIP release, see
  https://answers.launchpad.net/hplip/+question/30595
  Changed the hpijs.drv to support multiple products via
  multiple "Product" entries in the PPD but see
  https://bugs.launchpad.net/hplip/+bug/235148
  Several bug fixes (no Suse bugs).
  Many more supported printers.
  For details see release_notes.html
- Updated to version 2.8.5:
  Major toolbox (HP Device Manager) revamp/refresh.
  More dbus support (live status updating).
  hp-systray will exit if no HPLIP installed queues found which
  obsoletes HPLIP-2.8.4-systray_exit_if_no_device_2.patch
  Many bug fixes (no Suse bugs).
  Several more supported printers.
  For details see release_notes.html
* Fri Sep  5 2008 jsmeix@suse.de
- Keep all PPDs even if cupstestppd FAILs.
  With each CUPS version upgrade cupstestppd finds more
  and more errors so that more and more PPDs would be
  no longer included in the RPM which have been included
  before which results a regression.
  As far as we know there have been no problems at all because of
  not strictly compliant PPDs in HPLIP so that it is much better
  to provide all PPDs so that the matching printers can be used
  than to be rigorous regarding compliance to the PPD spec.
* Thu Sep  4 2008 jsmeix@suse.de
- Changed the "Conflicts: hpijs-standalone" in hplip-hpijs
  to "Obsoletes: hpijs-standalone" regardless of any version.
  hplip-hpijs and hpijs-standalone both contain /usr/bin/hpijs
  so that both packages have a RPM conflict.
  But when the minimalist hpijs-standalone is to be replaced
  by the full-featured hplip, hplip requires hplip-hpijs
  and this should silently supersede hpijs-standalone
  regardless of any version (see Novell/Suse Bugzilla bnc#388149).
* Thu Aug 14 2008 jsmeix@suse.de
- Removed the hplip init script which is obsolete since
  version 2.8.4 where hpssd is gone and replaced by
  hp-systray, see Novell/Suse Bugzilla bnc#390663.
* Tue Apr 29 2008 jsmeix@suse.de
- Added RPM requirement for python-gobject2 because the dbus stuff
  in HPLIP requires the Python module gobject but there is no
  automated RPM requirement for python-gobject2, see
  https://answers.launchpad.net/hplip/+question/30741
* Thu Apr 10 2008 jsmeix@suse.de
- HPLIP-2.8.4-systray_exit_if_no_device_2.patch lets hp-systray
  exit if the HPLIP driver seems to be not in use (i.e. if there
  is neither a 'hp:/...' nor a 'hpfax:/...' print queue), see
  https://bugs.launchpad.net/hplip/+bug/213938
  This patch obsoletes the whole hp-systray.wrapper stuff,
  see the entry below and Novell/Suse Bugzilla bnc#377885.
* Tue Apr  8 2008 jsmeix@suse.de
- Added hp-systray.wrapper which is a wrapper for hp-systray
  which runs it only if there is a 'hp:/...' print queue
  and changed /etc/xdg/autostart/hplip-systray.desktop
  to run the wrapper, see Novell/Suse Bugzilla bnc#377885.
* Thu Apr  3 2008 jsmeix@suse.de
- Updated to version 2.8.4:
  Elimination of all persistent startup daemons.
  The last daemon hpssd has been replaced with hp-systray.
  All interprocess communication uses now dbus.
  Therefore dbus-1-python version 0.80 or greater is required.
  PC send fax requires dbus and a running hp-systray to operate
  but hp-toolbox and hp-sendfax launch hp-systray automatically
  and there is also /etc/xdg/autostart/hplip-systray.desktop.
  When no HPLIP tools are running (e.g. hp-toolbox),
  and the user closes or disables hp-systray,
  there will be no HPLIP processes running whatsoever.
  Many bug fixes (no Suse bugs).
  One more supported LaserJet ZJStream printers (M1120),
  one OfficeJet (J6400), and two Photosmart (C4340, B8800)
  where the latter has a new printer device class (PSB9100).
  For details see release_notes.html
- Adapted the hplip init script to provide backward compatibility:
  It still exists to avoid that printer/scanner setup tools fail
  when they try to enable the "hplip" service but all it does
  is to stop a possibly running hpssd.
* Wed Apr  2 2008 jsmeix@suse.de
- Exchanged create_hal_global_fdi_from_models.dat with
  create_hal_global_fdi_from_hpmud_rules which creates the
  global HAL 70-hpmud.fdi file during build-time from the
  55-hpmud.rules file to be in sync with the udev rules file
  and to make sure to have all possible HPLIP device IDs, see
  https://bugs.launchpad.net/ubuntu/+source/hplip/+bug/195782
- Require the exact matching version of the hpijs sub-package
  to have the correct libhpip and libhpmud installed.
- Require pyxml to have the xml.parsers.expat Python module,
  see https://answers.launchpad.net/hplip/+question/25696
* Tue Feb 26 2008 jsmeix@suse.de
- Static "hpijs" PPD files via enable-foomatic-ppd-install
  require foomatic-rip-hplip via their cupsFilter entries
  so that enable-foomatic-rip-hplip-install is also needed.
  See https://answers.launchpad.net/hplip/+question/25654
  and see Novell/Suse Bugzilla bnc#364419.
* Thu Feb 21 2008 jsmeix@suse.de
- create_hal_global_fdi_from_models.dat creates the
  global HAL 70-hpmud.fdi file during build-time from the
  models.dat file (see Novell/Suse Bugzilla bnc#336658).
- Built version 2.8.2 in the traditional way with readymade
  PPD files in /usr/share/cups/model/manufacturer-PPDs/hplip/
  (i.e. without hpijs.drv and foomatic-rip-hplip)
- Updated to version 2.8.2:
  HPIJS PPD files are now created with the CUPS DDK instead of
  the foomatic database. Dynamic PPD files are now supported
  via the hpijs.drv file.
  Added foomatic-rip-hplip support. Foomatic-rip-hplip is for
  distros that do not have the latest foomatic-rip which is
  required for drv support.
  Updated the krgb patch for gpl ghostscript 8.61.
  Updated the "hp" backend to return only hplip supported devices
  during device discovery. If the device is not in models.dat
  the "hp" backend will exclude it.
  Changed margins to 0.125 inch from 0.
  Bumped libhpmud from 0.0.1 to 0.0.2 for support_type
  in hpmud_query_model().
  Several bug fixes (no Suse bugs).
  Several more supported printers (some more ZJStream printers).
- Updated to version 2.7.12:
  Added PJL support to "hp" backend which provides in-band
  printer status.
  Bumped libhpmud from 0.0.0 to 0.0.1 for statustype support
  in hpmud_query_model().
  Several bug fixes (no Suse bugs).
  Several more supported LaserJet printers, one ZJStream printer,
  one LJm1005 printer with binary-only plugin (LaserJet M1005 MFP).
* Fri Nov  9 2007 jsmeix@suse.de
- Changed rchplip (i.e. /etc/init.d/hplip):
  Added "$local_fs $remote_fs $syslog" to Required-Start
  to be on the safe side and added a line "export HOME=/tmp"
  to mitigate Novell/Suse Bugzilla bnc#339443.
* Tue Oct 23 2007 jsmeix@suse.de
- Updated to version 2.7.10:
  New LJZjsMono printer device class for ZJStream printers.
  ZJStream printers require JBIG which has issues
  (see Novell/Suse Bugzilla bnc#263181). Therefore the support
  for ZJStream printers is provided only via a binary-only plugin
  which is downloaded by "hp-setup" from the HP web-site only after
  the user has accepted the license terms.
  Applied patch for issue CVE-2007-5208 (hpssd command injection)
  Several bug fixes (no Suse bugs).
  Two more supported Photosmart and Officejet printers.
  For details see release_notes.html
- Updated to version 2.7.9:
  Made the default udev 55-hpmud.rules file more permissive
  (ie: MODE=0666) so that also device status works for any user.
  This looks sufficiently secure by default because the
  55-hpmud.rules matches now only for those USB product IDs
  which belong to HP printers and all-in-one devices so that
  other HP USB devices like keyboard, mouse, and mass storage
  devices won't get MODE=0666 by accident.
  All known product-ids that HPLIP/HPIJS supports have been
  added to the model.dat file.
  Many bug fixes (no Suse bugs).
  Some more supported Photosmart and Officejet printers.
  For details see release_notes.html
* Tue Sep 18 2007 jsmeix@suse.de
- Add a line-feed to the end of all PPDs to fix those PPDs where
  it is missing. See Novell/Suse Bugzilla bnc#309832:
  Unix/Linux text files must end with a line-feed.
  Otherwise reading the last line results EOF and then some
  programs may ignore the last line.
* Wed Sep 12 2007 jsmeix@suse.de
- Ignore cupstestppd FAILs because of errors in UIConstraints
  and/or NonUIConstraints which are detected since cupstestppd
  in CUPS > 1.2.7 (i.e. since openSUSE 10.3).
  See Novell/Suse Bugzilla bnc#309822: When this bug is fixed,
  cupstestppd would no longer result zero exit code.
  In the long run the PPDs should be fixed but as far as we know
  there have been no problems because of such UIConstraints errors
  so that it should be o.k. let those PPDs pass even if they are
  not strictly compliant.
* Tue Aug  7 2007 jsmeix@suse.de
- Changed /etc/udev/rules.d/55-hpmud.rules (via a change in
  change-udev-rules.diff) from OWNER="root" GROUP="lp" MODE="0660"
  to OWNER="root" GROUP="lp" MODE="0664" (i.e. allow read
  permissions for HP USB device files for normal users).
  Reason: Without read permissions even a simple command
  like "lsusb" cannot list HP USB devices to normal users
  which could cause unnecessary confusion.
  Furthermore have only read permissions for HP USB device files
  for normal users is in compliance to the default assumptions
  in upstream HPLIP and it should be sufficiently secure because
  for retrieving data from the device a matching request must be
  sent to the device which requires write permissions.
* Thu Aug  2 2007 jsmeix@suse.de
- Updated to version 2.7.7:
  Many bug fixes (no Suse bugs).
  Some more supported Photosmart printers.
  For details see release_notes.html
- fix-printing-white-spaces-and-empty-lines.diff is no longer
  needed because the bug is now fixed in the source.
* Thu Jul 26 2007 jsmeix@suse.de
- Changed change-udev-rules.diff so that 55-hpmud.rules matches
  also against the new SUBSYSTEM=="usb" but keep "usb_device"
  for backward compatibility (Novell/Suse Bugzilla bnc#294161).
* Fri Jul  6 2007 jsmeix@suse.de
- fix-printing-white-spaces-and-empty-lines.diff fixes printing
  white spaces and empty lines according to a mail from HP
  on the hplip-help@lists.sourceforge.net list.
* Tue Jul  3 2007 jsmeix@suse.de
- Updated to version 2.7.6:
  No more start-up daemons:
  hpiod is replaced by new direct device I/O (via hpmud library),
  hpssd (for device status) still exists but is started by default
  as a daemon by the first user who needs it which is not nice
  because this results a random user which runs hpssd therefore
  we (i.e. Novell/Suse) still provide /etc/init.d/hplip which
  is used to start hpssd as before during system boot.
  Many bug fixes (no Suse bugs) and some enhancements.
  Some more supported Photosmart, Color LaserJet, and DeskJet
  printers.
  For details see release_notes.html
* Thu Jun 21 2007 jsmeix@suse.de
- Added stop_on_removal to preun, insserv_cleanup to postun,
  and ldconfig to post and postun for the hpijs sub-package.
* Thu May 24 2007 ro@suse.de
- Added libusb-devel to BuildRequires.
* Fri Apr 27 2007 jsmeix@suse.de
- Updated to version 1.7.4a:
  Resolved a build issue that caused a couple missing files
  in the 1.7.4 release and a fix for hp-check (no Suse bugs).
* Mon Apr 23 2007 jsmeix@suse.de
- Updated to version 1.7.4:
  Many bug fixes (no Suse bugs).
  Some more supported DeskJet printers.
  For details see release_notes.html
* Mon Mar 26 2007 jsmeix@suse.de
- Updated to version 1.7.3:
  Many bug fixes (no Suse bugs).
  No new supported models but enhancements for some models.
  For details see release_notes.html
* Thu Mar  1 2007 jsmeix@suse.de
- Updated to version 1.7.2:
  Several more supported Officejet Pro devices.
  New OJProKx50 device class (derived from DJGenericVIP).
  Major hp-toolbox upgrade/redesign.
  Many bug fixes (no Suse bugs).
  fix-buffer-overflow.patch and hplip-1.7.1-1.patch are no longer
  needed because the bugs are now fixed in the sources.
* Fri Feb 16 2007 jsmeix@suse.de
- Added a fix for fat.c to fix-buffer-overflow.patch
  to aviod access when array subscript is above array bounds
  (Suse Bugzilla bnc#243047).
- Remove all byte-compiled Python .pyc (and perhaps .pyo)
  files which are created at run-time in /usr/share/hplip/
  via preun script (Suse Bugzilla bnc#244451).
* Mon Feb  5 2007 jsmeix@suse.de
- fix-buffer-overflow.patch fixes a too small string buffer
  which overflows in line 310 in ljcolor.cpp.
- Moved the hpijs man page to the hplip-hpijs sub-package
  so that there is no same file in hplip and hpijs-standalone
  (hplip-hpijs and hpijs-standalone conflict with each other).
* Thu Feb  1 2007 jsmeix@suse.de
- hplip-1.7.1-1.patch from HP fixes Deskjet D4100/D4160
  christmas-tree (firmware hangs up with flashing LEDs)
  on second print job.
- Removed /usr/bin/hpijs.without-libcups from hplip-hpijs
  to get rid of confusing RPM package requirements (hplip-hpijs
  requires cups-libs because of /usr/bin/hpijs).
- Created new package hpijs-standalone and hpijs-standalone.spec
  for a special version of /usr/bin/hpijs which neither needs
  a HPLIP library nor a CUPS library to run it.
* Wed Jan 31 2007 jsmeix@suse.de
- Removed explicite fstack-protector-all from CFLAGS and CXXFLAGS
  because fstack-protector will be enabled by default.
* Mon Jan 29 2007 jsmeix@suse.de
- Package 'sane' was renamed to 'sane-backends'.
  Adapted it so that it works with 'sane-backends'.
* Thu Jan 25 2007 jsmeix@suse.de
- Updated to version 1.7.1:
  Many bug fixes (no Suse bugs).
  No new supported models but enhancements for several models.
  For details see release_notes.html
- Removed the fix for uninitialized file pointer in api/model.c
  from fix-uninitialized-variables.diff because it is now
  fixed in the sources.
* Fri Jan 19 2007 jsmeix@suse.de
- Added fix for uninitialized file pointer in api/model.c to
  fix-uninitialized-variables.diff (Suse Bugzilla bnc#236709).
* Fri Jan 12 2007 jsmeix@suse.de
- Since version 1.6.12 /usr/bin/hpijs is linked with libcups
  so that the package hplip-hpijs could be no longer installed
  without at least the package cups-libs. Therefore an additional
  special /usr/bin/hpijs.without-libcups is built which does not
  require the CUPS library.
* Wed Dec 20 2006 jsmeix@suse.de
- Updated to version 1.6.12:
  Three more supported LaserJet printers.
  Many bug fixes (no Suse bugs).
  For details see release_notes.html
  Added SANE_DEBUG_HPAIO support for the hpaio SANE backend.
  The new models.dat file replaces the .xml files. The hplip_api
  can be used to get model attributes without running the HPLIP
  daemons. See hplip_api.h for reference (this affects the Suse
  Bugzilla bugs bnc#184798 and bnc#184824).
- Fixed hp-toolbox.wrapper to catch 'error' regardless of the case
  (see Suse Bugzilla bnc#229620).
* Tue Oct 17 2006 jsmeix@suse.de
- Updated to version 1.6.10:
  Several more supported LaserJet printers.
  Many bug fixes (no Suse bugs).
- Fixed typo in keyword in some LaserJet PPDs
  ("* PageRegion" -> "*PageRegion").
* Mon Sep 18 2006 jsmeix@suse.de
- Updated to version 1.6.9:
  Added support CD/DVD label printing (ie: PS D5100).
  Several more supported Photosmart printers.
  Many bug fixes (no Suse bugs).
* Mon Sep 11 2006 jsmeix@suse.de
- Using generalised cupsext* and pcardext* in the files section
  (instead of explicit only cupsext.so and pcardext.so)
  so that it works now both for Python 2.4 and 2.5
  (the latter installs additional *.egg-info files).
* Mon Sep  4 2006 jsmeix@suse.de
- Exchanged the hard RPM requirement for ghostscript_any by a
  supplements entry for hplip-hpijs so that there is no longer
  a mutual (cyclic) hard RPM dependency between hplip-hpijs
  and ghostscript-library.
* Thu Aug  3 2006 jsmeix@suse.de
- Updated to version 1.6.7:
  Changed from dynamic IP ports to static IANA IP ports
  for hpiod (2208) and hpssd (2207).
  Two more supported Photosmart printers.
  Several bug fixes (no Suse bugs).
* Mon Jul 17 2006 jsmeix@suse.de
- Fixed PPDs which contain "1284DeviceId" which must be
  "1284DeviceID" (detected by new CUPS 1.2 cupstestppd).
* Wed Jun 28 2006 jsmeix@suse.de
- Updated to maintenance release 1.6.6a:
  This provides various minor fixes and enhancements.
  For details see doc/release_notes.html in the source
  or /usr/share/doc/packages/hplip/release_notes.html
* Mon Jun 19 2006 jsmeix@suse.de
- Updated to version 1.6.6:
  HPLIP has reached 1.0 status.
  With this release a date encoded revision number x.y.m is used:
  x = major release number, y = year (6=2006), m = month (6=June)
  Correct URLs in HTML docs (obsoletes fix-doc-hrefs.diff).
  Removed DeviceOpen from hp backend. This fixes two problems:
  1) usblp will no longer be removed for device discovery
  2) device discovery will no longer cause Inkjets to power-up.
  Added hpaio.desc file for SANE.
  Several more supported printers.
- Cleaned up build (simplified spec file):
  Changed install dir for PPDs and doc in Makefile.am.
  Using configure without rpm-install.
  Using configure with --disable-cups-install.
  Links to work around inconsistent naming of python scripts
  and links to hpfax backend and its associated PPD file
  are no longer needed.
* Fri Jun  9 2006 jsmeix@suse.de
- Added man page for /usr/bin/hpijs (hpijs.1.gz).
- Fixed wrong URLs in HTML documentation (fix-doc-hrefs.diff).
- Added links to work around inconsistent naming of python scripts.
- Added links to hpfax backend and its associated PPD file
  to make them available as usual for CUPS setup tools.
* Mon May 22 2006 jsmeix@suse.de
- Fixed typo (missing '"') in hplip-init-script.diff
* Fri May 19 2006 jsmeix@suse.de
- Updated to version 0.9.11:
  Revised and updated documentation.
  Some more supported all-in-one devices and printers.
  Several bug fixes (no Suse bugs).
- Updated to version 0.9.10:
  Several bug fixes (no Suse bugs).
- Updated to version 0.9.9:
  Uses libusb for all USB I/O.
  CUPS USB DeviceURIs must be changed from
  "hp:/hp_model?device=/dev/usb/lpX" (no longer supported)
  to "hp:/hp_model?serial=xxxxxxxx".
  One more supported all-in-one device.
  Several bug fixes (no Suse bugs).
- Updated to version 0.9.8:
  New PC send fax support via special CUPS backend (hpfax)
  and special HP-Fax-hplip.ppd PPD file
  and a new send fax UI (hp-sendfax).
  Some more supported printers.
  Several bug fixes (no Suse bugs).
* Wed Apr 26 2006 jsmeix@suse.de
- Fixed PPDs for "LaserJet 5Si" and "LaserJet 5MP"
  (see Suse Bugzilla bnc#164991).
* Fri Feb 24 2006 jsmeix@suse.de
- Fixed an array index underflow (for LJ1010, LJ1012)
  in ljfastraster.cpp (Suse Bugzilla bnc#152720).
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Jan 12 2006 jsmeix@suse.de
- Set compiler flag "-fstack-protector-all" to build it with
  "Stack Protector" via a so called "canary" (requires gcc >= 4.1)
* Wed Jan  4 2006 jsmeix@suse.de
- Moved /usr/lib[64]/libhpip.* library files to the hplip-hpijs
  sub-package because /usr/bin/hpijs requires libhpip but for
  special cases (e.g. for a minimal printing system) it should
  be possible to use only HPIJS without the rest of HPLIP.
* Tue Jan  3 2006 jsmeix@suse.de
- Updated to version 0.9.7
  including the additional hplip-0.9.7-2.patch from HP.
* Thu Dec 22 2005 ro@suse.de
- requires: PyQt -> python-qt
* Thu Dec  1 2005 jsmeix@suse.de
- Removed unneeded KDE packages from "neededforbuild" since
  the new package python-qt was split from kdebindings3-python
  (see Suse Bugzilla bnc#135250).
* Mon Nov 28 2005 jsmeix@suse.de
- Replaced requirement for the package kdebindings3-python
  by a generic requirement for the RPM capability PyQt
  to avoid needless dependencies to KDE libraries
  (see Suse Bugzilla bnc#135250).
* Tue Nov 22 2005 jsmeix@suse.de
- Added -fno-strict-aliasing to the CXXFLAGS to avoid problems
  in ljfastraster.cpp (line 1213) and hpijs.cpp (lines 86, 223).
* Fri Nov 18 2005 jsmeix@suse.de
- Updated to version 0.9.6
* Wed Sep 21 2005 jsmeix@suse.de
- Updated to version 0.9.5
  including the additional hplip-0.9.5-3.patch from HP.
* Mon Sep 12 2005 jsmeix@suse.de
- Several PPDs contain "600x600x2dpi" which is not allowed
  according to the Adobe PPD specification section 5.9
  and which is therefore simply replaced by "600x1200dpi"
  (see Suse Bugzilla bnc#116393).
* Mon Aug 29 2005 jsmeix@suse.de
- Removed a non-working PPD.
- Fix "... is used uninitialized ..." warning.
* Tue Jul 26 2005 jsmeix@suse.de
- Updated to version 0.9.4
- Removed obsolete fixes for missing class prototypes.
- Removed obsolete fixes for HP_Business_Inkjet_3000.ppd
- Added a fix for condrestart in /etc/init.d/hplip
* Tue May 31 2005 jsmeix@suse.de
- Updated to version 0.9.3
* Tue May 24 2005 jsmeix@suse.de
- Fixed missing class prototypes, otherwise it fails with
  "error: ISO C++ forbids declaration of 'xxx' with no type".
* Tue May 17 2005 jsmeix@suse.de
- Fix "... is used uninitialized ..." warnings.
* Wed May  4 2005 jsmeix@suse.de
- Updated to version 0.9.2 which does no longer need
  the "fix C" (i.e. hplip-0.8.8.diff) from below.
* Sun Apr 10 2005 coolo@suse.de
- fix C
* Tue Mar 22 2005 jsmeix@suse.de
- Added PreReq.
* Thu Mar 17 2005 jsmeix@suse.de
- Fixed a bug in HP-DeskJet_3740-hpijs.ppd.gz:
  According to hpijs_readme.html the DeskJet 3740 belongs to the
  DJ3320 device class.
* Tue Mar  8 2005 jsmeix@suse.de
- Added %%suse_update_desktop_file stuff for hp-toolbox.
- Moved %%{_libdir}/libsane-hpaio.* to %%{_libdir}/sane/
  instead of creating symlinks (see Tue Mar 1 11:15:33).
* Tue Mar  1 2005 jsmeix@suse.de
- Added python-xml to RPM requirements because otherwise
  hpssd (i.e. /usr/share/hplip/hpssd.py) doesn't work.
- Create symlinks (via '%%triggerin -- sane') to all
  %%{_libdir}/libsane-hpaio.* so that SANE will find them.
- Added kdebindings3-python to RPM requirements because otherwise
  hp-toolbox (i.e. /usr/share/hplip/toolbox) doesn't work.
* Tue Feb 22 2005 jsmeix@suse.de
- Changed default media size from Letter to A4
  if this is an available choice in the PPD.
* Tue Feb 15 2005 jsmeix@suse.de
- Updated to version 0.8.8, for details see ChangeLog and
  http://hpinkjet.sourceforge.net/updates.php
- Removed the "compatibility"-links because they are not needed.
- Fixed basic stuff in the init script (needs further improvement).
- Source should be x86_64 clean (SUSE patch no longer needed).
* Tue Feb  1 2005 jsmeix@suse.de
- Updated to version 0.8.7, for details see ChangeLog and
  http://hpinkjet.sourceforge.net/updates.php
- Added triggerin and postun scripts to add and remove
  the SANE backend "hpaio" in /etc/sane.d/dll.conf
- Replaced hplip-0.8.4-models.xml.diff by
  hplip-0.8.7-models.xml.diff because the "HP LaserJet 1220"
  is now in the models.xml file but the entry is buggy.
* Tue Jan 25 2005 jsmeix@suse.de
- Branched the sub-package hplip-hpijs which contains only
  the plain HPIJS binary so that Ghostscript can require
  only this sub-package (without all the other stuff).
- Added a link to the toolbox program to have it accessible
  via the user's PATH.
- Added the usual 'rc'-link to the runlevel script.
- Added the following RPM requirements regarding printing:
  hplip requires hplip-hpijs and foomatic-filters
  hplip-hpijs requires ghostscript_any
  (There are no RPM requirements regarding scanning because
  HPLIP will be also used for plain printers.)
- Exchanged the destructive line for the cupsd in the runlevel script
  because cupsd runs as user lp and dies in case of a SIGHUP.
* Tue Jan 18 2005 jsmeix@suse.de
- patch hplip-0.8.4-models.xml.diff adds the "HP LaserJet 1220"
  to the list of known models of the SANE backend "hpaio"
* Wed Jan 12 2005 sf@suse.de
- add --libdir=%%_libdir to build on multilib archs
- add patch for cups search path for backends
* Thu Dec  2 2004 jsmeix@suse.de
- initial version
