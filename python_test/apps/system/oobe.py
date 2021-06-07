# arcticOS
# Copyright (c) 2021 Johnny Stene <jhonnystene@protonmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
def runApp(PhoneDisplay, KeyInput, BuildInfo, UserSettings):
    print("OOBE start...")
    PhoneDisplay.clear()
    PhoneDisplay.drawAppHeader("Welcome")
    PhoneDisplay.drawText("-- OOBE process here --", 18, 10, 35)
    PhoneDisplay.drawText("Press OK to continue", 18, 10, 50)
    PhoneDisplay.refresh()

    while True:
        key = KeyInput.getKey()

        if(key == "ok"):
            break
