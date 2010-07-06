#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 Tuquito Bienvenida 4.0
 Copyright (C) 2010
 Author: Mario Colque <mario@tuquito.org.ar>
 Tuquito Team! - www.tuquito.org.ar

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; version 3 of the License.
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA.
"""

import gtk, pygtk
pygtk.require("2.0")
import commands, os
import gettext, webkit, string
from user import home

# i18n
gettext.install('tuquito-bienvenida', '/usr/share/tuquito/locale')

class Welcome():
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file('/usr/lib/tuquito/tuquito-bienvenida/bienvenida.glade')
		self.window = self.builder.get_object('window')

		codename = commands.getoutput('cat /etc/tuquito/info | grep CODENAME').split('=')[1]
		release = commands.getoutput('cat /etc/tuquito/info | grep RELEASE').split('=')[1]
		edition = commands.getoutput('cat /etc/tuquito/info | grep EDITION').split('=')[1]
		user = os.getenv('USER')

		self.builder.get_object('window').connect('destroy', gtk.main_quit)
		browser = webkit.WebView()
		self.builder.get_object('scrolled').add(browser)
		browser.connect('button-press-event', lambda w, e: e.button == 3)
		text = {}
		text['release'] = release + ' (' + codename + ')'
		text['edition'] = edition
		text['title'] = _('Welcome to Tuquito!')
		text['release_title'] = _('Release')
		text['edition_title'] = _('Edition')
		text['doc'] = _('Documentation')
		text['sop'] = _('Support')
		text['pro'] = _('Project')
		text['com'] = _('Community')
		text['tukipedia'] = 'Tukipedia'
		text['tukipedia2'] = _('The source of information of excellence Tuquito')
		text['video'] = _('Videos Tuquito')
		text['video2'] = _('Videos and tutorials')
		text['forums'] = _('Forums')
		text['forums2'] = _('Find help on the official forums')
		text['mailist'] = _('Mailing List')
		text['mailist2'] = _('Join the mailing list open Tuquito')
		text['irc'] = _('Chat Room')
		text['irc2'] = _('Meet other users of Tuquito')
		text['urbano'] = _('Urban Tuquito')
		text['urbano2'] = _('Helps those who most need')
		text['other'] = _('Other projects')
		text['other2'] = _('Meet other projects Tuquito')
		text['donation'] = _('Donations')
		text['donation2'] = _('Making a small donation, you help us improve the product')
		text['get_involved'] = _('How to Participate')
		text['get_involved2'] = _('Ways and means to participate in the project')
		text['social'] = _('Tuquito Social')
		text['social2'] = _('Join the social network Tuquito')
		text['universo'] = _('Tuquito Universe')
		text['universo2'] = _('Find out everything that happens in Tuquito')
		text['facebook'] = 'Facebook'
		text['facebook2'] = _('Follow us on Facebook')
		text['twitter'] = 'Twitter'
		text['twitter2'] = _('Follow us on Twitter')
		text['show'] = _('Show this dialog at startup')
		text['close'] = _('Close')
		if os.path.exists(home + '/.tuquito/tuquito-biendenida/norun'):		
			text['checked'] = ('')
		else:
			text['checked'] = ('CHECKED')
		welcome = _('Hi')
		welcome2 = _('welcome to Tuquito 4!<br>Thank you very much for choosing us. We hope you enjoy the work of this great community.<br>The following links will help you get started in the operating system. Please send your suggestions to continue improving.')
		text['welcome'] = '%s, <b>%s</b>, %s' % (welcome, user, welcome2)
		template = open('/usr/lib/tuquito/tuquito-bienvenida/templates/bienvenida.html').read()		
		html = string.Template(template).safe_substitute(text)
		browser.load_html_string(html, 'file:/')
		browser.connect('title-changed', self.title_changed)
		self.window.show_all()

	def title_changed(self, view, frame, title):	
		if title.startswith('nop'):
		    return
		if title == 'event_irc':
				os.system('/usr/bin/xchat &')
		elif title == 'event_tukipedia':
			os.system('xdg-open http://tukipedia.tuquito.org.ar')
		elif title == 'event_video':
			os.system('xdg-open http://videos.tuquito.org.ar')
		elif title == 'event_forums':
			os.system('xdg-open http://foros.tuquito.org.ar')
		elif title == 'event_list':
			os.system('xdg-open http://groups.google.com/group/comunidad-tuquito')
		elif title == 'event_social':
			os.system('xdg-open http://tuquito.ning.com')
		elif title == 'event_universo':
			os.system('xdg-open http://universo.tuquito.org.ar')
		elif title == 'event_facebook':
			os.system('xdg-open http://www.facebook.com/pages/Tuquito/157877426382')
		elif title == 'event_twitter':
			os.system('xdg-open http://www.twitter.com/tuquitolinux')	
		elif title == 'event_urbano':
			os.system('xdg-open http://urbano.tuquito.org.ar')
		elif title == 'event_get_involved':
			os.system('xdg-open http://tuquito.org.ar/desarrollo.html')
		elif title == 'event_other':
			os.system('xdg-open http://tuquito.org.ar/proyectos.html')
		elif title == 'event_donation':
			os.system('xdg-open http://tuquito.org.ar/donaciones.html')
		elif title == 'event_close_true':
			if os.path.exists(home + '/.tuquito/tuquito-bienvenida/norun'):
				os.system('rm -rf ' + home + '/.tuquito/tuquito-bienvenida/norun')
			gtk.main_quit()
		elif title == 'event_close_false':
			os.system('mkdir -p ' + home + '/.tuquito/tuquito-bienvenida')
			os.system('touch ' + home + '/.tuquito/tuquito-bienvenida/norun')
			gtk.main_quit()
		elif title == 'checkbox_checked':
			if os.path.exists(home + '/.tuquito/tuquito-bienvenida/norun'):
				os.system('rm -rf ' + home + '/.tuquito/tuquito-bienvenida/norun')
		elif title == 'checkbox_unchecked':
			os.system('mkdir -p ' + home + '/.tuquito/tuquito-bienvenida')
			os.system('touch ' + home + '/.tuquito/tuquito-bienvenida/norun')

if __name__ == '__main__':
	gtk.gdk.threads_init()
	Welcome()
	gtk.main()
