from django.db import models
from django.utils import timezone

EQUIP_LIST = (
    ('CC36', 'Crimp Center 36'),
    ('CC64', 'Crimp Center 64'),
    ('LOFF', 'LockOff Station'),
    ('A-1', 'A-1'),
    ('DLab', 'DynaLab'),
    ('Twist', 'Twister'),
    ('USonic', 'Ultra Sonic'),
    ('pnsys', 'Pneumatic System'),
    ('sboard', 'Smart Board'),
    ('tpost', 'Tool Post'),
    ('ecut3300', 'Eco Cut 3300'),
    ('UCrimp', 'UniCrimp 220'),
    ('Mp104', 'Mecal P-104 press'),
    ('slice', 'Slice AMTI'),
    ('FumeEx', 'Fume Extractors'),
    ('UPS', 'UPS'),
    ('other','other'),
)
ISSUE_TYPE = (
    ('Quality', 'Quality Issue'),
    ('MachineD', 'Machine Down'),
    ('Software', 'Software'),
    ('Mechanical', 'Mechanical'),
    ('Pneumatic', 'Pnuematic'),
    ('Electrical', 'Electrical'),
    ('Setup', 'Setup'),
    ('Maintenance', 'Maintenance'),
    ('Warehouse', 'Warehouse'),
    ('Assembly', 'Assembly'),
)

TECH_REPAIR = (
    ('Evan', 'Evan'),
    ('Terell', 'Terell'),
    ('Tony', 'Tony'),
    ('Other','Other'),
)

PRIORITY_SCALE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('hold', 'HOLD'),
    ('wait', 'WAIT') ,
)

ISSUE_STATUS = (
    ('Active',  'Active'),
    ('wip', 'In Progress'),
    ('cancelled', 'Canceled'),
    ('Complete', 'Complete'),
)

class  Tracker(models.Model):
    user = models.ForeignKey( 'auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    issue_date = models.DateTimeField(default=timezone.now)
    resolution_date = models.DateTimeField(blank=True, null=True)
    equipment = models.CharField(max_length=15, choices=EQUIP_LIST)
    prioritynum = models.TextField(max_length=4, choices=PRIORITY_SCALE)
    status = models.CharField(max_length=10, choices=ISSUE_STATUS)
    issue_kind = models.CharField(max_length=15, choices=ISSUE_TYPE)
    issue_desc = models.TextField(max_length=300)
    tech_name = models.CharField(max_length=10, choices=TECH_REPAIR)
    timespent = models.DecimalField(max_digits=6, decimal_places=0)
    resolution_desc = models.TextField(max_length=500)

    def resolve(self):
        self.resolution_date = timezone.now()
        self.save()

    def __str__(self):
        return self.equipment

