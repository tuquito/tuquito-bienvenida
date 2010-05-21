#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 Tuquito Bienvenida 0.1
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

import gtk, sys, pygtk
pygtk.require("2.0")
import commands, os
import gettext, webkit, string
from user import home

# i18n
gettext.install('tuquito-bienvenida', '/usr/share/tuquito/locale')

class Welcome():
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file('bienvenida.glade')
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
		text['title'] = _('Bienvenid@ a Tuquito!')
		text['release_title'] = _('Release')
		text['edition_title'] = _('Edición')
		text['doc'] = _('Documentación')
		text['sop'] = _('Soporte')
		text['pro'] = _('Proyecto')
		text['com'] = _('Comunidad')
		text['tukipedia'] = _('Tukipedia')
		text['tukipedia2'] = _('La fuente de información por excelencia de Tuquito')
		text['video'] = _('Videos Tuquito')
		text['video2'] = _('Videos y tutoriales')
		text['forums'] = _('Foros')
		text['forums2'] = _('Buscá ayuda en los foros oficiales')
		text['mailist'] = _('Lista de correo')
		text['mailist2'] = _('Sumate a la lista de correo abierta de Tuquito')
		text['irc'] = _('Sala de chat')
		text['irc2'] = _('Conocé a otros usuarios de Tuquito!')
		text['urbano'] = _('Tuquito Urbano')
		text['urbano2'] = _('Ayudá a los que más necesitan!')
		text['other'] = _('Otros proyectos')
		text['other2'] = _('Conocé los otros proyectos de Tuquito')
		text['donation'] = _('Donaciones')
		text['donation2'] = _('Realizando una pequeña donación nos ayudas a mejorar el producto')
		text['get_involved'] = _('Como participar')
		text['get_involved2'] = _('Formas y medios para participar del proyecto')
		text['social'] = _('Tuquito Social')
		text['social2'] = _('Sumate a la red social de Tuquito!')
		text['universo'] = _('Universo Tuquito')
		text['universo2'] = _('Enterate de todo lo que pasa en Tuquito')
		text['facebook'] = _('Síguenos en Facebook')
		text['facebook2'] = _('Síguenos en Facebook')
		text['twitter'] = _('Síguenos en Twitter')
		text['twitter2'] = _('Síguenos en Twitter')
		text['show'] = _('Mostrar este diálogo al inicio')
		text['close'] = _('Cerrar')
		if os.path.exists(home + '/.tuquito/tuquito-biendenida/norun'):		
			text['checked'] = ('')
		else:
			text['checked'] = ('CHECKED')
		welcome = _('Hola')
		welcome2 = _(', bienvenido a Tuquito 4!<br>Muchas gracias por elegirnos. Esperamos que disfrutes del trabajo de esta gran comunidad.<br>Los siguientes enlaces te ayudarán a iniciarte en el sistema operativo. No dudes en enviarnos tus sugerencias para que sigamos mejorando.')
		text['welcome'] = welcome + ' <b>' + user + '</b>' + welcome2
		template = open('./templates/bienvenida.html').read()		
		html = string.Template(template).safe_substitute(text)
		browser.load_html_string(html, 'file:/')
		browser.connect('title-changed', self.title_changed)
		self.window.show_all()

	def title_changed(self, view, frame, title):	
		if title.startswith('nop'):
		    return
		# call directive looks like:
		#  "call:func:arg1,arg2"
		#  "call:func"
		if title == 'event_irc':
				os.system('/usr/bin/irc-tuquito &')
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
