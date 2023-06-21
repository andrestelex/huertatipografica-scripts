# MenuTitle: Tab with lowercase
import GlyphsApp
from PyObjCTools.AppHelper import callAfter

font = Glyphs.font
layers = Glyphs.currentDocument.selectedLayers()
layer = layers[0]
glyphname = layer.parent.name
outputString = ""
for thisGlyph in font.glyphs:
    if thisGlyph.subCategory == "Lowercase":
        outputString += "/" + glyphname + "/" + thisGlyph.name


callAfter(Glyphs.currentDocument.windowController().addTabWithString_, outputString)
print(outputString)
print("Fin")
