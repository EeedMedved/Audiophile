from django.db import models


class OperatingSystemVendor(models.Model):
    title = models.CharField(max_length=20)

    def __repr__(self):
        return '<OperatingSystemVendor %s>' % self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Разработчик ОС'
        verbose_name_plural = 'Разработчики ОС'


class OperatingSystem(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название ОС')
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Название версии ОС')
    vendor = models.ForeignKey(OperatingSystemVendor, on_delete=models.PROTECT)
    version = models.FloatField()
    release_date = models.DateField(verbose_name='Дата релиза')

    def __repr__(self):
        return '<OperatingSystem %s>' % self.title

    def __str__(self):
        return '{} {}'.format(self.title, str(self.version))

    class Meta:
        verbose_name = 'Операционная система'
        verbose_name_plural = 'Операционные системы'


class Phone(models.Model):
    SIM_CARD_NUMBER_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4')
    ]

    BLUETOOTH_VERSION_CHOICES = [
        (1.0, '1.0'),
        (2.0, '2.0'),
        (3.0, '3.0'),
        (4.0, '4.0'),
        (4.1, '4.1'),
        (4.2, '4.2'),
        (5.0, '5.0')
    ]

    WIFI_VERSION_CHOICES = [
        ('802.11n', 'Wi-Fi 802.11 b/g/n'),
        ('802.11ac', 'Wi-Fi 802.11 a/b/g/n/ac'),
        ('802.11ax', 'Wi-Fi 802.11 a/b/g/n/ac/ax')
    ]

    title = models.CharField(max_length=50, db_index=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT)
    dac = models.ForeignKey('DAC', on_delete=models.PROTECT, null=True, blank=True)
    weight = models.FloatField('Вес')
    has_minijack = models.BooleanField()
    has_nfc = models.BooleanField()
    presentation_year = models.PositiveSmallIntegerField('Год начала продаж')
    official_os = models.ManyToManyField(OperatingSystem)
    sim_card_number = models.PositiveSmallIntegerField(
        verbose_name='Количество сим-карт',
        choices=SIM_CARD_NUMBER_CHOICES
    )
    width = models.FloatField(verbose_name='Ширина')
    height = models.FloatField(verbose_name='Высота')
    thickness = models.FloatField(verbose_name='Толщина')
    ram = models.PositiveIntegerField(verbose_name='Объем ОЗУ в Мб')
    storage = models.PositiveIntegerField(verbose_name='Встроенная память в МБ')
    soc = models.ForeignKey('SoC', on_delete=models.PROTECT)
    bluetooth_supported_versions = models.FloatField(
        verbose_name='Максимальная версия Bluetooth',
        choices=BLUETOOTH_VERSION_CHOICES
    )
    wifi_supported_versions = models.CharField(
        max_length=15,
        choices=WIFI_VERSION_CHOICES,
    )
    battery_capacity = models.PositiveSmallIntegerField(
        verbose_name='Емкость батареи'
    )
    is_battery_removable = models.BooleanField(verbose_name='Съемная батарея')
    has_quick_charge = models.BooleanField(verbose_name='Быстрая зарядка')
    quick_charge_technology = models.CharField(max_length=30, null=True)

    def __repr__(self):
        return '<Phone %s>' % self.title

    def __str__(self):
        return '{} {}'.format(self.manufacturer.title, self.title)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class Manufacturer(models.Model):
    title = models.CharField(max_length=50, db_index=True)

    def __repr__(self):
        return '<Manufacturer %s>' % self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class DAC(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)

    def __repr__(self):
        return '<DAC %s>' % self.title

    def __str__(self):
        return '{} {}'.format(self.manufacturer.title, self.title)

    class Meta:
        verbose_name = 'ЦАП'
        verbose_name_plural = 'ЦАПы'


class AudioCodec(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)

    def __repr__(self):
        return '<AudioCodec %s>' % self.title

    def __str__(self):
        return '{} {}'.format(self.manufacturer.title, self.title)


class SoC(models.Model):
    CPU_BITS_CHOICES = [
        (32, '32 bit'),
        (64, '64 bit'),
    ]
    title = models.CharField(max_length=100, db_index=True)
    code = models.CharField(max_length=20, db_index=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    process_technology = models.PositiveSmallIntegerField(verbose_name='Техпроцесс')
    cpu = models.CharField(max_length=150)
    cpu_bits = models.PositiveSmallIntegerField(verbose_name='Архитектура процессора',
                                                choices=CPU_BITS_CHOICES)

    def __str__(self):
        return '{} {}'.format(self.manufacturer.title, self.title)

    def __repr__(self):
        return '<SoC %s>' % self.title

    class Meta:
        verbose_name = 'Система на кристалле'
        verbose_name_plural = 'Системы на кристалле'
