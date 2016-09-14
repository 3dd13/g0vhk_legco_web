from django.contrib import admin
from django import forms
from django.db import models
from legco.models import Party, Individual, Council, Constituency,  Meeting, Motion, VoteSummary, IndividualVote, Vote, NewsArticle, CouncilMember, CouncilMembershipType
from legco.models import Bill,  BillCommittee, BillThirdReading, BillFirstReading, BillSecondReading
from legco.models import MeetingSpeech, MeetingHansard
from legco.models import Question

class CouncilAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple}
    }

admin.site.register(Party)
admin.site.register(Vote)
admin.site.register(Individual)
admin.site.register(Council, CouncilAdmin)
admin.site.register(Constituency)
admin.site.register(Motion)
admin.site.register(Meeting)
admin.site.register(VoteSummary)
admin.site.register(IndividualVote)
admin.site.register(NewsArticle)
admin.site.register(Bill)
admin.site.register(BillCommittee)
admin.site.register(BillThirdReading)
admin.site.register(BillFirstReading)
admin.site.register(BillSecondReading)
admin.site.register(Question)
admin.site.register(MeetingSpeech)
admin.site.register(MeetingHansard)
admin.site.register(CouncilMember)
admin.site.register(CouncilMembershipType)

