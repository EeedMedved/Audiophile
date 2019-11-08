from django.contrib import admin

from .models import Manufacturer, Phone, DAC, AudioCodec, OperatingSystemVendor, OperatingSystem, SoC
from .models import DisplayResolution, DisplayTechnology


admin.site.register(Manufacturer)
admin.site.register(Phone)
admin.site.register(DAC)
admin.site.register(AudioCodec)
admin.site.register(OperatingSystem)
admin.site.register(OperatingSystemVendor)
admin.site.register(SoC)
admin.site.register(DisplayResolution)
admin.site.register(DisplayTechnology)
