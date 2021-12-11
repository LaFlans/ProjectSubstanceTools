import substance_painter.display

color_lut = substance_painter.display.get_color_lut_resource()
if(color_lut != None):
    print(color_lut.url())
else:
    print("No color profile is used.")

new_color_lut = substance_painter.resource.ResourceID(context="starter_assets",name="sepia")
substance_painter.display.set_color_lut_resource(new_color_lut)

envmap = substance_painter.display.get_environment_resource()
print(envmap.url())

new_envmap = substance_painter.resource.ResourceID(context="starter_assets",name="Bonifacio Street")
substance_painter.display.set_environment_resource(new_envmap)