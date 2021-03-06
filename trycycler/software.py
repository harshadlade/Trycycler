#!/usr/bin/env python3
"""
Copyright 2020 Ryan Wick (rrwick@gmail.com)
https://github.com/rrwick/Trycycler

This file is part of Trycycler. Trycycler is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version. Trycycler is distributed
in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details. You should have received a copy of the GNU General Public License along with Trycycler.
If not, see <http://www.gnu.org/licenses/>.
"""

import subprocess
import sys

from .log import log


def check_minimap2():
    try:
        output = subprocess.check_output(['minimap2', '--version'], stderr=subprocess.STDOUT)
    except FileNotFoundError:
        sys.exit('\nError: unable to find minimap2 - make sure that minimap2 is installed and '
                 'available on the path, then try again.')
    except subprocess.CalledProcessError:
        sys.exit('\nError: unable to determine minimap2 version - make sure that minimap2 is '
                 'correctly installed, then try again.')
    output = output.decode().strip()
    log(f'  minimap2: v{output}')


def check_muscle():
    try:
        output = subprocess.check_output(['muscle', '-version'], stderr=subprocess.STDOUT)
    except FileNotFoundError:
        sys.exit('\nError: unable to find MUSCLE - make sure that MUSCLE is installed and '
                 'available on the path, then try again.')
    except subprocess.CalledProcessError:
        sys.exit('\nError: unable to determine MUSCLE version - make sure that MUSCLE is '
                 'correctly installed, then try again.')
    output = output.decode().strip()
    version = parse_muscle_version(output)
    log(f'   MUSCLE: v{version}')


def parse_muscle_version(output):
    if 'MUSCLE v' in output:
        output = output.split('MUSCLE v')[1]
        output = output.split(' ')[0]
        return output.strip()
    else:
        return '?'


def check_mash():
    try:
        output = subprocess.check_output(['mash', '--version'], stderr=subprocess.STDOUT)
    except FileNotFoundError:
        sys.exit('\nError: unable to find Mash - make sure that Mash is installed and '
                 'available on the path, then try again.')
    except subprocess.CalledProcessError:
        sys.exit('\nError: unable to determine Mash version - make sure that Mash is '
                 'correctly installed, then try again.')
    output = output.decode().strip()
    log(f'      Mash: v{output}')


def check_r():
    try:
        output = subprocess.check_output(['R', '--version'], stderr=subprocess.STDOUT)
    except FileNotFoundError:
        sys.exit('\nError: unable to find R - make sure that R is installed and '
                 'available on the path, then try again.')
    except subprocess.CalledProcessError:
        sys.exit('\nError: unable to determine R version - make sure that R is '
                 'correctly installed, then try again.')
    output = output.decode().strip()
    version = parse_r_version(output)
    log(f'         R: v{version}')


def parse_r_version(output):
    if 'R version ' in output:
        output = output.split('R version ')[1]
        output = output.split(' ')[0]
        return output.strip()
    else:
        return '?'


def check_ape():
    try:
        output = subprocess.check_output(['R', '--quiet', '-e', 'packageVersion("ape")'],
                                         stderr=subprocess.STDOUT)
    except (FileNotFoundError, subprocess.CalledProcessError):
        sys.exit('\nError: unable to run R - make sure that R is correctly installed, then try '
                 'again.')
    output = output.decode().strip()
    if 'there is no package' in output:
        sys.exit('\nError: unable to find ape - make sure that the "ape" package is installed '
                 'for your R installation, then try again.')
    version = parse_ape_version(output)
    log(f'       ape: v{version}')


def parse_ape_version(output):
    if '[1] ‘' in output:
        output = output.split('[1] ‘')[1]
        output = output.split('’')[0]
        return output.strip()
    else:
        return '?'


def check_phangorn():
    try:
        output = subprocess.check_output(['R', '--quiet', '-e', 'packageVersion("phangorn")'],
                                         stderr=subprocess.STDOUT)
    except (FileNotFoundError, subprocess.CalledProcessError):
        sys.exit('\nError: unable to run R - make sure that R is correctly installed, then try '
                 'again.')
    output = output.decode().strip()
    if 'there is no package' in output:
        sys.exit('\nError: unable to find ape - make sure that the "phangorn" package is '
                 'installed for your R installation, then try again.')
    version = parse_phangorn_version(output)
    log(f'  phangorn: v{version}')


def parse_phangorn_version(output):
    if '[1] ‘' in output:
        output = output.split('[1] ‘')[1]
        output = output.split('’')[0]
        return output.strip()
    else:
        return '?'
