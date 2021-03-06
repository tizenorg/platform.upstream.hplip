#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2003-2009 Hewlett-Packard Development Company, L.P.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# Author: Don Welch
#

# Std Lib
import os
import sys
import getpass
import signal

# Local
from base.g import *
from base import utils, tui
from core_install import *


def progress_callback(cmd="", desc="Working..."):
    if cmd:
        log.info("%s (%s)" % (cmd, desc))
    else:
        log.info(desc)


def password_entry():
    return getpass.getpass(log.bold("Please enter the root/superuser password: "))

def password_user_entry():
    return getpass.getpass(log.bold("Please enter the user (%s)'s password: " % os.getenv('USER')))


def option_question_callback(opt, desc, default='y'):
    ok, ans = tui.enter_yes_no("Do you wish to enable '%s'" % desc, default)
    if not ok: sys.exit(0)
    return ans



def start(language, auto=True, test_depends=False,
          test_unknown=False, assume_network=False,
          max_retries=3, enable=None, disable=None):
    try:
        core =  CoreInstall(MODE_INSTALLER, INTERACTIVE_MODE)
        current_version = prop.installed_version_int
        log.debug("Currently installed version: 0x%06x" % current_version)
        core.enable = enable
        core.disable = disable

        if core.running_as_root():
            log.error("You are running the installer as root. It is highly recommended that you run the installer as")
            log.error("a regular (non-root) user. Do you still wish to continue?")

            ok, ans = tui.enter_yes_no(log.bold("Continue with installation"), 'n')
            if not ans or not ok:
                sys.exit(1)

        if auto:
            log.note("Running in automatic mode. The most common options will be selected.")

        log.info("")
        log.note("Defaults for each question are maked with a '*'. Press <enter> to accept the default.")

        if not auto:
            tui.title("INSTALLATION MODE")
            log.info("Automatic mode will install the full HPLIP solution with the most common options.")
            log.info("Custom mode allows you to choose installation options to fit specific requirements.")

            #if os.getenv('DISPLAY') and utils.find_browser() is not None:
            if 0:
                ok, choice = tui.enter_choice("\nPlease choose the installation mode (a=automatic*, c=custom, w=web installer, q=quit) : ",
                    ['a', 'c', 'w'], 'a')
            else:
                ok, choice = tui.enter_choice("\nPlease choose the installation mode (a=automatic*, c=custom, q=quit) : ",
                    ['a', 'c'], 'a')

            if not ok: sys.exit(0)

            if choice == 'a':
                auto = True

            elif choice == 'w':
                import web_install
                log.debug("Starting web browser installer...")
                web_install.start(language)
                return

        log.info("\nInitializing. Please wait...")
        core.init()

        if test_unknown:
            core.distro_name = 'unknown'
            core.distro = 0
            core.distro_version = 0


        #
        # HPLIP vs. HPIJS INSTALLATION
        #

        #if not auto:
            #tui.title("INSTALL TYPE")
            #log.info("For most users, it is recommended to install HPLIP with full support (scanning, faxing, toolbox, etc).")
            #log.info("For servers or minimal installations, you can also install print support only (HPIJS only).")

            #ok, choice = tui.enter_choice("\nInstall full hplip support (recommended) or print-only support (f=full hplip support*, p=printing only support, q=quit) ?",
                #['f', 'p'], 'f')
            #if not ok: sys.exit(0)
            #if choice  == 'p':
                #core.selected_component = 'hpijs'

        #log.debug(core.selected_component)
        core.selected_component = 'hplip'

        #
        # INTRODUCTION
        #

        tui.title("INTRODUCTION")

        if core.selected_component == 'hplip':
            log.info("This installer will install HPLIP version %s on your computer." % core.version_public)
            #core.hpijs_build = False
        #else:
            #log.info("This installer will install HPIJS version %s on your computer." % core.version_public)
            #core.hpijs_build = True

        log.info("Please close any running package management systems now (YaST, Adept, Synaptic, Up2date, etc).")

##        #
##        # RELEASE NOTES
##        #
##
##        if not auto:
##            if os.getenv('DISPLAY'):
##                tui.title("VIEW RELEASE NOTES")
##                log.info("Release notes from this version are available as a web (HTML) document.")
##                log.info("The release notes file will be shown in a separate web browser window.")
##
##                ok, ans = tui.enter_yes_no("\nWould you like to view the release notes for this version of HPLIP", 'n')
##
##                if ok and ans:
##                    log.info("Displaying release notes in a browser window...")
##                    core.show_release_notes_in_browser()
##
##                if not ok:
##                    sys.exit(0)

        # For testing, mark all dependencies missing
        if test_depends:
            for d in core.have_dependencies:
                core.have_dependencies[d] = False

        num_req_missing = core.count_num_required_missing_dependencies()
        num_opt_missing = core.count_num_optional_missing_dependencies()


        #
        # CONFIRM AND SELECT DISTRO NAME AND VERSION
        #

        tui.title("DISTRO/OS CONFIRMATION")


        if core.distro_known():
            log.info("Distro appears to be %s %s.\n" % (core.get_distro_data('display_name', '(unknown)'), core.distro_version))

        log.debug("Distro = %s Distro Name = %s Display Name= %s Version = %s Supported = %s" % \
            (core.distro, core.distro_name, core.distros[core.distro_name]['display_name'], \
            core.distro_version, core.distro_version_supported))

        distro_ok, ok = False, True
        if core.distro_known():
            ok, distro_ok = tui.enter_yes_no('Is "%s %s" your correct distro/OS and version'
                % (core.get_distro_data('display_name', '(unknown)'), core.distro_version))

        if not ok:
            sys.exit(0)

        core.distro_changed()

        if not distro_ok:
            tui.title("DISTRO/OS SELECTION")
            core.distro, core.distro_version = DISTRO_UNKNOWN, DISTRO_VER_UNKNOWN

            log.info(log.bold("\nChoose the name of the distro/OS that most closely matches your system:\n"))

            max_name = 0
            for d in core.distros_index:
                dd = core.distros[core.distros_index[d]]
                if dd['display']:
                    max_name = max(max_name, len(dd['display_name']))

            formatter = utils.TextFormatter(
                    (
                        {'width': 4},
                        {'width': max_name, 'margin': 2},
                    )
                )

            log.info(formatter.compose(("Num.", "Distro/OS Name")))
            log.info(formatter.compose(('-'*4, '-'*(max_name))))

            d_temp = {}
            x = 0
            for d in core.distros_index:
                dd = core.distros[core.distros_index[d]]

                if dd['display']:
                    d_temp[x] = d
                    log.info(formatter.compose((str(x), dd['display_name'])))
                    x += 1

            ok, y = tui.enter_range("\nEnter number 0...%d (q=quit) ?" % (x-1), 0, x-1)
            if not ok: sys.exit(0)

            core.distro = d_temp[y]
            core.distro_name = core.distros_index[core.distro]
            distro_display_name = core.distros[core.distro_name]['display_name']
            log.debug("Distro = %s Distro Name = %s Display Name= %s" %
                (core.distro, core.distro_name, distro_display_name))

            if core.distro != DISTRO_UNKNOWN:
                versions = core.distros[core.distro_name]['versions'].keys()
                versions.sort(lambda x, y: core.sort_vers(x, y))

                log.info(log.bold('\nChoose the version of "%s" that most closely matches your system:\n' % distro_display_name))

                formatter = utils.TextFormatter(
                        (
                            {'width': 4},
                            {'width': 40, 'margin': 2},
                        )
                    )

                log.info(formatter.compose(("Num.", "Distro/OS Version")))
                log.info(formatter.compose(('-'*4, '-'*40)))

                log.info(formatter.compose(("0", "Unknown or not listed")))

                x = 1
                for ver in versions:
                    ver_info = core.distros[core.distro_name]['versions'][ver]

                    if ver_info['code_name'] and ver_info['release_date']:
                        text = ver + ' ("' + ver_info['code_name'] + '", Released ' + ver_info['release_date'] + ')'

                    elif ver_info['code_name']:
                        text = ver + ' ("' + ver_info['code_name'] + '")'

                    elif ver_info['release_date']:
                        text = ver + ' (Released ' + ver_info['release_date'] + ')'

                    else:
                        text = ver

                    if not ver_info['supported']:
                        text += " [Unsupported]"

                    log.info(formatter.compose((str(x), text)))
                    x += 1

                ok, core.distro_version_int = tui.enter_range("\nEnter number 0...%d (q=quit) ?" %
                    (x-1), 0, x-1)
                if not ok: sys.exit(0)

                if core.distro_version_int == 0:
                    core.distro_version = DISTRO_VER_UNKNOWN
                    core.distro_version_supported = False
                else:
                    core.distro_version = versions[core.distro_version_int - 1]
                    core.distro_version_supported = core.get_ver_data('supported', False)

                log.debug("Distro = %s Distro Name = %s Display Name= %s Version = %s Supported = %s" % \
                    (core.distro, core.distro_name, core.distros[core.distro_name]['display_name'], \
                    core.distro_version, core.distro_version_supported))

                core.distro_changed()

                log.info("\nDistro set to: %s %s" %
                    (core.get_distro_data('display_name', '(unknown)'), core.distro_version))


            if core.distro == DISTRO_UNKNOWN or not core.distro_version_supported:
                log.error("The distribution/OS that you are running is not supported. This installer\ncannot install an unsupported distribution. Please check your distribution/OS\nand re-run this installer or perform a manual installation.")
                if num_req_missing:
                    log.error("The following REQUIRED dependencies are missing and need to be installed:")

                    for d, desc, opt in core.missing_required_dependencies():
                        log.error("Missing REQUIRED dependency: %s (%s)" % (d, desc))

                for d, desc, req, opt in core.missing_optional_dependencies():
                    if req:
                        log.warning("Missing OPTIONAL dependency: %s (%s) [Required for option '%s']" % (d, desc, opt))
                    else:
                        log.warning("Missing OPTIONAL dependency: %s (%s) [Optional for option '%s']" % (d, desc, opt))

                sys.exit(1)

        #
        # SELECT OPTIONS TO INSTALL
        #



        if not auto:
            tui.title("SELECT HPLIP OPTIONS")
            log.info("You can select which HPLIP options to enable. Some options require extra dependencies.")
            log.info("")
            num_opt_missing = core.select_options(option_question_callback)

        #else: # auto
            #ok, enable_par = tui.enter_yes_no("Would you like to enable support for parallel (LPT:) connected printers?", 'n')
            #if not ok: sys.exit(0)

            #core.selected_options['parallel'] = enable_par

            #if enable_par:
                #log.info("Parallel support enabled.")
        else:
            enable_par = False
            core.selected_options['parallel'] = False

        log.debug("Req missing=%d Opt missing=%d HPLIP=%s Component=%s" % \
            (num_req_missing, num_opt_missing, core.hplip_present, core.selected_component))


        #
        # COLLECT SUPERUSER PASSWORD
        #
        if not core.running_as_root():
            su_sudo = core.get_distro_data('su_sudo')
            if su_sudo == "sudo":
                tui.title("ENTER USER PASSWORD")
                ok = core.check_password(password_user_entry, progress_callback)
            else:
                tui.title("ENTER ROOT/SUPERUSER PASSWORD")
                ok = core.check_password(password_entry, progress_callback)

            if not ok:
                log.error("3 incorrect attempts. Exiting.")
                sys.exit(1)

        #
        # INSTALLATION NOTES
        #

        if core.distro_supported():
            distro_notes = core.get_distro_data('notes', '').strip()
            ver_notes = core.get_ver_data('notes', '').strip()

            if distro_notes or ver_notes:
                tui.title("INSTALLATION NOTES")

                if distro_notes:
                    log.info(distro_notes)

                if ver_notes:
                    log.info(ver_notes)

                log.info("")

                if not tui.continue_prompt("Please read the installation notes."):
                    sys.exit(0)

        #
        # PRE-INSTALL COMMANDS
        #
        tui.title("RUNNING PRE-INSTALL COMMANDS")
        if core.run_pre_install(progress_callback): # some cmds were run...
            num_req_missing = core.count_num_required_missing_dependencies()
            num_opt_missing = core.count_num_optional_missing_dependencies()
        log.info("OK")

        #
        # REQUIRED DEPENDENCIES INSTALL
        #

        depends_to_install = []
        if num_req_missing:
            tui.title("INSTALL MISSING REQUIRED DEPENDENCIES")

            log.warn("There are %d missing REQUIRED dependencies." % num_req_missing)
            log.notice("Installation of dependencies requires an active internet connection.")

            for depend, desc, option in core.missing_required_dependencies():
                log.warning("Missing REQUIRED dependency: %s (%s)" % (depend, desc))

                ok = False
                packages, commands = core.get_dependency_data(depend)
                log.debug("Packages: %s" % ','.join(packages))
                log.debug("Commands: %s" % ','.join(commands))

                if core.distro_version_supported and (packages or commands):
                    if auto:
                        answer = True
                    else:
                        ok, answer = tui.enter_yes_no("\nWould you like to have this installer install the missing dependency")
                        if not ok: sys.exit(0)

                    if answer:
                        ok = True
                        log.debug("Adding '%s' to list of dependencies to install." % depend)
                        depends_to_install.append(depend)

                else:
                    log.warn("This installer cannot install '%s' for your distro/OS and/or version." % depend)

                if not ok:
                    log.error("Installation cannot continue without this dependency. Please manually install this dependency and re-run this installer.")
                    sys.exit(0)

                #log.info("-"*10)
                #log.info("")

        #
        # OPTIONAL dependencies
        #

        if num_opt_missing:
            tui.title("INSTALL MISSING OPTIONAL DEPENDENCIES")
            log.warn("There are %d missing OPTIONAL dependencies." % num_opt_missing)

            log.notice("Installation of dependencies requires an active internet connection.")

            for depend, desc, required_for_opt, opt in core.missing_optional_dependencies():

                if required_for_opt:
                    log.warning("Missing REQUIRED dependency for option '%s': %s (%s)" % (opt, depend, desc))

                else:
                    log.warning("Missing OPTIONAL dependency for option '%s': %s (%s)" % (opt, depend, desc))

                installed = False
                packages, commands = core.get_dependency_data(depend)
                log.debug("Packages: %s" % ','.join(packages))
                log.debug("Commands: %s" % ','.join(commands))


                if core.distro_version_supported and (packages or commands):
                    if auto:
                        answer = True
                    else:
                        ok, answer = tui.enter_yes_no("\nWould you like to have this installer install the missing dependency")
                        if not ok: sys.exit(0)

                    if answer:
                        log.debug("Adding '%s' to list of dependencies to install." % depend)
                        depends_to_install.append(depend)

                    else:
                        log.warning("Missing dependencies may effect the proper functioning of HPLIP. Please manually install this dependency after you exit this installer.")
                        log.warning("Note: Options that have REQUIRED dependencies that are missing will be turned off.")

                        if required_for_opt:
                            log.warn("Option '%s' has been turned off." % opt)
                            core.selected_options[opt] = False
                else:
                    log.warn("This installer cannot install '%s' for your distro/OS and/or version." % depend)

                    if required_for_opt:
                        log.warn("Option '%s' has been turned off." % opt)
                        core.selected_options[opt] = False


                #log.info("-"*10)
                #log.info("")


        log.debug("Dependencies to install: %s" % depends_to_install)

        if core.distro_version_supported and \
            (depends_to_install or core.hplip_present) and \
            core.selected_component == 'hplip':

            #
            # CHECK FOR RUNNING PACKAGE MANAGER
            #

            pid, cmdline = core.check_pkg_mgr()
            while pid:
                ok, user_input = tui.enter_choice("A package manager '%s' appears to be running. Please quit the package manager and press enter to continue (i=ignore, r=retry*, f=force, q=quit) :"
                    % cmdline, ['i', 'r', 'q', 'f'], 'r')

                if not ok: sys.exit(0)

                if user_input == 'i':
                    log.warn("Ignoring running package manager. Some package operations may fail.")
                    break

                if user_input == 'f':
                    ok, ans = tui.enter_yes_no("\nForce quit of package manager '%s'" % cmdline, 'y')

                    if not ok: sys.exit(0)

                    if ans:
                        cmd = core.su_sudo() % ("kill %d" % pid)
                        status, output = core.run(cmd)

                        if status != 0:
                            log.error("Failed to kill process. You may need to manually quit the program.")

                pid, cmdline = core.check_pkg_mgr()


            #
            # CHECK FOR ACTIVE NETWORK CONNECTION
            #

            if not assume_network:
                tui.title("CHECKING FOR NETWORK CONNECTION")

                if not core.check_network_connection():
                    log.error("\nThe network appears to be unreachable. Installation cannot complete without access to")
                    log.error("distribution repositories. Please check the network and try again.")
                    sys.exit(1)
                else:
                    log.info("Network connection present.")

            #
            # PRE-DEPEND
            #

            tui.title("RUNNING PRE-PACKAGE COMMANDS")
            core.run_pre_depend(progress_callback)
            log.info("OK")

            #
            # INSTALL PACKAGES AND RUN COMMANDS
            #

            tui.title("DEPENDENCY AND CONFLICT RESOLUTION")

            packages = []
            commands_to_run = []
            package_mgr_cmd = core.get_distro_data('package_mgr_cmd')

            # HACK!
            individual_pkgs = True
            if package_mgr_cmd.startswith('xterm'):
                individual_pkgs = False

            if package_mgr_cmd:
                log.debug("Preparing to install packages and run commands...")

                for d in depends_to_install:
                    log.debug("*** Processing dependency: %s" % d)
                    pkgs, commands = core.get_dependency_data(d)

                    if pkgs:
                        log.debug("Package(s) '%s' will be installed to satisfy dependency '%s'." %
                            (','.join(pkgs), d))

                        packages.extend(pkgs)

                    if commands:
                        log.debug("Command(s) '%s' will be run to satisfy dependency '%s'." %
                            (','.join(commands), d))

                        commands_to_run.extend(commands)

            else:
                log.error("Invalid package manager")

            log.debug("Packages: %s" % packages)
            log.debug("Commands: %s" % commands_to_run)
            log.debug("Install individual packages: %s" % individual_pkgs)

            if package_mgr_cmd and packages:
                if individual_pkgs:
                    for packages_to_install in packages:
                        retries = 0
                        while True:
                            cmd = utils.cat(package_mgr_cmd)
                            log.debug("Package manager command: %s" % cmd)

                            log.info("Running '%s'\nPlease wait, this may take several minutes..." % cmd)
                            status, output = core.run(cmd)

                            if status != 0:
                                retries += 1
                                if retries < (max_retries+1):
                                    log.error("Command failed. Re-try #%d..." % retries)
                                    continue

                                log.error("Package install command failed with error code %d" % status)
                                ok, ans = tui.enter_yes_no("Would you like to retry installing the missing package(s)")

                                if not ok:
                                    sys.exit(0)

                                if ans:
                                    continue
                                else:
                                    log.warn("Some HPLIP functionality might not function due to missing package(s).")
                                    break
                            else:
                                break

                else:
                    packages_to_install = ' '.join(packages)
                    while True:
                        cmd = utils.cat(package_mgr_cmd)
                        log.debug("Package manager command: %s" % cmd)

                        log.info("Running '%s'\nPlease wait, this may take several minutes..." % cmd)
                        status, output = core.run(cmd)

                        if status != 0:
                            log.error("Package install command failed with error code %d" % status)
                            ok, ans = tui.enter_yes_no("Would you like to retry installing the missing package(s)")

                            if not ok:
                                sys.exit(0)

                            if ans:
                                continue
                            else:
                                log.warn("Some HPLIP functionality might not function due to missing package(s).")
                                break
                        else:
                            break

            if commands_to_run:
                for cmd in commands_to_run:
                    log.debug(cmd)
                    log.info("Running '%s'\nPlease wait, this may take several minutes..." % cmd)
                    status, output = core.run(cmd)

                    if status != 0:
                        log.error("Install command failed with error code %d" % status)
                        sys.exit(1)


            ##
            ## HPOJ REMOVAL
            ##

            #if core.hpoj_present and core.selected_component == 'hplip' and core.distro_version_supported:
                #log.error("HPOJ is installed and/or running. HPLIP is not compatible with HPOJ.")
                #failed = True
                #hpoj_remove_cmd = core.get_distro_data('hpoj_remove_cmd')

                #if hpoj_remove_cmd:
                    #if auto:
                        #answer = True
                    #else:
                        #ok, answer = tui.enter_yes_no("\nWould you like to have this installer attempt to uninstall HPOJ")

                    #if not ok: sys.exit(0)

                    #if answer:
                        #failed = core.remove_hpoj(progress_callback)

                        #if failed:
                            #log.error("HPOJ removal failed. Please manually stop/remove/uninstall HPOJ and then re-run this installer.")
                            #sys.exit(1)
                    #else:
                        #log.error("Please stop/remove/uninstall HPOJ and then re-run this installer.")
                        #sys.exit(1)

                #else:
                    #log.error("Please stop/remove/uninstall HPOJ and then re-run this installer.")
                    #sys.exit(1)


            #
            # HPLIP REMOVE
            #

            if core.hplip_present and core.selected_component == 'hplip' and core.distro_version_supported:
                failed = True
                log.warn("A previous install of HPLIP is installed and/or running.")

                hplip_remove_cmd = core.get_distro_data('hplip_remove_cmd')
                if hplip_remove_cmd:
                    if auto:
                        answer = True
                    else:
                        ok, answer = tui.enter_yes_no("\nWould you like to have this installer attempt to uninstall the previously installed HPLIP")
                    if not ok: sys.exit(0)

                    if answer:
                        failed = core.remove_hplip(progress_callback)

                else:
                    log.error("The previously installed version of HPLIP may conflict with the new one being installed.")
                    log.error("It is recommended that you quit this installer, and manually remove HPLIP before continuing.")
                    sys.exit(0)

                if failed:
                    log.warn("HPLIP removal failed. The previous install may have been installed using a tarball or this installer.")
                    log.warn("Continuing to run installer - this installation should overwrite the previous one.")


            #
            # POST-DEPEND
            #

            tui.title("RUNNING POST-PACKAGE COMMANDS")
            core.run_post_depend(progress_callback)
            log.info("OK")


            #
            # DEPENDENCIES RE-CHECK
            #

            tui.title("RE-CHECKING DEPENDENCIES")
            core.check_dependencies()

            num_req_missing = 0
            for depend, desc, opt in core.missing_required_dependencies():
                num_req_missing += 1
                log.error("A required dependency '%s (%s)' is still missing." % (depend, desc))

            if num_req_missing:
                if num_req_missing > 1:
                    log.error("Installation cannot continue without these dependencies.")
                else:
                    log.error("Installation cannot continue without this dependency.")

                log.error("Please manually install this dependency and re-run this installer.")
                sys.exit(1)

            for depend, desc, required_for_opt, opt in core.missing_optional_dependencies():
                if required_for_opt:
                    log.warn("An optional dependency '%s (%s)' is still missing." % (depend, desc))
                    log.warn("Option '%s' has been turned off." % opt)
                    core.selected_options[opt] = False
                else:
                    log.warn("An optional dependency '%s (%s)' is still missing." % (depend, desc))
                    log.warn("Some features may not function as expected.")


            if not num_opt_missing and not num_req_missing:
                log.info("OK")

        #
        # INSTALL LOCATION
        #

        log.debug("Install location = %s" % core.install_location)


        #
        # BUILD AND INSTALL
        #

        if not auto:
            tui.title("READY TO BUILD AND INSTALL")
            if not tui.continue_prompt("Ready to perform build and install."):
                sys.exit(0)

        tui.title("PRE-BUILD COMMANDS")
        core.run_pre_build(progress_callback)
        log.info("OK")

        tui.title("BUILD AND INSTALL")

        os.umask(0022)
        for cmd in core.build_cmds():
            log.info("Running '%s'\nPlease wait, this may take several minutes..." % cmd)
            status, output = core.run(cmd)

            if status != 0:
                if 'configure' in cmd:
                    log.error("Configure failed with error: %s" % CONFIGURE_ERRORS.get(status, CONFIGURE_ERRORS[1]))

                else:
                    log.error("'%s' command failed with status code %d" % (cmd, status))

                sys.exit(0)
            else:
                log.info("Command completed successfully.")

            log.info("")

        log.info("\nBuild complete.")

        #
        # POST BUILD
        #

        tui.title("POST-BUILD COMMANDS")
        core.run_post_build(progress_callback)

        #
        # OPEN MDNS MULTICAST PORT
        #

        if core.selected_options['network']:
            open_mdns_port = core.get_distro_ver_data('open_mdns_port')
            if open_mdns_port:
                tui.title("OPEN MDNS/BONJOUR FIREWALL PORT (MULTICAST PORT 5353)")

                paragraph = "In order to setup your printer on the network using mDNS/Bonjour, it is required that your internet firewall allows connections on port 5353. If this port is blocked by the firewall, connection to network printers using mDNS/Bonjour will not be possible."

                for p in tui.format_paragraph(paragraph):
                    log.info(p)
                log.info("")

                ok, ans = tui.enter_yes_no("Do you wish to open this port on your internet firewall")
                if not ok: sys.exit(0)

                if ans:
                    core.run_open_mdns_port()
                else:
                    log.warn("Skipping firewall setup. If this port is blocked on your firewall when setting up network printers, use SLP discovery and device URIs with ?ip=x.x.x.x. When using hp-setup, choose 'SLP' discovery under 'Advanced'.")


        #
        # Try to close running hp-systray (3.9.2 or later)
        #

        if current_version >= 0x030902: # 3.9.2
            try:
                # dBus
                #import dbus
                from dbus import SessionBus, lowlevel
            except ImportError:
                #log.error("Unable to load DBus")
                pass
            else:
                try:
                    args = ['', '', EVENT_SYSTEMTRAY_EXIT, prop.username, 0, '', '']
                    msg = lowlevel.SignalMessage('/', 'com.hplip.StatusService', 'Event')
                    msg.append(signature='ssisiss', *args)
                    tui.title("CLOSE HP_SYSTRAY")
                    log.info("Sending close message to hp-systray (if it is currently running)...")
                    SessionBus().send_message(msg)
                except:
                    pass

        # Restart or re-plugin if necessary (always True in 2.7.9+)
        if core.selected_component == 'hplip':
            tui.title("RESTART OR RE-PLUG IS REQUIRED")
            cmd = "hp-setup"
            paragraph = """If you are installing a USB connected printer, and the printer was plugged in when you started this installer, you will need to either restart your PC or unplug and re-plug in your printer (USB cable only). If you choose to restart, run this command after restarting: %s  (Note: If you are using a parallel connection, you will have to restart your PC. If you are using network/wireless, you can ignore and continue).""" % cmd

            for p in tui.format_paragraph(paragraph):
                log.info(p)
            log.info("")

            ok, choice = tui.enter_choice("Restart or re-plug in your printer (r=restart, p=re-plug in*, i=ignore/continue, q=quit) : ",
                ['r', 'p', 'i'], 'p')

            if not ok: sys.exit(0)

            if choice == 'r':
                log.note("")
                log.note("IMPORTANT! Make sure to save all work in all open applications before restarting!")

                ok, ans = tui.enter_yes_no(log.bold("Restart now"), 'n')
                if not ok: sys.exit(0)
                if ans:
                    ok = core.restart()
                    if not ok:
                        log.error("Restart failed. Please restart using the system menu.")

                sys.exit(0)

            elif choice == 'p': # 'p'
                if not tui.continue_prompt("Please unplug and re-plugin your printer now. "):
                    sys.exit(0)


        #
        # SETUP PRINTER
        #
        if core.selected_component == 'hplip':
            tui.title("PRINTER SETUP")

            if auto:
                install_printer = True
            else:
                ok, install_printer = tui.enter_yes_no("Would you like to setup a printer now")
                if not ok: sys.exit(0)

            if install_printer:
                log.info("Please make sure your printer is connected and powered on at this time.")
                if not core.run_hp_setup():
                    log.error("hp-setup failed. Please run hp-setup manually.")

    except KeyboardInterrupt:
        log.info("")
        log.error("Aborted.")

    sys.exit(0)

