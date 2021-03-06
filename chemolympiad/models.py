from django.db import models
import datetime

class Competition(models.Model):
    name = models.CharField(max_length=100, help_text='Name of problem collection, e.g. IChO, Prep Problems, Russian National Chemistry Olympiad')

    def __unicode__(self):
        return unicode(self.name)

class Question(models.Model):
    YEAR_CHOICES = tuple([(i, i) for i in range(datetime.date.today().year, 1950, -1)])

    year = models.IntegerField(choices=YEAR_CHOICES)
    competition = models.ForeignKey('Competition')
    number  = models.IntegerField()
    topics = models.ManyToManyField('Topic')

    def __unicode__(self):
        return unicode('Problem %s from the %s %s' % (self.number, self.year, self.competition))

    class Meta:
        ordering = ['competition', '-year']
        permissions = (('can_search', 'Can search the database'),
                        )

class Subfield(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.name)

class Topic(models.Model):
    name  = models.CharField(max_length= 40, help_text=
    '''Topics should be specific, but not too specific. For example,
    "Pericyclic Reactions or "Silicate chemistry" is about the right level
    of specificity, but "Analytical Chemistry" or "Mannich Reaction"
    is too vague/too specific. A good rule of thumb is that a topic
    should be about the right scope to be covered in a 1-hour lecture.
    Additionally, do not tag basic topics (stoichiometry; 1st-semester
    organic chem topics, etc.)''')
    subfield = models.ManyToManyField('Subfield')
    
    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']

