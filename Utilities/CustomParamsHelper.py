#MenuTitle: Custom Parameter Helper
# -*- coding: utf-8 -*-
__doc__="""
Useful for adding Replace Glyphs and Remove Glyphs parameters
"""
import GlyphsApp
import vanilla

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

glyphList = [g.name for g in thisFont.glyphs]

class OpenTab(object):

	def __init__(self):
		self.tabString = ''

		self.w = vanilla.FloatingWindow( (360, 80), "CustomParamsHelper", autosaveName="com.juandelperal.CustomParamsHelper.mainwindow" )
		self.w.text = vanilla.TextBox( (13, 15, 320, 20), "suffix to find (ex sc)", sizeStyle='small')
		self.w.suffix = vanilla.EditText( (15, 35, 200, 20), "H", sizeStyle='small', placeholder='ss01', callback=self.SavePreferences )
		self.w.go = vanilla.Button( (220, 30, 60, 30), "Go", sizeStyle='small', callback=self.GoForIt )
		self.w.cancel = vanilla.Button( (285, 30, 60, 30), "Close", sizeStyle='small', callback=self.Close )

		self.w.setDefaultButton( self.w.go )

		if not self.LoadPreferences( ):
			print "Error: Could not load preferences. Will resort to defaults."

		self.w.open()
		self.w.makeKey()


	def SavePreferences( self, sender ):
		Glyphs.defaults["com.juandelperal.CustomParamsHelper.mainwindow.suffix"] = self.w.suffix.get()

		return True

	def LoadPreferences( self ):
		try:
			self.w.suffix.set( Glyphs.defaults["com.juandelperal.CustomParamsHelper.mainwindow.suffix"] )
		except:
			return False

		return True

	def GoForIt(self, sender):
		suffix = self.w.suffix.get()
		targetGlyphs = [g for g in glyphList if suffix in g]

		Glyphs.clearLog()
		Glyphs.showMacroWindow()

		replaceList = []

		for glyph in targetGlyphs:
			replacement = glyph.replace('.' + suffix,"")
			if replacement in glyphList:
				replaceList.append("%s=%s" % ( glyph, replacement))

		removeList = []

		for glyph in targetGlyphs:
			replacement = glyph.replace('.' + suffix,"")
			if replacement in glyphList:

				removeList.append(glyph)

		print "Replace Glyphs code\n\n"
		for s in replaceList:
			print s
		print "\n\n\n\n\n\n\nRemove Glyphs code\n\n"
		for s in removeList:
			print s

		self.w.close()

	def Close(self, sender):
		self.w.close()

OpenTab()