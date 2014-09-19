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
License:        BSD-3-Clause and GPL-2.0+ and MIT
Group:          Network and Connectivity/Printing
# HPLIP has reached 1.0 status. With this release a date encoded revision number is used:
# x.y.m : x = major release number, y = year (eg: 6 = 2006), m = month (eg: 6a = second release in June)
# Official releases have a 3 digit number and release candidates have a 4 digit number: x.y.m.rc
Version:        3.12.4
Release:        0
Url:            http://hplipopensource.com
# Source0...Source9 is for sources from HP:
# URL for Source0: http://prdownloads.sourceforge.net/hplip/hplip-3.12.4.tar.gz
# URL to verify Source0: http://prdownloads.sourceforge.net/hplip/hplip-3.12.4.tar.gz.asc
# How to verify Source0 see: http://hplipopensource.com/node/327
# For example: /usr/bin/gpg --keyserver pgp.mit.edu --recv-keys 0xA59047B9
#              /usr/bin/gpg --verify hplip-3.12.4.tar.gz.asc hplip-3.12.4.tar.gz
# must result: Good signature from "HPLIP (HP Linux Imaging and Printing) <hplip@hp.com>"
Source0:        hplip-%{version}.tar.gz

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
#%%if 0%%{?suse_version} > 1130
#BuildRequires:  sane-backends-devel
#%%else
#BuildRequires:  sane-backends
#%%endif
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
#Requires:       %%{name}-hpijs = %%{version}-%%{release}
# Same rationale for the sane subpackage.
#Requires:       %%{name}-sane = %%{version}-%%{release}
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
%configure  --docdir=\$${prefix}/share/doc/hplip \
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
#            --with-mimedir=%%{_sysconfdir}/cups \
#            --with-docdir=%%{_defaultdocdir}/%%{name}
%__make

%install
%make_install

mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/usr/share/license/%{name}

# Remove the installed /etc/sane.d/dll.conf
# because this is provided by the sane-backends package:
#rm %%{buildroot}%%{_sysconfdir}/sane.d/dll.conf
# Remove the installed HAL fdi file because HAL is no longer used (HAL is deprecated):
#rm %%{buildroot}%%{_datadir}/hal/fdi/preprobe/10osvendor/20-hplip-devices.fdi
# Remove the outdated "Check and add printer for Suse 10.3 distro" udev rule
# and let the build fail if it does no longer match to notify about the change:
#grep 'for Suse 10.3 distro' %%{buildroot}%%{_sysconfdir}/udev/rules.d/56-hpmud_add_printer.rules || exit 1
#sed -i -e '/for Suse 10.3 distro/,+1 d' %%{buildroot}%%{_sysconfdir}/udev/rules.d/56-hpmud_add_printer.rules
# Begin "General tests and adjustments for all PPDs" (see manufacturer-PPDs.spec):
#pushd %%{buildroot}%%{_datadir}/cups/model/manufacturer-PPDs/%%{name}
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
#ln -s ../../../bin/foomatic-rip %%{buildroot}/usr/lib/cups/filter/foomatic-rip-hplip
# Begin "Desktop menue entry stuff":
# Install /usr/share/hplip/data/images/64x64/hp_logo.png as desktop icon file
# because it is used in the hplip.desktop.in and hplip-systray.desktop.in sources:
#install -D -m 644 %%{buildroot}%%{_datadir}/hplip/data/images/32x32/hp_logo.png %%{buildroot}%%{_datadir}/icons/hicolor/32x32/apps/HPmenu.png
#install -D -m 644 %%{buildroot}%%{_datadir}/hplip/data/images/64x64/hp_logo.png %%%%{buildroot}%%{_datadir}/icons/hicolor/64x64/apps/HPmenu.png
#install -D -m 644 %%{buildroot}%%{_datadir}/hplip/data/images/128x128/hp_logo.png %%{buildroot}%%{_datadir}/icons/hicolor/128x128/apps/HPmenu.png
#install -D -m 644 %%{buildroot}%%{_datadir}/hplip/data/images/256x256/hp_logo.png %%{buildroot}%%{_datadir}/icons/hicolor/256x256/apps/HPmenu.png
# Set up and install the desktop menue entry stuff using "Categories=System;Monitor;"
# and remove HP's hplip.desktop and hplip-systray.desktop files before because we use Source100:
# (additionally there is/was a typo in HP's install because of the trailing blank at 'applications ')
#rm %%{buildroot}%%{_datadir}/applications/hplip*.desktop
#%%suse_update_desktop_file -i %%{name} System HardwareSettings Printing
# Let suse_update_desktop_file add X-SuSE-translate key to /etc/xdg/autostart/hplip-systray.desktop
# so that we can update its translations with translation-only packages.
#%%suse_update_desktop_file %%{buildroot}/etc/xdg/autostart/hplip-systray.desktop
# End of "Desktop menue entry stuff".
# Install the man page for /usr/bin/hpijs:
#install -d %%{buildroot}%%{_mandir}/man1
#install -m 644 %%{SOURCE102} %%{buildroot}%%{_mandir}/man1/
# Begin "Desktop autostart notification tray stuff":
# Install the wrapper for hp-systray:
#install -m 755 %%{SOURCE106} %%{buildroot}%%{_bindir}/hp-systray.wrapper
# Change /etc/xdg/autostart/hplip-systray.desktop to call hp-systray.wrapper:
#sed -i -e '/^Exec=hp-systray$/s/hp-systray/hp-systray.wrapper/;' %%{buildroot}/etc/xdg/autostart/hplip-systray.desktop
# End of "Desktop autostart notification tray stuff".
# Find duplicate files:
#%%fdupes -s %%{buildroot}

%post
#%%if 0%%{?suse_version} > 1130
#%%icon_theme_cache_post
#%%else
#gtk-update-icon-cache %%{_datadir}/icons/hicolor || true
#%%endif
/sbin/ldconfig
#exit 0

#%%triggerin -- sane-backends
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
#%%if 0%%{?suse_version} > 1130
#%%icon_theme_cache_postun
#%%else
#gtk-update-icon-cache %%{_datadir}/icons/hicolor || true
#%%endif
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

#%%post hpijs
#/sbin/ldconfig
#exit 0

#%%postun hpijs
#/sbin/ldconfig
#exit 0

%files
%manifest hplip.manifest
%defattr(-, root, root)
/usr/share/license/%{name}
#%%config %%{_sysconfdir}/xdg/autostart/hplip-systray.desktop
#%%dir %%{_sysconfdir}/udev
#%%dir %%{_sysconfdir}/udev/rules.d
#%%config %%{_sysconfdir}/udev/rules.d/55-hpmud.rules
#%%config %%{_sysconfdir}/udev/rules.d/56-hpmud_add_printer.rules
#%%config %%{_sysconfdir}/udev/rules.d/56-hpmud_support.rules
#%%config %%{_sysconfdir}/udev/rules.d/86-hpmud_plugin.rules
#%%{_bindir}/hp-align
#%%{_bindir}/hp-check
#%%{_bindir}/hp-check-plugin
#%%{_bindir}/hp-clean
#%%{_bindir}/hp-colorcal
#%%{_bindir}/hp-config_usb_printer
#%%{_bindir}/hp-devicesettings
#%%{_bindir}/hp-diagnose_plugin
#%%{_bindir}/hp-diagnose_queues
#%%{_bindir}/hp-fab
#%%{_bindir}/hp-faxsetup
#%%{_bindir}/hp-firmware
#%%{_bindir}/hp-info
#%%{_bindir}/hp-levels
#%%{_bindir}/hp-linefeedcal
#%%{_bindir}/hp-makecopies
#%%{_bindir}/hp-makeuri
#%%{_bindir}/hp-mkuri
#%%{_bindir}/hp-pkservice
#%%{_bindir}/hp-plugin
#%%{_bindir}/hp-pqdiag
#%%{_bindir}/hp-print
#%%{_bindir}/hp-printsettings
#%%{_bindir}/hp-probe
#%%{_bindir}/hp-query
#%%{_bindir}/hp-scan
#%%{_bindir}/hp-sendfax
#%%{_bindir}/hp-setup
#%%{_bindir}/hp-systray
#%%{_bindir}/hp-testpage
#%%{_bindir}/hp-timedate
#%%{_bindir}/hp-toolbox
#%%{_bindir}/hp-uninstall
#%%{_bindir}/hp-unload
#%%{_bindir}/hp-upgrade
#%%{_bindir}/hp-wificonfig
#%%{_libdir}/python%%{py_ver}/site-packages/cupsext.*
#%%{_libdir}/python%%{py_ver}/site-packages/hpmudext.*
#%%{_libdir}/python%%{py_ver}/site-packages/pcardext.*
#%%{_libdir}/python%%{py_ver}/site-packages/scanext.*
#%%dir /usr/lib/cups
#%%dir /usr/lib/cups/backend
#/usr/lib/cups/backend/hpfax
%dir /usr/lib/cups/filter
/usr/lib/cups/filter/hpcups
#/usr/lib/cups/filter/hpcupsfax
#%%doc %%{_defaultdocdir}/%%{name}/
#%%{_datadir}/icons/hicolor/*/apps/HPmenu.png
#%%{_datadir}/applications/%%{name}.desktop
#%%{_bindir}/hp-systray.wrapper
#%%{_datadir}/hplip/
#%%exclude %%{_datadir}/hplip/data/models/models.dat

#%%files hpijs
#%%defattr(-, root, root)
#%%config %%{_sysconfdir}/hp/
#%%config %%{_sysconfdir}/cups/pstotiff.convs
#%%config %%{_sysconfdir}/cups/pstotiff.types
#%%{_bindir}/hpijs
#%%doc %%{_mandir}/man1/hpijs.1.gz
#%%{_libdir}/libhpip.*
#%%{_libdir}/libhpmud.*
#%%dir /usr/lib/cups
#%%dir /usr/lib/cups/backend
#/usr/lib/cups/backend/hp
#%%dir /usr/lib/cups/filter
#/usr/lib/cups/filter/foomatic-rip-hplip
#/usr/lib/cups/filter/hpcac
#/usr/lib/cups/filter/hplipjs
#/usr/lib/cups/filter/hpps
#/usr/lib/cups/filter/pstotiff
#%%dir %%{_datadir}/cups
#%%dir %%{_datadir}/cups/model
#%%dir %%{_datadir}/cups/model/manufacturer-PPDs
#%%{_datadir}/cups/model/manufacturer-PPDs/%%{name}/
#%%{_datadir}/%%{name}/data/models/models.dat
#%%dir %%attr(0774,root,lp) %%{_var}/log/hp

#%%files sane
#%%defattr(-, root, root)
#%%dir %%{_libdir}/sane
#%%{_libdir}/sane/libsane-hpaio.*

%changelog
