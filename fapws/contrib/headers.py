#    Copyright (C) 2009 William.os4y@gmail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from fapws.compat import convert_to_bytes


def redirect(start_response, location, permanent=None):
    header = [(b'location', convert_to_bytes(location)), (b'Content-Type', b"text/plain")]
    if permanent:
        start_response(b'301 Moved Permanently', header)
    else:
        start_response(b'302 Moved Temporarily', header)
    return []
